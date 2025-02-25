# coding:utf-8

"""
@author = super_fazai
@File    : ali_1688_real-times_update.py
@Time    : 2017/10/28 07:24
@connect : superonesfazai@gmail.com
"""

"""
本地长期更新(server可更新!), 部分goods_id采集会被强制登录(ip被封), 但是不是所有!
推荐放在server上更新!(目前只放在server上更新)
本地ip被封时, 可通过重启路由器来获取新ip
"""

import sys
sys.path.append('..')

from ali_1688_parse import ALi1688LoginAndParse
from my_pipeline import SqlServerMyPageInfoSaveItemPipeline

from settings import (
    IS_BACKGROUND_RUNNING,
    MY_SPIDER_LOGS_PATH,)

from sql_str_controller import al_select_str_6
from multiplex_code import (
    _get_new_db_conn,
    _get_async_task_result,
    _print_db_old_data,
    get_goods_info_change_data,
    ALDbGoodsInfoObj,
)

from fzutils.spider.async_always import *

"""
39.97那台无法更新已被封禁
放本地更新
"""

class ALUpdater(AsyncCrawler):
    """1688常规商品数据更新"""
    def __init__(self, *params, **kwargs):
        AsyncCrawler.__init__(
            self, 
            *params, 
            **kwargs,
            log_print=True,
            log_save_path=MY_SPIDER_LOGS_PATH + '/1688/实时更新/',)
        self.sql_cli = None
        self.goods_index = 1
        # 并发量
        self.concurrency = 10

    async def _get_db_old_data(self) -> (list, None):
        """
        获取db需求更新的数据
        :return:
        """
        self.sql_cli = SqlServerMyPageInfoSaveItemPipeline()
        result = None
        try:
            result = list(self.sql_cli._select_table(sql_str=al_select_str_6))
        except TypeError:
            self.lg.error('TypeError错误, 原因数据库连接失败...(可能维护中)')

        await _print_db_old_data(logger=self.lg, result=result)

        return result

    async def _get_new_ali_obj(self, index) -> None:
        if index % 10 == 0:
            # 不能共享一个对象了, 否则驱动访问会异常!
            try:
                del self.ali_1688
            except:
                pass
            collect()
            self.ali_1688 = ALi1688LoginAndParse(logger=self.lg)

    async def _update_one_goods_info(self, db_goods_info_obj, index) -> list:
        """
        更新一个goods的信息
        :param db_goods_info_obj:
        :param index: 索引值
        :return: ['goods_id', bool:'成功与否']
        """
        res = False
        await self._get_new_ali_obj(index=index)
        self.sql_cli = await _get_new_db_conn(
            db_obj=self.sql_cli,
            index=index,
            logger=self.lg)
        if self.sql_cli.is_connect_success:
            self.lg.info('------>>>| 正在更新的goods_id为({0}) | --------->>>@ 索引值为({1})'.format(
                db_goods_info_obj.goods_id,
                index))
            data = self.ali_1688.get_ali_1688_data(goods_id=db_goods_info_obj.goods_id)
            if isinstance(data, int):  # 单独处理返回tt为4041
                self.goods_index += 1
                return [db_goods_info_obj.goods_id, res]

            if data.get('is_delete') == 1:
                # 单独处理【原先插入】就是 下架状态的商品
                data['goods_id'] = db_goods_info_obj.goods_id
                data['shelf_time'], data['delete_time'] = get_shelf_time_and_delete_time(
                    tmp_data=data,
                    is_delete=db_goods_info_obj.is_delete,
                    shelf_time=db_goods_info_obj.shelf_time,
                    delete_time=db_goods_info_obj.delete_time,)
                try:
                    self.ali_1688.to_right_and_update_data(data, pipeline=self.sql_cli)
                except Exception:
                    self.lg.error(exc_info=True)

                await async_sleep(1.5)
                self.goods_index += 1
                res = True

                return [db_goods_info_obj.goods_id, res]

            data = self.ali_1688.deal_with_data()
            if data != {}:
                data = get_goods_info_change_data(
                    target_short_name='al',
                    logger=self.lg,
                    data=data,
                    db_goods_info_obj=db_goods_info_obj,)

                res = self.ali_1688.to_right_and_update_data(data, pipeline=self.sql_cli)
                await async_sleep(.3)

            else:  # 表示返回的data值为空值
                pass

        else:  # 表示返回的data值为空值
            self.lg.error('数据库连接失败，数据库可能关闭或者维护中')

        index += 1
        self.goods_index = index
        collect()
        await async_sleep(2.)       # 避免被发现使用代理

        return [db_goods_info_obj.goods_id, res]

    async def _update_db(self):
        """
        常规数据实时更新
        :return:
        """
        while True:
            self.lg = await self._get_new_logger(logger_name=get_uuid1())
            result = await self._get_db_old_data()
            if result is None:
                pass
            else:
                self.goods_index = 1
                tasks_params_list = TasksParamsListObj(
                    tasks_params_list=result,
                    step=self.concurrency)
                self.ali_1688 = ALi1688LoginAndParse(logger=self.lg)
                index = 1
                while True:
                    try:
                        slice_params_list = tasks_params_list.__next__()
                        # self.lg.info(str(slice_params_list))
                    except AssertionError:  # 全部提取完毕, 正常退出
                        break

                    tasks = []
                    for item in slice_params_list:
                        goods_id = item[1]
                        db_goods_info_obj = ALDbGoodsInfoObj(item=item, logger=self.lg)
                        self.lg.info('创建 task goods_id: {}'.format(goods_id))
                        tasks.append(self.loop.create_task(self._update_one_goods_info(
                            db_goods_info_obj=db_goods_info_obj,
                            index=index)))
                        index += 1
                    if tasks != []:
                        await _get_async_task_result(tasks=tasks, logger=self.lg)
                    else:
                        pass

                self.lg.info('全部数据更新完毕'.center(100, '#'))
            if get_shanghai_time().hour == 0:  # 0点以后不更新
                await async_sleep(60 * 60 * 5.5)
            else:
                await async_sleep(5.5)
            try:
                del self.ali_1688
            except:
                pass
            collect()

    def __del__(self):
        try:
            del self.lg
        except:
            pass
        try:
            del self.loop
        except:
            pass
        collect()

def _fck_run():
    _ = ALUpdater()
    loop = get_event_loop()
    loop.run_until_complete(_._update_db())
    try:
        del loop
    except:
        pass

def main():
    print('========主函数开始========')
    daemon_init()
    print('--->>>| 孤儿进程成功被init回收成为单独进程!')
    _fck_run()

if __name__ == '__main__':
    if IS_BACKGROUND_RUNNING:
        main()
    else:
        _fck_run()
