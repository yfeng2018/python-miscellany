# coding:utf-8

"""
@author = super_fazai
@File    : article_spider.py
@connect : superonesfazai@gmail.com
"""

"""
文章资讯爬虫obj

supported:
    1.  微信文章内容爬取(https://weixin.sogou.com)
    2.  简书文章内容爬取(https://www.jianshu.com)
    3.  今日头条文章内容爬取(https://www.toutiao.com)
    4.  搜狗头条(https://wap.sogou.com)
    5.  百度m站(https://m.baidu.com/)
    6.  qq看点文章内容爬取(根据QQ看点中分享出的地址)
    7.  天天快报(根据天天快报分享出的地址)
    8.  东方头条文章内容爬取(https://toutiao.eastday.com)
    9.  中青看点(https://focus.youth.cn/html/articleTop/mobile.html)
    10. 阳光宽频网(短视频)(https://www.365yg.com/)
    11. 凤凰网(https://news.ifeng.com/ | https://i.ifeng.com article m站都跳转到pc站, 故直接做pc)
    12. 51健康养生网(http://www.51jkst.com/)
    13. 彩牛养生网(权威医生: 对养生的见解, 短视频为主, 包含部分文章)(http://m.cnys.com/)
    14. 爱范儿(pc: https://www.ifanr.com/)
    15. 科学松鼠会(https://songshuhui.net/)
    16. 界面新闻(https://www.jiemian.com/)
    17. 澎湃网(https://m.thepaper.cn/)
    18. 虎嗅网(https://m.huxiu.com)
    19. 南方周末(http://www.infzm.com/wap/#/)
    20. 好奇心日报(http://m.qdaily.com/mobile/homes.html)
    21. 西瓜视频(短视频)(https://www.ixigua.com)
    22. 场库网(短视频)(https://www.vmovier.com/)
    23. 梨视频(短视频)(https://www.pearvideo.com/)
    24. 艾墨镇(短视频)(https://aimozhen.com/)
    25. 美拍(短视频)(https://www.meipai.com/)
    26. 百度好看视频(短视频)(https://haokan.baidu.com/)
    27. 七丽女性网(https://i.7y7.com/)
    28. 亲亲宝贝网(https://m.qbaobei.com/)
    29. 发条网(短视频or图文)(https://m.fatiao.pro/)
    30. 觅糖网(短视频or图文)(https://www.91mitang.com/)
    31. 雪球网(https://xueqiu.com)
    32. 5号女性网(http://m.5h.com/)
    33. 百思不得姐(http://www.budejie.com/)
    34. 煎蛋网(http://jandan.net/)
    35. 来福岛爆笑娱乐网(http://www.laifudao.com/)
    36. bilibili(短视频)(https://www.bilibili.com/)
    37. 快音视(短视频)(https://kuaiyinshi.com/hot/video/?source=kuai-shou&page=1&st=week)
    38. 搞笑gif图片集(https://m.gaoxiaogif.com/)
    39. 酷燃视频(https://krcom.cn/)
    40. 东方视频网(http://imedia.eastday.com/)(可采其中的热门视频)
    41. 腾讯微视(根据腾讯微视分享出的地址)
    42. 看了吗视频聚合网(http://www.klm123.com/mobile/index)(有全屏小视频也有短视频)
    43. 开眼短视频(https://www.kaiyanapp.com/detail.html?vid=52619)(视频id类似递增)
    44. 抖音(根据抖音分享出来的地址)(但是cp上传视频被403禁止)
    45. 今日小视频网(部分视频为全屏小视频)(http://m.jrtb.net/)
    46. 金华广众网(即金华广电网)(https://www.jinhua.com.cn/)(以下不做解析: 美食中特色推荐, 美食快讯, 因为不更新, 全是前几年的东西, 要附加做的解析: 舌尖上的金华[视频图文])
    47. 金华热线(即浙中在线)(http://www.0579.cn/)(手机版: http://m.0579.cn/)
    48. 金华晚报(https://www.96356.in/)(手机版)
    49. 百度app金华本地板块的视频解析
    50. 百度app全屏小视频板块页面解析
    51. 抖音搜索中分享出来的视频榜(https://www.iesdouyin.com/share/billboard/?id=0&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy)
    52. 义乌十八腔(https://m.18qiang.com/)(不推荐, 因为是论坛, 图文文章较少, 都为文字帖, 不上报, pass)
    53. 浙江在线金华频道(http://jinhua.zjol.com.cn/jsbd/)(只获取第一页的即时数据)
    
not supported:
    1. 男人窝(https://m.nanrenwo.net/)
    2. 爱秀美(https://m.ixiumei.com/)
    3. yoka时尚网(http://www.yoka.com/dna/m/)
    4. 美妆网(http://www.chinabeauty.cn/)
    5. 新华网(http://m.xinhuanet.com)
    6. 36氪(https://36kr.com)
    7. 太平洋时尚网(https://www.pclady.com.cn/)
    8. 网易新闻
    9. cnbeta(https://m.cnbeta.com/)
    10. 少数派(https://sspai.com/)
    11. 经济日报(https://www.jingjiribao.cn)
    12. 中国青年网(http://m.youth.cn/)
    13. 妈妈网(http://m.mama.cn/)
    14. 搞笑视频网(需浏览器手机模式查看)(http://www.xjnan.com/)
    15. 投资界(https://m.pedaily.cn/)
    16. zol笑话大全(http://xiaohua.zol.com.cn/)
    17. 多玩搞笑囧图(http://tu.duowan.cn/bxgif)(先不做pass, 得用driver, 发布太慢, pass)
    18. 嗡啪搞笑(http://wengpa.com/)
    19. 微短视频网(https://www.wdace.com/)(视频为iframe内切, 先不做)
    20. 搞笑视频网(https://www.gaoxiaovod.com/)(部分视频from youku, 需driver)
    21. 图虫视频网(https://tuchong.com/video/)(need driver, 可做, 根据列表页获取share_url然后auto)
    22. 咪咕视频网(http://m.miguvideo.com/)(可取里面的短视频的接口部分)
    23. 浙江资讯-手机新浪网(http://zj.sina.cn/news/list-p1.d.html)
    25. 金华新闻网(新闻板块: https://www.jhnews.com.cn/xw/)(更新慢, pass)
    26. 金华19楼(https://jinhua.19lou.com/)
    28. 金东新闻网(http://jdnews.zjol.com.cn/)(多为纯文字文章, pass)
    
视频地址解析神器: https://www.urlgot.top/
    
news_media_ranking_url(https://top.chinaz.com/hangye/index_news.html)
"""

from os import getcwd
from os.path import abspath
from ftfy import fix_text
from requests import session
from random import choice as random_choice
from random import sample as random_sample
from random import random as random_random

from my_items import WellRecommendArticle
from settings import (
    ARTICLE_ITEM_LIST,
    MY_SPIDER_LOGS_PATH,
    PHANTOMJS_DRIVER_PATH,
    FIREFOX_DRIVER_PATH,
    CHROME_DRIVER_PATH,
    IP_POOL_TYPE,)

from fzutils.spider.fz_driver import (
    PHANTOMJS,
    FIREFOX,
    CHROME,
    PC,
    PHONE,
    BaseDriver,)
from fzutils.internet_utils import _get_url_contain_params
from fzutils.data.list_utils import list_remove_repeat_dict_plus
from fzutils.spider.selector import (
    async_parse_field,
    parse_field,)
from fzutils.spider.async_always import *

class ArticleParser(AsyncCrawler):
    """article spider"""
    def __init__(self, logger=None, loop=None, *params, **kwargs):
        AsyncCrawler.__init__(
            self,
            *params,
            **kwargs,
            log_print=True,
            logger=logger,
            is_new_loop=False,
            loop=loop,
            log_save_path=MY_SPIDER_LOGS_PATH + '/articles/_/',
            ip_pool_type=IP_POOL_TYPE)
        self.request_num_retries = 6
        # api data
        self.hook_target_api_data = None

    async def _parse_article(self, article_url) -> dict:
        """
        解析文章内容
        :param article_url: 待抓取文章的url
        :return:
        """
        # 设置obj_origin_dict
        self.obj_origin_dict = await self._get_obj_origin()
        child_debug = await self.is_child_can_debug(article_url)
        if not child_debug:
            self.lg.error('article_url未匹配到对象 or debug未开启!')
            return {}

        try:
            article_url_type = await self._judge_url_type(article_url=article_url)
            parse_obj = await self._get_parse_obj(article_url_type=article_url_type)
            # self.lg.info(article_url_type)
            # pprint(parse_obj)
        except (ValueError, NotImplementedError):
            # NotImplementedError: article_url未知!
            self.lg.error('遇到错误: ', exc_info=True)
            return {}

        article_html, video_url = await self._get_article_html(
            article_url=article_url,
            article_url_type=article_url_type)
        # self.lg.info(article_html)
        try:
            title = await self._get_article_title(
                parse_obj=parse_obj,
                target_obj=article_html,
                video_url=video_url)
            author = await self._get_author(
                parse_obj=parse_obj,
                target_obj=article_html,
                video_url=video_url)
            head_url = await self._get_head_url(
                parse_obj=parse_obj,
                target_obj=article_html,
                video_url=video_url,)
            content = await self._get_article_content(
                parse_obj=parse_obj,
                target_obj=article_html,
                article_url=article_url,
                video_url=video_url,)
            # print(content)
            create_time = await self._get_article_create_time(
                parse_obj=parse_obj,
                target_obj=article_html,
                video_url=video_url,
                article_url=article_url,)
            comment_num = await self._get_comment_num(parse_obj=parse_obj, target_obj=article_html)
            fav_num = await self._get_fav_num(parse_obj=parse_obj, target_obj=article_html)
            praise_num = await self._get_praise_num(parse_obj=parse_obj, target_obj=article_html)
            tags_list = await self._get_tags_list(
                parse_obj=parse_obj,
                video_url=video_url,
                target_obj=article_html)
            profile = await self._get_profile(parse_obj=parse_obj, target_obj=article_html)
            site_id = await self._get_site_id(article_url_type=article_url_type)
        except (AssertionError, Exception):
            self.lg.error('遇到错误:', exc_info=True, stack_info=False)
            return {}

        _ = WellRecommendArticle()
        _['nick_name'] = author
        _['head_url'] = head_url
        _['profile'] = profile
        _['share_id'] = await self._get_share_id(
            article_url_type=article_url_type,
            article_url=article_url,
            video_url=video_url,
            parse_obj=parse_obj,)
        _['title'] = title
        _['comment_content'] = ''
        _['share_img_url_list'] = []
        _['goods_id_list'] = []
        _['div_body'] = content
        _['gather_url'] = article_url       # wx 阅读原文跳出个验证
        _['create_time'] = create_time
        _['site_id'] = site_id
        _['goods_url_list'] = []
        _['tags'] = tags_list
        _['share_goods_base_info'] = []     # [{'goods_id': 'xxx', 'img_url': 'xxx'}, ...]
        _['video_url'] = video_url
        _['likes'] = praise_num
        _['collects'] = fav_num
        _['comment_num'] = comment_num
        _['short_name'] = article_url_type

        return dict(_)

    async def get_article_list_by_article_type(self, article_type: str) -> list:
        """
        根据文章类型获取article list
        :param article_type:
        :return:
        """
        if article_type == 'zq':
            return await self.get_zq_article_list()

        elif article_type == 'hk':
            return await self.get_hk_article_list()

        elif article_type == 'lfd':
            return await self.get_lfd_article_list()

        elif article_type == 'gxg':
            return await self.get_gxg_article_list()

        elif article_type == 'pp':
            return await self.get_pp_article_list()

        elif article_type == 'kr':
            return await self.get_kr_article_list()

        elif article_type == 'dfsp':
            return await self.get_dfsp_article_list()

        elif article_type == 'lsp':
            return await self.get_lsp_article_list()

        elif article_type == 'mp':
            return await self.get_mp_article_list()

        elif article_type == 'klm':
            return await self.get_klm_article_list()

        elif article_type == 'jrxsp':
            return await self.get_jrxsp_article_list()

        elif article_type == 'jhgzw':
            return await self.get_jhgzw_article_list()

        elif article_type == 'jhrx':
            return await self.get_jhrx_article_list()

        elif article_type == 'jhwb':
            return await self.get_jhwb_article_list()

        elif article_type == 'jhbdsv':
            return await self.get_jhbdsv_article_list()

        elif article_type == 'bdqmxsv':
            return await self.get_bdqmxsv_article_list()

        elif article_type == 'dy0':
            return await self.get_dy0_article_list()

        elif article_type == 'jhzjol':
            return await self.get_jhzjol_article_list()

        else:
            raise NotImplemented

    async def get_jhzjol_article_list(self) -> list:
        """
        根据jhzjol 即时报道列表
        来源: http://jinhua.zjol.com.cn/jsbd/index.shtml
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 2):
                # 其实不需要page_num, 此处只是做个标记
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where jhzjol: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_jhzjol_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_jhzjol_recommend_article_list_by_page_num(self, page_num: int) -> list:
        # 只取第一页的即时数据
        headers = get_random_headers(
            connection_status_keep_alive=False,)
        headers.update({
            'Proxy-Connection': 'keep-alive',
            # 'Referer': 'http://jinhua.zjol.com.cn/jsbd/index_1.shtml',
        })
        body = Requests.get_url_body(
            url='http://jinhua.zjol.com.cn/jsbd/index.shtml',
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries, )
        assert body != ''
        # self.lg.info(body)

        article_div_list_sel = {
            'method': 'css',
            'selector': 'ul.newsLi li a',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=body,
            logger=self.lg,
            is_first=False, )
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'a ::attr("href")',
        }
        article_id_sel = {
            'method': 're',
            'selector': 't\d+_(\d+)\.shtml',
        }
        title_sel = {
            'method': 'css',
            'selector': 'a ::text',
        }
        # 电影时长(无)
        res = []
        for item in article_div_list:
            try:
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_url != ''
                article_url = article_url.replace('//', 'http://')
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_id != ''
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert title != ''
                if len(title) >= 30:
                    continue

                # 电影时长无, pass

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('jhzjol::123')
                'uid': get_uuid3(target_str='{}::{}'.format('jhzjol', article_id)),
                'article_type': 'jhzjol',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] jhzjol::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_dy0_article_list(self) -> list:
        """
        根据dy app 搜索页面分享出来的视频榜(均只有单页)
        来源: https://www.iesdouyin.com/share/billboard/?id=0&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = [{
                'video_rank_type': 'default',
            },{
                'video_rank_type': 'positive',
            }]

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where dy0: video_rank_type:{}]...'.format(
                k['video_rank_type'],
            )

        def get_now_args(k) -> list:
            return [
                k['video_rank_type'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_dy0_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_dy0_recommend_article_list_by_page_num(self, video_rank_type: str) -> list:
        """
        根据video_rank_type来解析对应的视频榜单(均只有单页)
        :param video_rank_type: 'defalut' 默认视频榜 or 'positive' 正能量榜
        :return:
        """
        # 根据dy app 搜索页面分享出来的视频榜(均只有单页)
        # 来源: https://www.iesdouyin.com/share/billboard/?id=0&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy
        headers = get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            upgrade_insecure_requests=False,
            cache_control='', )
        headers.update({
            'authority': 'www.iesdouyin.com',
            'accept': 'application/json',
            'x-requested-with': 'XMLHttpRequest',
            # 'referer': 'https://www.iesdouyin.com/share/billboard/?id=0&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy',
        })
        try:
            # 避免返回数据无法解码
            headers.pop('accept-encoding')
        except Exception:
            pass
        if video_rank_type == 'default':
            # 视频榜
            params = None
        elif video_rank_type == 'positive':
            # 正能量榜
            params = (
                ('type', 'positive'),
            )
        else:
            raise ValueError('video_rank_type 值异常!')

        body = Requests.get_url_body(
            url='https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/aweme/',
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries, )
        assert body != ''
        # self.lg.info(body)

        data = article_div_list = json_2_dict(
            json_str=body,
            logger=None,
            default_res={}, ).get('aweme_list', [])
        assert data != []
        # pprint(data)

        res = []
        for item in article_div_list:
            try:
                title = item.get('aweme_info', {}).get('desc', '')
                assert title != ''
                article_url = item.get('aweme_info', {}).get('share_url', '')
                assert article_url != ''

                article_id = item.get('aweme_info', {}).get('aweme_id', '')
                assert article_id != ''
                if len(title) >= 30:
                    continue

                # 视频时长(因为多为几十秒的小视频), pass
            except Exception:
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('dy::123')
                'uid': get_uuid3(target_str='{}::{}'.format('dy', article_id)),
                'article_type': 'dy',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] dy0::video_rank_type:{}'.format(
            '+' if res != [] else '-',
            video_rank_type,
        ))

        return res

    async def get_bdqmxsv_article_list(self) -> list:
        """
        获取百度app 的全屏小视频的list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 10):
                # 其实不需要page_num, 此处只是做个标记
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where bdqmxsv: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_bdqmxsv_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_bdqmxsv_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        解析bdqmxsv 单页的小视频article_list
        :param page_num:
        :return:
        """
        # 百度app的小视频发现接口, 其中的全屏视频文章可直接被抓取
        headers = {
            'Host': 'mbd.baidu.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '4557',
            # 'X-BD-QUIC': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'X-BDBoxApp-NetEngine': '3',
            'User-Agent': get_random_phone_ua(),
        # 'Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 SP-engine/2.18.0'
            # 'X-Bd-Traceid': '644a9f61e6cc425e8df842d2cb926de9',
            'Accept': '*/*',
            # 'X-TurboNet-Info': '2.13.2679.177',
            'Accept-Encoding': 'gzip, deflate',
        }

        params = (
            ('action', 'feed'),
            ('cmd', '210'),
            # ('maid', '_a2S8_aq28_qa28qiPSOtj8Pvag3h2aajiXT8jukvNlza-uNzuB3uli6-u_KO-ifY0HJ8lukSugkuXa90ivhI_PSv8oIi2ihgCSaa_asS8_M82uazxqSC'),
            ('refresh', '1'),
            ('imgtype', 'webp'),
            ('cfrom', '1099a'),
            ('from', '1099a'),
            ('network', '1_0'),
            ('osbranch', 'i0'),
            ('osname', 'baiduboxapp'),
            ('service', 'bdbox'),
            # ('sid', '1027585_4-2600_6645-1027088_2-1027514_1-1027521_1-1027598_3-3081_8171-5238_7311-2696_6930-1027056_2-3057_8089-5618_8591-1027583_1-1027195_1-1027384_2-1027255_3-1027604_1-5456_8016-1026924_1-5306_7565-1027258_2-3270_8882-2946_7781-1027230_2-5524_8269-1027659_1-2929_7702-1027285_1-1027328_5-1027599_1-1472_3438-5579_8458-3037_8036-1027425_3-1027641_1-1027564_2-3000026_2-1027249_1-1027654_1-1027525_2-5529_8280-1027151_2-5566_8411-1027577_2-5562_8387-1027102_1-5571_8441-1027346_1-1021859_1-5409_7877-3039_8040-5586_8486-5546_8581-1027597_2-1027562_1-1027251_1-5525_8271-1021774_1-2512_6387-2859_7452-1027460_2-1027128_2-1027379_1-1027652_2-2939_7745-1027218_1-1027225_1-1026985_1'),
            ('sst', '0'),
            ('st', '0'),
            ('ua', '1668_2224_iphone_11.22.0.17_0'),
            ('uid', 'E4317D7927A4F423B2A894710C308D015F8D69D51OMTBGHBERB'),
            # ('ut', 'iPad7,3_13.3.1'),
            # ('zid', '9iAc0yzbau51GKO563M1gzHzaPoPDD_d8nXwjCKxdBLITCmV4uqwJmkYrkuarE6BQqUXF7INisVWgScgYhwZ0qQ'),
        )

        data = {
            # 'data': '{\n  "upload_ids" : [\n    {\n      "clk" : 0,\n      "id" : "sv_5653763656459563687",\n      "show" : 0,\n      "clk_ts" : 0,\n      "show_ts" : 0\n    },\n    {\n      "clk" : 0,\n      "id" : "sv_3599925748637729943",\n      "show" : 0,\n      "clk_ts" : 0,\n      "show_ts" : 0\n    },\n    {\n      "clk" : 0,\n      "id" : "sv_5250727945753531281",\n      "show" : 0,\n      "clk_ts" : 0,\n      "show_ts" : 0\n    },\n    {\n      "clk" : 0,\n      "id" : "sv_4823468498756614746",\n      "show" : 1,\n      "clk_ts" : 0,\n      "show_ts" : 1587165880\n    },\n    {\n      "clk" : 0,\n      "id" : "sv_4439062174156612467",\n      "show" : 1,\n      "clk_ts" : 0,\n      "show_ts" : 1587165886\n    },\n    {\n      "clk" : 0,\n      "id" : "sv_5248424962721750237",\n      "show" : 1,\n      "clk_ts" : 0,\n      "show_ts" : 1587165886\n    },\n    {\n      "clk" : 0,\n      "id" : "sv_4130330140644084020",\n      "show" : 1,\n      "clk_ts" : 0,\n      "show_ts" : 1587165880\n    },\n    {\n      "clk" : 0,\n      "id" %3...'
            'data': dumps({
                "upload_ids": [
                    {
                        "clk": 0,
                        "id": "sv_5653763656459563687",
                        "show": 0,
                        "clk_ts": 0,
                        "show_ts": 0
                    },
                    {
                        "clk": 0,
                        "id": "sv_3599925748637729943",
                        "show": 0,
                        "clk_ts": 0,
                        "show_ts": 0
                    },
                    {
                        "clk": 0,
                        "id": "sv_5250727945753531281",
                        "show": 0,
                        "clk_ts": 0,
                        "show_ts": 0
                    },
                    {
                        "clk": 0,
                        "id": "sv_4823468498756614746",
                        "show": 1,
                        "clk_ts": 0,
                        "show_ts": datetime_to_timestamp(get_shanghai_time()),  # 1587165880
                    },
                    {
                        "clk": 0,
                        "id": "sv_4439062174156612467",
                        "show": 1,
                        "clk_ts": 0,
                        "show_ts": datetime_to_timestamp(get_shanghai_time())
                    },
                    {
                        "clk": 0,
                        "id": "sv_5248424962721750237",
                        "show": 1,
                        "clk_ts": 0,
                        "show_ts": datetime_to_timestamp(get_shanghai_time())
                    },
                    {
                        "clk": 0,
                        "id": "sv_4130330140644084020",
                        "show": 1,
                        "clk_ts": 0,
                        "show_ts": datetime_to_timestamp(get_shanghai_time())
                    },
                ]})
        }
        body = Requests.get_url_body(
            method='post',
            url='https://mbd.baidu.com/searchbox',
            headers=headers,
            params=params,
            data=data,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,)
        assert body != ''
        data = article_div_list = json_2_dict(
            json_str=body,
            logger=self.lg).get('data', {}).get('210', {}).get('itemlist', {}).get('items', [])
        # pprint(data)

        res = []
        for item in article_div_list:
            try:
                title = item.get('data', {}).get('title', '')
                assert title != ''
                _mode = item.get('data', {}).get('mode', '')
                assert _mode != ''
                article_url = item.get('data', {}).get('videoInfo', {}).get('pageUrl', '')
                assert article_url != ''

                article_id = re.compile('&vid=(\d+)').findall(article_url)[0]
                assert article_id != ''
                # self.lg.info('mode: {}, title: {}, article_url: {}'.format(_mode, title, article_url))

                if len(title) >= 30:
                    continue

                if '王者荣耀' in title \
                        or '王者农药' in title \
                        or '绝地求生' in title \
                        or '英雄联盟' in title:
                    continue

                # 视频时长(因为多为几十秒的小视频), pass
            except Exception:
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('bdqmxsv::123')
                'uid': get_uuid3(target_str='{}::{}'.format('bdqmxsv', article_id)),
                'article_type': 'bdqmxsv',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] bdqmxsv::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_jhbdsv_article_list(self) -> list:
        """
        获取百度app 金华本地的推荐中的短视频list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 20):
                # 去掉时长过长的短视频后列表较少(本来请求一次就取短视频文章), 此处增加数量
                # 每日更新有限, 就获取前几页的, 其实不需要page_num, 此处只是做个标记
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where jhbdsv: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_jhbdsv_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_jhbdsv_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        解析jhbdsv 单页的短视频article_list
        :param page_num: 此处无用途, 只做标记
        :return:
        """
        # 根据百度app的金华本地接口列表数据(包含视频)(也只处理视频)
        # 测试发现其中返回的数据中图文文章的prefetch_html字段打开的页面图片都是异常的(图片只能在百度app里面调起), pass
        headers = {
            'Host': 'mbd.baidu.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '601',
            # 'X-BDBoxApp-NetEngine': '3',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'X-Bd-Traceid': '16fe51d50af744aa9f405a6674a0ece3',
            # 'X-TurboNet-Info': '2.13.2679.177',
            'User-Agent': get_random_phone_ua(),  # 'BaiduBoxApp/11.22.0 iPad; CPU OS 13_3_1 like Mac OS X'
            'Accept-Encoding': 'gzip, deflate',
        }
        params = (
            ('action', 'feed'),
            ('cmd', '206'),
            ('refresh', '0'),
            ('cfrom', '1099a'),
            ('from', '1099a'),
            ('network', '1_0'),
            ('osbranch', 'i0'),
            ('osname', 'baiduboxapp'),
            # ('puid', '_avrijOq2iAqAqqqB'),
            ('service', 'bdbox'),
            # ('sid', '5279_7493-5343_7673-1027255_3-1027249_1-3108_8246-1027599_1-5420_7915-5159_7064-5318_7602-5505_8213-2387_6070-5546_8581-3200_8608-5409_7877-1027056_2-3057_8089-1768_6301-2849_7423-1027525_2-3085_8180-3188_8547-5276_7485-5177_7115-5566_8411-5482_8122-1027088_2-5247_7339-2411_6133-5553_8355-5351_7695-3022_7980-5358_7713-2583_6589-1027151_2-2964_7829-5270_7472-2422_6166-3092_8204-5344_7676-5525_8271-5557_8366-1027564_2-5508_8414-5297_7538-1027652_2-5426_7932-5291_7522-5309_7573-5188_7161-2558_7271-1027384_2-2966_7835-5164_7078-5295_7533-5618_8591-1869_4509-5568_8429-1027604_1-1027379_1-1027654_1-5288_7517-3072_8145-3234_8756-5306_7565-2119_5266-1549_3643-2702_6941-5397_7837-5292_7525-5605_8537-5189_7164-3195_8561-2929_7702-1027562_1-5623_8610-5456_8016-3281_8984-5571_8441-2762_7136-5437_7972-5399_7843-1027251_1-1027195_1-5382_7800-3021_7978-3037_8036-5305_7560-1027102_1-1026985_1-1027583_1-5434_7961-5524_8269-2939_7745-5529_8280-2132_5301-5287_7515-1021859_1-1027577_2-2962_7825-1027346_1-2512_6387-1027128_2-5511_8234-5562_8387-1026924_1-1892_4570-5302_7555-1027460_2-5253_7382-5540_8312-5191_7167-2859_7452-5258_7413-5380_7796-3000026_2-1021774_1-5501_8201-2696_6930-5337_8416-5356_7706-1027230_2-5208_7208-3270_8882-3068_8126-2701_6939-1027218_1-5495_8181-5244_7333-3095_8211-3081_8171-2429_6181-2720_7764-1027225_1-3094_8208-5354_7701-3066_8262-2407_6127-1756_4144-1027425_3-5290_7521-5289_7518-3008_7953-1472_3438-3051_8075-571_1173-5488_8587-5260_7422-5196_7178-5326_7620-5514_8240-5539_8310-5586_8486-1027514_1-965_2041-1027258_2-5274_7482-5465_8048-2991_7919-5474_8088-5238_7311-2949_7792-5304_7558-1027521_1-3269_8880-5341_7661-5396_7836-2734_7019-5277_7487-1027659_1-5229_7291-2862_7464-3039_8040-1027328_5-1027641_1-1027597_2-2946_7781-2520_6890-1027285_1-5476_8091-3150_8396-5579_8458-3038_8037-3246_8805-5621_8606-2163_5390-1027585_4-2600_6645-5551_8343-5507_8218-5552_8352-1027598_3-5387_7815-2466_6272'),
            ('sst', '0'),
            ('st', '0'),
            ('ua', '1668_2224_iphone_11.22.0.17_0'),
            ('uid', 'E4317D7927A4F423B2A894710C308D015F8D69D51OMTBGHBERB'),
            ('ut', 'iPad7,3_13.3.1'),
            # ('zid', '9iAc0yzbau51GKO563M1gzHzaPoPDD_d8nXwjCKxdBLL_jVT_hAYpPuHPN7r33duZtuXxOapOpFhVJsy0VCBMVg'),
        )
        data = {
            # 'data': '{"direction":"auto","refresh_type":0,"bundleVersion":"2.80.57","source":"bdbox_feed_attentiontab","upload_ids":[],"info":{"location":"120.072277,28.962932,---"},"data":{"tab_id":"109999333","tab_name":"","is_sub":0,"last_update_time":0,"session_id":"1587166932496","click_id":"f7c2394b4a3a374e9565268449e1f8b7","refresh_index":1,"refresh_count":1,"refresh_state":4,"pre_render":0,"context":{}}}'
            'data': dumps({
                'bundleVersion': '2.80.57',
                'data': {
                    # 'click_id': 'f7c2394b4a3a374e9565268449e1f8b7',
                    'context': {},
                    'is_sub': 0,
                    'last_update_time': 0,
                    'pre_render': 0,
                    'refresh_count': 1,
                    'refresh_index': 1,
                    'refresh_state': 4,
                    'session_id': get_now_13_bit_timestamp(),
                    'tab_id': '109999333',
                    'tab_name': ''
                },
                'direction': 'auto',
                'info': {'location': '120.072277,28.962932,---'},
                'refresh_type': 0,
                'source': 'bdbox_feed_attentiontab',
                'upload_ids': []
            })
        }
        body = Requests.get_url_body(
            method='post',
            url='https://mbd.baidu.com/searchbox',
            headers=headers,
            params=params,
            data=data,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=6,)
        assert body != ''
        # self.lg.info(body)

        data = article_div_list = json_2_dict(
            json_str=body,
            logger=self.lg, ).get('data', {}).get('206', {}).get('itemlist', {}).get('items', [])
        # pprint(data)

        res = []
        for item in article_div_list:
            try:
                title = item.get('data', {}).get('title', '')
                assert title != ''
                _mode = item.get('data', {}).get('mode', '')
                assert _mode != ''
                if _mode == 'video':
                    article_url = item.get('data', {}).get('videoInfo', {}).get('pageUrl', '')
                else:
                    # 跳过图文文章, 因为其中图片只能在百度app里面调起
                    # article_url = item.get('data', {}).get('prefetch_html', '')
                    continue
                assert article_url != ''

                article_id = re.compile('sv_(\d+)').findall(article_url)[0]
                assert article_id != ''

                if len(title) >= 30:
                    continue

                # 视频时长
                # eg: '03:29'
                video_duration = item.get('data', {}).get('duration', '')
                assert video_duration != ''
                video_duration_minute, video_duration_second = video_duration.split(':')
                if (int(video_duration_minute) * 60 + int(video_duration_second)) >= 5. * 60:
                    # 5分钟以上不要
                    continue

                # self.lg.info('mode: {}, title: {}, video_duration: {}, article_url: {}'.format(_mode, title, video_duration, article_url))
            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('jhbdsv::123')
                'uid': get_uuid3(target_str='{}::{}'.format('jhbdsv', article_id)),
                'article_type': 'jhbdsv',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] jhbdsv::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_jhwb_article_list(self) -> list:
        """
        获取jhwb m站首页的文章推荐
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 10):
                # 每日更新有限, 就获取前几页的
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where jhwb: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_jhwb_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_jhwb_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        获取jhwb 单页article_list
        :param page_num:
        :return:
        """
        headers = get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            upgrade_insecure_requests=False,
            cache_control='',
        )
        headers.update({
            'authority': 'www.96356.in',
            'accept': 'text/html, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            # 'referer': 'https://www.96356.in/',
        })
        url = 'https://www.96356.in/page/{}'.format(page_num)
        body = Requests.get_url_body(
            url=url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=6,
            proxy_type=PROXY_TYPE_HTTPS, )
        assert body != ''
        # self.lg.info(body)

        article_div_list_sel = {
            'method': 'css',
            'selector': 'article.excerpt',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=body,
            logger=self.lg,
            is_first=False, )
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'h2 a ::attr("href")',
        }
        article_id_sel = {
            'method': 're',
            'selector': '/articles/(\d+)',
        }
        title_sel = {
            'method': 'css',
            'selector': 'h2 a ::text',
        }
        # 电影时长(无)
        res = []
        for item in article_div_list:
            try:
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_url != ''
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_id != ''
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert title != ''
                if len(title) >= 30:
                    continue

                # 电影时长无, pass

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('jhwb::123')
                'uid': get_uuid3(target_str='{}::{}'.format('jhwb', article_id)),
                'article_type': 'jhwb',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] jhwb::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_jhrx_article_list(self) -> list:
        """
        获取jhrx m站首页的最新热点页面数据
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 15):
                # 每日更新有限, 就获取前几页的, 并不能返回全部前15页的, 后续是无返回的
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where jhrx: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_jhrx_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_jhrx_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        获取单页article_list
        :param page_num:
        :return:
        """
        headers = get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            upgrade_insecure_requests=False,
            cache_control='',
        )
        headers.update({
            'accept': 'application/json',
            'referer': 'http://m.0579.cn/',
            'X-Requested-With': 'XMLHttpRequest',
        })
        params = (
            ('getmsg', '1'),
            ('page', str(page_num)),  # 1, 2, 3, ...
            ('last_time', '0' if page_num == 1 else get_now_13_bit_timestamp()[0:10]),  # 第一页为'0', 后面为当前10位时间戳
        )

        body = Requests.get_url_body(
            url='http://m.0579.cn/index.php',
            headers=headers,
            params=params,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS, )
        assert body != ''
        # self.lg.info(body)

        data = json_2_dict(
            json_str=body,
            logger=self.lg, ).get('data', [])
        # pprint(data)
        article_div_list = data

        # 电影时长(无)
        res = []
        for item in article_div_list:
            try:
                article_id = item.get('to_id', '')
                assert article_id != ''
                article_url = 'http://m.0579.cn/read.php?tid={}'.format(article_id)
                assert article_url != ''
                title = item.get('title', '')
                assert title != ''
                if len(title) >= 30:
                    continue

                # 电影时长无, pass

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('jhrx::123')
                'uid': get_uuid3(target_str='{}::{}'.format('jhrx', article_id)),
                'article_type': 'jhrx',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })
        # pprint(res)

        self.lg.info('[{}] jhrx::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_jhgzw_article_list(self) -> list:
        """
        获取jhgzw 金华24小时的页面的数据
        :return:
        """
        # 采用金华24小时的页面的数据(即广众网的资讯点更多进入的首页的页面数据: https://news.jinhua.com.cn/), 因为其包括时事,生活, 奇闻, 突发的页面数据
        # 由于官网美食, 摄影, 活动等不更新, 此处不处理其页面数据, 视频的由于cp后台 不支持m3u8的下载, 也pass
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 8):
                # 每日更新有限, 就获取前几页的
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where jhgzw: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_jhgzw_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_jhgzw_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        根据page_num获取单页的article_list
        :return:
        """
        headers = get_random_headers(
            user_agent_type=0,
            cache_control='',)
        headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'referer': 'https://news.jinhua.com.cn/?pp=12',
        })
        params = (
            ('pp', str(12 * (page_num - 1))),  # 格式为: '0', '12', '24'
        )

        body = Requests.get_url_body(
            url='https://news.jinhua.com.cn/',
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,)
        assert body != ''
        # self.lg.info(body)

        article_div_list_sel = {
            'method': 'css',
            'selector': 'ul.teaser li h4',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=body,
            logger=self.lg,
            is_first=False, )
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'a ::attr("href")',
        }
        article_id_sel = {
            'method': 're',
            'selector': '/(\d+)\.html',
        }
        title_sel = {
            'method': 'css',
            'selector': 'a ::text',
        }
        # 电影时长(无)
        res = []
        for item in article_div_list:
            try:
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_url != ''
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_id != ''
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert title != ''
                if len(title) >= 30:
                    continue

                if 'jinhua.com.cn' not in article_url:
                    # 去掉不合法的网址
                    continue

                if '新型冠状病毒肺炎疫情通报' in title or \
                        '新型冠状病毒肺炎疫情情况' in title:
                    # 去掉每日播报
                    continue

                # 电影时长无, pass

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('jhgzw::123')
                'uid': get_uuid3(target_str='{}::{}'.format('jhgzw', article_id)),
                'article_type': 'jhgzw',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] jhgzw::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_jrxsp_article_list(self) -> list:
        """
        获取jrxsp 首页每个分类的的article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            # m站首页接口
            sort_dict_list = [
                # 不取推荐的, 因为推荐的常含游戏的
                # {
                #     'name': '推荐',
                #     'sort_key': 'tuijian',
                #     'page_num': 1,          # 推荐只有一页
                # },
                {
                    'name': '娱乐',
                    'sort_key': 'yule',
                },
                {
                    'name': '搞笑',
                    'sort_key': 'gaoxiao',
                },
                {
                    'name': '影视',
                    'sort_key': 'yingshi',
                },
                {
                    'name': '美食',
                    'sort_key': 'meishi',
                },
                {
                    'name': '音乐',
                    'sort_key': 'yinyue',
                },
                {
                    'name': '儿童',
                    'sort_key': 'ertong',
                },
                {
                    'name': '体育',
                    'sort_key': 'tiyu',
                },
                {
                    'name': '综艺',
                    'sort_key': 'zongyi',
                },
                {
                    'name': '宠物',
                    'sort_key': 'chongwu',
                },
                {
                    'name': '生活',
                    'sort_key': 'shenghuo',
                },
            ]
            new_sort_dict_list = []
            for item in sort_dict_list:
                for page_num in range(1, 3):
                    # 取前面2页
                    tmp_item = item.copy()
                    tmp_item['page_num'] = page_num
                    new_sort_dict_list.append(tmp_item)

            sort_dict_list = new_sort_dict_list
            # pprint(sort_dict_list)

            for target_sort_dict in sort_dict_list:
                # mp视频更新有限, 就每个分类获取第2页的
                tasks_params_list.append(target_sort_dict)

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where jrxsp: sort_name: {}, sort_key: {}, page_num:{}]...'.format(
                k['name'],
                k['sort_key'],
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['sort_key'],
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_jrxsp_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_jrxsp_recommend_article_list_by_page_num(self, sort_key: str, page_num: int) -> list:
        """
        获取jrxsp 每个分类的某页article_list
        :param sort_key:
        :param page_num:
        :return:
        """
        headers = get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            cache_control='',
        )
        headers.update({
            'Proxy-Connection': 'keep-alive',
        })
        url = 'http://m.jrtb.net/{}'.format(sort_key)
        if page_num > 1:
            params = (
                ('page', page_num),
            )
        else:
            params = None

        body = Requests.get_url_body(
            url=url,
            headers=headers,
            params=params,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS, )
        assert body != ''
        # self.lg.info(body)

        article_div_list_sel = {
            'method': 'css',
            'selector': 'div.list_content section',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=body,
            logger=self.lg,
            is_first=False, )
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'a.article_link ::attr("href")',
        }
        article_id_sel = {
            'method': 're',
            'selector': '/(\w+)\.html',
        }
        title_sel = {
            'method': 'css',
            'selector': 'div.item_detail h3 ::text',
        }
        # 电影时长(无)
        res = []
        for item in article_div_list:
            try:
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_url != ''
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_id != ''
                article_url = 'http://m.jrtb.net/{}/{}.html'.format(
                    sort_key,
                    article_id)
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert title != ''
                if len(title) >= 30:
                    continue

                # 电影时长无, pass

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('jrxsp::123')
                'uid': get_uuid3(target_str='{}::{}'.format('jrxsp', article_id)),
                'article_type': 'jrxsp',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] jrxsp::sort_key:{}::page_num:{}'.format(
            '+' if res != [] else '-',
            sort_key,
            page_num,
        ))

        return res

    async def get_klm_article_list(self) -> list:
        """
        获取klm m站某几个分类的article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            # m站接口
            device_id = 'klm{}'.format(get_uuid1().replace('-', ''))
            channel_id_list = [
                '100',      # 小视频(全屏),
                # '42',       # 推荐的短视频, 这个不怎么更新 先不采集
            ]
            for channel_id in channel_id_list:
                for page_num in range(1, 30):
                    # klm视频更新有限
                    tasks_params_list.append({
                        'device_id': device_id,
                        'channel_id': channel_id,
                        'page_num': page_num,
                    })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where klm: channel_id: {}, page_num:{}]...'.format(
                k['channel_id'],
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['channel_id'],
                k['page_num'],
                k['device_id'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_klm_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_klm_recommend_article_list_by_page_num(self, channel_id, page_num: int, device_id) -> list:
        """
        获取klm 某个分类的单页接口数据
        :param channel_id:
        :param page_num:
        :param device_id: 使用同一个device_id, 来得到后续数据
        :return:
        """
        headers = get_random_headers(
            user_agent_type=1,
            upgrade_insecure_requests=False,
            cache_control='',
        )
        headers.update({
            'accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            # 'referer': 'http://www.klm123.com/mobile/index',
        })
        params = (
            ('channel_id', str(channel_id)),  # 小视频(全屏)为'100', 推荐为'42'
            ('page', str(page_num)),
            ('page_size', '6'),
        )
        # 必须, 否则获取到的数据值很少
        cookies = {
            'deviceId': device_id,
        }

        body = Requests.get_url_body(
            url='http://www.klm123.com/api/channel/videos',
            headers=headers,
            params=params,
            cookies=cookies,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries, )
        assert body != ''
        data = json_2_dict(
            json_str=body,
            default_res={},
            logger=self.lg, ).get('data', {}).get('videos', [])
        # pprint(data)

        res = []
        for item in data:
            try:
                article_id = item.get('video', {}).get('videoId', '')
                assert article_id != ''
                title = item.get('video', {}).get('title', '')
                assert title != ''
                article_url = item.get('video', {}).get('shareUrl', '')
                assert article_url != ''

                video_duration = int(item.get('video', {}).get('streams', [])[0].get('duration', '0'))
                if video_duration >= 5 * 60:
                    # 5分钟以上不要
                    continue

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('klm::123')
                'uid': get_uuid3(target_str='{}::{}'.format('klm', article_id)),
                'article_type': 'klm',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] klm::channel_id:{}::page_num:{}'.format(
            '+' if res != [] else '-',
            channel_id,
            page_num,
        ))

        return res

    async def get_mp_article_list(self) -> list:
        """
        获取mp pc 每个分类第二页的 article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            # pc站首页接口
            sort_dict_list = [
                {
                    'name': '热门',
                    'url': 'https://www.meipai.com/home/hot_timeline',
                    'tid': '',
                    'page_num': 2,
                },
                {
                    'name': '搞笑',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '13',
                    'page_num': 2,
                },
                {
                    'name': '爱豆',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '16',
                    'page_num': 2,
                },
                {
                    'name': '高颜值',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '474',
                    'page_num': 2,
                },
                {
                    'name': '舞蹈',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '63',
                    'page_num': 2,
                },
                {
                    'name': '音乐',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '62',
                    'page_num': 2,
                },
                {
                    'name': '美食',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '59',
                    'page_num': 2,
                },
                {
                    'name': '美妆',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '27',
                    'page_num': 2,
                },
                {
                    'name': '吃秀',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '423',
                    'page_num': 2,
                },
                {
                    'name': '萌宠',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '6',
                    'page_num': 2,
                },
                {
                    'name': '旅行',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '426',
                    'page_num': 2,
                },
                {
                    'name': '手工',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '450',
                    'page_num': 2,
                },
                {
                    'name': '运动',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '487',
                    'page_num': 2,
                },

                # 自己测试有返回值加的
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '2',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '3',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '4',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '5',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '15',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '18',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '19',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '20',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '22',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '23',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '26',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '27',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '28',
                    'page_num': 2,
                },
                {
                    'name': '未知',
                    'url': 'https://www.meipai.com/squares/new_timeline',
                    'tid': '30',
                    'page_num': 2,
                },
            ]
            for target_sort_dict in sort_dict_list:
                # mp视频更新有限, 就每个分类获取第2页的
                tasks_params_list.append(target_sort_dict)

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where mp: sort_name: {}, tid: {}, page_num:{}]...'.format(
                k['name'],
                k['tid'],
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['url'],
                k['tid'],
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_mp_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_mp_recommend_article_list_by_page_num(self, url, tid, page_num: int) -> list:
        """
        根据分类id tid, page_num获取pc的article_list
        :param url:
        :param tid:
        :param page_num:
        :return:
        """
        # 不使用maxid, 默认只获取第二页的所有可获取到的
        max_id = ''
        headers = get_random_headers(
            upgrade_insecure_requests=False,
            cache_control='', )
        headers.update({
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            # 'referer': 'https://www.meipai.com/medias/hot',
        })
        params = [
            ('page', str(page_num)),    # 从第2页开始
            ('count', '96'),            # 12的倍数, 即返回的item数, 测试发现 可一次性返回需求总数据, 最大值为
        ]
        if page_num == 2:
            # 第二页 无maxid 字段
            pass
        else:
            params.append(
                ('maxid', str(max_id))
            )

        if tid != '':
            # 非热门则需要tid
            params.append(
                ('tid', str(tid)),
            )

        body = Requests.get_url_body(
            url=url,
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,)
        assert body != ''

        data = json_2_dict(
            json_str=body,
            default_res={},
            logger=None, ).get('medias', {})
        # pprint(data)

        res = []
        for item in data:
            try:
                article_url = item.get('url', '')
                assert article_url != ''
                article_id = str(item.get('id', ''))
                assert article_id != ''
                title = item.get('caption_complete', '').replace('\n', ' ')
                assert title != ''
                if len(title) >= 30:
                    continue

                video_duration = int(item.get('time', '0'))
                if video_duration >= 5 * 60:
                    # 5分钟以上不要
                    continue

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('mp::123')
                'uid': get_uuid3(target_str='{}::{}'.format('mp', article_id)),
                'article_type': 'mp',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] mp::tid:{}::page_num:{}'.format(
            '+' if res != [] else '-',
            tid,
            page_num,
        ))

        return res

    async def get_lsp_article_list(self) -> list:
        """
        获取lsp pc 排行榜(https://www.pearvideo.com/popular) article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            # 旗帜 只有第一页不做
            cate_id_list = [
                '',     # 总榜为空
                '1',    # 社会
                '2',    # 世界
                '3',    # 财富
                '4',    # 娱乐
                '5',    # 生活
                '6',    # 美食
                '8',    # 科技
                '9',    # 体育
                '10',   # 新知
                '31',   # 汽车
                '59',   # 音乐
            ]
            for cate_id in cate_id_list:
                for page_num in [0, 10]:
                    # 页面自增方式为: 0, 10, 20, 30, ...
                    # lsp视频排行榜更新有限, 就获取第一页的
                    tasks_params_list.append({
                        'cate_id': cate_id,
                        'page_num': page_num,
                    })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where lsp: cate_id: {}, page_num:{}]...'.format(
                k['cate_id'],
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['cate_id'],
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_lsp_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_lsp_recommend_article_list_by_page_num(self, cate_id, page_num: int):
        """
        根据cate_id, page_num获取pc排行榜的article_list
        :param cate_id:
        :param page_num:
        :return:
        """
        headers = get_random_headers(
            cache_control='', )
        headers.update({
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            # 'Referer': 'https://www.pearvideo.com/popular',
        })
        params = (
            ('reqType', '1'),
            ('categoryId', cate_id),  # 总榜'' 新知10 社会1 世界2 体育9 生活5 科技8 娱乐4 财富3 汽车31 美食6 音乐59 旗帜 只有第一页不做
            ('start', str(page_num)),  # 0, 10, 20, 30, ...
            # ('sort', '8'),              # 总榜8, 其他子分类第二页都是9, 测试发现可为''
            ('mrd', str(random_random())),  # eg: '0.0657313191878468'
        )

        body = Requests.get_url_body(
            url='https://www.pearvideo.com/popular_loading.jsp',
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,)
        # self.lg.info(body)
        assert body != ''

        article_div_list_sel = {
            'method': 'css',
            'selector': 'li.popularem',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=body,
            logger=self.lg,
            is_first=False,)
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'a.actplay ::attr("href")',
        }
        article_id_sel = {
            'method': 're',
            'selector': 'video_(\d+)',
        }
        title_sel = {
            'method': 'css',
            'selector': 'h2.popularem-title ::text',
        }
        # 电影时长
        video_duration_sel = {
            'method': 'css',
            'selector': 'div.cm-duration ::text',
        }
        # 电影时长(无)
        res = []
        for item in article_div_list:
            try:
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_url != ''
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_id != ''
                article_url = 'https://www.pearvideo.com/video_{}'.format(article_id)
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert title != ''
                if len(title) >= 30:
                    continue

                video_duration = parse_field(
                    parser=video_duration_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert video_duration != ''
                video_duration_minute, video_duration_second = video_duration.split(':')
                if (int(video_duration_minute) * 60 + int(video_duration_second)) >= 5 * 60:
                    # 5分钟以上不要
                    continue

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('lsp::123')
                'uid': get_uuid3(target_str='{}::{}'.format('lsp', article_id)),
                'article_type': 'lsp',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(res)
        self.lg.info('[{}] lsp::cate_id:{}::page_num:{}'.format(
            '+' if res != [] else '-',
            cate_id,
            page_num,
        ))

        return res

    async def get_dfsp_article_list(self) -> list:
        """
        获取dfsp pc热门视频(http://imedia.eastday.com/node2/2015imedia/rmsp/index.html)article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 8):
                # kr视频每日更新有限, 就获取前几页的
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where dfsp: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_dfsp_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_dfsp_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        根据page_num获取pc热门视频页的article_list
        :param page_num:
        :return:
        """
        headers = get_random_headers(
            cache_control='',)
        headers.update({
            # 'Referer': 'http://imedia.eastday.com/node2/2015imedia/rmsp/index.html',
        })
        url = 'http://imedia.eastday.com/node2/2015imedia/rmsp/index{}.html'.format(
            '' if page_num == 1 else page_num-1,
        )
        body = Requests.get_url_body(
            url=url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            encoding='gbk',)
        assert body != ''

        article_div_list_sel = {
            'method': 'css',
            'selector': 'ul.videolist5 li',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=body,
            logger=self.lg,
            is_first=False,)
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'p.tx5 a ::attr("href")',
        }
        article_id_sel = {
            'method': 're',
            'selector': '/(\w+)\.html',
        }
        title_sel = {
            'method': 'css',
            'selector': 'p.tx5 a ::text',
        }
        # 电影时长(无)
        res = []
        for item in article_div_list:
            try:
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_url != ''
                if 'http:' not in article_url:
                    article_url = 'http://imedia.eastday.com' + article_url
                else:
                    pass
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_id != ''
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert title != ''
                if len(title) >= 30:
                    continue

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('dfsp::123')
                'uid': get_uuid3(target_str='{}::{}'.format('dfsp', article_id)),
                'article_type': 'dfsp',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        self.lg.info('[{}] dfsp::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_kr_article_list(self) -> list:
        """
        获取kr pc首页(https://krcom.cn)最新推荐视频article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 8):
                # kr视频每日更新有限, 就获取前几页的
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where kr: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_kr_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_kr_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        根据page_num获取pc视频页的最新推荐article_list
        :param page_num:
        :return:
        """
        # 该接口偶尔会没数据
        headers = get_random_headers(
            upgrade_insecure_requests=False,
            cache_control='', )
        headers.update({
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'referer': 'https://krcom.cn/',
        })
        now_time = get_shanghai_time()
        # self.lg.info(now_time)
        # 格式: '5;2019111409' (当前小时还得减一小时)
        now_hour = int(str(now_time)[11:13])
        if now_hour > 0 and now_hour < 10:
            new_now_hour = '0' + str(now_hour - 1)
        elif now_hour == 0:
            new_now_hour = '23'
        else:
            new_now_hour = str(now_hour - 1)

        cursor = '{};{}{}{}{}'.format(
            page_num * 5,
            str(now_time)[0:4],
            str(now_time)[5:7],
            str(now_time)[8:10],
            new_now_hour,
        )
        # self.lg.info(cursor)
        params = (
            ('ajwvr', '6'),
            ('cursor', cursor),
            ('op', '4427060390002831'),
            ('__rnd', get_now_13_bit_timestamp()),
        )

        body = Requests.get_url_body(
            url='https://krcom.cn/aj/home/Recomalbum',
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,)
        data = Requests._wash_html(json_2_dict(
            json_str=body,
            default_res={},
            logger=self.lg,).get('data', ''))
        # print(data)

        # 组合生成url
        # 原生url
        # https://krcom.cn/1638781994/episodes/2358773:4259607863075356
        # channel_id=1504145281&vid=2358773:4326964350123027
        # https://krcom.cn/1504145281/episodes/2358773:4326964350123027

        article_div_list_sel = {
            'method': 'css',
            'selector': 'div.V_list_a',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=data,
            logger=self.lg,
            is_first=False, )
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'div.V_list_a ::attr("action-data")',
        }
        article_id_sel = {
            'method': 're',
            'selector': 'vid=(\d+\:\w+)',
        }
        channel_id_sel = {
            'method': 're',
            'selector': 'channel_id=(\d+)',
        }
        title_sel = {
            'method': 'css',
            'selector': 'h3 ::text',
        }
        # 电影时长
        video_duration_sel = {
            'method': 'css',
            'selector': 'span.time ::text',
        }
        res = []
        for item in article_div_list:
            try:
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_url != ''
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert article_id != ''
                channel_id = parse_field(
                    parser=channel_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert channel_id != ''
                article_url = 'https://krcom.cn/{}/episodes/{}'.format(channel_id, article_id)
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert title != ''
                if len(title) >= 30:
                    continue

                video_duration = parse_field(
                    parser=video_duration_sel,
                    target_obj=item,
                    logger=self.lg,
                    is_print_error=False,
                )
                assert video_duration != ''
                video_duration_minute, video_duration_second = video_duration.split(':')
                if (int(video_duration_minute) * 60 + int(video_duration_second)) >= 5 * 60:
                    # 5分钟以上不要
                    continue

            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('kr::123')
                'uid': get_uuid3(target_str='{}::{}'.format('kr', article_id)),
                'article_type': 'kr',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        self.lg.info('[{}] kr::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_pp_article_list(self) -> list:
        """
        获取pp的最新视频article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 8):
                # pp视频每日更新有限, 就获取前几页的
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where pp: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_pp_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_pp_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        根据page_num获取pc视频页的最新推荐article_list
        :param page_num:
        :return:
        """
        # 来源(https://www.thepaper.cn/) 点击视频
        headers = get_random_headers(
            upgrade_insecure_requests=False,
            cache_control='',
        )
        headers.update({
            'accept': 'text/html, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            # 'Referer': 'https://www.thepaper.cn/channel_26916',
        })
        params = (
            # ('channelID', '26916'),
            ('channelID', ''),
            ('pageidx', str(page_num)),
        )
        body = Requests.get_url_body(
            url='https://www.thepaper.cn/load_video_chosen.jsp',
            headers=headers,
            params=params,
            # cookies=cookies,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,)
        assert body != ''
        # self.lg.info(body)

        article_div_list_sel = {
            'method': 'css',
            'selector': 'li.video_news',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=body,
            is_first=False,
            logger=self.lg,)
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'div.video_list_pic a ::attr("href")',
        }
        article_id_sel = {
            'method': 're',
            'selector': 'newsDetail_forward_(\d+)',
        }
        title_sel = {
            'method': 'css',
            'selector': 'div.video_title ::text',
        }
        res = []
        for item in article_div_list:
            try:
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                )
                assert article_url != ''
                article_url = 'https://m.thepaper.cn/{}'.format(article_url)
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                )
                assert article_id != ''
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                )
                assert title != ''
            except AssertionError:
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('pp::123')
                'uid': get_uuid3(target_str='{}::{}'.format('pp', article_id)),
                'article_type': 'pp',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(article_url_list)
        self.lg.info('[{}] pp::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_gxg_article_list(self) -> list:
        """
        获取gxg的article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 8):
                # lfd每日更新有限, 就获取前7页的
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where gxg: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_gxg_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_gxg_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        根据page_num获取首页的最新推荐article_list
        :param page_num:
        :return:
        """
        headers = get_random_headers(
            user_agent_type=1,
            cache_control='',
        )
        headers.update({
            'Referer': 'https://m.gaoxiaogif.com/',
        })
        url = 'https://m.gaoxiaogif.com/index_{}.html'.format(page_num) \
            if page_num > 1 else 'https://m.gaoxiaogif.com/index.html'
        body = Requests.get_url_body(
            url=url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            encoding='gbk',)
        assert body != ''
        # self.lg.info(body)

        article_div_list_sel = {
            'method': 'css',
            'selector': 'div.text ul#tp_lists li.item',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=body,
            is_first=False,
            logger=self.lg, )
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'li a ::attr("href")',
        }
        article_id_sel = {
            'method': 're',
            'selector': '/(\d+)\.html',
        }
        title_sel = {
            'method': 'css',
            'selector': 'li h3 ::text',
        }
        res = []
        for item in article_div_list:
            try:
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                )
                assert article_url != ''
                article_url = 'https://m.gaoxiaogif.com' + article_url
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                )
                assert article_id != ''
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                )
                assert title != ''
            except AssertionError:
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('gxg::123')
                'uid': get_uuid3(target_str='{}::{}'.format('gxg', article_id)),
                'article_type': 'gxg',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(article_url_list)
        self.lg.info('[{}] gxg::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_lfd_article_list(self) -> list:
        """
        获取lfd的article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 8):
                # lfd每日更新有限, 就获取前6页的
                tasks_params_list.append({
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where lfd: page_num:{}]...'.format(
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_lfd_recommend_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_lfd_recommend_article_list_by_page_num(self, page_num: int) -> list:
        """
        根据page_num获取lfd首页的最新推荐article_list
        :param page_num:
        :return:
        """
        headers = get_random_headers(connection_status_keep_alive=False)
        headers.update({
            'Proxy-Connection': 'keep-alive',
        })
        url = 'http://www.laifudao.com/index_{}.html'.format(page_num)
        body = Requests.get_url_body(
            url=url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,)
        assert body != ''
        # print(body)

        article_div_list_sel = {
            'method': 'css',
            'selector': 'article',
        }
        article_div_list = parse_field(
            parser=article_div_list_sel,
            target_obj=body,
            is_first=False,
            logger=self.lg,)
        assert article_div_list != []
        # pprint(article_div_list)

        # 文章有图的选择器
        article_had_img_sel = {
            'method': 'css',
            'selector': 'div.post-content section.pic-content',
        }
        # 文章地址选择器
        article_url_sel = {
            'method': 'css',
            'selector': 'article h1 a ::attr("href")',
        }
        article_id_sel = {
            'method': 're',
            'selector': '/(\d+)\.htm',
        }
        title_sel = {
            'method': 'css',
            'selector': 'article h1 a ::text',
        }
        res = []
        for item in article_div_list:
            try:
                # 只要有图的, 纯文字无法发布
                article_had_img = parse_field(
                    parser=article_had_img_sel,
                    target_obj=item,
                    is_print_error=False,
                    logger=self.lg,
                )
                assert article_had_img != ''
                article_url = parse_field(
                    parser=article_url_sel,
                    target_obj=item,
                    logger=self.lg,
                )
                assert article_url != ''
                article_url = 'http://www.laifudao.com' + article_url
                article_id = parse_field(
                    parser=article_id_sel,
                    target_obj=article_url,
                    logger=self.lg,
                )
                assert article_id != ''
                title = parse_field(
                    parser=title_sel,
                    target_obj=item,
                    logger=self.lg,
                )
                assert title != ''
            except AssertionError:
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('lfd::123')
                'uid': get_uuid3(target_str='{}::{}'.format('lfd', article_id)),
                'article_type': 'lfd',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        # pprint(article_url_list)
        self.lg.info('[{}] lfd::page_num:{}'.format(
            '+' if res != [] else '-',
            page_num,
        ))

        return res

    async def get_hk_article_list(self) -> list:
        """
        获取hk的article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            # 分类
            self.hk_tab_name_list = [
                'yingshi',
                'yinyue',
                'gaoxiao',
                'vlog',
                'yule',
                # 'dongman',
                'shenghuo',
                'xiaopin',
                'zongyi',
                # 'youxi',
                'miaodong',
                'jiaoyu',
                'junshi',
                'keji',
                'qiche',
                'tiyu',
                'wenhua',
                'qinzi',
                'shehui',
                'sannong',
                'chongwu',
                'meishi',
                'shishang',
            ]
            # 随机赛选一个区间
            _ = random_sample(self.hk_tab_name_list, 5)
            for tab_name in _:
                tasks_params_list.append({
                    'tab_name': tab_name,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where hk: tab_name:{}]...'.format(
                k['tab_name'],
            )

        def get_now_args(k) -> list:
            return [
                k['tab_name'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_hk_recommend_article_list_by_tab_name,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',)
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_hk_recommend_article_list_by_tab_name(self, tab_name: str):
        """
        根据tab_name 获取hk推荐页的article_list
        :param tab_name:
        :return:
        """
        headers = get_random_headers(
            connection_status_keep_alive=False,
            upgrade_insecure_requests=False,
            cache_control='',)
        headers.update({
            'sec-fetch-mode': 'cors',
            'content-type': 'application/x-www-form-urlencoded',
            'referer': 'https://haokan.baidu.com/',
            'authority': 'haokan.baidu.com',
            'sec-fetch-site': 'same-origin',
        })
        params = (
            ('tab', tab_name),
            ('act', 'pcFeed'),
            ('pd', 'pc'),
            ('num', '5'),               # 返回数
            ('shuaxin_id', get_now_13_bit_timestamp()),
        )
        url = 'https://haokan.baidu.com/videoui/api/videorec'
        body = Requests.get_url_body(
            url=url,
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,)
        assert body != ''
        # self.lg.info(body)
        data = json_2_dict(
            json_str=body,
            default_res={},
            logger=self.lg,) \
            .get('data', {}) \
            .get('response', {}) \
            .get('videos', [])
        assert data != []
        # pprint(data)

        res = []
        for item in data:
            try:
                title = item.get('title', '')
                assert title != ''
                # 标题必须小于等于30
                assert len(title) <= 30
                article_id = item.get('id', '')
                assert article_id != ''
                video_play_url = item.get('play_url', '')
                # 跳过视频文章
                assert video_play_url != ''
                article_url = 'https://haokan.baidu.com/v?vid={}'.format(article_id)
            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('hk::123')
                'uid': get_uuid3(target_str='{}::{}'.format('hk', article_id)),
                'article_type': 'hk',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        self.lg.info('[{}] hk::tab_name:{}'.format(
            '+' if res != [] else '-',
            tab_name,
        ))

        return res

    async def get_zq_article_list(self) -> list:
        """
        获取zq的article_list
        :return:
        """
        def get_tasks_params_list() -> list:
            tasks_params_list = []
            for page_num in range(1, 5):
                # 蹿红页, 默认只有4页
                tasks_params_list.append({
                    'type': '1',
                    'page_num': page_num,
                })

            for page_num in range(1, 2):
                # 七天页, 默认只有1页
                tasks_params_list.append({
                    'type': '2',
                    'page_num': page_num,
                })

            for page_num in range(1, 3):
                # 总榜页, 默认只有2页
                tasks_params_list.append({
                    'type': '3',
                    'page_num': page_num,
                })

            return tasks_params_list

        def get_create_task_msg(k) -> str:
            return 'create task[where zq: type: {}, page_num: {}]...'.format(
                k['type'],
                k['page_num'],
            )

        def get_now_args(k) -> list:
            return [
                k['page_num'],
                k['type'],
            ]

        all_res = await get_or_handle_target_data_by_task_params_list(
            loop=self.loop,
            tasks_params_list=get_tasks_params_list(),
            func_name_where_get_create_task_msg=get_create_task_msg,
            func_name=self.get_zq_shoot_to_fame_article_list_by_page_num,
            func_name_where_get_now_args=get_now_args,
            func_name_where_handle_one_res=None,
            func_name_where_add_one_res_2_all_res=default_add_one_res_2_all_res,
            one_default_res=[],
            step=self.concurrency,
            logger=self.lg,
            get_all_res=True,
            concurrent_type=0,
        )
        all_res = list_remove_repeat_dict_plus(
            target=all_res,
            repeat_key='article_id',
        )
        # pprint(all_res)
        self.lg.info('all_res_len: {}'.format(len(all_res)))

        return all_res

    @catch_exceptions_with_class_logger(default_res=[])
    def get_zq_shoot_to_fame_article_list_by_page_num(self, page_num: int, _type: str) -> list:
        """
        根据page_num 获取zq蹿红页的article_list
        :param page_num: 1开始
        :return:
        """
        # rasp报错: Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'ssl_choose_client_version', 'unsupported protocol')],
        # 导致原因: 系统tls安全性提高了
        # 解决方案: 修改协议最低版本
        # $ vi /etc/ssl/openssl.cnf
        # [system_default_sect]
        # MinProtocol = TLSv1.2
        # CipherString = DEFAULT@SECLEVEL = 2
        # 修改为
        # [system_default_sect]
        # MinProtocol = TLSv1.0
        # CipherString = DEFAULT@SECLEVEL = 1
        headers = get_random_headers(
            user_agent_type=1,
            upgrade_insecure_requests=False,
            cache_control='',)
        headers.update({
            # 'Sec-Fetch-Mode': 'cors',
            # 'Sec-Fetch-Site': 'same-origin',
            'Origin': 'https://focus.youth.cn',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://focus.youth.cn/html/articleTop/mobile.html',
            'X-Requested-With': 'XMLHttpRequest',
        })
        data = dumps({
            'type': _type,
            'page': str(page_num),
            'catid': '0',
        })
        body = Requests.get_url_body(
            method='post',
            url='https://focus.youth.cn/WebApi/Article/top2',
            headers=headers,
            data=data,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,)
        assert body != ''
        # self.lg.info(body)

        data = json_2_dict(
            json_str=body,
            logger=self.lg,
            default_res={},).get('data', {}).get('items', [])
        assert data != []
        # pprint(data)

        res = []
        for item in data:
            try:
                title = item.get('title', '')
                assert title != ''
                # 标题必须小于等于30
                assert len(title) <= 30
                article_id = item.get('id', '')
                video_play_url = item.get('video_play_url', '')
                assert article_id != ''
                # 跳过视频文章
                assert video_play_url == ''
                # 跳过无图的
                _extra = item.get('extra', [])
                assert _extra != []
                article_url = 'https://focus.youth.cn/mobile/detail/id/{}#'.format(article_id)
            except (AssertionError, Exception):
                continue

            res.append({
                # db中存储的uid eg: get_uuid3('zq::123')
                'uid': get_uuid3(target_str='{}::{}'.format('zq', article_id)),
                'article_type': 'zq',
                'title': title,
                'article_id': str(article_id),
                'article_url': article_url,
            })

        self.lg.info('[{}] zq::type:{}::page_num:{}'.format(
            '+' if res != [] else '-',
            _type,
            page_num,
        ))

        return res

    @staticmethod
    async def _get_obj_origin() -> dict:
        """
        设置obj_origin_dict
        :return:
        """
        return {
            'wx': {
                'debug': True,
                'name': '搜狗微信公众号(部分图片无法跨域下载)',
                'url': 'https://weixin.sogou.com',
                'obj_origin': 'mp.weixin.qq.com',
                'site_id': 4,
            },
            'tt': {
                'debug': True,
                'name': '今日头条',
                'url': 'https://www.toutiao.com',
                'obj_origin': 'www.toutiao.com',
                'site_id': 5,
            },
            'js': {
                'debug': True,
                'name': '简书',
                'url': 'https://www.jianshu.com',
                'obj_origin': 'www.jianshu.com',
                'site_id': 6,
            },
            'kb': {
                'debug': True,
                'name': '天天快报',
                'url': '根据天天快报分享出的地址',
                'obj_origin': 'kuaibao.qq.com',
                'site_id': 7,
            },
            'kd': {
                'debug': True,
                'name': 'qq看点',
                'url': '根据QQ看点中分享出的地址',
                'obj_origin': 'post.mp.qq.com',
                'site_id': 8,
            },
            'df': {
                'debug': True,
                'name': '东方头条',
                'url': 'https://toutiao.eastday.com',
                'obj_origin': 'toutiao.eastday.com',
                'site_id': 9,
            },
            'sg': {
                'debug': True,
                'name': '搜狗头条',
                'url': 'https://wap.sogou.com',
                'obj_origin': 'sa.sogou.com',
                'site_id': 10,
            },
            'bd': {
                'debug': True,
                'name': '百度m站',
                'url': 'https://m.baidu.com/',
                'obj_origin': 'm.baidu.com',
                'site_id': 11,
            },
            'zq': {
                'debug': True,
                'name': '中青看点',
                'url': 'https://focus.youth.cn/html/articleTop/mobile.html',
                'obj_origin': 'focus.youth.cn',
                'site_id': 12,
            },
            'fh': {
                'debug': True,
                'name': '凤凰网',
                'url': 'https://news.ifeng.com/',
                'obj_origin': 'news.ifeng.com',
                'site_id': 13,
            },
            'ys': {
                'debug': True,
                'name': '51健康养生网',
                'url': 'http://www.51jkst.com/',
                'obj_origin': 'www.51jkst.com',
                'site_id': 14,
            },
            'cn': {
                'debug': True,
                'name': '彩牛养生网(短视频)',
                'url': 'http://m.cnys.com/',
                'obj_origin': 'm.cnys.com',
                'site_id': 15,
            },
            'if': {
                'debug': True,
                'name': '爱范儿',
                'url': 'https://www.ifanr.com/',
                'obj_origin': 'www.ifanr.com',
                'site_id': 16,
            },
            'ss': {
                'debug': True,
                'name': '科学松鼠会',
                'url': 'https://songshuhui.net/',
                'obj_origin': 'songshuhui.net',
                'site_id': 17,
            },
            'jm': {
                'debug': True,
                'name': '界面新闻',
                'url': 'https://www.jiemian.com/',
                'obj_origin': 'www.jiemian.com',
                'site_id': 18,
            },
            'pp': {
                'debug': True,
                'name': '澎湃网',
                'url': 'https://m.thepaper.cn/',
                'obj_origin': 'm.thepaper.cn',
                'site_id': 19,
            },
            'hx': {
                'debug': True,
                'name': '虎嗅网',
                'url': 'https://m.huxiu.com',
                'obj_origin': 'm.huxiu.com',
                'site_id': 20,
            },
            'nfzm': {
                'debug': True,
                'name': '南方周末',
                'url': 'http://www.infzm.com/wap/#/',
                'obj_origin': 'www.infzm.com',
                'site_id': 21,
            },
            'hqx': {
                'debug': True,
                'name': '好奇心日报',
                'url': 'http://m.qdaily.com/mobile/homes.html',
                'obj_origin': 'm.qdaily.com',
                'site_id': 22,
            },
            'hk': {
                'debug': True,
                'name': '百度好看视频(短视频)',
                'url': 'https://haokan.baidu.com/',
                'obj_origin': 'haokan.baidu.com',
                'site_id': 23,
            },
            'xg': {
                'debug': True,
                'name': '西瓜视频(短视频)',
                'url': 'https://www.ixigua.com',
                'obj_origin': 'www.ixigua.com',
                'site_id': 24,
            },
            'yg': {
                'debug': True,
                'name': '阳光宽频网(短视频)',
                'url': 'https://www.365yg.com/',
                'obj_origin': 'www.365yg.com',
                'site_id': 25,
            },
            'ck': {
                'debug': True,
                'name': '场库网(短视频)',
                'url': 'https://www.vmovier.com/',
                'obj_origin': 'www.vmovier.com',
                'site_id': 26,
            },
            '91mt': {
                'debug': True,
                'name': '觅糖网',
                'url': 'https://www.91mitang.com',
                'obj_origin': 'www.91mitang.com',
                'site_id': 27,
            },
            'mp': {
                'debug': True,
                'name': '美拍(短视频)',
                'url': 'https://www.meipai.com/',
                'obj_origin': 'www.meipai.com',
                'site_id': 28,
            },
            '7y7': {
                'debug': True,
                'name': '七丽女性网(部分图片无法跨域下载)',
                'url': 'https://i.7y7.com/',
                'obj_origin': 'i.7y7.com',
                'site_id': 29,
            },
            'qqbb': {
                'debug': True,
                'name': '亲亲宝贝网',
                'url': 'https://m.qbaobei.com/',
                'obj_origin': 'm.qbaobei.com',
                'site_id': 30,
            },
            'ft': {
                'debug': True,
                'name': '发条网(短视频)',
                'url': 'https://m.fatiao.pro/',
                'obj_origin': 'fatiao.pro',
                'site_id': 31,
            },
            'xq': {
                'debug': True,
                'name': '雪球网',
                'url': 'https://xueqiu.com',
                'obj_origin': 'xueqiu.com',
                'site_id': 32,
            },
            'bdj': {
                'debug': True,
                'name': '百思不得姐',
                'url': 'http://www.budejie.com',
                'obj_origin': 'www.budejie.com',
                'site_id': 33,
            },
            'blbl': {
                'debug': False,
                'name': 'bilibili(短视频)',
                'url': 'https://www.bilibili.com',
                'obj_origin': 'www.bilibili.com',
                'site_id': 34,
            },
            'kys': {
                'debug': False,
                'name': '快音视(短视频)',
                'url': 'https://kuaiyinshi.com/hot/video/?source=kuai-shou&page=1&st=week',
                'obj_origin': 'kuaiyinshi.com',
                'site_id': 35,
            },
            'gxg': {
                'debug': True,
                'name': '搞笑gif图片集',
                'url': 'https://m.gaoxiaogif.com',
                'obj_origin': 'm.gaoxiaogif.com',
                'site_id': 36,
            },
            'kr': {
                'debug': True,
                'name': '酷燃视频',
                'url': 'https://krcom.cn',
                'obj_origin': 'krcom.cn',
                'site_id': 37,
            },
            'txws': {
                'debug': True,
                'name': '腾讯微视',
                'url': '根据腾讯微视分享出的地址',
                'obj_origin': 'h5.weishi.qq.com',
                'site_id': 38,
            },
            'lsp': {
                'debug': True,
                'name': '梨视频(短视频)',
                'url': 'https://www.pearvideo.com/',
                'obj_origin': 'www.pearvideo.com',
                'site_id': 39,
            },
            'dfsp': {
                'debug': True,
                'name': '东方视频',
                'url': 'http://imedia.eastday.com/',
                'obj_origin': 'imedia.eastday.com',
                'site_id': 40,
            },
            'lfd': {
                'debug': True,
                'name': '来福岛爆笑娱乐网',
                'url': 'http://www.laifudao.com/',
                'obj_origin': 'www.laifudao.com',
                'site_id': 41,
            },
            '5h': {
                'debug': True,
                'name': '5号女性网',
                'url': 'http://m.5h.com/',
                'obj_origin': 'm.5h.com',
                'site_id': 42,
            },
            'klm': {
                'debug': True,
                'name': '看了吗视频聚合网',
                'url': 'http://www.klm123.com/mobile/index',
                'obj_origin': 'www.klm123.com',
                'site_id': 43,
            },
            'amz': {
                'debug': True,
                'name': '艾墨镇(短视频)',
                'url': 'https://aimozhen.com/',
                'obj_origin': 'aimozhen.com',
                'site_id': 44,
            },
            'jd': {
                'debug': True,
                'name': '煎蛋网',
                'url': 'http://jandan.net',
                'obj_origin': 'jandan.net',
                'site_id': 45,
            },
            'ky': {
                'debug': False,
                'name': '开眼小视频',
                'url': '无地址',
                'obj_origin': 'www.kaiyanapp.com',
                'site_id': 46,
            },
            'dy': {
                'debug': False,
                'name': '抖音',
                'url': '根据抖音分享出来的短地址',
                'obj_origin': 'v.douyin.com',
                'site_id': 47,
            },
            'jrxsp': {
                'debug': False,
                'name': '今日小视频',
                'url': 'http://m.jrtb.net',
                'obj_origin': 'm.jrtb.net',
                'site_id': 48,
            },
            'jhgzw': {
                'debug': False,
                'name': '金华广众网',
                'url': 'https://www.jinhua.com.cn',
                'obj_origin': 'jinhua.com.cn',
                'site_id': 49,
            },
            'jhrx': {
                'debug': False,
                'name': '金华热线',
                'url': 'http://m.0579.cn/',
                'obj_origin': 'm.0579.cn',
                'site_id': 50,
            },
            'jhwb': {
                'debug': False,
                'name': '金华晚报',
                'url': 'https://www.96356.in/',
                'obj_origin': '96356.in',
                'site_id': 51,
            },
            'jhbdsv': {
                'debug': False,
                'name': '百度app金华本地板块的视频',
                'url': '此处无值',
                'obj_origin': 'sv.baidu.com',
                'site_id': 52,
            },
            'bdqmxsv': {
                'debug': False,
                'name': '百度app全屏小视频板块的视频',
                'url': '此处无值',
                'obj_origin': 'quanmin.baidu.com',
                'site_id': 53,
            },
            'jhyw18q': {
                'debug': False,
                'name': '金华义乌18腔',
                'url': 'https://m.18qiang.com/',
                'obj_origin': 'm.18qiang.com',
                'site_id': 54,
            },
            'jhzjol': {
                'debug': False,
                'name': '浙江在线金华频道',
                'url': 'http://jinhua.zjol.com.cn/jsbd/',
                'obj_origin': 'jinhua.zjol.com.cn',
                'site_id': 55,
            },
        }

    async def get_article_spiders_intro(self) -> str:
        """
        获取可用文章爬虫介绍
        :return:
        """
        _ = await self._get_obj_origin()
        intro_str = '<tr><th>index</th><th>name</th><th>url</th></tr>'
        order_list = [value for value in _.values()]
        order_list.sort(key=lambda k: (k.get('site_id', 0)))

        index = 1
        for item in order_list:
            try:
                debug = item.get('debug', False)
                name = item.get('name', '')
                assert name != ''
                url = item.get('url', '')
            except AssertionError:
                self.lg.error('遇到错误:', exc_info=True)
                continue

            if debug:
                a, b = index, name
                if re.compile('^http').findall(url) != []:
                    c = '<a href=\"{}\" target=\"_blank\">{}</a>'.format(url, url)
                else:
                    c = url
                intro_str += '<tr><th>{}</th><th>{}</th><th>{}</th></tr>'.format(
                    a,
                    b,
                    c,)
                index += 1

            else:
                continue

        res = '<style type=\"text/css\">table{border-collapse: collapse;margin: 0 auto;text-align: center;}table td, table th{border: 1px solid #cad9ea;color: #666;height: 30px;}table thead th{background-color: #CCE8EB;width: 100px;}table tr:nth-child(odd){background: #fff;}table tr:nth-child(even){background: #F5FAFA;}</style>' \
            + '<table border=\"1\">' + intro_str + '</table>'

        return res

    async def _get_html_by_driver(self,
                                  url,
                                  _type=PHANTOMJS,
                                  load_images=False,
                                  headless=False,
                                  user_agent_type=PC,
                                  exec_code='',
                                  css_selector='',
                                  timeout=20,):
        """
        使用driver获取异步页面
        :return:
        """
        if _type == PHANTOMJS:
            executable_path = PHANTOMJS_DRIVER_PATH
        elif _type == FIREFOX:
            executable_path = FIREFOX_DRIVER_PATH
        else:
            raise ValueError('_type value 异常!')

        body = await unblock_request_by_driver(
            url=url,
            type=_type,
            executable_path=executable_path,
            ip_pool_type=self.ip_pool_type,
            load_images=load_images,
            headless=headless,
            user_agent_type=user_agent_type,
            exec_code=exec_code,
            css_selector=css_selector,
            timeout=timeout,
            logger=self.lg,)

        return body

    def unblock_get_wx_article_html(self, article_url) -> tuple:
        """
        得到wx文章内容
        :return: body, video_url
        """
        body = Requests.get_url_body(
            url=article_url,
            headers=get_random_headers(),
            ip_pool_type=self.ip_pool_type,)
        # self.lg.info(body)
        assert body != '', '获取到wx的body为空值!'

        return self._wash_wx_article_body(
            article_url=article_url,
            body=body)

    async def _get_tt_article_html(self, article_url) -> tuple:
        """
        得到头条文章内容
        :param article_url:
        :return: body, video_url
        """
        # 兼容m站
        article_url = article_url.replace('m.toutiao', 'www.toutiao')

        headers = await async_get_random_headers()
        headers.update({
            'authority': 'www.toutiao.com',
            'referer': 'https://www.toutiao.com/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            logger=self.lg,)
        # self.lg.info(str(body))
        assert body != '', '获取到tt的body为空值!'

        return body, ''

    async def _get_js_article_html(self, article_url) -> tuple:
        """
        得到简书文章html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers()
        headers.update({
            'authority': 'www.jianshu.com',
            'referer': 'https://www.jianshu.com/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            # https代理太慢, 直接http
            # proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != '', '获取到的js的body为空值!'
        # self.lg.info(str(body))

        return body, ''

    @staticmethod
    async def _wash_tt_article_content(content) -> str:
        """
        清洗头条文章的content内容
        :return: body, video_url
        """
        content = content[6:-6]
        # print(content)
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('\\\\u003C', '<'),
                ('\\\\u003E', '>'),
                ('\\\\u002F', '/'),
                # 下面2个过滤顺序不能调换
                ('&quot;', '"'),
                ('\\\\"', '"'),

                ('&#x3D;', '='),
                ('&nbsp;', ' '),
                ('&#160;', ' '),
                ('&lt;', '<'),
                ('&#60;', '<'),
                ('&gt;', '>'),
                ('&#62;', '>'),
                ('&amp;', '&'),
                ('&#38;', '&'),
                ('&#34;', '"'),
            ],
            add_sensitive_str_list=None,
            is_default_filter=False,
            is_lower=False,)

        # print(content)
        # 最初有效, 后面无效
        # content = fix_text(text=content[6:-6])
        # print(content)
        # 图片设置居中
        content = re.compile(' inline=\"0\">').sub(' style=\"height:auto;width:100%;\">', content)

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_js_article_content(content) -> str:
        """
        清洗简书文章的content内容
        :param content:
        :return:
        """
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                (' data-original-src=', ' src='),
                (' data-original-filesize=\".*?\"', ' style=\"height:auto;width:100%;\"'),
                ('<img src=\"\/\/', '<img src=\"http://'),
            ],
            add_sensitive_str_list=[
                '<div class=\"image-caption\">图片发自简书App</div>',
            ],
            is_default_filter=False,
            is_lower=False,)

        # 直接处理到原js
        _ = '<style type="text/css">.ant-back-top{-webkit-box-sizing:border-box;box-sizing:border-box;margin:0;padding:0;color:rgba(0,0,0,.65);font-size:14px;font-variant:tabular-nums;line-height:1.5;list-style:none;-webkit-font-feature-settings:"tnum","tnum";font-feature-settings:"tnum","tnum";position:fixed;right:100px;bottom:50px;z-index:10;width:40px;height:40px;cursor:pointer}.ant-back-top-content{width:40px;height:40px;overflow:hidden;color:#fff;text-align:center;background-color:rgba(0,0,0,.45);border-radius:20px}.ant-back-top-content,.ant-back-top-content:hover{-webkit-transition:all .3s cubic-bezier(.645,.045,.355,1);transition:all .3s cubic-bezier(.645,.045,.355,1)}.ant-back-top-content:hover{background-color:rgba(0,0,0,.65)}.ant-back-top-icon{width:14px;height:16px;margin:12px auto;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAoCAYAAACWwljjAAAABGdBTUEAALGPC/xhBQAAAbtJREFUWAntmMtKw0AUhhMvS5cuxILgQlRUpIggIoKIIoigG1eC+AA+jo+i6FIXBfeuXIgoeKVeitVWJX5HWhhDksnUpp3FDPyZk3Nm5nycmZKkXhAEOXSA3lG7muTeRzmfy6HneUvIhnYkQK+Q9NhAA0Opg0vBEhjBKHiyb8iGMyQMOYuK41BcBSypAL+MYXSKjtFAW7EAGEO3qN4uMQbbAkXiSfRQJ1H6a+yhlkKRcAoVFYiweYNjtCVQJJpBz2GCiPt7fBOZQpFgDpUikse5HgnkM4Fi4QX0Fpc5wf9EbLqpUCy4jMoJSXWhFwbMNgWKhVbRhy5jirhs9fy/oFhgHVVTJEs7RLZ8sSEoJm6iz7SZDMbJ+/OKERQTttCXQRLToRUmrKWCYuA2+jbN0MB4OQobYShfdTCgn/sL1K36M7TLrN3n+758aPy2rrpR6+/od5E8tf/A1uLS9aId5T7J3CNYihkQ4D9PiMdMC7mp4rjB9kjFjZp8BlnVHJBuO1yFXIV0FdDF3RlyFdJVQBdv5AxVdIsq8apiZ2PyYO1EVykesGfZEESsCkweyR8MUW+V8uJ1gkYipmpdP1pm2aJVPEGzAAAAAElFTkSuQmCC) 100%/100% no-repeat}@media screen and (max-width:768px){.ant-back-top{right:60px}}@media screen and (max-width:480px){.ant-back-top{right:20px}}.ant-affix{position:fixed;z-index:10}._3VRLsv{-webkit-box-sizing:content-box;box-sizing:content-box;width:1000px;padding-left:16px;padding-right:16px;margin-left:auto;margin-right:auto}._3Z3nHf,.ouvJEz{background-color:#fff;border-radius:4px;margin-bottom:10px;-webkit-box-shadow:0 1px 3px rgba(26,26,26,.1);box-shadow:0 1px 3px rgba(26,26,26,.1)}body.reader-night-mode ._3Z3nHf,body.reader-night-mode .ouvJEz{background-color:#3d3d3d;-webkit-box-shadow:0 1px 3px rgba(0,0,0,.3);box-shadow:0 1px 3px rgba(0,0,0,.3)}._3kbg6I{background-color:#f9f9f9}body.reader-night-mode ._3kbg6I{background-color:#2d2d2d}._3VRLsv{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start;min-height:calc(100vh - 66px);padding-top:10px;font-size:16px}._gp-ck{-ms-flex-negative:0;flex-shrink:0;width:730px;margin-bottom:24px;margin-right:10px}.ouvJEz{padding:24px}._2OwGUo{-ms-flex-negative:0;flex-shrink:0;width:260px}._3Z3nHf{padding:16px}.QxT4hD{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin-bottom:16px;padding-left:12px;border-left:4px solid #ec7259;font-size:18px;font-weight:500;height:20px;line-height:20px}._3yfjDE{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;height:calc(100vh - 56px)}._3yfjDE,.l3_euy{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.l3_euy{margin-bottom:32px;padding-bottom:48px;border-bottom:1px solid #eee}body.reader-night-mode .l3_euy{border-color:#2f2f2f}._23lAnl{width:280px;height:280px;margin-right:48px}._2msktx{font-size:24px;font-weight:500;margin-bottom:8px}._1gKcub{font-size:14px;width:400px;line-height:1.7}._2QxXJ4{display:-webkit-box;display:-ms-flexbox;display:flex}._2QxXJ4,._3Fatyw{-webkit-box-align:center;-ms-flex-align:center;align-items:center}._3Fatyw{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;font-size:14px}._3Fatyw>i{font-size:18px;margin-right:4px}._3Fatyw+._3Fatyw{margin-left:120px}._16zCst,._26qd_C{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;height:56px}.FTZkZo{-webkit-box-sizing:content-box;box-sizing:content-box;width:1000px;padding-left:16px;padding-right:16px;margin-left:auto;margin-right:auto;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;height:56px}._16zCst{max-width:730px;overflow:hidden;padding:0 24px}._2zeTMs{margin:0;font-size:24px;font-weight:700;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;white-space:nowrap}._26qd_C{-ms-flex-negative:0;flex-shrink:0}.qzhJKO{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._2JlnTn{width:40px;height:40px;border-radius:50%}._22gUMi{color:#7d7d7d;margin:0 10px}._1bCFo7{width:320px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}._3PUMf1{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;height:32px}._2W7JCU{width:8px;height:8px;background-color:#8c8c8c;margin:0 5px;border-radius:50%;cursor:pointer;-webkit-transition:background-color .1s;-o-transition:background-color .1s;transition:background-color .1s}._2W7JCU:hover{background-color:#737373}._2W7JCU._1je2YA{background-color:#595959;pointer-events:none}body.reader-night-mode ._2W7JCU:hover{background-color:#a6a6a6}body.reader-night-mode ._2W7JCU._1je2YA{background-color:#bfbfbf}._3F7sjs{width:100%;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap}._3F7sjs,._3kPlPc{-ms-flex-negative:0;flex-shrink:0}._3kPlPc{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;font-size:24px;color:#404040;width:32px;height:32px;padding:4px;border-radius:4px;cursor:pointer;overflow:hidden}._3kPlPc:hover{background-color:rgba(51,51,51,.1)}body.reader-night-mode ._3kPlPc:hover{background-color:#4d4d4d}body.reader-night-mode ._2SihW7,body.reader-night-mode ._5g0jij .ant-dropdown-menu-sub{background-color:#3d3d3d}._5g0jij .ant-dropdown-menu-submenu-title{padding:8px 20px 8px 12px;color:#666}._5g0jij .ant-dropdown-menu-submenu-title:hover{background-color:rgba(236,114,89,.1)}body.reader-night-mode ._5g0jij .ant-dropdown-menu-submenu-title{color:#a6a6a6}body.reader-night-mode ._5g0jij .ant-dropdown-menu-submenu-title:hover{background-color:#303030}._5g0jij .ant-dropdown-menu-submenu-arrow{top:7px;right:8px}._5g0jij .ant-dropdown-menu-submenu-arrow-icon{color:#666}body.reader-night-mode ._5g0jij .ant-dropdown-menu-submenu-arrow-icon{color:#a6a6a6}._1SgxkY{padding:8px 12px;color:#666}._1SgxkY:hover{background-color:rgba(236,114,89,.1)}body.reader-night-mode ._1SgxkY{color:#a6a6a6}body.reader-night-mode ._1SgxkY:hover{background-color:#303030}._1Jdfvb{-webkit-box-sizing:content-box;box-sizing:content-box;width:1000px;padding-left:16px;padding-right:16px;margin-left:auto;margin-right:auto}.W2TSX_{background-color:#f2f2f2}.W2TSX_::-webkit-input-placeholder{color:#999}.W2TSX_::-moz-placeholder{color:#999}.W2TSX_:-ms-input-placeholder{color:#999}.W2TSX_::-ms-input-placeholder{color:#999}.W2TSX_::placeholder{color:#999}body.reader-night-mode .W2TSX_{background-color:#333}._1LI0En{position:relative;display:block}._2xr8G8{position:fixed;left:0;right:0;bottom:0;background-color:#fff;-webkit-box-shadow:0 -1px 3px rgba(26,26,26,.1);box-shadow:0 -1px 3px rgba(26,26,26,.1);z-index:100}body.reader-night-mode ._2xr8G8{background-color:#3d3d3d;-webkit-box-shadow:0 -1px 3px rgba(0,0,0,.3);box-shadow:0 -1px 3px rgba(0,0,0,.3)}._1Jdfvb{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding-top:10px;padding-bottom:10px}._1Jdfvb.ufcbR-{-webkit-box-align:end;-ms-flex-align:end;align-items:flex-end}._1Jdfvb.ufcbR- .W2TSX_{width:560px;height:56px;padding-right:80px;border-radius:4px}.TDvCqd{display:-webkit-box;display:-ms-flexbox;display:flex;position:relative}.TDvCqd[focus-within] .W2TSX_{will-change:width,height,padding-right,border-radius}.TDvCqd:focus-within .W2TSX_{will-change:width,height,padding-right,border-radius}.W2TSX_{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;width:200px;height:36px;resize:none;margin-right:16px;padding:8px 18px;border-radius:18px;border:none;-webkit-transition:all .2s cubic-bezier(.19,.4,.17,.85);-o-transition:all .2s cubic-bezier(.19,.4,.17,.85);transition:all .2s cubic-bezier(.19,.4,.17,.85)}._2qhU6p{position:absolute;right:16px;bottom:8px;font-size:20px;margin-right:12px;color:#969696}._2qhU6p:hover{color:#7d7d7d}.-pXE92{color:#969696;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.-pXE92,._3nj4GN{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._3nj4GN{font-size:14px;cursor:pointer}._3nj4GN>span{margin-left:8px;line-height:20px}._3nj4GN .anticon{font-size:22px}._3nj4GN:not(:last-child){margin-right:12px}._3nj4GN._3oieia{color:#ec7259}.rEsl9f{-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin-bottom:32px;color:#969696;font-size:13px}.rEsl9f,.s-dsoj{display:-webkit-box;display:-ms-flexbox;display:flex}.s-dsoj>:not(:last-child){margin-right:8px}._3tCVn5{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;color:#ec7259}._3tCVn5 i{margin-right:.5em}._3_y8t4{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;width:100%;margin:20px 0;padding:8px 16px;border-radius:4px;background-color:#f2f2f2}body.reader-night-mode ._3_y8t4{background-color:#4d4d4d}._3_y8t4._1cBl4m,body.reader-night-mode ._3_y8t4._1cBl4m{background-color:rgba(218,158,85,.1)}._3_y8t4._1cBl4m ._1NiROM{background-image:url(data:image/png;base64,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);-webkit-animation:none;animation:none}._1NiROM{-ms-flex-negative:0;flex-shrink:0;width:32px;height:32px;cursor:pointer;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAABwCAMAAADxPgR5AAAAgVBMVEUAAADrcFrqb1vqb1rrb1rrcFrrcFvvc1/rcFrucVzrb1rrb1ruc1z4dGXxdWDrb1rrcVzrcVzscVv/lGvrcFvtcVvscVvscFvscF3velv/gHzrb1rrcFvscVzrcFvtcVzrcFvqcFvrcFztcVzzeV/rb1vqb1rqb1rrcFzrcFvqb1ocs5f0AAAAKnRSTlMA+8fo7c5wH98k5JYsCxinTEp5BLJSgms2DwbawELyOtKfZGATjPi4i4l1OaSPAAAD10lEQVRo3rTY2ZaqMBAF0BOMzGCDIoPtrG2b///A+5AS0fZqCsJ+d9WiKqeSJXiCzI0uzs6XQkh/51wiNwswkiQ7T3/UCz/Tc5bAsnjpCPWGcJYxrEndqTIwdVPYsF4IZUgs1hjqy1EszheGKJ57KZ19Xmxj79Q0Jy/eFvnekc+dLdBX/K26wtnRwwvecRaqru+4Xwyu3dmt8uBtPvNVd5bXBGxZ2GlkVOGjKpKdbmTgmf92flwmhj0pQ9X6nYPBc+69PDQw1hzunXU8RhakIht3zmyNu1FEGiekFIrMUrClM0VECSNLRfx1z93kK7KEgUiRRY2e6oUiET66NUS4GMAVt6GYft+kwiDVRGmR2fz8AAMFvskcy9sCTjFYelv85Zv8Cdq+NSyoafeL/+bRk/R9Nayo6Rulh5fmDs0vhSUpzdF5va5oX08CWBNMaJPjhYw6XsGiik5Fhj8SulpcWOXSFZfg2ZX2GSyjLXfFk1joA1PDstrXk4rxiDKzhnVryjYeFO2qtY+ugwJdOqKbFCNIN3qdPOw0/gnln9TuhtM7ZjXHKOYrvW/+zPWAkRzoRD5lJWwwkiZ8zHgq6N4aTamzmD4MVSYYTSIfDuXU9IFVRLMyQR9RNxmxHmllthbDAj1UukbceTitDAahLTzw6WQsOyHM8cm3IpucH9j8HsVEn9EAn4SqtduCKdDnNGnXWoiPJqpjfwJP2K63M90TvIJKHvrcGec2FEdGQeLEYDi2wdD/n3n8gkqcGaH09P9yt2lKsAtyQynpbGa6PeyC3FBS+jJapHt2QXYo97ROI4o9tyA7lDlt7Au9cLgFuaGkd9qFWrtlF2SHckuHZUdrnFuQHcpY9x8+xXBgQSVyoyD6FI/TsIImB+9Egdd3RTOsoMkbpdGN+Fe9tawwDMMwSumaso21DMYeZTvslv//wF10C4PIdlxXPxAIUSJLiuGCeapZ0HBL81izpRaHBljrDo2eFkAaq2ihJn610wnia682IC21V5vu8ga627P68lY9T8A6Ec+T4gEG+i/1AIslBtAdH5zEkIooYLiTIkouExEysDJRLoRBPV4I81IfeC0Cqb8ww0xfUo8fZphxrS+ox49r1ECaCurxAyk1cl8K6vEjN2UqnN6gntxUIG2Tz5BzOlwVtgltDI2Tzhjytr7czT1v+9LdoPW2oN1Ndu8YwT0o8Y6Ctg+7Gsd5EQLLppFsjNC5XawepzjQphoRq/xhX2+JV+CxrSjFLGHZ1cziFulsqoKxy5DquuceCq3yyu6eSsl87XqPxXL/6jxwnv9/DpgJGnh/f/gBFVizjSPxtMoAAAAASUVORK5CYII=);background-position:50%;background-repeat:no-repeat;background-size:cover}._30e-qR{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAABwCAMAAADxPgR5AAAAjVBMVEUAAADsblrqcFrqblrrblrpbVnrb1rrb1r7hXPvdF/rcFvqb1vrcFvrcFvrb1rtclzucl/5dWTrcFrrcFvvclzqcVzte17rcFvscVvscFvscVvrcVvscF3vdV7rb1rrb1vscFztcVzscVvrb1rwd17rcFvscVvqb1rrcFvrcFvqb1rqb1rrcFvsb1vqb1rZDUZoAAAALnRSTlMAZZnaMk2z+gUYz8eMcO0sHwrheSJJDaGCbFJLNhPkxEE5KKgQsEOU2PLpuL9arCjQDwAABLlJREFUaN681wl2qjAUBuAfqBBmkMGxdcSh9mX/y3s95IK0B2JQ6LcAQ+6UK/pJM1+/bZxpYFnB1NncdD9LMZI88xyLt7AcL8sxsHDuWlzCcuchBmP7Dlfg+DaGsDUtrsgyt3jVyuW9uCu8Yvk7loE7S5a7MHpn7D0Kd8tk5ga/I7vEs8Iv3vQx0yK0iLTZB2/6CvGM2Gvm7pLsIbFPLs1cejF6y6aNQJ7XeGh9bgR3mqEf5jVCuYihJF40Qusx9BDda9PQGJQxzbjXawRlk4CTq8/QC/OvnAQTKFrwysFGb/aBVxZQMq8zf8JTTlNO5lCgc1Ic8aRjwYmOh6qAWD5e4FtVUlTv97nGS9afXNDV8mekeFFq1HlUqE/Hxsts53GtTriwyTGAfMOFCTpEAd0vxyByumMQoRVzKX82BmJTHl2GNh7VZ4rBpFSrHlpk1H9rDGhN/Zi1vC00j3wMyqcpGXcFtMDAio6ghpb4kiMGdhSRs0L8RPvSCYM70WaFH5b1qB0ePQdLNIkWvdoYgX0V4wQNK0mFDlapK9y5YsQwKLK9zcazoYiJgeOituUlTfk81/jmKp+o8dIWFVPsnwyKPKPkQRET+6oJYlv0bqnaGKUN+u2Blv0jqUEMVQaBqjigomz2xBnjHYhzszNCXlqPeeCal8LG4nTBmAfiQgvVvQkTdDv6B/0kL5q3RTKJ0S25t2IuanSPTlH5eUXe3RZxYn7TbXTaizrN67H28fhJu6RdjW+fzZIsSqIVV/XLO5MElJNg2z7awoNJJEGd1e+w82ispbxyDdEiOpgVSUy1ujFECiN0o9WrKw6+WZmhWySSWH1/oPYH1UAL3axMICGGTYqM6lXG48RBC88kGmRc2hd9ipXUP0vyQi/NUrGF1Ix+Qae2l3srd69bjBZsXuYvBZG2vo4bbTgPxElRaAytWJYkyxhytKfdKLQ7jG5HxeLQGB9dSGU3pTYcGzXilNrjHaN7p4YXBc8wOkaj5q8P/POQKhRN/J84M2hxGASiMMoIEQomNA3dzUqjlPaU///3tlTroz044yHpd6sUwuiM8+ZpR0fRM0l/PJzV0vNJw5aFdZSwVfNfJw4ntiwu9cLvqVA55+tdv1jrhX9hrraOgK+oQA18/WpjLm8v+2DQINQvb6Y9eZJtqQZ/THtCA2a2lEuazH1gGjAkRjVEx5aFTiyMxGBF1DS62F87gT9Cv8fzT+REFGTipkAmQghvCoQwpP6GQOqf3ocZHkshdvg50LzI3E4MMxjXBJB5cJtKnqzqAfKSH9caB9LePAml+tSTKB9IG0fum0nkTe1UYpWP3G2mQm8yQy5RlYlNpgJsE2mApeetCFFum8iNIW8ysWyUylihMdRmfUWTmMv/BpUhmfXVaO6NJuGwFFTCycy9RvtymNMJlrNGiJPUvpQbtAjRvi0hQN6gbbegPQWaPpYWs1iZBb27yb73M8LuDyV7PwV9/7Hrv3o7NAIABoEgGI/H0H+fUUhECD9zfBu3L855hGApTbKM6KzL6hw4oKERLPwxz1t4gGeWKDER1hwz40K6GSrIxpDf3HMDaO2T3U0o+Z1db4TlYjpfz6M+B4QfxfL+YHl/sMb94QKtd3ujrQOdfAAAAABJRU5ErkJggg==);-webkit-animation:spinning 1s linear infinite;animation:spinning 1s linear infinite}._2qk-7T{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAABwCAMAAADxPgR5AAAAgVBMVEUAAADrb1rrcFvqb1vscFvrcVzrb1rscFvwdF//in7rb1rrcFvqcFrrb1vrcFvuc1zvc17rb1rrcFvrcFrrcFvrb1vrcVvwc1zyeVzse17/c2bscF3rcFvrb1rrcFvrcFvscVvrcVvtcVztcFvscVvsclvscF3tcV3rb1zsc1vqb1qqgzfAAAAAKnRSTlMA+s/HcEvtZhgF8+LelosrH+fIvbaheSISDQo2wKjVsIOBYVRRQ0I5JzXOPizQAAADRklEQVRo3ryX23qrIBCFB0ED1lMOxlPbpDlv3v8B98UQMW00GoH/rh/1mzBr1gJgGoXP4g31ooCQIPLoJmZ+AZao/MQj8gnES/wKDJPuKZEDELpPwRiceXIEHuNggsuGyJGQzQXm4lM5CerDHI6/exnQfHu6plkpRJml19M2p8Hvzh7fn5RP2WWZHzJ4QnbIl7LL53vzUydd7b63Nxjgtv3uapnUb4j30Wlk3MBLmrjT3I+pUoqk8zGrR/aEdX5kImACmZ7NaDHhS7GI9LxmE9rZNidkYmJrWNgKMbqtC3nni8Nk+Je8s4BR/LTineEtzq2UPzCCWCp2JbxJuZOKGF5ybwhhMANG7qKM3d+ygVk0S73HMfpFBcykiLSOr+fT4zAb7r2eVf+evhUYoLpnf68fs0DtrwIjVGqPQU/mCKr042AIrnSkAp6RqPkswBiFmtVkQEDSgEEa0itjrfKIgVGYSsm6r6E7MMyup6kpwV9SgmFK7BxJ4RHlmTMY56y8DQ8cddSaRR8HR+iCFg05WICHGCdPLMHACuyvNShGjAArCAwcCi0XHevm0YeQfuls0BICLCHQGptWVWJTQa0i4Q9/BvVgV1ZhuFpMX0Pq4GFL3svLB1+jCms+aU0Td52R4gf/oJ+1VKwnrWka/BfMtz2+x15NGbIYXOsHX3P7jgm30M9KtqwG1/rZaitWOKM36CeULeHgWj83nNOqjbUlDCA7DK4NsMR4a0/e3HbBHM/h1hQH2wUPrTFQwsx2wQxFBCgwZsB2QcCwKdTMUPsFqZoahjNjv2Cu4jRG29sviNaP1Vl4sl/whGeiau3VfsErDouyYWq/YKqMGKEN7RdEI0bKHqX9giUaXgWNsF9QYNQ4L+i8pc6HxrktnBvfebQ5D2/nx5PzA9j5FcP1Jcr5NdH5Rdj5Vd/5Y8b5c839g1Q/uf9XbwdVAIQwEEOFrAL8G9wzJx7QCakABDD5/YgvNz0q4LMJPgzR0xc+7tHzJT7Q0hM0PrLTGQEPJXQKeh+7wjnPECyjSdYRnXNZ3QMHMjTChT/qeYsP8NQSJSfCqmNmXkgHUMEVhhzrB2PGkH7ueQVau5DdM5TcjV3vwfKudD5wHACeP/zOAcLuAXk0BwAAAABJRU5ErkJggg==)}._35-1od{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;margin:0 16px;overflow:hidden}._2aoc2_{font-size:14px;font-weight:500;margin-bottom:2px;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;white-space:nowrap}.iWiJE9{font-size:12px}._2z_B4K{color:#da9e55;margin-right:8px}._1jirLm,._3u_PHG{color:#969696}._1jirLm{-ms-flex-negative:0;flex-shrink:0;font-size:13px}@-webkit-keyframes _2cozGY{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}@keyframes _2cozGY{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}.video-package{display:block;width:100%;margin-bottom:20px;border:1px solid #eee;background-color:hsla(0,0%,60%,.15);-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}body.reader-night-mode .video-package{border-color:#2f2f2f}.video-package:after{content:"";display:block;width:110px;height:110px;background-color:rgba(0,0,0,.4);background-image:url(data:image/png;base64,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);background-position:50%;background-size:50%;background-repeat:no-repeat;-webkit-transition:all .1s linear;-o-transition:all .1s linear;transition:all .1s linear}.video-package br{display:none}.video-package .video-description{padding:10px;line-height:32px;max-height:110px;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;float:left;margin-left:110px}.H8iPN2{display:-webkit-box;display:-ms-flexbox;display:flex;width:100%;margin-bottom:20px;border:1px solid #eee;background-color:hsla(0,0%,60%,.15);-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}body.reader-night-mode .H8iPN2{border-color:#2f2f2f}._1paJhJ{position:relative;cursor:pointer}._1paJhJ,._1paJhJ>img{width:110px;height:110px}._1paJhJ>img{min-width:110px;min-height:110px}._1paJhJ:hover:after{background-color:rgba(0,0,0,.2)}._1paJhJ:after{position:absolute;top:0;left:0;content:"";display:block;width:110px;height:110px;background-color:rgba(0,0,0,.4);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAABYCAYAAABxlTA0AAANJUlEQVR4Ae2dCVCU5xnHYUEEb8QTtYqjqEGJOtY7mpkotRKtZByJR62tJDFV422mdmpba00VdJogE5PYycSoDY4H1QHjwTROvGujolCDjrfgfYVLQez/v/HZeRf4ll3Yb/fbZXcGnve73vd9fvt+7/m8z/r7GeTz/Plz0/Hjx/vWr18/OiQk5CX8RTZo0KBTvXr1GgUGBjZ48RfC7JaVlRXjr4h/paWlBUVFRZeLi4tz8Zfz5MmTrP79+3/n7+9fbgTV/N2ZiSNHjgxo2rRpbLNmzV5t0aJFH8J0Rn4I/e7duycfPnz4zaNHj9IHDRp0zBnxekQchw8f7nX+/PmUgoKCfJRal3yYFtNk2q6G5JISDIoBWVlZs9u3b5/QvHnzKC0l8ao/uHPnztXbt2/nXblyJT87O5vyBxwX37hxowThYj7bsWPHkHbt2gW3atUqBOHGUVFR4ZBtcRzesmXLn6BqCdVK4/79+9nXr19fHx0dnYxq5JnWfc46rytglJr6JSUlCyMiImY1bNiwTcVM81W+fPny2VOnTmVv3bo1e8uWLTcr3lOT4wkTJrQZP358VO/evaM6derUs6qqp7Cw8OalS5fWBgcHJ3Xt2vVJTdKx5xndAKPEzu/SpcsSNFZhakZQmsug2KmMjIxvly5d+t2DBw90LUWhoaEBy5Yt6zt69OhX8EX3RqkNVPODhvHehQsXVqBEr1HPOyvsdMBHjx4dCLCfhoWFWdV3T58+fXzgwIGvFy9evB8ltsBZCjgSD0p0o1WrVo0YPnz4qKCgoCbqs/fu3TsD0G8PHDjwqHq+tmGnAUbJDLp48eI6lJKpKCUBkjGUkAf79+9PnzlzZua1a9d0exUlPXtkhw4d6qekpLw2YsSIWLxhlvoaOjzD27Whc+fO70CHUnviqu4epwBGqX0pMjJyO17HbpIgqwK02unx8fE70EA9lfNGkmgog1JTU+MGDx4cq1YdqLa+xycO3bv/1Ta/tQZ88uTJBLTif0dD0lAyk5eXl42q4PNNmzblyTkjy8mTJ4ej6vh1eHi4pYeDBrgQvZi5ffr0WV+bvNcKML7lj1ByZ0sGysvLy3bt2rV53LhxX8s5T5JpaWmjxowZM8lkMlkawtzc3ORu3bq9V1M9TDV5EK+/CXXVVypcdOZvz50794+eCpccmHfqQF2EC3WkrtRZzjkiHS7B7NuiI5+O1+k1SQiN1+mRI0d+hBJtHgjIeU+VKLEh+/btm4PGMFp0QLWXiYFQrKN9ZocA81tEQntVuOfOnTs0YMCAdY8fP9a1PyuKuko2adIk4NixYzO6d+8+RNIkZOgegwbR7okkh4o9Rl2bVbjIwO6ePXumeBtcAqVO1I06CmDqTgZybI+0GzAbNAw74yVSJoxO+ZfPnnlVwRX1zJK6UUcVMhmQhdWNNg7sqiLYFcMo6DOJh9UCv11vhiu6UgYEBPidPXt2plpdYDT6lj1duGpLMAcR7OdKgmjQsljn1hW41Ju6UmfqLhzIhGzkWEvaBIxGrR5HaDKIYPcFvYUPvbHO1QIk56kzdZcuHJmQDRnJPVVJm4Axt/CJDH85iFiyZMmH3tIVqwpGdeeoOxmQBe8lGzKy9ZxmHcxZMaxtHZSJG4xyvoiLi9tjK7K6cm3Hjh0/w6DkV9QXJfgZ1hKHas3CaQLGmlaWTDlybgETI3+tKwDt0RMTWL9Ht808d8GpTqwpWgYl6vNVVhGcLBe4+IbKFi5c+Ln6kC/s58fJLLIhC7Iis6q4VCrBHAqjtN6QlYhDhw79a+jQoalVPVzXzx08eDB+yJAhvyAHroygVLerOJSuVIK5hiZwOVnO+dy6DlJLf7IhI14nM7KreK8VYBT5AC5Qyk1ciTDqZLnk0Z2SbMhI8kB2ZCjHlFaAubQuq79cQ+Myj3qzL1yZABmRFa+QHRmqd1kBpt2CXOQCpVHW0CRPRpRkRFaSN5Uhz1kAo98bLUYhbB25+isPuUKuXLnyZdgqJMPUKSk9Pf11Lre7Il1npEFW0qMgQ9WCyAIYXY0ZkhjtFly9tD5r1qwETOSHYR42HDYMk2DFk5iUlNRH8mRkSVZkJnmEdZGFpQVw27Zt4+QGGoVI2FWScNW0Gjdu3GbBggWLMP/6Plrrtuo1I4ZVZmD5huTR3A/msBizRUd4kuZMrVu3fldvixvJgEi8YpoT2Xz9kMc9U6dO3Q7jEEMuS7FKu3Xr1sdipoU55EEcPptLMF7L0aIobcVcDVfS1pK0WYCNQuyZM2fWbNy4cTjnZ432ITOyk3wJUzNg2ufKBdQn2RI2moShXlPYMLyTn5+/HNVHV6PlT2UnTE14/Uw0fpbM0spRwkaVaEQ6owH8EwxD3oWdWTOj5FNlR6Zk64+6oh+mJf/DTNI+F53lme7IsK062FZ+sI2gBKOptEmTJqUboWpDVzNF7JMxjflTE/dEiAI0fpawp0js3QgeNWrUm+jWJa1evbqvu/OtMiRbEyYpLOtKtCx3dwZrmj66da3nz5+/8OrVq+9PnDgxvKbx1PY5lSHZEnCkRIpSkC9hT5WwxnkZRod/Q7duCi10XK2HypBsTagvOkkmuCdCwp4s2a1Dv3706dOn1wD2qzC2rjTvrZd+KkOyNUnHmAmC/g96JeyOeFEHNkXj9zamFf+yaNEil3TrVIZka+IGP1Geu3kk7E0SXabOsP/9c05Ozm/17tapDMnWCjC+6RJvAltRlx49egzNzMxcs2LFCkvPqeI9tT1WGQpgS0OA4u2VJViFhmF28OzZs3+jnnNmWGUIwCHmobIzE/CQuFzW6Jm4sVqgcAelhL1VYrawKDk5+R966acyJFsCLpLEuD1Vwl4oy7Fe9m8ss8+D+VOWXvqpDMk2UAXMvb96JezOeG/evJm7fPnyL7A37pLe+VAZmgFzgl0S5cZqCXuD5OQV9j9vTkhIOOQqc1uVIdkGIhOXxUyKu9YBNsfT4cL6sRS+KDKmTJmShklwl+4ufcHQjJBsA2GZkitAQd/wa1+SVy0JoP+dN2/el7AGva11j57nVYZkS8CWEkt/C3omrmfcMJDOQx27Qc8GzJ78qwzJNpA+buRBOrOQsKdINiS7d+/ejupgjxEs71WGZGuiAyFp6DgTT2cWHgL3OTamfDNs2LD5Y8eOzTACXLKT1QwyJVsTN9XRgZBApacQCRtVYkLl/Jw5c/7Qq1evT9GYPTZKPlV2ZEq25k3P9M4EY4lXmFG6YYEwpNEf6jR2u76aPn36t67qdjny5b1gZ36ETBkwz0Xg9cown8U/+rgxml0YN53AEHwX9uYtmDZtmiHhkhnZCUe6E2PYDJgWKHQSxBOcJKaPG4aN8EG36yTqtsWwsv8ndvQYdjqVzGTxgizFV5tlNg3GHNsFKB0ISdhVEp3ye2paeKvyExMTV8GoOXHbtm3mL1+9brSwykxlaQGMnTKfSKahFKqT3k7xwidxVifXrl27npABNg/mqxvxusEqdLHFYrG65915nazITPKApft1EraaFwXks2IjDH8JW2JiYtLkRp/UJrB3795x2AU6gXfQ8R2mHix1saUE8yI94lHyQ9dX9M7045HvvxYBMiIrua4y5DkrwHQ3KI0d/YrR9ZU86JNVEyAj8cFGdmSo3mkFGB1j+g1bKzfQrxgmkIPk2CetCZANGclZsiNDOaa0AswT9OWIDr25RYdlSij9ivG871OZANmQEa+QGdlVvKsSYO5UpC9HuZFO29xp6yX5MJqkrzWykXyRWcVdnrxm1YuQmyl9m8FVGpXDsH+o+WZwRkdHmbDZNdcn3FVOp22Vk6mbZ8hCdtqTEVlpkahURciNHD6j0t4gx/SIB4ONCDmuq5IMyEL0JyMtXxG8R7OK4EV8O/VgNX4GExlmp590p9KvX7/f1VWvJzSHPXHixAeNGjVqRT5g8z3Y9ELPQdNTq2YJZgR8EL4b38DkcSGPGTE94tFpG4/r0oc6U3eBSyYoaHG24JKPTcC8AcU/h15IGeaH7gaxr2OGEbdS/ZhD5/+nrtSZukvsZGKP+9tqATNC+gejF1KJnP7DMD/7Szn2dkldVZ9pZGGPzzRysVkHVwSHCj0Vs1zmSQ1ew7e6G6ZIXuv9jyWXcGEt/3Nhgfnp1IiIiDfluDrpEGA0ej7noHo6B0WFXo4521h6IZVvjq8OVncXuWPDieTB2ZK6UCe1WqDO1J0MHEnPrjpYjZDDQXSyY/iqyHlW/uy+eEM/mTpQF7VBo67UuaqhsDDQkg5VERUjQTelkovxnTt3bvJUB3Z0OAcbi8ludzEuoPEqvYcN0G9JP5kZo0c8jtM9aYKIeWWemXeBS52oG3UUfWsia1WCJUFs+vO6n3ngAItjANGxptIpgJk4Hdrh2/8YXRjfD5Uo34bTAEucKM2+n9oRGJBOByxx05ej78eidARM0L6fO9MZsJRmjADr7A/2CQOXSd9PTroMtZ8fG0R6Z9LzR1NpOWprxUFvdXVr5BzNOCeSvPFnf/8PDtJFz61AWfoAAAAASUVORK5CYII=);background-position:50%;background-size:50%;background-repeat:no-repeat;-webkit-transition:all .1s linear;-o-transition:all .1s linear;transition:all .1s linear}._3_y-pA{padding:10px;line-height:32px;max-height:110px;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1}._3_y-pA,._3nROLh{-webkit-box-orient:vertical}._3nROLh{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start;margin-bottom:20px}._10T2go{border:none}.ISr9-J{cursor:pointer;font-size:14px;margin-top:4px}._2rhmJa code,._2rhmJa pre,._2rhmJa pre[class*=language-]{font-family:Consolas,Monaco,"Andale Mono","Ubuntu Mono",monospace;font-size:12px}._2rhmJa{font-weight:400;line-height:1.8;margin-bottom:20px}._2rhmJa h1,._2rhmJa h2,._2rhmJa h3,._2rhmJa h4,._2rhmJa h5,._2rhmJa h6{font-weight:700;margin:0 0 16px}._2rhmJa h1{font-size:26px}._2rhmJa h2{font-size:24px}._2rhmJa h3{font-size:22px}._2rhmJa h4{font-size:20px}._2rhmJa h5{font-size:18px}._2rhmJa h6{font-size:16px}._2rhmJa p{margin-bottom:20px;word-break:break-word}._2rhmJa hr{margin:0 0 20px;border:0;border-top:1px solid #eee!important}body.reader-night-mode ._2rhmJa hr{border-color:#2f2f2f!important}._2rhmJa blockquote{padding:20px;background-color:#fafafa;border-left:6px solid #e6e6e6;word-break:break-word;font-size:16px;font-weight:normal;line-height:30px;margin:0 0 20px}body.reader-night-mode ._2rhmJa blockquote{background-color:#595959;border-color:#262626}._2rhmJa blockquote h1:last-child,._2rhmJa blockquote h2:last-child,._2rhmJa blockquote h3:last-child,._2rhmJa blockquote h4:last-child,._2rhmJa blockquote h5:last-child,._2rhmJa blockquote h6:last-child,._2rhmJa blockquote li:last-child,._2rhmJa blockquote ol:last-child,._2rhmJa blockquote p:last-child,._2rhmJa blockquote ul:last-child{margin-bottom:0}._2rhmJa blockquote .image-package{width:100%;margin-left:0}._2rhmJa ol,._2rhmJa ul{word-break:break-word;margin:0 0 20px 20px}._2rhmJa ol li,._2rhmJa ul li{line-height:30px}._2rhmJa ol li ol,._2rhmJa ol li ul,._2rhmJa ul li ol,._2rhmJa ul li ul{margin-top:16px}._2rhmJa ol{list-style-type:decimal}._2rhmJa ul{list-style-type:disc}._2rhmJa code{padding:2px 4px;border:none;vertical-align:middle;white-space:pre-wrap}._2rhmJa :not(pre) code{color:#c7254e;background-color:#f2f2f2}body.reader-night-mode ._2rhmJa :not(pre) code{background-color:#262626}._2rhmJa pre,._2rhmJa pre[class*=language-]{word-wrap:normal;word-break:break-all;white-space:pre;overflow:auto;margin-bottom:20px;border-radius:4px;padding:1em;line-height:1.5;color:#ccc;background:#2d2d2d}._2rhmJa pre[class*=language-] code,._2rhmJa pre code{padding:0;background-color:rgba(0,0,0,0);white-space:pre}._2rhmJa table{width:100%;margin-bottom:20px;border-collapse:collapse;border:1px solid #eee;border-left:none;word-break:normal}body.reader-night-mode ._2rhmJa table,body.reader-night-mode ._2rhmJa table td,body.reader-night-mode ._2rhmJa table th{border-color:#2f2f2f}._2rhmJa table td,._2rhmJa table th{padding:8px;border:1px solid #eee;line-height:20px;vertical-align:middle}._2rhmJa table th{font-weight:bold}._2rhmJa table thead th{vertical-align:middle;text-align:inherit}._2rhmJa table tr:nth-of-type(2n){background-color:hsla(0,0%,70.2%,.15)}._2rhmJa table .image-package{width:100%;margin-left:0}._2rhmJa img{max-width:100%}._2rhmJa .image-package{width:100%;margin:0;padding-bottom:25px;text-align:center;font-size:0}._2rhmJa .image-package img{max-width:100%;width:auto;height:auto;vertical-align:middle;border:0}body.reader-night-mode ._2rhmJa .image-package img{opacity:.85}._2rhmJa .image-package .image-container{position:relative;z-index:95;background-color:#e6e6e6;-webkit-transition:background-color .1s linear;-o-transition:background-color .1s linear;transition:background-color .1s linear;margin:0 auto}body.reader-night-mode ._2rhmJa .image-package .image-container{background-color:#595959}._2rhmJa .image-package .image-container-fill{z-index:90}._2rhmJa .image-package .image-container .image-view{position:absolute;top:0;left:0;width:100%;height:100%;overflow:hidden}._2rhmJa .image-package .image-container .image-view-error{cursor:pointer;color:grey}body.reader-night-mode ._2rhmJa .image-package .image-container .image-view-error{color:#b3b3b3}._2rhmJa .image-package .image-container .image-view-error:after{content:"\56FE\7247\83B7\53D6\5931\8D25\FF0C\8BF7\70B9\51FB\91CD\8BD5";position:absolute;top:50%;left:50%;width:100%;-webkit-transform:translate(-50%,-50%);-ms-transform:translate(-50%,-50%);transform:translate(-50%,-50%);color:inherit;font-size:14px}._2rhmJa .image-package .image-container .image-view img.image-loading{opacity:.3}._2rhmJa .image-package .image-container .image-view img{-webkit-transition:all .15s linear;-o-transition:all .15s linear;transition:all .15s linear;z-index:95;opacity:1}._2rhmJa .image-package .image-caption{min-width:20%;max-width:80%;min-height:43px;display:inline-block;padding:10px;margin:0 auto;border-bottom:1px solid #eee;font-size:13px;color:#999}._2rhmJa .image-package .image-caption:empty{display:none}body.reader-night-mode ._2rhmJa .image-package .image-caption{border-color:#2f2f2f}._2rhmJa .math-block[mathimg="1"]{display:block;margin:1em auto}._2rhmJa .math-inline[mathimg="1"]{display:inline;margin:0 3px;vertical-align:middle}._2rhmJa .math-block[mathimg="1"],._2rhmJa .math-inline[mathimg="1"]{max-width:100%}body.reader-night-mode ._2rhmJa .math-block[mathimg="1"],body.reader-night-mode ._2rhmJa .math-inline[mathimg="1"]{-webkit-filter:invert(.8);filter:invert(.8)}._3GbnS5{padding:0;line-height:1.5;position:relative;width:100%;height:1px;margin:20px 0;border:none;border-top:#b3b3b3;display:table;white-space:nowrap;text-align:center}._3GbnS5:after,._3GbnS5:before{content:"";display:table-cell;position:relative;top:50%;left:0;width:50%;border-top:1px solid;border-top-color:inherit;-webkit-transform:scaleY(.5) translateY(50%);-ms-transform:scaleY(.5) translateY(50%);transform:scaleY(.5) translateY(50%);-webkit-transform-origin:50% 50% 0;-ms-transform-origin:50% 50% 0;transform-origin:50% 50% 0;-webkit-transform-origin:initial;-ms-transform-origin:initial;transform-origin:initial}._2Lt-af{display:inline-block;padding:0 12px;font-size:14px;font-weight:normal;text-align:center;white-space:nowrap;color:#b3b3b3;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}._2Lt-af>a{margin-left:.5em}._19DgIp{width:100%;height:1px;margin:16px 0;background-color:#eee}body.reader-night-mode ._19DgIp{background-color:#2f2f2f}._23ISFX{position:relative;display:block;margin:0 auto}._23ISFX-mask{position:fixed;top:0;right:0;left:0;bottom:0;background-color:rgba(0,0,0,.5);height:100vh;filter:alpha(opacity=50);z-index:1000}._23ISFX-mask-hidden{display:none}._23ISFX-wrap{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1050;overflow:auto;outline:0;-webkit-overflow-scrolling:touch}._23ISFX-wrap-middle{text-align:center}._23ISFX-wrap-middle:before{content:"";display:inline-block;width:0;height:100%;vertical-align:middle}._23ISFX-wrap-middle ._23ISFX{position:static;display:inline-block;text-align:left;vertical-align:middle}._23ISFX-content{position:relative;background-color:#fff;border-radius:4px;-webkit-box-shadow:0 2px 8px rgba(26,26,26,.1);box-shadow:0 2px 8px rgba(26,26,26,.1)}body.reader-night-mode ._23ISFX-content{background-color:#3d3d3d}._23ISFX-close{position:absolute;top:0;right:0;margin:0;padding:0;border:0;outline:0;color:grey;background-color:rgba(0,0,0,0);cursor:pointer;text-decoration:none}._23ISFX-close-x{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;width:48px;height:48px;font-size:16px}._23ISFX-close:hover{color:#4d4d4d}body.reader-night-mode ._23ISFX-close:hover{color:#b3b3b3}._23ISFX-header{border-bottom:1px solid #eee;border-radius:4px 4px 0 0}._23ISFX-title{margin:0;font-size:18px;font-weight:bold}._23ISFX-body{line-height:1.5;word-wrap:break-word}._23ISFX-footer{border-top:1px solid #eee;border-radius:4px 4px 0 0;text-align:right}._23ISFX-footer,._23ISFX-header{padding:16px 24px}body.reader-night-mode ._23ISFX-footer,body.reader-night-mode ._23ISFX-header{border-color:#2f2f2f}._23ISFX.zoom-appear,._23ISFX.zoom-enter{-webkit-transform:none;-ms-transform:none;transform:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.KdlMNE{height:480px;overflow-y:scroll;padding:0 24px}._2cxUIy{margin:0;padding:0;list-style:none}.LtPwLP{margin-bottom:16px;padding-bottom:16px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;-webkit-box-align:center;-ms-flex-align:center;align-items:center;border-bottom:1px solid #eee}.LtPwLP>div{min-height:100px;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1}.LtPwLP img{width:150px;height:100px;border-radius:4px;border:1px solid #f2f2f2;-ms-flex-negative:0;flex-shrink:0}._2ssoa1{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin:30px 0;line-height:20px;border-radius:30px;background-color:#f2f2f2}body.reader-night-mode ._2ssoa1{background-color:#333}._2bdkP8{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;width:33.33%;height:60px;font-size:14px;font-weight:bold}._3dvb2i{height:20px;color:#8c8c8c;font-weight:normal;border-left:1px solid #eee;border-right:1px solid #eee;cursor:pointer}body.reader-night-mode ._3dvb2i{border-color:#2f2f2f}.ant-select{-webkit-box-sizing:border-box;box-sizing:border-box;color:rgba(0,0,0,.65);font-size:14px;font-variant:tabular-nums;line-height:1.5;-webkit-font-feature-settings:"tnum","tnum";font-feature-settings:"tnum","tnum";position:relative;display:inline-block;outline:0}.ant-select,.ant-select ol,.ant-select ul{margin:0;padding:0;list-style:none}.ant-select>ul>li>a{padding:0;background-color:#fff}.ant-select-arrow{display:inline-block;color:inherit;font-style:normal;line-height:0;text-align:center;text-transform:none;vertical-align:-.125em;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;position:absolute;top:50%;right:11px;margin-top:-6px;color:rgba(0,0,0,.25);font-size:12px;line-height:1;-webkit-transform-origin:50% 50%;-ms-transform-origin:50% 50%;transform-origin:50% 50%}.ant-select-arrow>*{line-height:1}.ant-select-arrow svg{display:inline-block}.ant-select-arrow:before{display:none}.ant-select-arrow .ant-select-arrow-icon{display:block}.ant-select-arrow .ant-select-arrow-icon svg{-webkit-transition:-webkit-transform .3s;transition:-webkit-transform .3s;transition:transform .3s;transition:transform .3s,-webkit-transform .3s}.ant-select-selection{display:block;-webkit-box-sizing:border-box;box-sizing:border-box;background-color:#fff;border:1px solid #d9d9d9;border-top:1.02px solid #d9d9d9;border-radius:4px;outline:none;-webkit-transition:all .3s cubic-bezier(.645,.045,.355,1);transition:all .3s cubic-bezier(.645,.045,.355,1);-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.ant-select-selection:hover{border-color:#fa9e87;border-right-width:1px!important}.ant-select-focused .ant-select-selection,.ant-select-selection:active,.ant-select-selection:focus{border-color:#fa9e87;border-right-width:1px!important;outline:0;-webkit-box-shadow:0 0 0 2px rgba(236,114,89,.2);box-shadow:0 0 0 2px rgba(236,114,89,.2)}.ant-select-selection__clear{position:absolute;top:50%;right:11px;z-index:1;display:inline-block;width:12px;height:12px;margin-top:-6px;color:rgba(0,0,0,.25);font-size:12px;font-style:normal;line-height:12px;text-align:center;text-transform:none;background:#fff;cursor:pointer;opacity:0;-webkit-transition:color .3s ease,opacity .15s ease;transition:color .3s ease,opacity .15s ease;text-rendering:auto}.ant-select-selection__clear:before{display:block}.ant-select-selection__clear:hover{color:rgba(0,0,0,.45)}.ant-select-selection:hover .ant-select-selection__clear{opacity:1}.ant-select-selection-selected-value{float:left;max-width:100%;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}.ant-select-no-arrow .ant-select-selection-selected-value{padding-right:0}.ant-select-disabled{color:rgba(0,0,0,.25)}.ant-select-disabled .ant-select-selection{background:#f5f5f5;cursor:not-allowed}.ant-select-disabled .ant-select-selection:active,.ant-select-disabled .ant-select-selection:focus,.ant-select-disabled .ant-select-selection:hover{border-color:#d9d9d9;-webkit-box-shadow:none;box-shadow:none}.ant-select-disabled .ant-select-selection__clear{display:none;visibility:hidden;pointer-events:none}.ant-select-disabled .ant-select-selection--multiple .ant-select-selection__choice{padding-right:10px;color:rgba(0,0,0,.33);background:#f5f5f5}.ant-select-disabled .ant-select-selection--multiple .ant-select-selection__choice__remove{display:none}.ant-select-selection--single{position:relative;height:32px;cursor:pointer}.ant-select-selection--single .ant-select-selection__rendered{margin-right:24px}.ant-select-no-arrow .ant-select-selection__rendered{margin-right:11px}.ant-select-selection__rendered{position:relative;display:block;margin-right:11px;margin-left:11px;line-height:30px}.ant-select-selection__rendered:after{display:inline-block;width:0;visibility:hidden;content:".";pointer-events:none}.ant-select-lg{font-size:16px}.ant-select-lg .ant-select-selection--single{height:40px}.ant-select-lg .ant-select-selection__rendered{line-height:38px}.ant-select-lg .ant-select-selection--multiple{min-height:40px}.ant-select-lg .ant-select-selection--multiple .ant-select-selection__rendered li{height:32px;line-height:32px}.ant-select-lg .ant-select-selection--multiple .ant-select-arrow,.ant-select-lg .ant-select-selection--multiple .ant-select-selection__clear{top:20px}.ant-select-sm .ant-select-selection--single{height:24px}.ant-select-sm .ant-select-selection__rendered{margin-left:7px;line-height:22px}.ant-select-sm .ant-select-selection--multiple{min-height:24px}.ant-select-sm .ant-select-selection--multiple .ant-select-selection__rendered li{height:16px;line-height:14px}.ant-select-sm .ant-select-selection--multiple .ant-select-arrow,.ant-select-sm .ant-select-selection--multiple .ant-select-selection__clear{top:12px}.ant-select-sm .ant-select-arrow,.ant-select-sm .ant-select-selection__clear{right:8px}.ant-select-disabled .ant-select-selection__choice__remove{color:rgba(0,0,0,.25);cursor:default}.ant-select-disabled .ant-select-selection__choice__remove:hover{color:rgba(0,0,0,.25)}.ant-select-search__field__wrap{position:relative;display:inline-block}.ant-select-search__field__placeholder,.ant-select-selection__placeholder{position:absolute;top:50%;right:9px;left:0;max-width:100%;height:20px;margin-top:-10px;overflow:hidden;color:#bfbfbf;line-height:20px;white-space:nowrap;text-align:left;text-overflow:ellipsis}.ant-select-search__field__placeholder{left:12px}.ant-select-search__field__mirror{position:absolute;top:0;left:0;white-space:pre;opacity:0;pointer-events:none}.ant-select-search--inline{position:absolute;width:100%;height:100%}.ant-select-search--inline .ant-select-search__field__wrap{width:100%;height:100%}.ant-select-search--inline .ant-select-search__field{width:100%;height:100%;font-size:100%;line-height:1;background:rgba(0,0,0,0);border-width:0;border-radius:4px;outline:0}.ant-select-search--inline>i{float:right}.ant-select-selection--multiple{min-height:32px;padding-bottom:3px;cursor:text;zoom:1}.ant-select-selection--multiple:after,.ant-select-selection--multiple:before{display:table;content:""}.ant-select-selection--multiple:after{clear:both}.ant-select-selection--multiple .ant-select-search--inline{position:static;float:left;width:auto;max-width:100%;padding:0}.ant-select-selection--multiple .ant-select-search--inline .ant-select-search__field{width:.75em;max-width:100%}.ant-select-selection--multiple .ant-select-selection__rendered{height:auto;margin-bottom:-3px;margin-left:5px}.ant-select-selection--multiple .ant-select-selection__placeholder{margin-left:6px}.ant-select-selection--multiple .ant-select-selection__rendered>ul>li,.ant-select-selection--multiple>ul>li{height:24px;margin-top:3px;line-height:22px}.ant-select-selection--multiple .ant-select-selection__choice{position:relative;float:left;max-width:99%;margin-right:4px;padding:0 20px 0 10px;overflow:hidden;color:rgba(0,0,0,.65);background-color:#fafafa;border:1px solid #e8e8e8;border-radius:2px;cursor:default;-webkit-transition:padding .3s cubic-bezier(.645,.045,.355,1);transition:padding .3s cubic-bezier(.645,.045,.355,1)}.ant-select-selection--multiple .ant-select-selection__choice__disabled{padding:0 10px}.ant-select-selection--multiple .ant-select-selection__choice__content{display:inline-block;max-width:100%;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;-webkit-transition:margin .3s cubic-bezier(.645,.045,.355,1);transition:margin .3s cubic-bezier(.645,.045,.355,1)}.ant-select-selection--multiple .ant-select-selection__choice__remove{color:inherit;font-style:normal;line-height:0;text-align:center;text-transform:none;vertical-align:-.125em;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;position:absolute;right:4px;color:rgba(0,0,0,.45);font-weight:bold;line-height:inherit;cursor:pointer;-webkit-transition:all .3s;transition:all .3s;display:inline-block;font-size:12px;font-size:10px\9;-webkit-transform:scale(.83333333) rotate(0deg);-ms-transform:scale(.83333333) rotate(0deg);transform:scale(.83333333) rotate(0deg)}.ant-select-selection--multiple .ant-select-selection__choice__remove>*{line-height:1}.ant-select-selection--multiple .ant-select-selection__choice__remove svg{display:inline-block}.ant-select-selection--multiple .ant-select-selection__choice__remove:before{display:none}.ant-select-selection--multiple .ant-select-selection__choice__remove .ant-select-selection--multiple .ant-select-selection__choice__remove-icon{display:block}:root .ant-select-selection--multiple .ant-select-selection__choice__remove{font-size:12px}.ant-select-selection--multiple .ant-select-selection__choice__remove:hover{color:rgba(0,0,0,.75)}.ant-select-selection--multiple .ant-select-arrow,.ant-select-selection--multiple .ant-select-selection__clear{top:16px}.ant-select-allow-clear .ant-select-selection--single .ant-select-selection-selected-value{padding-right:16px}.ant-select-allow-clear .ant-select-selection--multiple .ant-select-selection__rendered,.ant-select-show-arrow .ant-select-selection--multiple .ant-select-selection__rendered{margin-right:20px}.ant-select-open .ant-select-arrow-icon svg{-webkit-transform:rotate(180deg);-ms-transform:rotate(180deg);transform:rotate(180deg)}.ant-select-open .ant-select-selection{border-color:#fa9e87;border-right-width:1px!important;outline:0;-webkit-box-shadow:0 0 0 2px rgba(236,114,89,.2);box-shadow:0 0 0 2px rgba(236,114,89,.2)}.ant-select-combobox .ant-select-arrow{display:none}.ant-select-combobox .ant-select-search--inline{float:none;width:100%;height:100%}.ant-select-combobox .ant-select-search__field__wrap{width:100%;height:100%}.ant-select-combobox .ant-select-search__field{position:relative;z-index:1;width:100%;height:100%;-webkit-box-shadow:none;box-shadow:none;-webkit-transition:all .3s cubic-bezier(.645,.045,.355,1),height 0s;transition:all .3s cubic-bezier(.645,.045,.355,1),height 0s}.ant-select-combobox.ant-select-allow-clear .ant-select-selection:hover .ant-select-selection__rendered,.ant-select-combobox.ant-select-show-arrow .ant-select-selection:hover .ant-select-selection__rendered{margin-right:20px}.ant-select-dropdown{margin:0;padding:0;color:rgba(0,0,0,.65);font-variant:tabular-nums;line-height:1.5;list-style:none;-webkit-font-feature-settings:"tnum","tnum",;font-feature-settings:"tnum","tnum",;position:absolute;top:-9999px;left:-9999px;z-index:1050;-webkit-box-sizing:border-box;box-sizing:border-box;font-size:14px;font-variant:normal;background-color:#fff;border-radius:4px;outline:none;-webkit-box-shadow:0 2px 8px rgba(0,0,0,.15);box-shadow:0 2px 8px rgba(0,0,0,.15)}.ant-select-dropdown.slide-up-appear.slide-up-appear-active.ant-select-dropdown-placement-bottomLeft,.ant-select-dropdown.slide-up-enter.slide-up-enter-active.ant-select-dropdown-placement-bottomLeft{-webkit-animation-name:antSlideUpIn;animation-name:antSlideUpIn}.ant-select-dropdown.slide-up-appear.slide-up-appear-active.ant-select-dropdown-placement-topLeft,.ant-select-dropdown.slide-up-enter.slide-up-enter-active.ant-select-dropdown-placement-topLeft{-webkit-animation-name:antSlideDownIn;animation-name:antSlideDownIn}.ant-select-dropdown.slide-up-leave.slide-up-leave-active.ant-select-dropdown-placement-bottomLeft{-webkit-animation-name:antSlideUpOut;animation-name:antSlideUpOut}.ant-select-dropdown.slide-up-leave.slide-up-leave-active.ant-select-dropdown-placement-topLeft{-webkit-animation-name:antSlideDownOut;animation-name:antSlideDownOut}.ant-select-dropdown-hidden{display:none}.ant-select-dropdown-menu{max-height:250px;margin-bottom:0;padding-left:0;overflow:auto;list-style:none;outline:none}.ant-select-dropdown-menu-item-group-list{margin:0;padding:0}.ant-select-dropdown-menu-item-group-list>.ant-select-dropdown-menu-item{padding-left:20px}.ant-select-dropdown-menu-item-group-title{height:32px;padding:0 12px;color:rgba(0,0,0,.45);font-size:12px;line-height:32px}.ant-select-dropdown-menu-item-group-list .ant-select-dropdown-menu-item:first-child:not(:last-child),.ant-select-dropdown-menu-item-group:not(:last-child) .ant-select-dropdown-menu-item-group-list .ant-select-dropdown-menu-item:last-child{border-radius:0}.ant-select-dropdown-menu-item{position:relative;display:block;padding:5px 12px;overflow:hidden;color:rgba(0,0,0,.65);font-weight:normal;line-height:22px;white-space:nowrap;text-overflow:ellipsis;cursor:pointer;-webkit-transition:background .3s ease;transition:background .3s ease}.ant-select-dropdown-menu-item:hover:not(.ant-select-dropdown-menu-item-disabled){background-color:#fff5f0}.ant-select-dropdown-menu-item:first-child{border-radius:4px 4px 0 0}.ant-select-dropdown-menu-item:last-child{border-radius:0 0 4px 4px}.ant-select-dropdown-menu-item-selected{color:rgba(0,0,0,.65);font-weight:600;background-color:#fafafa}.ant-select-dropdown-menu-item-disabled,.ant-select-dropdown-menu-item-disabled:hover{color:rgba(0,0,0,.25);cursor:not-allowed}.ant-select-dropdown-menu-item-active:not(.ant-select-dropdown-menu-item-disabled){background-color:#fff5f0}.ant-select-dropdown-menu-item-divider{height:1px;margin:1px 0;overflow:hidden;line-height:0;background-color:#e8e8e8}.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item{padding-right:32px}.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item .ant-select-selected-icon{position:absolute;top:50%;right:12px;color:rgba(0,0,0,0);font-weight:bold;font-size:12px;text-shadow:0 .1px 0,.1px 0 0,0 -.1px 0,-.1px 0;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);-webkit-transition:all .2s;transition:all .2s}.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item:hover .ant-select-selected-icon{color:rgba(0,0,0,.87)}.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item-disabled .ant-select-selected-icon{display:none}.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item-selected .ant-select-selected-icon,.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item-selected:hover .ant-select-selected-icon{display:inline-block;color:#ec7259}.ant-select-dropdown--empty.ant-select-dropdown--multiple .ant-select-dropdown-menu-item{padding-right:12px}.ant-select-dropdown-container-open .ant-select-dropdown,.ant-select-dropdown-open .ant-select-dropdown{display:block}.ant-empty{margin:0 8px;font-size:14px;line-height:22px;text-align:center}.ant-empty-image{height:100px;margin-bottom:8px}.ant-empty-image img{height:100%}.ant-empty-image svg{height:100%;margin:auto}.ant-empty-description{margin:0}.ant-empty-footer{margin-top:16px}.ant-empty-normal{margin:32px 0;color:rgba(0,0,0,.25)}.ant-empty-normal .ant-empty-image{height:40px}.ant-empty-small{margin:8px 0;color:rgba(0,0,0,.25)}.ant-empty-small .ant-empty-image{height:35px}._3kWNZz{text-align:center;padding:24px}.WVHbKq{font-size:24px;font-weight:500;margin-bottom:8px}._3eFswX{font-size:16px;color:#969696;margin-top:8px}._3eFswX>span{color:#da9e55}._1VQzqI{text-align:center;padding:24px 64px}._19gUNB{font-size:16px;font-weight:600;text-align:center;margin:16px 0}._1tunN3{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;-webkit-box-align:center;-ms-flex-align:center;align-items:center;height:72px;border-top:1px solid #eee}body.reader-night-mode ._1tunN3{border-color:#2f2f2f}._3ktw48{font-size:14px}._1iwqfH{font-size:28px;font-weight:500;float:right;color:#ec7259}._3b3lMj{font-size:14px}._1YY-Yc{font-size:12px;white-space:normal;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}.ant-select-selection-selected-value ._1YY-Yc{display:none}._1Ye-SM{margin:24px 0;padding:6px 24px}._1P9XxY{text-align:left;font-size:13px;color:#969696}._3osc0S{display:block;margin-top:16px;margin-bottom:24px;text-align:center}._1FUlTu{font-size:14px;font-weight:500;margin-bottom:12px}.ekdgh6{font-size:14px;color:#969696;margin-bottom:16px}.aC6MAl{font-size:14px;font-weight:normal;padding:6px 20px}._1kCBjS{-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;font-size:14px;color:#969696;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}._1kCBjS,._3BUZPB,._18vaTa{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._3BUZPB>span{margin-left:8px}._3BUZPB:not(:last-child){margin-right:12px}._2Bo4Th{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;width:40px;height:40px;color:#969696;border:1px solid #eee;border-radius:50%;font-size:18px;cursor:pointer}body.reader-night-mode ._2Bo4Th{border-color:#2f2f2f}._3Nksh7{background-color:#ec7259;color:#fff}._3Nksh7,body.reader-night-mode ._3Nksh7{border-color:#ec7259}._1LOh_5{cursor:pointer}._1LOh_5 .anticon{font-size:12px}._1x1ok9{cursor:pointer}._1x1ok9 .anticon{font-size:16px}._1yN79W{background-color:#f2f2f2}._1yN79W::-webkit-input-placeholder{color:#999}._1yN79W::-moz-placeholder{color:#999}._1yN79W:-ms-input-placeholder{color:#999}._1yN79W::-ms-input-placeholder{color:#999}._1yN79W::placeholder{color:#999}body.reader-night-mode ._1yN79W{background-color:#333}._3uZ5OL{text-align:center;padding:48px 64px}._2PLkjk{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin-bottom:24px}._2R1-48{min-width:50px;min-height:50px;width:50px;height:50px;border-radius:50%;border:1px solid #eee}._2h5tnQ{font-size:24px;font-weight:500;margin-left:16px}._1-bCJJ{-ms-flex-wrap:wrap;flex-wrap:wrap}._1-bCJJ,.LMa6S_{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.LMa6S_{-webkit-box-align:center;-ms-flex-align:center;align-items:center;width:162.5px;height:56px;font-size:16px;color:#969696;margin-bottom:12px;margin-right:12px;border-radius:10px;border:1px solid #eee;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}body.reader-night-mode .LMa6S_{border-color:#2f2f2f}.LMa6S_._1vONvL{color:#ec7259}.LMa6S_._1vONvL,body.reader-night-mode .LMa6S_._1vONvL{border-color:#ec7259}.LMa6S_._1sSZ6C{cursor:not-allowed;color:#969696;opacity:.5}.LMa6S_>i{font-size:20px}.LMa6S_>span{font-size:28px;font-style:italic}.LMa6S_:nth-child(3n){margin-right:0}.LMa6S_:nth-last-child(-n+3){margin-bottom:0}.LMa6S_:last-child{margin-right:0}._2ByDWa{position:relative;font-size:28px}._2ByDWa>span{font-size:16px;font-style:normal;opacity:1}._2ByDWa>input{position:absolute;top:50%;left:50%;width:100%;height:36px;margin:0 auto;text-align:center;-webkit-transform:translate(-50%,-50%);-ms-transform:translate(-50%,-50%);transform:translate(-50%,-50%);background-color:rgba(0,0,0,0);opacity:0;cursor:pointer}._2ByDWa>input::-webkit-inner-spin-button,._2ByDWa>input::-webkit-outer-spin-button{display:none}._2ByDWa._1vONvL>span{opacity:0}._2ByDWa._1vONvL>input{opacity:1;cursor:text}._3PA8BN>i{font-size:30px}._3PA8BN>span{font-size:16px;font-style:normal;margin-left:4px}._3PA8BN,._3PA8BN._1vONvL{color:#404040}body.reader-night-mode ._3PA8BN,body.reader-night-mode ._3PA8BN._1vONvL{color:#b3b3b3}._1yN79W{display:block;width:100%;height:80px;resize:none;margin-top:12px;padding:12px;border:none;border-radius:10px}._1_B577{font-size:15px;margin:12px 0}._3A-4KL{margin-top:24px;font-size:18px;font-weight:normal;padding:10px 48px}._3W59v5{display:block}.Uz-vZq,.VwEQ52{display:-webkit-box;display:-ms-flexbox;display:flex}.VwEQ52{-ms-flex-preferred-size:50%;flex-basis:50%;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;-webkit-box-align:center;-ms-flex-align:center;align-items:center;overflow:hidden}.VwEQ52:first-child{padding-right:20px}.VwEQ52:last-child{position:relative;padding-left:20px}.VwEQ52:last-child:before{content:"";position:absolute;width:1px;height:20px;left:0;background-color:#eee}body.reader-night-mode .VwEQ52:last-child:before{background-color:#2f2f2f}.VwEQ52:first-child:last-child{position:static;padding-left:0;padding-right:0}.VwEQ52:first-child:last-child:before{display:none}.VwEQ52 ._3nYIo3{min-width:54px;min-height:54px;width:54px;height:54px;border-radius:50%;border:1px solid #eee}body.reader-night-mode .VwEQ52 ._3nYIo3{border-color:#2f2f2f}.VwEQ52 ._2lfNuF{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;margin-left:10px;overflow:hidden}.VwEQ52 ._2lfNuF .Cqpr1X{color:#2d2d2d;font-weight:500;font-size:14px;margin-bottom:2px;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;white-space:nowrap}body.reader-night-mode .VwEQ52 ._2lfNuF .Cqpr1X{color:#b3b3b3}.VwEQ52 ._2lfNuF ._2qBui4{color:#969696;font-size:12px}.VwEQ52+.VwEQ52 ._2lfNuF{margin-left:0}._2pnG2B{margin-top:20px}._2pnG2B:last-child{padding:0}._2pnG2B:before{display:none}._2pnG2B ._3nYIo3{width:54px;height:72px;min-width:54px;min-height:72px;border-radius:4px}._2pnG2B ._2lfNuF{margin-left:10px;margin-right:12px}._2pnG2B ._2lfNuF ._2WEj6j{margin-top:2px;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}._13lIbp ._2qBui4{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._13lIbp ._14FSyQ,._13lIbp .H4XBOO>img{width:24px;height:24px;min-width:24px;min-height:24px;border-radius:50%;border:2px solid #fff}body.reader-night-mode ._13lIbp ._14FSyQ,body.reader-night-mode ._13lIbp .H4XBOO>img{border-color:#3d3d3d}._14FSyQ{color:inherit;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;color:#969696;background-color:#ececec}._14FSyQ:active,._14FSyQ:hover{color:inherit}body.reader-night-mode ._14FSyQ{background-color:#505050}.H4XBOO:not(:first-child){margin-left:-6px}.H4XBOO:last-of-type{margin-right:6px}._191KSt{cursor:pointer}._26JdYM{display:-webkit-box;display:-ms-flexbox;display:flex}._26JdYM ._3GKFE3{margin-top:0;margin-bottom:48px}._3LHFA-{width:40px;height:40px;border-radius:50%;border:1px solid #eee;margin-right:10px}body.reader-night-mode ._3LHFA-{border-color:#2f2f2f}._3GKFE3{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;margin-top:16px}._1u_H4i{padding:12px 16px;width:100%;height:90px;font-size:13px;border:1px solid #eee;border-radius:4px;background-color:#fafafa;resize:none;display:inline-block;vertical-align:top;outline-style:none}._1u_H4i::-webkit-input-placeholder{color:#999}._1u_H4i::-moz-placeholder{color:#999}._1u_H4i:-ms-input-placeholder{color:#999}._1u_H4i::-ms-input-placeholder{color:#999}._1u_H4i::placeholder{color:#999}body.reader-night-mode ._1u_H4i{background-color:#333;border-color:#2f2f2f}._3IXP9Q{-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;margin-top:16px;font-size:14px;color:#969696}._3IXP9Q,.SKZUyR{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.SKZUyR{-ms-flex-negative:0;flex-shrink:0}._3MkVdm{font-size:18px;margin-right:12px}._3MkVdm:hover{color:#7d7d7d}._3Tp4of{-ms-flex-negative:0;flex-shrink:0;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._2lR7N6{padding:20px 0 30px;--base-color:#dfdfdf}body.reader-night-mode ._2lR7N6{--base-color:#737373}._2lR7N6 ._17_lFi{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin-bottom:16px}._2lR7N6 ._17_lFi ._3k5vgx{margin-right:6px;width:38px;height:38px;border-radius:50%;background-color:var(--base-color)}._2lR7N6 ._17_lFi .U36Th9{margin-bottom:6px;height:16px;width:60px;background-color:var(--base-color)}._2lR7N6 ._17_lFi ._9aTHBB{height:12px;width:120px;background-color:var(--base-color)}._2lR7N6 ._1Lq8tt{width:100%;height:16px;margin-bottom:8px;background-color:var(--base-color);-webkit-animation:_1i8o5w 1s ease-in-out infinite;animation:_1i8o5w 1s ease-in-out infinite}._2lR7N6 ._1muh0x{-webkit-animation-delay:-.5s;animation-delay:-.5s}._2lR7N6 ._3Pu4Wf{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding-top:4px;color:var(--base-color);font-size:16px}._2lR7N6 ._3Pu4Wf ._1mcOnW{height:14px;width:40px;margin-left:5px;margin-right:10px;background-color:var(--base-color)}@-webkit-keyframes _1i8o5w{0%{width:60%}50%{width:100%}to{width:60%}}@keyframes _1i8o5w{0%{width:60%}50%{width:100%}to{width:60%}}._1JPdR9{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start;-ms-flex-wrap:wrap;flex-wrap:wrap;width:345px;margin-top:12px}._3K5dOX{-ms-flex-negative:0;flex-shrink:0;width:110px;height:110px;margin-right:5px;margin-bottom:5px;border:1px solid #eee;border-radius:4px;background-position:50%;background-repeat:no-repeat;background-size:contain}body.reader-night-mode ._3K5dOX{border-color:#2f2f2f}._2IUqvs{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start}._2IUqvs._3uuww8 ._1K9gkf{padding-bottom:0;border:none}._2IUqvs:last-child ._1K9gkf{margin-bottom:0;padding-bottom:0;border:none}._1_jhXc{width:40px;height:40px;border:1px solid #eee;border-radius:50%;overflow:hidden}body.reader-night-mode ._1_jhXc{border-color:#2f2f2f}._1K9gkf{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;margin-left:10px;margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid #eee}body.reader-night-mode ._1K9gkf{border-color:#2f2f2f}._1whZvR,._2ti5br{position:relative;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin-top:12px;font-size:15px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}._1whZvR:hover ._1NgfK-,._2ti5br:hover ._1NgfK-{visibility:visible;opacity:1}._1Jvkh4,._1NgfK-,._2GXD2V{cursor:pointer;margin-right:12px;color:#b0b0b0}._1Jvkh4:hover,._1NgfK-:hover,._2GXD2V:hover{color:#9c9c9c}._1NgfK-{position:absolute;right:0;visibility:hidden;opacity:0}._1NgfK-.ant-popover-open{visibility:visible;opacity:1}._2GXD2V{margin-right:16px}._2GXD2V._5LkTIL,._2GXD2V:hover{color:#ec7259}._23G05g{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;font-size:15px;font-weight:500}._1xqkrI{margin-top:2px;font-size:12px;color:#969696}._3pyYXB{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;margin-left:4px;padding:0 2px;font-size:12px;font-weight:normal;color:#ec7259;border:1px solid #ec7259;border-radius:4px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}._2bDGm4{margin-top:10px;font-size:16px;line-height:1.5}._2kvBge{margin-top:20px}._3g0yKR{padding:20px 0 16px;border-top:1px solid #eee}._3g0yKR ._3d_vFY{display:-webkit-box;display:-ms-flexbox;display:flex}._3g0yKR:last-child{padding-bottom:0}body.reader-night-mode ._3g0yKR{border-color:#2f2f2f}._1Y3RXD{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;font-size:15px;margin:12px 0;color:#0681d0;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:pointer}._1whZvR{margin-top:16px;padding-top:16px;border-top:1px solid #eee}body.reader-night-mode ._1whZvR{border-color:#2f2f2f}.WliqwT{color:#969696;padding-left:12px;border-left:1px solid #eee}.T4mGDk{color:#0681d0;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:pointer}body.reader-night-mode .WliqwT{border-color:#2f2f2f}._13OjNv{display:-webkit-box;display:-ms-flexbox;display:flex;margin-top:24px;margin-bottom:8px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;color:#969696}._3ubyu9,._13OjNv,.LaYREM{-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}._3ubyu9,.LaYREM{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;width:32px;height:32px;line-height:32px;font-size:14px;margin:0 4px;border:1px solid #eee;border-radius:50%;cursor:pointer}body.reader-night-mode ._3ubyu9,body.reader-night-mode .LaYREM{border-color:#2f2f2f}._3ubyu9:hover,.LaYREM:hover{background-color:#f2f2f2}._1i9WqE._3ubyu9,.LaYREM._1i9WqE{color:#ec7259;border-color:#ec7259;pointer-events:none}._3ubyu9{width:auto;padding-left:12px;padding-right:12px;border-radius:20px}._10KzV0{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._10KzV0 ._2R7vBo{margin-left:6px;font-size:14px;font-weight:normal}._2zSaYx{display:-webkit-box;display:-ms-flexbox;display:flex}._1ekjko,._393S4n{font-size:12px;font-weight:normal;color:#969696;margin-left:12px;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}body.reader-night-mode ._1ekjko{color:#666}._1ekjko._1BIpxf{color:#2d2d2d}body.reader-night-mode ._1ekjko._1BIpxf{color:#969696}._2gPNSa{margin-top:30px;margin-bottom:30px}._1DVmvZ{font-size:12px;font-weight:normal;color:#969696;margin-left:12px;padding:2px 8px;border:1px solid #eee;border-radius:16px;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}body.reader-night-mode ._1DVmvZ{border-color:#2f2f2f}._1DVmvZ._1BIpxf{color:#fff;background-color:#ec7259;border-color:#ec7259}body.reader-night-mode ._1DVmvZ._1BIpxf{color:#3d3d3d;border-color:#ec7259}._3SnN_k{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;font-size:18px;padding-top:20px;padding-bottom:20px}._3b8Ibd{text-align:center}._3b8Ibd>img{width:169px;height:140px}._3b8Ibd ._1DiGFn{margin-top:28px;margin-bottom:8px;font-size:14px;color:#969696}._3b8Ibd ._1DiGFn ._3QdbM2{color:#ec7259}._1Kc1pc{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;padding:20px 0}._1Kc1pc:not(:last-child){border-bottom:1px solid #eee}body.reader-night-mode ._1Kc1pc{border-color:#2f2f2f}._1Kc1pc ._3cgiY6{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._1MTfTm{min-width:50px;min-height:50px;width:50px;height:50px;border-radius:4px;border:1px solid #eee}body.reader-night-mode ._1MTfTm{border-color:#2f2f2f}._1gXCcE{margin:0 12px}._3puJ3K{display:block;font-size:16px;font-weight:500;margin-bottom:2px}._1AkY7D{font-size:12px;color:#969696}._1v2f0N{height:480px;padding:24px;overflow-y:scroll}._3fC9Lb{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}._2MEVQW{display:block;margin-left:24px;cursor:pointer}._2MEVQW>span{margin-left:4px}._3qtwqN,.q-2pty{display:block;text-align:center;margin:32px 0;color:#969696}._3qtwqN{cursor:pointer}.RtGuHg{padding:24px 0}.saTF2Q{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._3sAsA5{margin-left:12px;font-size:14px;font-weight:normal;line-height:1;color:#969696;cursor:pointer}._3sAsA5>span{margin-left:3px}._99AOeY{display:-webkit-box;display:-ms-flexbox;display:flex;padding:16px 0}._99AOeY:not(:last-child){border-bottom:1px solid #eee}body.reader-night-mode ._99AOeY{border-color:#2f2f2f}._3CGUtf{-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;width:48px;margin-right:16px;font-family:Arial-BoldItalicMT,sans-serif;font-size:22px;font-weight:normal;color:#b3b3b3}._1euQZJ,._3CGUtf{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._1euQZJ{margin-bottom:4px}._130BbT{display:block;text-align:center;font-size:12px;color:#da9e55;background-color:rgba(218,158,85,.15);margin-left:4px;padding:2px 10px;border-radius:12px;line-height:20px}._1JV12M{font-size:16px;font-weight:500}._1JV12M:hover{text-decoration:underline}.Fm0jls{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;font-size:12px;color:#969696}.Fm0jls ._17ywf4{color:#ec7259;margin-right:8px}._37OvKa{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;margin-top:16px;margin-bottom:32px}._37OvKa>i{color:#ec7259;font-size:20px;margin-right:8px}._2xV5A4{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding:16px 0}._2xV5A4:not(:last-child){border-bottom:1px solid #eee}body.reader-night-mode ._2xV5A4{border-color:#2f2f2f}._1MmGv5{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._2E7TMH{width:50px;height:50px;border-radius:50%;border:1px solid #eee}._2eSeIY{font-size:16px;font-weight:500;margin-left:12px}._1NZ1BD{margin:32px 0}._2nF7af{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}._2nVyQz{margin-bottom:24px}._2CcN3T{font-size:14px;font-weight:400;line-height:18px;padding-left:5px;border-left:4px solid #ec7259}._3S34Y_{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin:0}._3S34Y_>img{width:144px;height:144px;margin-bottom:12px}._2JdSds{line-height:18px;font-size:13px;font-weight:normal;color:#999;cursor:pointer}._2JdSds>span{margin-left:2px;pointer-events:none}._2Nttfz{-ms-flex-wrap:wrap;flex-wrap:wrap}._2Nttfz,._3s5t0Q,.H7E3vT{display:-webkit-box;display:-ms-flexbox;display:flex}._3s5t0Q,.H7E3vT{-ms-flex-negative:0;flex-shrink:0;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin-right:12px;margin-bottom:12px;cursor:pointer}._3s5t0Q{background-color:#f5f5f5;padding:5px 10px 5px 5px;border-radius:4px}body.reader-night-mode ._3s5t0Q{background-color:#4d4d4d}._3s5t0Q .anticon{margin-right:2px;font-size:12px}._1lsejJ{padding:7px 10px}._2vEwGY{-ms-flex-negative:0;flex-shrink:0;width:24px;height:24px;margin-right:8px;border-radius:2px}._2-Djqu{font-size:14px;line-height:20px}.H7E3vT{font-size:14px;color:#999}.H7E3vT .anticon{margin-left:4px;font-size:12px}._29KFEa{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;font-size:14px;font-weight:normal;line-height:18px}._29KFEa .anticon{margin-left:1px;font-size:12px}._1iTR78{margin-bottom:24px}._11jppn{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;padding:20px 0;border-bottom:1px solid #eee}._11jppn:first-child{padding-top:0}._11jppn:last-child{padding-bottom:0;border:none}body.reader-night-mode ._11jppn{border-color:#2f2f2f}.em6wEs,.JB6qEE{overflow:hidden}.em6wEs{font-size:18px;font-weight:500;margin-bottom:4px;color:#404040;-o-text-overflow:ellipsis;text-overflow:ellipsis;white-space:nowrap}body.reader-night-mode .em6wEs{color:#b3b3b3}._2voXH8:active,._2voXH8:hover{text-decoration:underline}._3fvgn4{font-size:13px;color:#666;line-height:20px;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}._1pJt6F{margin-top:8px}._1pJt6F,._3IWz1q{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._34VC_H{width:24px;height:24px;margin-right:4px;border-radius:50%}._3tPsL6{font-size:13px;color:#969696;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;white-space:nowrap}._10MMAm{margin-left:20px}._3zGDUj{display:block;-ms-flex-negative:0;flex-shrink:0;width:150px;height:120px;border-radius:4px;border:1px solid hsla(0,0%,50.2%,.1)}._22bNOL{margin-bottom:10px;border-radius:4px;overflow:hidden}._3FPkr1{position:relative;display:block;width:100%;height:100%;background-position:50%;background-repeat:no-repeat;background-size:cover}._3Tj3M5{position:absolute;display:block;font-size:12px;padding:2px 6px;color:#fff;cursor:pointer}._2ibkP3,._3Tj3M5{bottom:0;right:0;background-color:rgba(0,0,0,.5)}._2ibkP3{position:fixed;top:0;left:0;height:100vh;z-index:1100;filter:alpha(opacity=50)}body.reader-night-mode ._2ibkP3{background-color:rgba(61,61,61,.75);filter:alpha(opacity=75)}._2jDHp5{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1150;overflow:hidden;outline:0;-webkit-overflow-scrolling:touch}.L-NY99{height:auto;max-height:100vh;max-width:100%;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:-webkit-zoom-out;cursor:zoom-out;-webkit-transition:-webkit-transform .2s ease-in-out;transition:-webkit-transform .2s ease-in-out;-o-transition:transform .2s ease-in-out;transition:transform .2s ease-in-out;transition:transform .2s ease-in-out,-webkit-transform .2s ease-in-out;-webkit-transform-origin:0 0;-ms-transform-origin:0 0;transform-origin:0 0}._3G_AE-{-webkit-transition:none;-o-transition:none;transition:none}._3C00cT{position:fixed}._2kc3FH,._2TG34g{position:absolute;top:50%;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);width:60px;height:60px;font-size:24px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;border-radius:50%;color:#fff;cursor:pointer}._2kc3FH:hover,._2TG34g:hover{background-color:hsla(0,0%,100%,.1)}body.reader-night-mode ._2kc3FH,body.reader-night-mode ._2TG34g{color:#bfbfbf}._3yUKnr{cursor:default;opacity:.4}._3yUKnr:hover{background-color:rgba(0,0,0,0)}._2TG34g{left:24px}._2kc3FH{right:24px}._2Gw6nl{position:absolute;bottom:32px;left:50%;-webkit-transform:translate3d(-50%,0,0);transform:translate3d(-50%,0,0);padding:6px 16px;border-radius:20px;border:1px solid #fff;background-color:rgba(0,0,0,.4);font-size:14px;color:#fff}body.reader-night-mode ._2Gw6nl{color:#bfbfbf;border-color:#bfbfbf}._2Gw6nl:active,._2Gw6nl:focus,._2Gw6nl:hover{color:#fff}body.reader-night-mode ._2Gw6nl:active,body.reader-night-mode ._2Gw6nl:focus,body.reader-night-mode ._2Gw6nl:hover{color:#bfbfbf}._3Pnjry{position:fixed;top:216px;left:calc((100vw - 1000px)/2 - 78px);-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}._1pUUKr{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;margin-bottom:16px;cursor:pointer;color:#969696}._1pUUKr,._2VdqdF{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}._2VdqdF{-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;width:48px;height:48px;font-size:18px;border-radius:50%;-webkit-box-shadow:0 1px 3px rgba(26,26,26,.1);box-shadow:0 1px 3px rgba(26,26,26,.1);background-color:#fff}body.reader-night-mode ._2VdqdF{background-color:#404040}.P63n6G{margin-top:4px;font-size:14px;text-align:center;color:#969696;overflow:hidden;height:19px}._2LKTFF{-webkit-transition:-webkit-transform .2s;transition:-webkit-transform .2s;-o-transition:transform .2s;transition:transform .2s;transition:transform .2s,-webkit-transform .2s}._1GPnWJ{display:block;height:19px}._1GPnWJ.RhY_sp{visibility:hidden;opacity:0}._1pUUKr._2Z1aZJ ._2VdqdF{color:#fff;background-color:#ec7259}._1pUUKr._2Z1aZJ .P63n6G{color:#ec7259}._1pUUKr._2Z1aZJ ._2LKTFF{-webkit-transform:translateY(-19px);-ms-transform:translateY(-19px);transform:translateY(-19px)}._3MOB7g{text-align:center;padding:24px}._1U9mRW{font-size:24px;font-weight:500;margin-bottom:16px}._2rxlQh{font-size:16px;margin-bottom:24px}._2mpYuT{margin-bottom:16px}._21FTIM{display:block;padding:16px 24px}._3qpYUS{margin-bottom:16px}._1I6Gjn,._3qpYUS{display:-webkit-box;display:-ms-flexbox;display:flex}._1I6Gjn{-webkit-box-align:center;-ms-flex-align:center;align-items:center;font-size:15px}._1I6Gjn>span{margin:0 8px}._21urAK{display:block;padding:12px 16px;width:100%;height:auto;font-size:14px;border:1px solid #eee;border-radius:4px;background-color:#f2f2f2;resize:none}._21urAK::-webkit-input-placeholder{color:#999}._21urAK::-moz-placeholder{color:#999}._21urAK:-ms-input-placeholder{color:#999}._21urAK::-ms-input-placeholder{color:#999}._21urAK::placeholder{color:#999}body.reader-night-mode ._21urAK{background-color:#333;border-color:#2f2f2f}._1RuRku{font-size:30px;font-weight:700;word-break:break-word}._21bLU4 .ant-back-top{bottom:96px}@media only screen and (max-width:900px){._21bLU4 .ant-back-top{display:none}}._3MyrRP{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;width:40px;height:40px;border-radius:50%;color:#8c8c8c;font-size:18px;-webkit-box-shadow:0 1px 3px rgba(26,26,26,.1);box-shadow:0 1px 3px rgba(26,26,26,.1);background-color:#fff}body.reader-night-mode ._3MyrRP{-webkit-box-shadow:0 1px 3px rgba(0,0,0,.3);box-shadow:0 1px 3px rgba(0,0,0,.3);background-color:#3d3d3d}._1KC9MV{position:absolute;width:40px;height:40px;top:-150%;background-image:url(data:image/png;base64,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);background-position:50%;background-repeat:no-repeat;background-size:cover}._3yPTTQ{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;height:40px;margin:0 -24px 20px;font-size:14px;line-height:14px;color:#0681d0;background:#e4f4fe}._3yPTTQ>i{font-size:16px;margin-right:4px}._3yPTTQ .anticon-spin{-webkit-animation-duration:1.5s;animation-duration:1.5s}._2C7CDc{width:960px;margin:0 auto;padding-top:80px;text-align:center}._35eZ2j{width:200px}._2Tso_9{font-size:32px;font-weight:500;color:#ec7259;margin-top:16px;margin-bottom:40px}._1aPG4O{font-size:20px;margin-top:4px}._2mcXeT{margin-top:32px}._33ha_L{display:inline-block;text-decoration:none}.xiRCyp{width:125px;height:125px}._3YhoEV{color:#404040;font-size:20px;margin-top:8px}body.reader-night-mode ._3YhoEV{color:#b3b3b3}</style>'
        content = _ + content

        return content

    async def _get_article_html(self, article_url, article_url_type) -> tuple:
        """
        获取文章的html
        :return:
        """
        video_url = ''
        body = ''
        try:
            if article_url_type == 'wx':
                return await unblock_func(
                    func_name=self.unblock_get_wx_article_html,
                    func_args=[
                        article_url,
                    ],
                    default_res=('', ''),
                    logger=self.lg, )

            elif article_url_type == 'tt':
                return await self._get_tt_article_html(article_url=article_url)

            elif article_url_type == 'js':
                return await self._get_js_article_html(article_url=article_url)

            elif article_url_type == 'kd':
                return await unblock_func(
                    func_name=self.unblock_get_kd_article_html,
                    func_args=[
                        article_url,
                    ],
                    default_res=('', ''),
                    logger=self.lg,)

            elif article_url_type == 'kb':
                return await unblock_func(
                    func_name=self.unblock_get_kb_article_html,
                    func_args=[
                        article_url,
                    ],
                    default_res=('', ''),
                    logger=self.lg,)

            elif article_url_type == 'df':
                return await self._get_df_article_html(article_url=article_url)

            elif article_url_type == 'sg':
                return await self._get_sg_article_html(article_url=article_url)

            elif article_url_type == 'bd':
                return await self._get_bd_article_html(article_url=article_url)

            elif article_url_type == 'zq':
                return await self._get_zq_article_html(article_url=article_url)

            elif article_url_type == 'yg':
                return await self._get_yg_article_html(article_url=article_url)

            elif article_url_type == 'xg':
                return await self._get_xg_article_html(article_url=article_url)

            elif article_url_type == 'fh':
                return await self._get_fh_article_html(article_url=article_url)

            elif article_url_type == 'ys':
                return await self._get_ys_article_html(article_url=article_url)

            elif article_url_type == 'cn':
                return await self._get_cn_article_html(article_url=article_url)

            elif article_url_type == 'if':
                return await self._get_if_article_html(article_url=article_url)

            elif article_url_type == 'ss':
                return await self._get_ss_article_html(article_url=article_url)

            elif article_url_type == 'jm':
                return await self._get_jm_article_html(article_url=article_url)

            elif article_url_type == 'pp':
                return await self._get_pp_article_html(article_url=article_url)

            elif article_url_type == 'hx':
                return await self._get_hx_article_html(article_url=article_url)

            elif article_url_type == 'nfzm':
                return await self._get_nfzm_article_html(article_url=article_url)

            elif article_url_type == 'hqx':
                return await self._get_hqx_article_html(article_url=article_url)

            elif article_url_type == 'ck':
                return await self._get_ck_article_html(article_url=article_url)

            elif article_url_type == 'lsp':
                return await unblock_func(
                    func_name=self.unblock_get_lsp_article_html,
                    func_args=[
                        article_url,
                    ],
                    default_res=('', ''),
                    logger=self.lg,)

            elif article_url_type == 'amz':
                return await self._get_amz_article_html(article_url=article_url)

            elif article_url_type == 'mp':
                return await unblock_func(
                    func_name=self.unblock_get_mp_article_html,
                    func_args=[
                        article_url,
                    ],
                    default_res=('', ''),
                    logger=self.lg,)

            elif article_url_type == 'hk':
                return await self._get_hk_article_html(article_url=article_url)

            elif article_url_type == '7y7':
                return await self._get_7y7_article_html(article_url=article_url)

            elif article_url_type == 'qqbb':
                return await self._get_qqbb_article_html(article_url=article_url)

            elif article_url_type == 'ft':
                return await self._get_ft_article_html(article_url=article_url)

            elif article_url_type == '91mt':
                return await self._get_91mt_article_html(article_url=article_url)

            elif article_url_type == 'xq':
                return await self._get_xq_article_html(article_url=article_url)

            elif article_url_type == '5h':
                return await self._get_5h_article_html(article_url=article_url)

            elif article_url_type == 'bdj':
                return await self._get_bdj_article_html(article_url=article_url)

            elif article_url_type == 'jd':
                return await self._get_jd_article_html(article_url=article_url)

            elif article_url_type == 'lfd':
                return await self._get_lfd_article_html(article_url=article_url)

            elif article_url_type == 'blbl':
                return await self._get_blbl_article_html(article_url=article_url)

            elif article_url_type == 'kys':
                return await self._get_kys_article_html(article_url=article_url)

            elif article_url_type == 'gxg':
                return await self._get_gxg_article_html(article_url=article_url)

            elif article_url_type == 'kr':
                return await self._get_kr_article_html(article_url=article_url)

            elif article_url_type == 'dfsp':
                return await self._get_dfsp_article_html(article_url=article_url)

            elif article_url_type == 'txws':
                return await self._get_txws_article_html(article_url=article_url)

            elif article_url_type == 'klm':
                return await self._get_klm_article_html(article_url=article_url)

            elif article_url_type == 'ky':
                return await self._get_ky_article_html(article_url=article_url)

            elif article_url_type == 'dy':
                return await self._get_dy_article_html(article_url=article_url)

            elif article_url_type == 'jrxsp':
                return await self._get_jrxsp_article_html(article_url=article_url)

            elif article_url_type == 'jhgzw':
                return await self._get_jhgzw_article_html(article_url=article_url)

            elif article_url_type == 'jhrx':
                return await self._get_jhrx_article_html(article_url=article_url)

            elif article_url_type == 'jhwb':
                return await self._get_jhwb_article_html(article_url=article_url)

            elif article_url_type == 'jhbdsv':
                return await self._get_jhbdsv_article_html(article_url=article_url)

            elif article_url_type == 'bdqmxsv':
                return await self._get_bdqmxsv_article_html(article_url=article_url)

            elif article_url_type == 'jhyw18q':
                return await self._get_jhyw18q_article_html(article_url=article_url)

            elif article_url_type == 'jhzjol':
                return await self._get_jhzjol_article_html(article_url=article_url)

            else:
                raise AssertionError('未实现的解析!')

        except AssertionError:
            self.lg.error('遇到错误:', exc_info=True)

            return body, video_url

    async def _get_jhzjol_article_html(self, article_url) -> tuple:
        """
        获取jhzjol html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(
            connection_status_keep_alive=False,
        )
        headers.update({
            'Proxy-Connection': 'keep-alive',
            # 'Referer': 'http://jinhua.zjol.com.cn/jsbd/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        return body, video_url

    async def _get_jhyw18q_article_html(self, article_url) -> tuple:
        """
        获取jhyw18q html
        :param article_url:
        :return:
        """
        video_url = ''
        parser_obj = await self._get_parse_obj(article_url_type='jhyw18q')
        article_id = await async_parse_field(
            parser=parser_obj['article_id'],
            target_obj=article_url,
            logger=self.lg, )
        assert article_id != ''
        self.lg.info('article_id: {}'.format(article_id))

        headers = await async_get_random_headers(
            user_agent_type=1,
            cache_control=''
        )
        headers.update({
            'referer': 'https://m.18qiang.com/',
        })
        params = (
            ('tid', article_id),
        )
        body = await unblock_request(
            url='https://m.18qiang.com/read.php',
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries, )
        assert body != ''
        # self.lg.info(body)

        return body, video_url

    async def _get_bdqmxsv_article_html(self, article_url) -> tuple:
        """
        获取bdqmxsv html
        :param article_url:
        :return:
        """
        parser_obj = await self._get_parse_obj(article_url_type='bdqmxsv')
        article_id = await async_parse_field(
            parser=parser_obj['article_id'],
            target_obj=article_url,
            logger=self.lg,)
        assert article_id != ''
        self.lg.info('article_id: {}'.format(article_id))

        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            upgrade_insecure_requests=False,
            cache_control='', )
        headers.update({
            'authority': 'quanmin.baidu.com',
            'accept': '*/*',
            # 'referer': 'https://quanmin.baidu.com/sv?source=share-h5&pd=qm_share_mvideo&vid=4538982913039184503&shared_cuid=AqqqB',
        })
        params = (
            ('source', 'share-h5'),
            ('pd', 'qm_share_mvideo'),
            ('vid', article_id),        # '4538982913039184503'
            # ('shared_cuid', 'AqqqB'),
            ('_format', 'json'),
        )

        body = await unblock_request(
            url='https://quanmin.baidu.com/wise/growth/api/sv/immerse',
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,
        )
        assert body != ''
        # self.lg.info(body)

        data = json_2_dict(
            json_str=body,
            default_res={},
            logger=self.lg, ).get('data', {})
        assert data != {}
        try:
            data['four_palace_relate_list'] = []
            data['comment_info'] = []
        except Exception:
            pass
        # pprint(data)

        self.hook_target_api_data = data
        video_url = self.hook_target_api_data\
            .get('meta', {})\
            .get('video_info', {})\
            .get('clarityUrl', [])[0]\
            .get('url', '')
        self.lg.info('video_url: {}'.format(video_url))

        return body, video_url

    async def _get_jhbdsv_article_html(self, article_url) -> tuple:
        """
        获取jhbdsv html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
        )
        headers.update({
            'authority': 'sv.baidu.com',
        })
        if 'sv.baidu.com/videoui' not in article_url:
            raise ValueError('待采集的文章地址值异常, article_url: {}'.format(article_url))
        else:
            pass

        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        data = json_2_dict(
            json_str=re.compile('window\.__PRELOADED_STATE__ = (.*); document\.querySelector').findall(body)[0],
            logger=None, ).get('curVideoMeta', {})
        # pprint(data)

        self.hook_target_api_data = data
        assert self.hook_target_api_data != {}
        video_url = self.hook_target_api_data\
            .get('videoInfoExt', {})\
            .get('default', {})\
            .get('defaultUrlHttp', '')
        assert video_url != ''
        self.lg.info('video_url: {}'.format(video_url))

        return body, video_url

    async def _get_jhwb_article_html(self, article_url) -> tuple:
        """
        获取jhwb html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
        )
        headers.update({
            'authority': 'www.96356.in',
            # 'referer': 'https://www.96356.in/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        return body, video_url

    async def _get_jhrx_article_html(self, article_url) -> tuple:
        """
        获取金华热线 html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            cache_control='',)
        headers.update({
            'Proxy-Connection': 'keep-alive',
            'referer': 'http://m.0579.cn',
        })

        body = await unblock_request(
            url=article_url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        body = body.replace('<imgsrc', '<img src',)

        return body, video_url

    async def _get_jhgzw_article_html(self, article_url) -> tuple:
        """
        获取jhgzw html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers(user_agent_type=0)
        headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'referer': 'https://food.jinhua.com.cn/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        body = body.replace('id=\"m3u8\"value=', 'id=\"m3u8\" value=',)
        # self.lg.info(body)

        # 处理纯视频的
        video_url_sel = {
            'method': 'css',
            'selector': 'section#videocontent input#m3u8 ::attr("value")',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg,)
        # self.lg.info(video_url)
        if video_url != '':
            self.lg.info('video_url: {}'.format(video_url))
        else:
            pass

        return body, video_url

    async def _get_jrxsp_article_html(self, article_url) -> tuple:
        """
        获取jrxsp html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            cache_control='', )
        headers.update({
            'Proxy-Connection': 'keep-alive',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        video_url_sel = {
            'method': 'css',
            'selector': 'div.media video ::attr("src")',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg,)
        assert video_url != ''
        video_url = 'http:' + video_url if video_url != '' else ''
        self.lg.info('video_url: {}'.format(video_url))

        return body, video_url

    async def _get_dy_article_html(self, article_url) -> tuple:
        """
        获取dy html
        :param article_url:
        :return:
        """
        item_ids = ''
        if 'v.douyin.com' in article_url:
            # 处理从dy 分享出来的短地址
            headers = await async_get_random_headers(
                user_agent_type=1,
                connection_status_keep_alive=False,
                cache_control='', )
            headers.update({
                'authority': 'v.douyin.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            })
            # 下面需设置allow_redirects=False, 才可获取到数据
            body = await unblock_request(
                url=article_url,
                headers=headers,
                ip_pool_type=self.ip_pool_type,
                proxy_type=PROXY_TYPE_HTTPS,
                num_retries=self.request_num_retries,
                allow_redirects=False,
                logger=self.lg,)
            assert body != ''
            # self.lg.info(body)

            # 获取未被重定向的a标签地址进行后续请求
            a_sel = {
                'method': 're',
                'selector': 'href=\"(.*?)\"',
            }
            target_a_url = await async_parse_field(
                parser=a_sel,
                target_obj=body,
                logger=self.lg, )
            assert target_a_url != ''
            self.lg.info('获取到待跳转的原地址: {}'.format(target_a_url))

            # 获取跳转后的body, 目的获取item_ids, dytk
            body = await unblock_request(
                url=target_a_url,
                headers=headers,
                ip_pool_type=self.ip_pool_type,
                proxy_type=PROXY_TYPE_HTTPS,
                num_retries=self.request_num_retries,
                logger=self.lg,)
            assert body != ''
            # self.lg.info(body)

            item_ids_sel = {
                'method': 're',
                'selector': 'itemId\: \"(\d+)\",',
            }
            dytk_sel = {
                'method': 're',
                'selector': 'dytk\: \"(\w+)\"',
            }
            item_ids = await async_parse_field(
                parser=item_ids_sel,
                target_obj=body,
                logger=self.lg,
            )
            dytk = await async_parse_field(
                parser=dytk_sel,
                target_obj=body,
                logger=self.lg,
            )
            assert item_ids != ''
            assert dytk != ''
            self.lg.info('item_ids: {}, dytk: {}'.format(item_ids, dytk))

            # 下面是官方web页面获取视频数据接口, 但是视频无法被cp服务器上传, so pass
            # headers = await async_get_random_headers(
            #     user_agent_type=1,
            #     connection_status_keep_alive=False,
            #     upgrade_insecure_requests=False,
            #     cache_control='', )
            # headers.update({
            #     'authority': 'www.iesdouyin.com',
            #     'accept': '*/*',
            #     'x-requested-with': 'XMLHttpRequest',
            #     # 'referer': 'https://www.iesdouyin.com/share/video/6788405311460920583/?region=CN&amp;mid=6788399235936750339&amp;u_code=14a6g7j4m&amp;titleType=title&amp;timestamp=1581400527&amp;utm_campaign=client_share&amp;app=aweme&amp;utm_medium=ios&amp;tt_from=copy&amp;utm_source=copy',
            #     'referer': target_a_url,
            # })
            # params = (
            #     ('item_ids', item_ids),
            #     ('dytk', dytk),
            # )
            # body = await unblock_request(
            #     url='https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/',
            #     headers=headers,
            #     params=params,
            #     ip_pool_type=self.ip_pool_type,
            #     proxy_type=PROXY_TYPE_HTTPS,
            #     num_retries=self.request_num_retries,
            #     logger=self.lg,)
            # # self.lg.info(body)
            # assert body != ''
            # self.hook_target_api_data = json_2_dict(
            #     json_str=body,
            #     default_res={},
            #     logger=self.lg, ).get('item_list', [])[0]
            # # pprint(self.hook_target_api_data)
            #
            # video_url = self.hook_target_api_data\
            #     .get('video', {})\
            #     .get('download_addr', {})\
            #     .get('url_list', [])[0]
            # self.lg.info('获取到dy video_url: {}'.format(video_url))

        elif 'www.iesdouyin.com' in article_url:
            item_ids_sel = {
                'method': 're',
                'selector': '/video/(\d+)/'
            }
            item_ids = await async_parse_field(
                parser=item_ids_sel,
                target_obj=article_url,
                logger=self.lg,
            )
            assert item_ids != ''
            self.lg.info('item_ids: {}'.format(item_ids))

        else:
            raise ValueError('article_url 为抖音未知类型地址, 请检查!')

        # ** dy 去水印
        # 三方去水印工具地址: https://sy.kuakuavideo.com/douyin.html
        headers = await async_get_random_headers(
            user_agent_type=1,
            upgrade_insecure_requests=False,
            cache_control='',)
        headers.update({
            'accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'XMLHttpRequest',
            'token': '22dxy8bf7haegdj2gnylz072mxta41rk',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Origin': 'https://sy.kuakuavideo.com',
            'referer': 'https://sy.kuakuavideo.com/douyin.html',
        })
        # args = ()
        # server 上加载路径错误
        # r = str(get_js_parser_res(
        #     js_path='./js/hook_video_remove_watermark.js',
        #     func_name='generateRandom',
        #     *args,
        # ))
        # 改用直接导入, 测试报错 AttributeError: 'NoneType' object has no attribute 'fork_exec'
        # from execjs import compile as execjs_compile
        # js_code = '''
        # function generateRandom() {
        #     c = Math.random().toString(10).substring(2);
        #     return c
        # }
        # '''
        # r = execjs_compile(js_code).call('generateRandom', *args)
        # 改用python 直接生成
        from random import random as random_random
        r = str(random_random())[2:][0:15]

        # 测试: r = '6316272011432618' -> e = '75aed7a243ede5ec1f3b8548e0283539
        e = article_url + '@&^' + r
        e = md5_encrypt(target_str=e)
        self.lg.info('r: {}, e: {}'.format(r, e))

        # data = '{"sourceURL":"https://v.douyin.com/nXCh6q","e":"75aed7a243ede5ec1f3b8548e0283539","r":"6316272011432618","ticket":"","randstr":""}'
        data = dumps({
            'sourceURL': article_url,
            'e': e,
            'r': r,
            'ticket': '',
            'randstr': '',
        })
        body = await unblock_request(
            method='post',
            url='https://sy.kuakuavideo.com/douyin',
            headers=headers,
            data=data,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)
        self.hook_target_api_data = json_2_dict(
            json_str=body,
            default_res={},
            logger=self.lg,).get('data', {})
        # pprint(self.hook_target_api_data)

        video_url = self.hook_target_api_data.get('realDownloadURL', '')
        assert video_url != ''
        self.lg.info('获取到dy video_url: {}'.format(video_url))

        # 构造跟官方web接口同样结构的数据, 以便数据模板公用
        self.hook_target_api_data['desc'] = self.hook_target_api_data.get('title', '')
        self.hook_target_api_data['aweme_id'] = item_ids

        return body, video_url

    async def _get_ky_article_html(self, article_url) -> tuple:
        """
        获取ky html
        :param article_url:
        :return:
        """
        parser_obj = await self._get_parse_obj(article_url_type='ky')
        article_id = await async_parse_field(
            parser=parser_obj['article_id'],
            target_obj=article_url,
            logger=self.lg, )
        assert article_id != ''
        self.lg.info('article_id: {}'.format(article_id))

        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            upgrade_insecure_requests=False,
            cache_control='', )
        headers.update({
            'authority': 'baobab.kaiyanapp.com',
            'accept': '*/*',
            'origin': 'https://www.kaiyanapp.com',
            # 'sec-fetch-site': 'same-site',
            # 'sec-fetch-mode': 'cors',
            # 'referer': 'https://www.kaiyanapp.com/detail.html?vid=52619',
        })
        params = (
            ('f', 'web'),
        )
        url = 'https://baobab.kaiyanapp.com/api/v1/video/{}'.format(article_id)

        body = await unblock_request(
            url=url,
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries, )
        # self.lg.info(body)
        self.hook_target_api_data = json_2_dict(
            json_str=body,
            default_res={},
            logger=self.lg,
        )
        # pprint(data)

        video_url = self.hook_target_api_data.get('playUrl', '')
        assert video_url != ''
        self.lg.info('video_url: {}'.format(video_url))

        return body, video_url

    async def _get_klm_article_html(self, article_url) -> tuple:
        """
        获取klm html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers(
            user_agent_type=1,
            cache_control='',)
        headers.update({
            # 'referer': 'http://www.klm123.com/mobile/index',
        })

        body = await unblock_request(
            url=article_url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        video_url_sel = {
            'method': 'css',
            'selector': 'video source ::attr("src")',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg, )
        assert video_url != ''
        video_url = video_url.replace(' ', '')
        self.lg.info('klm video_url: {}'.format(video_url))

        return body, video_url

    async def _get_txws_article_html(self, article_url) -> tuple:
        """
        获取txws html
        :param article_url:
        :return:
        """
        parser_obj = await self._get_parse_obj(article_url_type='txws')
        article_id = await async_parse_field(
            parser=parser_obj['article_id'],
            target_obj=article_url,
            logger=self.lg, )
        assert article_id != ''
        self.lg.info('article_id: {}'.format(article_id))

        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            upgrade_insecure_requests=False,
            cache_control='', )
        headers.update({
            'authority': 'h5.weishi.qq.com',
            'accept': 'application/json',
            'origin': 'https://h5.weishi.qq.com',
            'x-requested-with': 'XMLHttpRequest',
            'content-type': 'application/json',
            # 'sec-fetch-site': 'same-origin',
            # 'sec-fetch-mode': 'cors',
            # 'referer': 'https://h5.weishi.qq.com/weishi/feed/6ZWI9iM5q1Ipfc65v/wsfeed?wxplay=1&id=6ZWI9iM5q1Ipfc65v&spid=1556715970981610&qua=v1_and_weishi_6.1.5_588_312026001_d&chid=100000014&pkg=3670&attach=cp_reserves3_1000000012&from=groupmessage&isappinstalled=0',
        })
        # cookies 必须
        cookies = {
            # 'LOLWebSet_AreaBindInfo_2939161681': '%257B%2522areaid%2522%253A%25222%2522%252C%2522areaname%2522%253A%2522%25E6%25AF%2594%25E5%25B0%2594%25E5%2590%2589%25E6%25B2%2583%25E7%2589%25B9%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25222939161681%2522%252C%2522rolename%2522%253A%2522%25E9%2587%258A%25E6%2588%2592%25E5%2599%258C%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C2939161681%257C2%257C2939161681*%257C%257C%257C%257C%2525E9%252587%25258A%2525E6%252588%252592%2525E5%252599%25258C*%257C%257C%257C1571287757%2522%252C%2522md5str%2522%253A%25229357D9A7E7A47EAF76E8601D9B46297D%2522%252C%2522roleareaid%2522%253A%25222%2522%252C%2522sPartition%2522%253A%25222%2522%257D',
            # 'RK': 'CLo97uh4d/',
            # 'actdaojuqqcomrouteLine': 'wxlolmall',
            # 'eas_sid': 'c1y527g1t141V7t9Z2w2H3o1m6',
            # 'ied_qq': 'o2939161681',
            # 'pac_uid': '0_5d9bf9e063d76',
            # 'person_id_bak': '5300148305753943',
            # 'pgv_info': 'ssid',
            # 'pgv_pvi': '308360192',
            # 'pgv_pvid': '7670180216',
            # 'pgv_si': 's2792151040',
            # 'ptcz': '3057abc40cfc1a41ca314fc3250c2d7083357e953406539f6c35138770471c7d',
            # 'ptui_loginuin': '2939161681',
            # 'sd_cookie_crttime': '1557540981306',
            # 'sd_userid': '27191557540981306',
            'skey': '@wIDWAlXuP',
            # 'tvfe_boss_uuid': '897b2b175de68297',
            # 'uin': 'o1006770934',
            # 'uin_cookie': 'o2939161681',
            # 'wsreq_logseq': '351269000',
        }
        params = (
            ('from', 'groupmessage'),
            # ('t', '0.016109720074739764'),
            ('g_tk', '2133740682'),  # 定值
        )
        data = dumps({
            'feedid': article_id,
            'recommendtype': 0,
            'datalvl': 'all',
            '_weishi_mapExt': {}
        })

        body = await unblock_request(
            method='post',
            url='https://h5.weishi.qq.com/webapp/json/weishi/WSH5GetPlayPage',
            headers=headers,
            params=params,
            data=data,
            cookies=cookies,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        # self.lg.info(body)
        data = json_2_dict(
            json_str=body,
            default_res={},
            logger=self.lg,).get('data', {})
        # pprint(data)
        self.hook_target_api_data = data

        video_url = self.hook_target_api_data.get('feeds', [])[0].get('video_url', '')
        assert video_url != ''
        self.lg.info('video_url: {}'.format(video_url))

        return body, video_url

    async def _get_dfsp_article_html(self, article_url) -> tuple:
        """
        获取dfsp html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers()
        headers.update({
            # 'Referer': 'http://imedia.eastday.com/node2/2015imedia/rmsp/index.html',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,
            logger=self.lg,
            encoding='gbk',)
        assert body != ''
        # self.lg.info(body)

        video_url_sel = {
            'method': 're',
            'selector': 'var source = \"(.*?)\";',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg,)
        assert video_url != ''
        self.lg.info('video_url: {}'.format(video_url))

        return body, video_url

    async def _get_kr_article_html(self, article_url) -> tuple:
        """
        获取kr html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers(
            user_agent_type=1,
        )
        headers.update({
            'Referer': 'https://krcom.cn/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,)
        assert body != ''
        # self.lg.info(body)

        video_info_sel = {
            'method': 're',
            'selector': '\$CONFIG\[\'video_info\'\]=(.*?);</script>',
        }
        video_info = unquote_plus(await async_parse_field(
            parser=video_info_sel,
            target_obj=body,
            logger=self.lg,))
        assert video_info != ''
        # self.lg.info(video_info)

        # 此处json解码失败, 但是还是解码部分, 还是处理
        video_info = json_2_dict(
            json_str=video_info,
            default_res={},
            logger=self.lg,)
        assert video_info != {}
        # pprint(video_info)

        video_url_sel = {
            'method': 're',
            'selector': '\"mp4_720p_mp4\":\"(.*?)\",',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=video_info,
            logger=self.lg,)
        if video_url == '':
            # 存在没有720p的, 取hd
            video_url_sel = {
                'method': 're',
                'selector': '\"mp4_hd_mp4\":\"(.*?)\",',
            }
            video_url = await async_parse_field(
                parser=video_url_sel,
                target_obj=video_info,
                logger=self.lg,)
            if video_url == '':
                video_url_sel = {
                    'method': 're',
                    'selector': '\"mp4_ld_mp4\":\"(.*?)\",',
                }
                video_url = await async_parse_field(
                    parser=video_url_sel,
                    target_obj=video_info,
                    logger=self.lg, )
            else:
                pass
        else:
            pass

        assert video_url != ''
        self.lg.info('video_url: {}'.format(video_url))

        title_sel = {
            'method': 're',
            'selector': '\"video_title\":\"(.*?)\",',
        }
        title = await async_parse_field(
            parser=title_sel,
            target_obj=video_info,
            logger=self.lg, )
        # self.lg.info(title)
        assert title != ''

        self.hook_target_api_data = {}
        self.hook_target_api_data['title'] = title

        return body, video_url

    async def _get_gxg_article_html(self, article_url) -> tuple:
        """
        获取gxg html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(
            user_agent_type=1,)
        headers.update({
            # 'Referer': 'https://m.gaoxiaogif.com/index_2.html',
        })

        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,
            logger=self.lg,
            encoding='gbk',)
        assert body != ''
        # self.lg.info(body)

        return body, video_url

    async def _get_kys_article_html(self, article_url) -> tuple:
        """
        获取kys html
        :param article_url:
        :return:
        """
        # 返回的视频播放地址加密的, 此处直接获取动态渲染结果
        # //jsmov2.a.yximgs.com/upic/2019/07/05/13/BMjAxOTA3MDUxMzA4MTdfMTIwMDU4MjA4N18xNDgwNTM0NzQ3NV8xXzM=_b_Ba9cd9e5539759a6b73d0e2b400cc9dc9.mp4
        # //jsmov2.a.yximgs.com/upic/2019/07/05/13/:131:125:183:171:210:181:161:149:140:125:146:153:185:128:199:171:117:125:161:206:192:179:161:157:208:125:146:153:117:128:183:171:117:126:126:162:210:180:145:187:208:126:162:145:113:129:199:187:116:126:163:162:210:190:199:161:150:143:176:163:131:148:134:205:165:105:178:159:143:153:134:139:142:105:175:122:163:106:128:206:113:149:127:204:142:150:125:183:188:105:178:167:122.mp4

        body = await self._get_html_by_driver(
            url=article_url,
            load_images=False,
            user_agent_type=PHONE,
            css_selector='div#player-box video',
            timeout=20,                         # 设置时间短点
        )
        assert body != ''

        video_url_sel = {
            'method': 'css',
            'selector': 'div#player-box video ::attr("src")',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg,)
        video_url = 'https:' + video_url if video_url != '' else ''
        assert video_url != ''
        self.lg.info('video_url: {}'.format(video_url))

        return body, video_url

    async def _get_blbl_article_html(self, article_url) -> tuple:
        """
        获取bilibili html
        :param article_url:
        :return:
        """
        parser_obj = await self._get_parse_obj(article_url_type='blbl')
        article_id = await async_parse_field(
            parser=parser_obj['article_id'],
            target_obj=article_url,
            logger=self.lg,)
        assert article_id != ''

        headers = await async_get_random_headers(user_agent_type=1)
        headers.update({
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://m.bilibili.com/',
        })
        url = 'https://m.bilibili.com/video/{}.html'.format(article_id)
        body = await unblock_request(
            url=url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        target_data_sel = {
            'method': 're',
            'selector': 'window.__INITIAL_STATE__=(.*?);if\(window',
        }
        self.hook_target_api_data = json_2_dict(
            json_str=parse_field(
                parser=target_data_sel,
                target_obj=body,
                logger=self.lg,),
            default_res={},
            logger=self.lg,)
        # pprint(self.hook_target_api_data)

        video_url = self.hook_target_api_data\
            .get('reduxAsyncConnect', {})\
            .get('videoInfo', {})\
            .get('initUrl', '')
        assert video_url != ''
        video_url = 'https:' + video_url \
            if re.compile('http').findall(video_url) == [] else video_url
        self.lg.info('video_url: {}'.format(video_url))

        return body, video_url

    async def _get_lfd_article_html(self, article_url) -> tuple:
        """
        获取lfd html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers()
        xid_sel = {
            'method': 're',
            'selector': 'xid=(\w+)',
        }
        xid = await async_parse_field(
            parser=xid_sel,
            target_obj=article_url,
            logger=self.lg,)
        # xid 非必传
        # assert xid != ''

        params = (('xid', xid),) if xid != '' else None
        body = await unblock_request(
            url=article_url,
            headers=headers,
            params=params,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            # proxy_type=PROXY_TYPE_HTTPS,      # https 失败率较高
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        return body, video_url

    async def _get_jd_article_html(self, article_url) -> tuple:
        """
        获取jd的html
        :param article_url:
        :return:
        """
        video_url = ''

        # 替换为m站 article_url
        article_url = article_url.replace('http://jandan.net', 'http://i.jandan.net')

        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,
            cache_control='',)
        headers.update({
            'Proxy-Connection': 'keep-alive',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        # 赋值data
        base_data_sel = {
            'method': 're',
            'selector': '<script type=\"application/ld\+json\">(.*?)</script>',
        }
        base_data = await async_parse_field(
            parser=base_data_sel,
            target_obj=body,
            logger=self.lg,)
        assert base_data != ''
        base_data = json_2_dict(
            json_str=base_data,
            default_res={},
            logger=self.lg,)
        assert base_data != {}
        # pprint(base_data)
        self.hook_target_api_data = {}
        self.hook_target_api_data['base_data'] = base_data

        # 赋值article_id
        parse_obj = await self._get_parse_obj(article_url_type='jd')
        article_id = await async_parse_field(
            parser=parse_obj['article_id'],
            target_obj=body,
            logger=self.lg,)
        assert article_id != ''
        self.hook_target_api_data['article_id'] = str(article_id)

        return body, video_url

    async def _get_bdj_article_html(self, article_url) -> tuple:
        """
        获取bdj html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(connection_status_keep_alive=False)
        headers.update({
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.budejie.com/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        return body, video_url

    async def _get_5h_article_html(self, article_url) -> tuple:
        """
        获取5h html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,)
        headers.update({
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://m.5h.com/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            verify=False,
            num_retries=self.request_num_retries,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        return body, video_url

    async def _get_xq_article_html(self, article_url) -> tuple:
        """
        获取雪球网 html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers()
        headers.update({
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Site': 'none',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        hook_target_api_data_sel = {
            'method': 're',
            'selector': 'window\.SNOWMAN_STATUS = (.*?);window\.SNOWMAN_TARGET',
        }
        self.hook_target_api_data = json_2_dict(
            json_str=await async_parse_field(
                parser=hook_target_api_data_sel,
                target_obj=body,
                logger=self.lg,),
            default_res={},
            logger=self.lg,)
        assert self.hook_target_api_data != {}
        # pprint(self.hook_target_api_data)

        return body, video_url

    async def _get_91mt_article_html(self, article_url) -> tuple:
        """
        获取91觅糖 html
        :param article_url:
        :return:
        """
        parse_obj = await self._get_parse_obj(article_url_type='91mt')
        article_id = await async_parse_field(
            parser=parse_obj['article_id'],
            target_obj=article_url,
            logger=self.lg,)
        assert article_id != ''

        # 研究发现, 视频or图文文章的所有信息在视频详情页中都有, 故直接请求视频详情页
        headers = await async_get_random_headers(
            user_agent_type=1,
            cache_control='',)
        headers.update({
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': article_url,
        })
        video_detail_url = 'https://www.91mitang.com/pageDetails/{}'.format(article_id)
        body = await unblock_request(
            url=video_detail_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            logger=self.lg, )
        assert body != ''
        # self.lg.info(body)

        video_url_sel = {
            'method': 're',
            'selector': '\"contentUrl\": \"(.*?)\",',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg,)
        if video_url != '':
            self.lg.info('此为视频文章!')
            self.lg.info('got video_url: {}'.format(video_url))
        else:
            self.lg.info('此为图文文章!')

        return body, video_url

    async def _get_ft_article_html(self, article_url) -> tuple:
        """
        获取ft 的html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(user_agent_type=1)
        headers.update({
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Site': 'none',
            'Referer': 'https://m.fatiao.pro/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        assert body != ''
        # self.lg.info(body)

        if 'detail' in article_url:
            self.lg.info('此为视频文章')
            video_url_sel = {
                'method': 're',
                'selector': 'src: \[\"(.*?)\"\],',
            }
            video_url = await async_parse_field(
                parser=video_url_sel,
                target_obj=body,
                logger=self.lg,)
            self.lg.info('got video_url: {}'.format(video_url))
        else:
            pass

        return body, video_url

    async def _get_qqbb_article_html(self, article_url) -> tuple:
        """
        获取qqbb html
        :param article_url:
        :return:
        """
        async def get_next_page_body_by_page_num(article_url: str,
                                                 parse_obj: dict,
                                                 page_num: int=1) -> tuple:
            """
            根据page_num获取对应页码文章信息
            :param article_url:
            :param parse_obj:
            :param page_num:
            :return:
            """
            # 是否还有下一页
            had_next_page = False
            # 下一页的content
            next_content = ''

            self.lg.info('获取第{}页body...'.format(page_num))
            if page_num > 1:
                # eg:
                # 首页: https://m.qbaobei.com/a/1145214.html
                # 第二页: https://m.qbaobei.com/a/1145214_2.html
                article_url = article_url.replace('.html', '_{}.html'.format(page_num))
                if page_num > 2:
                    referer = re.compile('\.html')\
                        .sub('_{}\.html'.format(page_num-1), article_url)
                else:
                    # 2
                    referer = article_url
            else:
                referer = article_url
            # self.lg.info('article_url: {}'.format(article_url))

            headers = await async_get_random_headers(
                user_agent_type=1,
                connection_status_keep_alive=False,)
            headers.update({
                'authority': 'm.qbaobei.com',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-site': 'none',
                # 'referer': 'https://m.qbaobei.com/',
                'referer': referer,
                # 'cookie': 'Hm_lvt_3d8ae083091c839222c62a3e4ab746ee=1565660348; PHPSESSID=85ukti67lk3419g8hcnbogc025; Hm_lvt_4ba23929a20904dd1920a6e67b6258d3=1565660780; Hm_lvt_90f5390d52559687ed0ea6b8603e7018=1565660780; Hm_lpvt_4ba23929a20904dd1920a6e67b6258d3=1565671441; Hm_lpvt_90f5390d52559687ed0ea6b8603e7018=1565671441; Hm_lpvt_3d8ae083091c839222c62a3e4ab746ee=1565671441',
            })
            body = await unblock_request(
                url=article_url,
                headers=headers,
                ip_pool_type=self.ip_pool_type,
                num_retries=self.lg,
                logger=self.lg,)
            assert body != ''
            # self.lg.info(body)

            had_next_text_sel = {
                'method': 'css',
                'selector': 'div.detail_page a[id^="href_"] ::text',
            }
            # 因为如果存在第三页的话, 第二页是有上一页和下一页的
            had_next_text_list = await async_parse_field(
                parser=had_next_text_sel,
                target_obj=body,
                logger=self.lg,
                is_first=False)
            if '下一页' in had_next_text_list:
                had_next_page = True
                # self.lg.info('有下一页!')
            else:
                pass
            if page_num > 1:
                next_content_sel = {
                    'method': 're',
                    'selector': '<article class=\"art-body art-body-\d+.*?\">(.*)<div class=\"detail_page\">',
                }
                next_content = await async_parse_field(
                    parser=next_content_sel,
                    target_obj=body,
                    logger=self.lg, )
                # self.lg.info(next_content)
            else:
                pass

            return body, next_content, had_next_page

        video_url = ''
        parse_obj = await self._get_parse_obj(article_url_type='qqbb')
        if 'video_' not in article_url:
            # 图文
            had_next_page = True
            page_num = 1
            last_body = ''
            while had_next_page:
                body, next_content, had_next_page = await get_next_page_body_by_page_num(
                    article_url=article_url,
                    parse_obj=parse_obj,
                    page_num=page_num, )
                if page_num > 1:
                    last_body = re.compile('<div class=\"detail_page\">') \
                        .sub(next_content + '<div class="detail_page">', last_body)
                else:
                    last_body = body
                # self.lg.info('last_body: {}'.format(last_body))
                page_num += 1

            # self.lg.info(last_body)

        else:
            self.lg.info('此为视频文章')
            last_body = (await get_next_page_body_by_page_num(
                article_url=article_url,
                parse_obj=parse_obj,
                page_num=1,))[0]
            # 视频文章
            video_url_sel = {
                'method': 're',
                'selector': '\"contentUrl\": \"(.*?)\",'
            }
            video_url = await async_parse_field(
                parser=video_url_sel,
                target_obj=last_body,
                logger=self.lg,)
            self.lg.info('got video_url: {}'.format(video_url))

        return last_body, video_url

    async def _get_7y7_article_html(self, article_url) -> tuple:
        """
        获取7y7 html
        :param article_url:
        :return:
        """
        async def get_next_page_body_by_page_num(article_url: str,
                                                 parse_obj: dict,
                                                 page_num: int=1) -> tuple:
            """
            获取下一页的body信息
            :param page_num:
            :return:
            """
            # 是否还有下一页
            had_next_page = False
            # 下一页的content
            next_content = ''

            self.lg.info('获取第{}页body...'.format(page_num))
            if page_num > 1:
                # eg:
                # 首页: https://i.7y7.com/caizhuang/47/385947.html
                # 第二页: https://i.7y7.com/caizhuang/47/385947_2.html
                article_url = article_url.replace('.html', '_{}.html'.format(page_num))
                if page_num > 2:
                    referer = re.compile('\.html').sub('_{}\.html'.format(page_num-1), article_url)
                else:
                    # 2
                    referer = article_url
            else:
                referer = article_url
            # self.lg.info('article_url: {}'.format(article_url))

            headers = await async_get_random_headers(
                user_agent_type=1,
                connection_status_keep_alive=False, )
            headers.update({
                'authority': 'i.7y7.com',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-site': 'none',
                # 'referer': 'https://i.7y7.com/',
                'referer': referer,                 # 请求下一页时必须使用上一页的地址
                # 'cookie': 'Hm_lvt_7905279f5e0979a49bdc161dbad2708d=1565659612; Hm_lvt_8257a196df3916574fa89d7567071790=1565659642; Hm_lvt_6557398d368c2c5d56b4ebf03da843a7=1565659990; Hm_lpvt_6557398d368c2c5d56b4ebf03da843a7=1565659990; Hm_lpvt_8257a196df3916574fa89d7567071790=1565660942; Hm_lpvt_7905279f5e0979a49bdc161dbad2708d=1565660942',
            })
            body = await unblock_request(
                url=article_url,
                headers=headers,
                ip_pool_type=self.ip_pool_type,
                num_retries=self.request_num_retries,
                logger=self.lg, )
            assert body != ''
            # self.lg.info(body)

            had_next_text_sel = {
                'method': 'css',
                'selector': 'div.detail_page a[id^="href_"] ::text',
            }
            # 因为如果存在第三页的话, 第二页是有上一页和下一页的
            had_next_text_list = await async_parse_field(
                parser=had_next_text_sel,
                target_obj=body,
                logger=self.lg,
                is_first=False)
            if '下一页' in had_next_text_list:
                had_next_page = True
                # self.lg.info('有下一页!')
            else:
                pass
            if page_num > 1:
                next_content_sel = {
                    'method': 're',
                    'selector': '<div class=\"contents\">(.*?)</div><div class=\"detail_page\">',
                }
                next_content = await async_parse_field(
                    parser=next_content_sel,
                    target_obj=body,
                    logger=self.lg,)
                # self.lg.info(next_content)
            else:
                pass

            return body, next_content, had_next_page

        video_url = ''
        parse_obj = await self._get_parse_obj(article_url_type='7y7')
        had_next_page = True
        page_num = 1
        last_body = ''
        while had_next_page:
            body, next_content, had_next_page = await get_next_page_body_by_page_num(
                article_url=article_url,
                parse_obj=parse_obj,
                page_num=page_num,)
            if page_num > 1:
                last_body = re.compile('</div><div class=\"detail_page\">')\
                    .sub(next_content+'</div><div class="detail_page">', last_body)
            else:
                last_body = body
            # self.lg.info('last_body: {}'.format(last_body))
            page_num += 1

        # self.lg.info(last_body)

        return last_body, video_url

    async def _get_hk_article_html(self, article_url) -> tuple:
        """
        获取hk html
        :param article_url:
        :return:
        """
        parse_obj = await self._get_parse_obj(article_url_type='hk')
        video_id = await async_parse_field(
            parser=parse_obj['article_id'],
            target_obj=article_url,
            logger=self.lg,)
        assert video_id != ''
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,)
        headers.update({
            'authority': 'haokan.baidu.com',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-site': 'none',
            'referer': 'https://haokan.baidu.com/',
            # 'cookie': 'BAIDUID=1666ADBB95B083DBB2DA29E9BEFCB50B:FG=1; BIDUPSID=1666ADBB95B083DBB2DA29E9BEFCB50B; PSTM=1553750958; H_WISE_SIDS=130611_124610_128699_132218_131777_128065_130510_126064_130163_120216_131602_132213_131517_132261_118882_118872_131401_118851_118819_118796_130763_132244_131649_131576_131555_131536_131534_131529_130222_131295_131872_131391_129565_107313_131796_131392_130120_131874_130569_131196_130348_129647_131246_125086_131435_131686_131036_131906_132090_129838_130413_129646_124030_132204_130824_110085_131767_127969_131506_123289_130818_127417_131550_131826_131750_131264_131263_131662_131946_128808; BDUSS=RtNkhNbXFTQWY1flppR3ZOd281SGtuMGlOaHhuWX5QUX5XZ3Y2MFZ4cHNIaGRkSVFBQUFBJCQAAAAAAAAAAAEAAADfukJXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGyR71xske9cRz; pgv_pvi=169221120; locale=zh; yjs_js_security_passport=66b912c3641c4e58bd4cd990686fb14faf28df5f_1565146880_js; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1565229221; COMMON_LID=f3435a0e1c48660589c8fcd526e0f8bf; Hm_lvt_77ca61e523cd51ec7ac7a23bc4d24edf=1565229278; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1565229363; HK_CH_EXPIRED_TIME=1565279999000; HK_CH_IS_CLICKED=0; HK_SID=3116_2-3157_2-3168_1-3217_1-3265_1-3292_1; Hm_lpvt_77ca61e523cd51ec7ac7a23bc4d24edf=1565229372; HK_CH_REFRESH_TIMES=3; HK_CH_MAT_INDEX=0',
        })
        params = (
            ('vid', video_id),
            ('tab', 'recommend'),
        )
        url = 'https://haokan.baidu.com/v'
        body = await unblock_request(
            url=url,
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,
            logger=self.lg,)
        assert body != '', '获取hk的body为空值!'
        # self.lg.info(body)

        self.hook_target_api_data = json_2_dict(
            json_str=re.compile('window.__PRELOADED_STATE__ = (.*?); document\.querySelector').findall(body)[0],
            default_res={},
            logger=self.lg,)
        try:
            self.hook_target_api_data.pop('openAppInfo')
        except:
            pass
        assert self.hook_target_api_data != {}
        # pprint(self.hook_target_api_data)

        video_url = self.hook_target_api_data\
            .get('curVideoMeta', {})\
            .get('videoInfoExt', {})\
            .get('default', {})\
            .get('defaultUrlHttp', '')
        assert video_url != ''
        self.lg.info('got hk video_url: {}'.format(video_url))

        return body, video_url

    def unblock_get_mp_article_html(self, article_url) -> tuple:
        """
        阻塞获取美拍的html
        :param article_url:
        :return:
        """
        driver = BaseDriver(
            # phantomjs被封, 无数据, 改用firefox
            type=FIREFOX,
            executable_path=FIREFOX_DRIVER_PATH,
            load_images=True,
            headless=True,
            user_agent_type=PHONE,
            ip_pool_type=self.ip_pool_type,
            logger=self.lg,)
        driver.get_url_body(
            url=article_url,
            timeout=25,)
        # 点击播放按钮
        driver.find_element(value='div.Button.play-btn').click()
        sleep(2.)
        body = driver._wash_html(html=driver.page_source)
        # self.lg.info(body)

        video_url_sel = {
            'method': 'css',
            'selector': 'div.meipai-player video source ::attr("src")',
        }
        video_url = parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg,)
        if video_url != '' and re.compile('http').findall(video_url) == []:
           video_url = 'https:' + video_url
        else:
            pass
        self.lg.info('Get mp video_url: {}'.format(video_url))
        try:
            del driver
        except:
            try:
                del driver
            except:
                pass
        assert body != '', '获取到mp的body为空值!'
        assert video_url != '', 'mp 的video_url不为空值!'

        return body, video_url

    async def _get_amz_article_html(self, article_url) -> tuple:
        """
        获取amz html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,)
        headers.update({
            'authority': 'aimozhen.com',
            'referer': 'https://aimozhen.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        # 只能获取到iframe, 故切入到视频文章中
        # todo request只能获取到部分的
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            logger=self.lg, )
        # self.lg.info(body)
        assert body != '', '获取hx的body为空值!'

        return body, video_url

    def unblock_get_lsp_article_html(self, article_url) -> tuple:
        """
        阻塞获取梨视频的html
        :param artice_url:
        :return:
        """
        driver = BaseDriver(
            # phantomjs失败率高, 改用firefox
            # type=PHANTOMJS,
            # executable_path=PHANTOMJS_DRIVER_PATH,
            type=FIREFOX,
            executable_path=FIREFOX_DRIVER_PATH,
            ip_pool_type=self.ip_pool_type,
            load_images=True,
            headless=True,
            logger=self.lg,)
        driver.get_url_body(
            url=article_url,
            timeout=25,)
        # driver.save_screenshot('tmp.png')
        # self.lg.info(driver._wash_html(html=driver.page_source))
        driver.find_element(value='i.play-icon.i-icon').click()
        sleep(2.)
        body = driver._wash_html(html=driver.page_source)
        # self.lg.info(body)

        video_url_sel = {
            'method': 'css',
            'selector': 'div.video-main video ::attr("src")',
        }
        video_url = parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg,)
        self.lg.info('Get lsp video_url: {}'.format(video_url))
        try:
            del driver
        except:
            pass
        assert video_url != '', 'lsp 的video_url不为空值!'
        assert body != '', '获取到lsp的body为空值!'

        return body, video_url

    async def _get_ck_article_html(self, article_url) -> tuple:
        """
        获取ck html
        :param article_url:
        :return:
        """
        # 走api
        # 获取article_id
        parse_obj = await self._get_parse_obj(article_url_type='ck')
        article_id = await async_parse_field(
            parser=parse_obj['article_id'],
            target_obj=article_url,
            logger=self.lg,)
        assert article_id != '', 'article_id != ""'
        # method1: driver 请求pc地址但是user_agent=phone
        # method2: driver pc 页面转phone, 可获得下方接口
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,)
        headers.update({
            'origin': 'https://h5.vmovier.com',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'accept': '*/*',
            'referer': 'https://h5.vmovier.com/index.html?id={}'.format(article_id),
            'authority': 'www.vmovier.com',
        })
        params = (
            ('id', str(article_id)),
        )
        url = 'https://www.vmovier.com/post/getViewData'
        body = await unblock_request(
            url=url,
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,
            logger=self.lg,)
        # self.lg.info(body)
        assert body != '', '获取hx的body为空值!'
        self.hook_target_api_data = json_2_dict(
            json_str=body,
            logger=self.lg,
            default_res={},).get('data', {})
        assert self.hook_target_api_data != {}, 'ck的api data为空dict!'
        # pprint(self.hook_target_api_data)
        video_url = self.hook_target_api_data.get('video_link', '')
        assert video_url != "", 'video_url != ""'

        return body, video_url

    async def _get_hqx_article_html(self, article_url) -> tuple:
        """
        get hqx html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(user_agent_type=1)
        headers.update({
            # 'Referer': 'http://m.qdaily.com/mobile/homes.html',
            'Referer': article_url,
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            verify=False,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        # self.lg.info(body)
        assert body != '', '获取hqx的body为空值!'

        return body, video_url

    async def _get_nfzm_article_html(self, article_url) -> tuple:
        """
        get nfzm html
        :param article_url:
        :return:
        """
        async def get_nfzm_api2():
            """
            获取二版接口
            :return:
            """
            nonlocal article_id

            self.lg.info('getting nfzm 2 version api ...')
            headers = await async_get_random_headers(
                user_agent_type=1,
                connection_status_keep_alive=False,
                cache_control='',
                upgrade_insecure_requests=False,)
            headers.update({
                'accept': 'application/json, text/plain, */*',
                'referer': 'http://www.infzm.com/wap/',
                'origin': 'http://www.infzm.com',
            })
            params = (
                ('version', '1.1.19'),
                ('platform', 'wap'),
                ('machine_id', 'aad315f2d84daf16a62f0fe74131aac0'),
                ('user_id', '3360728'),
                # ('token', '18f407e66d82ba5920ebe88d539f4921x97c7'),
            )
            api_url = 'http://api.infzm.com/mobile/contents/{}'.format(article_id)
            body = await unblock_request(
                url=api_url,
                headers=headers,
                params=params,
                ip_pool_type=self.ip_pool_type,
                num_retries=self.request_num_retries,
                verify=False,
                logger=self.lg,)
            # self.lg.info(body)
            assert body != '', '获取hx的body为空值!'
            hook_target_api_data = await self.get_nfzm_hook_target_api_data(
                body=body,)

            return hook_target_api_data

        # 走api
        video_url = ''
        headers = await async_get_random_headers(user_agent_type=1)
        headers.update({
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        params = (
            ('version', '1.1.15'),
            ('platform', 'wap'),
            ('user_id', ''),
            ('token', ''),
        )
        # 获取article_id
        parse_obj = await self._get_parse_obj(article_url_type='nfzm')
        article_id = await async_parse_field(
            parser=parse_obj['article_id'],
            target_obj=article_url,
            logger=self.lg, )
        assert article_id != '', 'nfzm的article_id != ""'
        api_url = 'http://api.infzm.com/mobile/contents/{}'.format(article_id)
        body = await unblock_request(
            url=api_url,
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            verify=False,
            logger=self.lg,)
        # self.lg.info(body)
        assert body != '', '获取hx的body为空值!'
        self.hook_target_api_data = await self.get_nfzm_hook_target_api_data(
            body=body,)
        # pprint(self.hook_target_api_data)
        if self.hook_target_api_data.get('content', {}).get('fulltext', '') == '':
            # 可能是会员文章, 用另一接口
            self.hook_target_api_data = await get_nfzm_api2()
        else:
            pass

        return body, video_url

    async def get_nfzm_hook_target_api_data(self, body) -> dict:
        hook_target_api_data = json_2_dict(
            json_str=body,
            logger=self.lg,
            default_res={},).get('data', {})
        assert hook_target_api_data != {}, 'nfzm的api data为空dict!'

        return hook_target_api_data

    async def _get_hx_article_html(self, article_url) -> tuple:
        """
        get hx html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,)
        headers.update({
            'authority': 'm.huxiu.com',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        # self.lg.info(body)
        assert body != '', '获取hx的body为空值!'
        has_video_url_sel = {
            'method': 'css',
            'selector': 'div#article-video-head',
        }
        has_video_url = await async_parse_field(
            parser=has_video_url_sel,
            target_obj=body,
            logger=self.lg,)
        if has_video_url != '':
            # 视频文章
            self.lg.info('此为视频文章')
            video_url_sel = {
                'method': 're',
                'selector': ",file: '(.*?)',ak:",
            }
            video_url = await async_parse_field(
                parser=video_url_sel,
                target_obj=body,
                logger=self.lg,)
            self.lg.info('video_url: {}'.format(video_url))
        else:
            pass

        return body, video_url

    async def _get_pp_article_html(self, article_url) -> tuple:
        """
        get pp html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers(user_agent_type=1)
        headers.update({
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,
            logger=self.lg, )
        # self.lg.info(body)
        assert body != '', '获取if的body为空值!'

        video_url_sel = {
            'method': 'css',
            'selector': 'div.news_content video source ::attr("src")',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg, )
        if video_url != '':
            self.lg.info('此为视频文章')
            self.lg.info('pp_video_url: {}'.format(video_url))

        return body, video_url

    async def _get_jm_article_html(self, article_url) -> tuple:
        """
        get jm html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers()
        headers.update({
            'referer': 'https://www.jiemian.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            logger=self.lg, )
        # self.lg.info(body)
        assert body != '', '获取if的body为空值!'

        if '/video/' in article_url:
            self.lg.info('此为视频文章')
            video_url_sel = {
                'method': 'css',
                'selector': 'div.video-main video ::attr("src")',
            }
            video_url = await async_parse_field(
                parser=video_url_sel,
                target_obj=body,
                logger=self.lg, )
            self.lg.info('jm_video_url: {}'.format(video_url))

        return body, video_url

    async def _get_ss_article_html(self, article_url) -> tuple:
        """
        获取ss的html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers()
        headers.update({
            'referer': 'https://songshuhui.net/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        # self.lg.info(body)
        assert body != '', '获取if的body为空值!'

        return body, video_url

    async def _get_if_article_html(self, article_url) -> tuple:
        """
        获取if的html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers()
        headers.update({
            'authority': 'www.ifanr.com',
            'referer': 'https://www.ifanr.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            # 'if-none-match': '"5d101f41-e0ce"',
            # 'if-modified-since': 'Mon, 24 Jun 2019 00:54:25 GMT',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        # self.lg.info(body)
        assert body != '', '获取if的body为空值!'
        video_url_sel = {
            'method': 'css',
            'selector': 'iframe.js-video-src',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg,)
        if video_url != '':
            self.lg.info('此为视频文章')
            self.lg.info('cn_video_url: {}'.format(video_url))

        return body, video_url

    async def _get_cn_article_html(self, article_url) -> tuple:
        """
        获取cn的html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers(user_agent_type=1)
        headers.update({
            'Referer': 'http://m.cnys.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        # self.lg.info(body)
        assert body != '', '获取cn的body为空值!'
        video_url_sel = {
            'method': 'css',
            'selector': 'div.video-play-wrap mip-search-video ::attr("video-src")',
        }
        video_url = await async_parse_field(
            parser=video_url_sel,
            target_obj=body,
            logger=self.lg,)
        if video_url != '':
            self.lg.info('此为视频文章')
            self.lg.info('cn_video_url: {}'.format(video_url))

        return body, video_url

    async def _get_ys_article_html(self, article_url) -> tuple:
        """
        获取51ys的html
        :param article_url:
        :return:
        """
        video_url = ''
        headers = await async_get_random_headers()
        headers.update({
            'referer': 'http://www.51jkst.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=self.request_num_retries,
            logger=self.lg,)
        # self.lg.info(body)
        assert body != '', '获取的ys的body为空值!'

        return body, video_url

    async def _get_fh_article_html(self, article_url) -> tuple:
        """
        获取fh的html
        :param article_url:
        :return:
        """
        async def _get_fh_video_url(body) -> str:
            """
            获取video_url
            :param article_url:
            :param body:
            :return:
            """
            vid_selector = {
                'method': 're',
                'selector': ',\"vid\":\"(\w+-\w+-\w+-\w+-\w+)\"',
            }
            m3u8_base_url_selector = {
                'method': 're',
                'selector': ',\"m3u8Url\":\"(.*?)\"',
            }
            vid = await async_parse_field(
                parser=vid_selector,
                target_obj=body,
                logger=self.lg, )
            assert vid != '', 'vid != ""'
            m3u8_base_url = await async_parse_field(
                parser=m3u8_base_url_selector,
                target_obj=body,
                logger=self.lg, )
            assert m3u8_base_url != '', 'm3u8_base_url != ""'
            self.lg.info('Getting auth_params ...')
            headers = await async_get_random_headers()
            headers.update({
                # 'Referer': 'https://v.ifeng.com/c/7n9OP680pzt',
            })
            url = 'https://shankapi.ifeng.com/feedflow/getVideoAuthUrl/{}/getVideoAuthPath'.format(vid)
            params = (
                ('callback', 'getVideoAuthPath'),
            )
            body = await unblock_request(
                url=url,
                headers=headers,
                params=params,
                ip_pool_type=self.ip_pool_type,
                num_retries=self.request_num_retries,
                logger=self.lg)
            # self.lg.info(str(body))
            auth_params = json_2_dict(
                json_str=re.compile('\((.*)\)').findall(body)[0],
                logger=self.lg
            ).get('data', {}).get('authUrl', '')
            assert auth_params != '', 'auth_params != ""'
            self.lg.info('获取到视频auth_params: {}'.format(auth_params))

            video_url = m3u8_base_url.replace('http', 'https') + '?' + auth_params
            self.lg.info('m3u8_url: {}'.format(video_url))

            return video_url

        video_url = ''
        if 'v.ifeng.com' in article_url:
            # 视频
            # 用requests请求body(速度更快)
            # TODO 不用driver, 因为失败率太高!!
            headers = await async_get_random_headers()
            body = await unblock_request(
                url=article_url,
                headers=headers,
                ip_pool_type=self.ip_pool_type,
                num_retries=self.request_num_retries,
                logger=self.lg,)

        else:
            # requests 无效, 无法获取article content
            body = await self._get_html_by_driver(
                url=article_url,
                _type=PHANTOMJS,
                load_images=False,)

        # self.lg.info(str(body))
        assert body != '', '获取fh的body不为空值!'
        if 'v.ifeng.com' in article_url:
            # 视频
            self.lg.info('此为视频文章')
            video_url = await _get_fh_video_url(
                body=body,)

        else:
            pass

        return body, video_url

    async def _get_yg_article_html(self, article_url) -> tuple:
        """
        获取yg article的html
        :param article_url:
        :return:
        """
        exec_code = '''
        # 等待视频自动播放后, 获取网页源码
        sleep(2.5)
        '''
        self.lg.info('此链接为视频链接')
        body = await self._get_html_by_driver(
            url=article_url,
            _type=FIREFOX,
            exec_code=exec_code,
            headless=True,
            load_images=True,)
        # self.lg.info(str(body))
        video_url_selector = {
            'method': 'css',
            'selector': 'div.index-content video ::attr("src")',
        }
        tmp_video_url = await async_parse_field(
            parser=video_url_selector,
            target_obj=body,
            logger=self.lg,)
        video_url = 'https:' + tmp_video_url if tmp_video_url != '' else ''
        # self.lg.info(video_url)

        return body, video_url

    async def _get_xg_article_html(self, article_url) -> tuple:
        """
        获取xg article的html
        :param article_url:
        :return:
        """
        exec_code = '''
        # 等待视频自动播放后, 获取网页源码
        sleep(2.5)
        '''
        self.lg.info('此链接为视频链接')
        body = await self._get_html_by_driver(
            url=article_url,
            _type=FIREFOX,
            exec_code=exec_code,
            headless=True,
            load_images=True,)
        # self.lg.info(str(body))
        video_url_selector = {
            'method': 'css',
            'selector': 'div video ::attr("src")',
        }
        tmp_video_url = await async_parse_field(
            parser=video_url_selector,
            target_obj=body,
            logger=self.lg, )
        video_url = 'https://' + tmp_video_url.replace('http://', '') if tmp_video_url != '' else ''
        # self.lg.info(video_url)

        return body, video_url

    async def _get_zq_article_html(self, article_url) -> tuple:
        """
        获取zq article的html
        :param article_url:
        :return:
        """
        video_url = ''

        # todo 下面这种类型手动需更改为标准的url格式
        # article_url = 'https://focus.youth.cn/mobile/detail?id=17197839#'
        # 标准的url: https://focus.youth.cn/mobile/detail/id/17230881#
        article_url = re.compile('detail\?id=').sub('detail/id/', article_url)
        # self.lg.info(article_url)

        headers = await async_get_random_headers(user_agent_type=1)
        headers.update({
            # 'Referer': 'https://focus.youth.cn/html/articleTop/mobile.html?type=1',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            proxy_type=PROXY_TYPE_HTTPS,
            logger=self.lg)
        # self.lg.info(body)
        assert body != '', '获取zq的body为空值!'

        return body, video_url

    async def _get_bd_article_html(self, article_url) -> tuple:
        """
        获取bd article的html
        :param article_url:
        :return:
        """
        async def _get_hk_params(article_id) -> tuple:
            """
            获取好看视频的article_id和params
            :param article_url:
            :return:
            """
            return (
                ('pd', 'wise'),
                ('vid', str(article_id)),
                ('is_invoke', '1'),
                ('innerIframe', '1'),
                ('type', 'share'),
            )

        async def _get_target_url_and_params_by_article_url(article_url) -> tuple:
            """
            获取最后请求的url跟parmas
            :param article_url:
            :return:
            """
            is_haokan = False
            # 只要是好看视频都可以进 https://haokan.baidu.com/videoui/page/searchresult进行搜索得到对应页面
            if 'm.baidu.com' in article_url:
                # 下面.com在article_url得参数里
                if 'mbd.baidu.com' in article_url:
                    article_id = re.compile('news_(\d+)').findall(article_url)[0]
                    url = 'https://mbd.baidu.com/newspage/data/landingpage'
                    params = (
                        ('context', dumps({
                            'nid': 'news_{}'.format(article_id),
                        })),
                        ('pageType', '1'),
                    )

                elif 'haokan.baidu.com' in article_url:
                    is_haokan = True
                    # 获取视频id
                    article_id = re.compile('vid%253D(\d+)').findall(article_url)[0]
                    # self.lg.info(article_id)
                    url = 'https://haokan.baidu.com/videoui/page/searchresult'
                    params = await _get_hk_params(article_id=article_id)

                else:
                    raise NotImplemented

            elif 'sv.baidu.com' in article_url:
                # 在二级域名上
                is_haokan = True
                # 获取视频id
                article_id = re.compile('sv_(\d+)').findall(article_url)[0]
                url = 'https://haokan.baidu.com/videoui/page/searchresult'
                params = await _get_hk_params(article_id=article_id)

            else:
                params = None
                url = article_url

            # if isinstance(params, tuple):
            #     self.lg.info(_get_url_contain_params(
            #         url=url,
            #         params=params,))

            return url, params, is_haokan

        # TODO bd的文字详情的图片在chrome中无法显示, 但是firefox中可以, 此处还未解决!
        video_url = ''
        headers = await async_get_random_headers(
            user_agent_type=1,)
        headers.update({
            'Referer': 'https://m.baidu.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        url, params, is_haokan = await _get_target_url_and_params_by_article_url(
            article_url=article_url,)

        body = await unblock_request(
            url=url,
            headers=headers,
            params=params,
            ip_pool_type=self.ip_pool_type,
            num_retries=self.request_num_retries,
            logger=self.lg)
        # self.lg.info(body)
        assert body != '', '获取bd的body为空值!'

        if is_haokan:
            video_url_selector = {
                'method': 'css',
                'selector': 'div.play1er-box video ::attr("src")',
            }
            video_url = await async_parse_field(
                parser=video_url_selector,
                target_obj=body,
                logger=self.lg,)

        else:
            pass

        return body, video_url

    async def _get_sg_article_html(self, article_url) -> tuple:
        """
        获取搜狗新闻资讯article html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers(user_agent_type=1)
        headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'https://wap.sogou.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        if '/sgs_video.php' in article_url:
            self.lg.info('该文章含视频!')
            # body 为动态加载的, 需要driver
            body = await self._get_html_by_driver(
                # phantomjs 失败率高!
                # _type=PHANTOMJS,
                _type=FIREFOX,
                url=article_url,
                load_images=False,
                headless=True,)
        else:
            # 包含视频的url容易请求出错
            body = await unblock_request(
                url=article_url,
                headers=headers,
                params=None,
                ip_pool_type=self.ip_pool_type,
                num_retries=self.request_num_retries,
                logger=self.lg)

        # self.lg.info(body)
        assert body != '', '获取sg的body为空值!'

        video_url = ''
        if '/sgs_video.php' in article_url:
            video_url_selector = {
                'method': 'css',
                # 'selector': 'video#my-video source ::attr("src")',
                'selector': 'div.ui-video video ::attr("src")',
            }
            video_url = await async_parse_field(
                parser=video_url_selector,
                target_obj=body,
                logger=self.lg,)
            self.lg.info('video_url: {}'.format(video_url))

        return body, video_url

    async def _get_df_article_html(self, article_url) -> tuple:
        """
        获取东方新闻的html
        :param article_url:
        :return:
        """
        headers = await async_get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,)
        headers.update({
            'Referer': 'http://toutiao.eastday.com/',
        })
        body = await unblock_request(
            url=article_url,
            headers=headers,
            params=None,
            ip_pool_type=self.ip_pool_type,
            logger=self.lg,)
        # self.lg.info(body)
        assert body != '', '获取df的body为空值!'

        video_url = ''
        # self.lg.info(article_url)
        if '/video/' in article_url:
            # 表示该文章为视频文章
            self.lg.info('该文章包含视频!')
            video_url = await self._get_df_video_url(body=body)

        return body, video_url

    async def _get_df_video_url(self, body) -> str:
        """
        获取df的video_url
        :return:
        """
        video_selector = {
            'method': 'css',
            'selector': 'video#J_video ::attr("src")',
        }
        video_url = await async_parse_field(
            parser=video_selector,
            target_obj=body,
            logger=self.lg,)

        video_url = 'https:' + video_url if video_url != '' else ''

        return video_url

    def unblock_get_kd_article_html(self, article_url):
        """
        获取qq看点的html
        :param article_url:
        :return:
        """
        video_url = ''
        if '/kan/video' in article_url:
            self.lg.info('此链接为视频链接')
            driver = BaseDriver(
                # server上调用报: selenium.common.exceptions.WebDriverException: Message: invalid argument: can't kill an exited process
                type=FIREFOX,
                executable_path=FIREFOX_DRIVER_PATH,

                # type=CHROME,
                # executable_path=CHROME_DRIVER_PATH,
                load_images=True,
                # todo 必须是无头, 否则linux server启动驱动失败!!
                headless=True,
                user_agent_type=PHONE,
                ip_pool_type=self.ip_pool_type,
                logger=self.lg,)

            # 播放按钮
            play_btn_css_sel = 'div#video-play span.tvp_button_play'
            driver.get_url_body(
                url=article_url,
                # 必须存在, 否则无后续操作
                css_selector=play_btn_css_sel,
                timeout=25,)
            driver.find_element(value=play_btn_css_sel).click()
            sleep(2.)
            body = driver._wash_html(html=driver.page_source)
            # self.lg.info(body)
            try:
                del driver
            except:
                try:
                    del driver
                except:
                    pass
            video_url_sel = {
                'method': 'css',
                'selector': 'div video ::attr("src")',
            }
            video_url = parse_field(
                parser=video_url_sel,
                target_obj=body,
                logger=self.lg)
            self.lg.info('got kd video_url: {}'.format(video_url))

        else:
            headers = get_random_headers()
            headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'authority': 'post.mp.qq.com',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'If-Modified-Since': 'Wed, 15 May 2019 10:17:11 GMT',
            })
            # self.lg.info(article_url)

            body = Requests.get_url_body(
                url=article_url,
                headers=headers,
                ip_pool_type=self.ip_pool_type,
                num_retries=self.request_num_retries,)

        # self.lg.info(body)
        assert body != '', '获取到的kd的body为空值!'

        return body, video_url

    def unblock_get_kb_article_html(self, article_url):
        """
        获取天天快报的html
        :param article_url:
        :return:
        """
        def get_special_case_api_data() -> dict:
            """
            二类情况接口数据获取
            :return:
            """
            nonlocal parse_obj
            # # todo 有两种情况, 一种是文章, 一种是视频
            _id = parse_field(
                parser=parse_obj['article_id2'],
                target_obj=article_url,
                logger=self.lg,
                is_print_error=True,)
            self.lg.info('_id: {}'.format(_id))
            params = (
                ('id', str(_id)),  # eg: '20190721A0JCZT00'
                ('openid', ''),
                # ('ukey', 'ukey_155817081468585658'),
                ('style', 'json'),
            )
            body = Requests.get_url_body(
                url='https://kuaibao.qq.com/getSubNewsContent',
                headers=headers,
                params=params,
                ip_pool_type=self.ip_pool_type,
                proxy_type=PROXY_TYPE_HTTPS,
                # 只进行2次请求, 避免时间过长无法执行下步请求
                num_retries=3,)
            # self.lg.info(body)
            data = json_2_dict(
                json_str=body,
                default_res={},
                logger=self.lg,)
            assert data != {}, 'data 不管是视频或者文章都不为空值!'
            # pprint(data)

            return data

        video_url = ''
        headers = get_random_headers(
            user_agent_type=1,
            connection_status_keep_alive=False,)
        headers.update({
            'authority': 'kuaibao.qq.com',
        })
        body = Requests.get_url_body(
            url=article_url,
            headers=headers,
            ip_pool_type=self.ip_pool_type,
            proxy_type=PROXY_TYPE_HTTPS,
            num_retries=3,)
        # self.lg.info(body)
        assert body != '', '获取到的kb的body为空值!'
        parse_obj = self.unblock_get_parse_obj(article_url_type='kb')
        article_title = parse_field(
            parser=parse_obj['title'],
            target_obj=body,
            logger=self.lg,)
        if article_title == '':
            self.hook_target_api_data = get_special_case_api_data()
            # pprint(self.hook_target_api_data)
            # todo play_url != ""表明是视频文章
            play_url = self.hook_target_api_data\
                .get('attribute', {})\
                .get('VIDEO_0', {})\
                .get('playurl', '')
            # self.lg.info('play_url: {}'.format(play_url))

            if play_url != '':
                # 单独处理含视频的
                # 表示title获取到为空值, 可能是含视频的
                # TODO 暂时先不获取天天快报含视频的
                self.lg.info('此article_url可能含有视频')
                driver = BaseDriver(
                    # type=FIREFOX,
                    # executable_path=FIREFOX_DRIVER_PATH,

                    # server上chrome成功, firefox一直显示超时, 故用chromedriver
                    type=CHROME,
                    executable_path=CHROME_DRIVER_PATH,
                    load_images=True,
                    headless=True,
                    user_agent_type=PHONE,
                    ip_pool_type=self.ip_pool_type,
                    logger=self.lg,)
                driver.get_url_body(
                    url=article_url,
                    # 必须等待这个显示后再关闭, 否则无video_url
                    css_selector='div#mainVideo video',
                    timeout=25,)
                # 点击播放按钮
                try:
                    self.lg.info('执行第一类播放点击ing...')
                    # 第一类
                    driver.find_element(value='div.play-btn').click()
                except Exception:
                    self.lg.error('遇到错误:', exc_info=True)
                    self.lg.info('执行第二类播放点击ing...')
                    # 第二类
                    driver.find_element(value='txpdiv.txp_btn_play').click()
                sleep(2.)
                body = driver._wash_html(html=driver.page_source)
                try:
                    del driver
                except:
                    try:
                        del driver
                    except:
                        pass
                # self.lg.info(body)
                # TODO 有多种视频类型格式, 先处理这种
                video_url_sel = {
                    'method': 'css',
                    'selector': 'div#mainVideo video:nth-child(1) ::attr("src")',
                }
                video_url = parse_field(
                    parser=video_url_sel,
                    target_obj=body,
                    logger=self.lg,)
                self.lg.info('video_url: {}'.format(video_url))

            else:
                self.lg.info('此文章为二类图文文章!')

        else:
            pass

        return body, video_url

    def _wash_wx_article_body(self, article_url, body) -> tuple:
        """
        清洗wx文章
        :return: body, video_url
        """
        # 处理微信防盗链
        body = re.compile('<head>').sub('<head><meta name=\"referrer\" content=\"never\">', body)
        body = re.compile('data-src=').sub('src=', body)

        video_url = ''
        # 单独处理含视频标签的
        try:
            # todo 现在wx的video iframe內值src 再去请求都是视频加载失败!(先不处理,)
            # videos_url_list = re.compile('<div class=\"tvp_video\"><video.*?src=\"(.*?)\"></video><div class=\"tvp_shadow\">').findall(body)
            videos_url_list = re.compile('<iframe class=\"video_iframe.*?\" .*? src=\"(.*?)\"></iframe>').findall(body)
            assert videos_url_list != []
            self.lg.info('视频list: {}'.format(videos_url_list))
            self.lg.info('此文章含视频! 正在重新获取文章html...')

            driver = BaseDriver(
                # type=PHANTOMJS,
                # executable_path=PHANTOMJS_DRIVER_PATH,
                type=FIREFOX,
                executable_path=FIREFOX_DRIVER_PATH,

                user_agent_type=PC,
                load_images=True,                   # 加载图片
                headless=False,
                logger=self.lg,
                ip_pool_type=self.ip_pool_type,
            )
            # driver.get_url_body(
            #     url=article_url,
            #     timeout=20,)
            # sleep(1.5)
            # try:
            #     driver.find_element(value='i.icon_mid_play').click()
            #     sleep(5.)
            # except Exception:
            #     self.lg.error('遇到错误: ', exc_info=True)
            #
            # video_body = driver._wash_html(html=driver.page_source)
            # self.lg.info('video_body: {}'.format(video_body))
            # 筛选出来的iframe src为无效url
            # video_iframe_list = re.compile('<iframe.*?>.*?</iframe>').findall(video_body)
            # pprint(video_iframe_list)
            # for item in video_iframe_list:
            #     print(item)
            # video_src_list_sel = {
            #     'method': 're',
            #     'selector': '<iframe.*? src=\"(.*?)\".*?>.*?</iframe>',
            # }
            # video_src_list = parse_field(
            #     parser=video_src_list_sel,
            #     target_obj=video_body,
            #     logger=self.lg,
            #     is_first=False,)
            # pprint(video_src_list)
            #
            # for item in video_src_list:
            #     item = re.compile('&amp;').sub('&', item)
            #     item = re.compile('&article_title=.*?......').sub('', item)
            #     item = re.compile('&random_num=.*?......').sub('', item)
            #     item = re.compile('&scene=.*?......').sub('', item)
            #     item = re.compile('%A8%E7%99%BD%E6%88%91%E4%BB%AC%E6%9C%80%E5%A5%BD%E7%9A%84%E2%80%9C%E9%98%BF%E4%B8%AD%E5%93%A5%E5%93%A5%E2%80%9D%EF%BC%8C%E8%BF%99%E4%BA%94%E4%B8%AA%E5%9F%8E%E5%B8%82%E7%8E%A9%E5%97%A8%E4%BA%86......').sub('', item)
            #     item = re.compile('&version=.*?\.js').sub('', item)
            #     item = 'https://mp.weixin.qq.com' + item
            #     print(item)

            # https://mp.weixin.qq.com/mp/videoplayer?video_h=186.75&amp;video_w=332&amp;scene=&amp;random_num=3913&amp;article_title=%E4%B8%BA%E8%A1%A8%E7%99%BD%E6%88%91%E4%BB%AC%E6%9C%80%E5%A5%BD%E7%9A%84%E2%80%9C%E9%98%BF%E4%B8%AD%E5%93%A5%E5%93%A5%E2%80%9D%EF%BC%8C%E8%BF%99%E4%BA%94%E4%B8%AA%E5%9F%8E%E5%B8%82%E7%8E%A9%E5%97%A8%E4%BA%86......&amp;source=4&amp;vid=wxv_970345944447320066&amp;mid=2654654251&amp;idx=1&amp;__biz=MjM5NzI1MTY0MQ==&amp;nodetailbar=0&amp;uin=&amp;key=&amp;pass_ticket=&amp;version=/mmbizwap/zh_CN/htmledition/js/appmsg/index480909.js&amp;devicetype=&amp;wxtoken=777&amp;sessionid=svr_11683bddae1&amp;preview=0
            # https://mp.weixin.qq.com/mp/videoplayer?video_h=186.75&amp;video_w=332&amp;scene=&amp;random_num=3913&amp;source=4&amp;vid=wxv_970345944447320066&amp;mid=2654654251&amp;idx=1&amp;__biz=MjM5NzI1MTY0MQ==&amp;nodetailbar=0&amp;uin=&amp;key=&amp;pass_ticket=&amp;version=/mmbizwap/zh_CN/htmledition/js/appmsg/index480909.js&amp;devicetype=&amp;wxtoken=777&amp;sessionid=svr_11683bddae1&amp;preview=0
            # 真实video_url: http://mpvideo.qpic.cn/tjg_3889235330_50000_ebf83ae259fd4629b6398d9b410e7334.f10002.mp4?dis_k=4034e2a5a2103ae29dd781b14286888d&amp;dis_t=1567481729

            tmp_body = driver.get_url_body(
                url=videos_url_list[0],
                timeout=20.,)
            # self.lg.info(tmp_body)
            assert tmp_body != '', 'tmp_body为空值!'

            try:
                del driver
            except:
                pass

            try:
                embed_div = re.compile('(<embed.*?)</div></div>').findall(tmp_body)[0]
                # self.lg.info(embed_div)
                # 获取video 的width, height
                video_width_and_height_tuple = re.compile('bgcolor=\".*?\" width=\"(\d+)px\" height=\"(\d+)px\"').findall(embed_div)[0]
                embed_div = '<embed width="{}px" height="{}px" src="{}" />'.format(
                    video_width_and_height_tuple[0],
                    video_width_and_height_tuple[1],
                    videos_url_list[0])
            except IndexError:
                raise IndexError('获取video_div时索引异常!')

            video_div = '<div style=\"text-align:center; width:100%; height:100%;\">' + embed_div + '</div>'
            # self.lg.info(video_div)
            # (只处理第一个视频)
            body = re.compile('<iframe class=\"video_iframe.*?\" .*?></iframe>').sub(
                repl=video_div,
                string=body,
                count=1,)
            video_url = videos_url_list[0]
        except AssertionError:
            pass
        except Exception:
            self.lg.error('遇到错误: ', exc_info=True)
        # self.lg.info(body)

        return body, video_url

    def unblock_get_parse_obj(self, article_url_type) -> dict:
        """
        获取到对应的解析对象
        :param article_url_type:
        :return:
        """
        # pprint(self.obj_origin_dict)
        for item in ARTICLE_ITEM_LIST:
            if article_url_type == item.get('short_name', ''):
                if item.get('obj_origin', '') == \
                        self.obj_origin_dict[article_url_type].get('obj_origin', ''):
                    parse_obj = item

                    return parse_obj

        raise NotImplementedError('未找到解析对象!')

    async def _get_parse_obj(self, article_url_type) -> dict:
        """
        获取到对应解析对象
        :return:
        """
        return self.unblock_get_parse_obj(
            article_url_type=article_url_type,)

    async def _get_praise_num(self, parse_obj, target_obj):
        """
        点赞数
        :param parse_obj:
        :param target_obj:
        :return:
        """
        praise_num = 0

        _ = await async_parse_field(
            parser=parse_obj.get('praise_num'),
            target_obj=target_obj,
            logger=self.lg)
        # self.lg.info(str(_))
        try:
            praise_num = int(_)
        except:
            pass

        return praise_num

    async def _get_fav_num(self, parse_obj, target_obj):
        """
        收藏数
        :param parse_obj:
        :param target_obj:
        :return:
        """
        short_name = parse_obj.get('short_name', '')

        fav_num = await async_parse_field(
            parser=parse_obj.get('fav_num'),
            target_obj=target_obj,
            logger=self.lg)

        if short_name == 'ck':
            fav_num = self.hook_target_api_data.get('count_like', 0)

        elif short_name == 'xq':
            fav_num = self.hook_target_api_data.get('fav_count', 0)

        elif short_name == 'blbl':
            fav_num = self.hook_target_api_data\
                .get('reduxAsyncConnect', {})\
                .get('videoInfo', {})\
                .get('stat', {})\
                .get('like', 0)

        else:
            pass

        try:
            fav_num = int(fav_num)
        except:
            fav_num = 0

        return fav_num

    async def _get_profile(self, parse_obj, target_obj):
        """
        推荐人简介或个性签名
        :param parse_obj:
        :param target_obj:
        :return:
        """
        short_name = parse_obj.get('short_name', '')

        profile = await async_parse_field(
            parser=parse_obj.get('profile'),
            target_obj=target_obj,
            logger=self.lg)

        if short_name == 'xq':
            profile = self.hook_target_api_data\
                .get('user', {})\
                .get('description', '')
        else:
            pass

        return profile

    async def _get_author(self, parse_obj, target_obj, video_url):
        """
        作者
        :param parse_obj:
        :param target_obj:
        :return:
        """
        short_name = parse_obj.get('short_name', '')
        assert short_name != ''
        author_selector = parse_obj.get('author')

        short_name_list = [
            'kb',
            'kd',
            'sg',
            'bd',
            'fh',
            'cn',
            'if',
            'ss',
            'jm',
            'pp',
            'hx',
            'hqx',
            'xg',
            'lsp',
            '7y7',
            'qqbb',
            'ft',
            '91mt',
            '5h',
            'bdj',
            'jd',
            'lfd',
        ]
        if short_name in short_name_list:
            if video_url != '':
                author_selector = parse_obj.get('video_author')
            else:
                pass

        else:
            pass

        # self.lg.info(target_obj)
        author = await async_parse_field(
            parser=author_selector,
            target_obj=target_obj,
            logger=self.lg)
        if short_name == 'kb':
            if video_url != '':
                if author == '':
                    author_selector2 = parse_obj.get('video_author2')
                    author = await async_parse_field(
                        parser=author_selector2,
                        target_obj=target_obj,
                        logger=self.lg,)
                    if author == '':
                        author_selector3 = parse_obj.get('video_author3')
                        author = await async_parse_field(
                            parser=author_selector3,
                            target_obj=target_obj,
                            logger=self.lg, )
            else:
                if author == '':
                    author = self.hook_target_api_data\
                        .get('card', {})\
                        .get('chlname', '')
                else:
                    pass

        elif short_name == 'pp':
            if author == '':
                # 湃客发的文章
                author_selector2 = parse_obj.get('author2')
                author = await async_parse_field(
                    parser=author_selector2,
                    target_obj=target_obj,
                    logger=self.lg, )
            else:
                pass

        elif short_name == 'nfzm':
            author = self.hook_target_api_data\
                .get('content', {})\
                .get('author', '')

        elif short_name == 'ck':
            author = self.hook_target_api_data.get('editor_username', '')

        elif short_name == 'xq':
            author = self.hook_target_api_data\
                .get('user', {})\
                .get('screen_name', '')

        elif short_name == 'hk':
            author = self.hook_target_api_data\
                .get('curVideoMeta', {})\
                .get('mth', {})\
                .get('author_name', '')

        elif short_name == 'blbl':
            author = self.hook_target_api_data\
                .get('reduxAsyncConnect', {})\
                .get('videoInfo', {})\
                .get('owner', {})\
                .get('name', '')

        elif short_name == 'txws':
            author = self.hook_target_api_data\
                .get('feeds', [])[0]\
                .get('poster', {})\
                .get('nick', '')

        elif short_name == 'jhbdsv':
            author = self.hook_target_api_data.get('source_name', '')

        elif short_name == 'bdqmxsv':
            author = self.hook_target_api_data\
                .get('author', {})\
                .get('name', '')

        else:
            pass

        short_name_list2 = [
            'df',
            'bd',
            'fh',
            'ys',
            'cn',
            'if',
            'ss',
            'jm',
            'pp',
            'hx',
            'nfzm',
            'hqx',
            'xg',
            'ck',
            'lsp',
            'amz',
            'kd',
            '7y7',
            'qqbb',
            'ft',
            '91mt',
            'xq',
            '5h',
            'bdj',
            'jd',
            'lfd',
            'blbl',
            'kys',
            'gxg',
            'kr',
            'dfsp',
            'txws',
            'klm',
            'ky',
            'dy',
            'jrxsp',
            'jhgzw',
            'jhrx',
            'mp',
            'jhwb',
            'jhbdsv',
            'bdqmxsv',
            'jhyw18q',
            'jhzjol',
        ]
        if short_name in short_name_list2:
            pass
        else:
            assert author != '', '获取到的author为空值!'

        return author

    async def _get_article_title(self, parse_obj, target_obj, video_url):
        """
        文章title
        :param parse_obj:
        :param target_obj:
        :return:
        """
        # self.lg.info(target_obj)
        short_name = parse_obj.get('short_name', '')
        assert short_name != ''
        # 可为None, 因为部分走接口
        title_sel = parse_obj.get('title', None)

        short_name_list = [
            'df',
            'kb',
            'kd',
            'sg',
            'bd',
            'fh',
            'cn',
            'if',
            'ss',
            'jm',
            'pp',
            'hx',
            'hqx',
            'xg',
            'lsp',
            '7y7',
            'qqbb',
            'ft',
            '91mt',
            '5h',
            'bdj',
            'jd',
            'lfd',
            'blbl',
            'jhgzw',
            'jhrx',
            'jhwb',
            'jhyw18q',
            'jhzjol',
        ]
        if short_name in short_name_list:
            if video_url != '':
                title_sel = parse_obj.get('video_title')
            else:
                pass
        else:
            pass

        # self.lg.info(target_obj)
        title = await async_parse_field(
            parser=title_sel,
            target_obj=target_obj,
            logger=self.lg)

        if short_name == 'kb':
            if video_url != '':
                if title == '':
                    # 情况1:
                    title_selector2 = parse_obj.get('video_title2')
                    # pprint(title_selector2)
                    title = await async_parse_field(
                        parser=title_selector2,
                        target_obj=target_obj,
                        logger=self.lg,)
                    if title == '':
                        # 情况2
                        title_selector3 = parse_obj.get('video_title3')
                        # pprint(title_selector3)
                        title = await async_parse_field(
                            parser=title_selector3,
                            target_obj=target_obj,
                            logger=self.lg, )
                    else:
                        pass
                else:
                    pass
            else:
                if title == '':
                    # 情况1
                    title = self.hook_target_api_data.get('title', '')
                else:
                    pass

        elif short_name == 'nfzm':
            # pprint(self.hook_target_api_data)
            title = self.hook_target_api_data\
                .get('content', {})\
                .get('subject', '')

        elif short_name == 'ck':
            title = self.hook_target_api_data.get('title', '')

        elif short_name == 'xq':
            title = self.hook_target_api_data.get('title', '')

        elif short_name == 'hk':
            title = self.hook_target_api_data\
                .get('curVideoMeta', {})\
                .get('title', '')

        elif short_name == 'jd':
            title = self.hook_target_api_data\
                .get('base_data', {})\
                .get('title', '')

        elif short_name == 'ky':
            title = self.hook_target_api_data\
                .get('title', '')

        elif short_name == 'dy':
            title = self.hook_target_api_data\
                .get('desc', '')

        elif short_name == 'ft':
            if video_url != '':
                if title == '':
                    title_selector2 = parse_obj.get('video_title2')
                    title = await async_parse_field(
                        parser=title_selector2,
                        target_obj=target_obj,
                        logger=self.lg, )

                else:
                    pass

        elif short_name == 'blbl':
            title = self.hook_target_api_data\
                .get('reduxAsyncConnect', {})\
                .get('videoInfo', {})\
                .get('title', '')

        elif short_name == 'kr':
            title = self.hook_target_api_data.get('title', '')

        elif short_name == 'txws':
            pprint(self.hook_target_api_data)
            title = self.hook_target_api_data.get('feeds', [])[0].get('feed_desc', '')
            if title == '':
                title = self.hook_target_api_data.get('feeds', [])[0].get('material_desc', '')
            else:
                pass

        elif short_name == 'jhbdsv':
            title = self.hook_target_api_data.get('title', '')

        elif short_name == 'bdqmxsv':
            title = self.hook_target_api_data\
                .get('meta', {})\
                .get('title', '')

        else:
            pass

        title = await self._wash_title(
            short_name=short_name,
            title=title)
        # self.lg.info(title)

        short_name_list2 = [
            'kys',
        ]
        if short_name in short_name_list2:
            if video_url != '':
                pass
            else:
                assert title != '', '获取到的title为空值!'
        else:
            assert title != '', '获取到的title为空值!'

        return title

    async def _wash_title(self, short_name, title) -> str:
        """
        清洗title
        :param short_name:
        :param title:
        :return:
        """
        if short_name == 'tt':
            title = await self._wash_tt_title(title=title)

        elif short_name == 'kys':
            title = await self._wash_kys_title(title=title)

        elif short_name == 'kr':
            title = await self._wash_kr_title(title=title)

        elif short_name == 'txws':
            title = await self._wash_txws_title(title=title)

        elif short_name == 'mp':
            title = await self._wash_mp_title(title=title)

        elif short_name == 'ky':
            title = await self._wash_ky_title(title=title)

        elif short_name == 'dy':
            title = await self._wash_dy_title(title=title)

        elif short_name == 'jhrx':
            title = await self._wash_jhrx_title(title=title)

        elif short_name == 'bdqmxsv':
            title = await self._wash_bdqmxsv_title(title=title)

        elif short_name == 'jhyw18q':
            title = await self._wash_jhyw18q_title(title=title)

        elif short_name == 'jhzjol':
            title = await self._wash_jhzjol_title(title=title)

        else:
            pass

        return title

    @staticmethod
    async def _wash_jhzjol_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[
            ],
            add_sensitive_str_list=[
                '浙江日报丨',
                '浙江日报头版丨',
                '浙江在线金华频道',
                '浙江日报整版关注丨',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_jhyw18q_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[
            ],
            add_sensitive_str_list=[
                '-义乌十八腔',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_bdqmxsv_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[
            ],
            add_sensitive_str_list=[
                '全民小视频',
                '@全民小助手',
                '\#\#',
                '全民小助手',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_jhrx_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[
                ('  ', ' '),
            ],
            add_sensitive_str_list=[
                '-大金华论坛',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_dy_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[
                ('  ', ' '),
            ],
            add_sensitive_str_list=[
                '\@\w+',     # eg: '@抖音小助手'
                '\#\w+',     # eg: '#波波脱口秀'
                '抖音',
                'douyin',
                'DOUYIN',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_ky_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[],
            add_sensitive_str_list=[
                '开眼',
                'kaiyan',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_mp_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[],
            add_sensitive_str_list=[
                '美拍小助手',
                '美拍',
                '我要上热门',
                '\#\#',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_txws_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[],
            add_sensitive_str_list=[
                '微视',
                '腾讯',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_kr_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[],
            add_sensitive_str_list=[
                # 洗掉eg: '20180824期'
                '\d+期',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_kys_title(title: str) -> str:
        title = wash_sensitive_info(
            data=title,
            replace_str_list=[],
            add_sensitive_str_list=[
                '快手',
                '抖音',
                '火山',
                '美拍',
            ],
            is_default_filter=False,
            is_lower=False,
        )

        return title

    @staticmethod
    async def _wash_tt_title(title: str) -> str:
        """
        :param title:
        :return:
        """
        title = fix_text(text=title[6:-6])

        return title

    async def _get_head_url(self, parse_obj, target_obj, video_url) -> str:
        """
        得到文章发布者的头像url
        :param parse_obj:
        :param target_obj:
        :return:
        """
        short_name = parse_obj.get('short_name', '')
        head_url_sel = parse_obj.get('head_url')

        short_name_list = [
            'kb',
            'kd',
            'hx',
            'hqx',
            'lsp',
            '7y7',
            'qqbb',
            'ft',
            '91mt',
            'bdj',
        ]
        if short_name in short_name_list:
            if video_url != '':
                head_url_sel = parse_obj.get('video_head_url')
            else:
                pass
        else:
            pass

        # self.lg.info(target_obj)
        head_url = await async_parse_field(
            parser=head_url_sel,
            target_obj=target_obj,
            logger=self.lg)

        if short_name == 'kb':
            if video_url != '':
                if head_url == '':
                    head_url_sel2 = parse_obj.get('video_head_url2')
                    head_url = await async_parse_field(
                        parser=head_url_sel2,
                        target_obj=target_obj,
                        logger=self.lg)
                else:
                    pass
            else:
                pass

        elif short_name == '7y7':
            if video_url != '':
                pass
            else:
                head_url = 'https://i.7y7.com' + head_url if head_url != '' else ''

        elif short_name == 'xq':
            head_url = ''

        elif short_name == 'bdj':
            # 小头像换成原图
            head_url = head_url.replace('_mini', '')

        elif short_name == 'hk':
            head_url = self.hook_target_api_data\
                .get('curVideoMeta', {})\
                .get('mth', {})\
                .get('author_photo', '')

        elif short_name == 'blbl':
            head_url = self.hook_target_api_data\
                .get('reduxAsyncConnect', {})\
                .get('videoInfo', {})\
                .get('owner', {})\
                .get('face', '')

        elif short_name == 'txws':
            head_url = self.hook_target_api_data\
                .get('feeds', [])[0]\
                .get('poster', {})\
                .get('avatar', '')

        else:
            pass

        # 天天快报存在头像为''
        if head_url != '' \
                and not head_url.startswith('http'):
            head_url = 'https:' + head_url
        else:
            pass

        return head_url

    async def _get_share_id(self, **kwargs) -> str:
        """
        得到唯一的share_id
        :return:
        """
        article_url_type = kwargs.get('article_url_type', '')
        article_url = kwargs.get('article_url', '')
        video_url = kwargs.get('video_url', '')
        parse_obj = kwargs.get('parse_obj', {})
        short_name = parse_obj.get('short_name', '')

        short_name_list = [
            'wx',
            'sg',
        ]
        if article_url_type in short_name_list:
            return get_uuid1()

        article_id_selector = await self._get_article_id_selector(
            article_url_type=article_url_type,
            article_url=article_url,)
        share_id = await async_parse_field(
            parser=article_id_selector,
            target_obj=article_url,
            logger=self.lg)

        short_name_list2 = [
            'kb',
            'zq',
        ]
        if short_name in short_name_list2:
            if share_id == '':
                share_id = await async_parse_field(
                    parser=parse_obj.get('article_id2'),
                    target_obj=article_url,
                    logger=self.lg)
            else:
                pass

        elif short_name == 'kd':
            if share_id == '':
                # 视频文章id
                share_id = get_uuid1()
            else:
                pass

        elif short_name == 'jd':
            share_id = self.hook_target_api_data.get('article_id', '')

        elif short_name == 'dy':
            share_id = self.hook_target_api_data.get('aweme_id', '')

        else:
            pass

        assert share_id != '', '获取到的share_id为空值!'

        return share_id

    async def _get_article_id_selector(self, article_url_type, article_url) -> (dict, None):
        """
        获取article_id的selector
        :param self:
        :param article_url_type:
        :return:
        """
        for item in ARTICLE_ITEM_LIST:
            if article_url_type == item.get('short_name', ''):
                if article_url_type == 'bd':
                    if 'haokan.baidu.com' in article_url:
                        return item.get('video_id')

                    elif 'sv.baidu.com' in article_url:
                        return item.get('video_id2')

                    else:
                        pass

                elif article_url_type == 'jm':
                    if '/video/' in article_url:
                        return item.get('video_id')

                else:
                    pass

                return item.get('article_id')

        raise NotImplementedError

    async def _get_comment_num(self, parse_obj, target_obj) -> int:
        """
        文章评论数
        :param parse_obj:
        :param target_obj:
        :return:
        """
        comment_num = 0
        short_name = parse_obj.get('short_name', '')

        _ = await async_parse_field(
            parser=parse_obj.get('comment_num'),
            target_obj=target_obj,
            logger=self.lg)
        # self.lg.info(str(_))

        if short_name == 'nfzm':
            comment_num = self.hook_target_api_data\
                .get('content', {})\
                .get('comment_count', '')

        elif short_name == 'ck':
            comment_num = self.hook_target_api_data.get('count_comment', '')

        elif short_name == 'kb':
            if _ == '':
                comment_num = self.hook_target_api_data\
                    .get('count_info', {})\
                    .get('comments', '')
            else:
                pass

        elif short_name == 'blbl':
            comment_num = self.hook_target_api_data\
                .get('reduxAsyncConnect', {})\
                .get('videoInfo', {})\
                .get('stat', {})\
                .get('reply', 0)

        else:
            pass

        try:
            comment_num = int(_)
        except ValueError:      # 未提取到评论默认为0
            pass

        return comment_num

    async def _get_tags_list(self, parse_obj, video_url, target_obj) -> list:
        """
        获取文章的tags list
        :param parse_obj:
        :param target_obj:
        :return:
        """
        short_name = parse_obj.get('short_name', '')

        is_first = False
        if short_name == 'kd'\
                or short_name == 'bd':
            # 取第一个str
            is_first = True

        short_name_list = [
            'kd',
            '7y7',
            'qqbb',
            'ft',
        ]
        tags_list_sel = parse_obj.get('tags_list')
        if short_name in short_name_list:
            if video_url != '':
                tags_list_sel = parse_obj.get('video_tags_list')
            else:
                pass
        else:
            pass

        tags_list = await async_parse_field(
            parser=tags_list_sel,
            target_obj=target_obj,
            is_first=is_first,
            logger=self.lg)
        if tags_list == '':
            return []

        short_name_list2 = [
            'tt',
            'js',
            'kd',
            'if',
            'ss',
            'lsp',
            '7y7',
            'qqbb',
        ]
        if short_name in short_name_list2:
            tags_list = [{
                'keyword': i,
            } for i in tags_list]

        elif short_name == 'kd':
            tags_list = tags_list.split(',')

        elif short_name == 'bd':
            # self.lg.info(str(tags_list))
            if tags_list != '':
                ori_tag_json_data = tags_list + ']'
                tmp_tag_list = json_2_dict(
                    json_str=ori_tag_json_data,
                    default_res=[],
                    logger=self.lg)
                # pprint(tmp_tag_list)
                tags_list = []
                for item in tmp_tag_list:
                    try:
                        name = item.get('name', '')
                        assert name != '', 'name != ""'
                    except AssertionError:
                        continue
                    tags_list.append({
                        'keyword': name,
                    })
                # pprint(tags_list)

            else:
                pass

        elif short_name == 'nfzm':
            tags_list = []
            ori_tags_list = self.hook_target_api_data\
                .get('content', {})\
                .get('tags', [])
            for item in ori_tags_list:
                try:
                    tag_name = item.get('title', '')
                    assert tag_name != ''
                except AssertionError:
                    continue
                tags_list.append({
                    'keyword': tag_name,
                })

        elif short_name == 'blbl':
            tags_list = []
            ori_tags_list = self.hook_target_api_data\
                .get('reduxAsyncConnect', {})\
                .get('videoTag', [])
            for item in ori_tags_list:
                try:
                    tag_name = item.get('tag_name', '')
                    assert tag_name != ''
                except AssertionError:
                    continue
                tags_list.append({
                    'keyword': tag_name,
                })

        else:
            pass

        tags_list = list_remove_repeat_dict_plus(
            target=tags_list,
            repeat_key='keyword',)

        return tags_list

    async def _get_article_create_time(self, parse_obj, target_obj, video_url, article_url) -> str:
        """
        文章创建时间点
        :param parse_obj:
        :param target_obj:
        :return:
        """
        async def parse_create_time(short_name, create_time) -> str:
            """
            解析create_time
            :param create_time:
            :return:
            """
            try:
                create_time = str(date_parse(create_time))
            except ValueError:
                self.lg.error('获取article create_time时, 遇到错误:', exc_info=True)
                self.lg.info('默认设置当前时间为文章创建时间点!')
                create_time = str(get_shanghai_time())

            return create_time

        short_name = parse_obj.get('short_name', '')
        assert short_name != ''
        create_time_sel = parse_obj.get('create_time')

        short_name_list = [
            'sg',
            'bd',
            'cn',
            'if',
            'ss',
            'jm',
            'pp',
            'hx',
            'hqx',
            'xg',
            'lsp',
            'kd',
            '7y7',
            'qqbb',
            'ft',
            '91mt',
            'xq',
            '5h',
            'bdj',
            'lfd',
        ]
        if short_name in short_name_list:
            if video_url != '':
                create_time_sel = parse_obj.get('video_create_time')
            else:
                pass

        elif short_name == 'fh':
            if video_url != '':
                create_time_sel = parse_obj.get('video_create_time')
            else:
                if 'feng.ifeng.com' in article_url:
                    create_time_sel = parse_obj.get('create_time2')
                else:
                    pass

        else:
            pass

        # self.lg.info(target_obj)
        create_time = await async_parse_field(
            parser=create_time_sel,
            target_obj=target_obj,
            logger=self.lg)
        # self.lg.info(create_time)
        short_name_list2 = [
            'cn',
            'if',
            'ss',
            'jm',
            'pp',
            'hx',
            'hqx',
            'lsp',
            'mp',
            '7y7',
            'qqbb',
            'ft',
            '91mt',
            '5h',
        ]
        short_name_list3 = [
            'js',
            'kd',
            'bdj',
            'hk',
            'blbl',
        ]
        if short_name == 'sg':
            if video_url != '':
                # 原先为2019/05/05 11:13, 替换为标准的
                create_time = await parse_create_time(
                    short_name=short_name,
                    create_time=create_time,)

            else:
                create_time = create_time.replace('/', '-')

        elif short_name == 'bd':
            if video_url != '':
                pass

            else:
                if create_time != '':
                    try:
                        create_time = str(timestamp_to_regulartime(create_time[:10]))
                    except Exception:
                        self.lg.error('遇到错误:', exc_info=True)
                        create_time = ''

        elif short_name in short_name_list2:
            if create_time != '':
                create_time = await parse_create_time(
                    short_name=short_name,
                    create_time=create_time)

        elif short_name == 'kb':
            if create_time == '':
                create_time = await parse_create_time(
                    short_name=short_name,
                    create_time=self.hook_target_api_data.get('pub_time', ''),)
            else:
                pass

        elif short_name in short_name_list3:
            if short_name == 'hk':
                create_time = self.hook_target_api_data\
                    .get('curVideoMeta', {})\
                    .get('publish_time', '')
            elif short_name == 'blbl':
                create_time = self.hook_target_api_data\
                    .get('reduxAsyncConnect', {})\
                    .get('videoInfo', {})\
                    .get('ctime', '')
            else:
                pass
            if create_time != '':
                # eg: ori_data = '1565402168'
                create_time = create_time[0:10] if isinstance(create_time, str) else create_time
                create_time = str(timestamp_to_regulartime(int(create_time)))
                # self.lg.info(create_time)
            else:
                pass

        elif short_name == 'nfzm':
            create_time = await parse_create_time(
                short_name=short_name,
                create_time=self.hook_target_api_data.get('content', {}).get('publish_time', ''))

        elif short_name == 'ck':
            create_time = str(timestamp_to_regulartime(int(self.hook_target_api_data.get('publish_time', ''))))

        elif short_name == 'xq':
            try:
                create_time = timestamp_to_regulartime(
                    int(str(self.hook_target_api_data.get('created_at', ''))[0:10]))
            except Exception:
                self.lg.error('遇到错误:', exc_info=True)

        elif short_name == 'jd':
            create_time = await parse_create_time(
                short_name=short_name,
                create_time=self.hook_target_api_data.get('base_data', {}).get('pubDate', ''))

        elif short_name == 'lfd':
            if create_time != '':
                create_time = create_time.replace(' ', '')
                create_time = await parse_create_time(
                    short_name=short_name,
                    create_time=create_time,)
            else:
                pass

        else:
            pass

        if create_time == '':
            create_time = str(get_shanghai_time())
        else:
            pass
        # assert create_time != '', '获取到的create_time为空值!'

        return create_time

    async def _get_article_content(self, parse_obj, target_obj, article_url, video_url) -> str:
        """
        article content
        :return:
        """
        short_name = parse_obj.get('short_name', '')
        content_sel = parse_obj.get('content')

        short_name_list = [
            'kb',
            'kd',
            'cn',
            'if',
            'ss',
            'jm',
            'pp',
            'hx',
            'hqx',
            'xg',
            'lsp',
            '7y7',
            'qqbb',
            'ft',
            '91mt',
            '5h',
            'bdj',
            'jd',
            'lfd',
            'jhgzw',
            'jhrx',
            'jhwb',
        ]
        if short_name in short_name_list:
            if video_url != '':
                content_sel = parse_obj.get('video_article_content')
            else:
                pass

        elif short_name == 'fh':
            if video_url != '':
                content_sel = parse_obj.get('video_article_content')
            else:
                if 'feng.ifeng.com' in article_url:
                    content_sel = parse_obj.get('content2')
                else:
                    pass
        else:
            pass

        # self.lg.info(str(target_obj))
        # pprint(content_sel)
        content = await async_parse_field(
            parser=content_sel,
            target_obj=target_obj,
            logger=self.lg)

        short_name_list3 = [
            'hx',
            'hqx',
        ]
        short_name_list4 = [
            '7y7',
            'qqbb',
        ]
        if short_name in short_name_list3:
            if video_url == '' and content != '':
                # 加上主图
                article_main_img_div = await async_parse_field(
                    parser=parse_obj.get('article_main_img'),
                    target_obj=target_obj,
                    logger=self.lg)
                content = article_main_img_div + content
            else:
                pass

        elif short_name == 'kb':
            if video_url != '':
                pass
            else:
                if content == '':
                    # 第二类图文
                    content = self.hook_target_api_data.get('cnt_html_origin', '')
                    if content == '':
                        # 第三类图文
                        ori_content = self.hook_target_api_data.get('orig_content', [])
                        for item in ori_content:
                            try:
                                _type = item.get('type' '')
                                if _type == 'img_url':
                                    img_url = item.get('img_url', '')
                                    assert img_url != ''
                                    content += '<img src=\"{}\">'.format(img_url)
                                elif _type == 'cnt_article':
                                    _desc = item.get('desc', '')
                                    assert _desc != ''
                                    content += '<p>{}</p>'.format(_desc)
                                else:
                                    raise ValueError('_type: {}, 值异常!'.format(_type))

                            except (AssertionError, Exception):
                                # self.lg.error('遇到错误:', exc_info=True)
                                continue

                    else:
                        pass
                    if content == '':
                        # 第四类图文
                        kb_attribute = self.hook_target_api_data.get('attribute', {})
                        # eg: '<P>这个男厕的将小便池和洗手池结合的一体化设计，洗手的水顺便也能清理小便池，充分利用了水资源！</P><P><!--IMG_0--></P>'
                        kb_content = self.hook_target_api_data\
                            .get('content', {})\
                            .get('text', '')

                        # pprint(kb_attribute)
                        # self.lg.info(kb_content)
                        for key, value in kb_attribute.items():
                            # eg: key = 'IMG_0'
                            try:
                                img_url = value.get('url', '')
                                assert img_url != ''
                                kb_content = kb_content.replace('<!--{}-->'.format(key), '<img src=\"{}\">'.format(img_url))
                            except (AssertionError, Exception):
                                # self.lg.error('遇到错误:', exc_info=True)
                                continue

                        # self.lg.info(str(kb_content))
                        content = kb_content

                    else:
                        pass
                else:
                    pass

        elif short_name == 'nfzm':
            content = self.hook_target_api_data\
                .get('content', {})\
                .get('fulltext', '')

        elif short_name == 'ck':
            content = self.hook_target_api_data.get('content', '')

        elif short_name == 'xq':
            content = self.hook_target_api_data.get('text', '')

        elif short_name == 'amz':
            # 不管content是否为空, 都进入
            video_iframe = await self._get_amz_video_iframe(
                parse_obj=parse_obj,
                target_obj=target_obj,)
            self.lg.info('video_iframe: {}'.format(video_iframe))
            # 视频iframe在前面
            content = video_iframe + content

        elif short_name in short_name_list4:
            if video_url != '':
                pass
            else:
                if content != '':
                    # 加上最上方描述div
                    desc_div = await async_parse_field(
                        parser=parse_obj.get('desc_div'),
                        target_obj=target_obj,
                        logger=self.lg)
                    if desc_div != '':
                        content = '<p>{}</p>'.format(desc_div) + content
                    else:
                        pass
                else:
                    pass

        elif short_name == 'jd':
            ori_img_url_list = self.hook_target_api_data\
                .get('base_data', {})\
                .get('images', [])
            assert ori_img_url_list != []
            article_main_img_div = ''
            for img_url in ori_img_url_list:
                if img_url != '':
                    img_url = 'http:' + img_url if re.compile('http').findall(img_url) == [] else img_url
                    article_main_img_div += '<img src=\"{}\">'.format(img_url)
                else:
                    continue
            content = article_main_img_div + content

        elif short_name == 'blbl':
            content = self.hook_target_api_data\
                .get('reduxAsyncConnect', {})\
                .get('videoInfo', {})\
                .get('desc', '')

        elif short_name == 'ky':
            content = self.hook_target_api_data\
                .get('description', '')

        else:
            pass

        content = await self._wash_article_content(
            short_name=short_name,
            content=content,)
        content = await self.unify_wash_article_content(
            short_name=short_name,
            content=content,)

        short_name_list2 = [
            'df',
            'sg',
            'bd',
            'kb',
            'kd',
            'yg',
            'fh',
            'cn',
            'if',
            'ss',
            'jm',
            'pp',
            'hx',
            'nfzm',
            'hqx',
            'xg',
            'ck',
            'lsp',
            'mp',
            'hk',
            '7y7',
            'qqbb',
            'ft',
            '91mt',
            'xq',
            '5h',
            'bdj',
            'jd',
            'lfd',
            'blbl',
            'kys',
            'kr',
            'dfsp',
            'txws',
            'klm',
            'ky',
            'dy',
            'jrxsp',
            'jhgzw',
            'jhrx',
            'jhwb',
            'jhbdsv',
            'bdqmxsv',
            'jhyw18q',
            'jhzjol',
        ]
        if short_name in short_name_list2:
            if video_url != '':
                pass
            else:
                assert content != '', '获取到的content为空值!'

        else:
            assert content != '', '获取到的content为空值!'

        # hook 防盗链
        content = '<meta name=\"referrer\" content=\"never\">' + content \
            if content != '' else ''
        print(content)
        # cp后台处理, 此处不处理
        # content = await self._wash_my_style_in_content(content=content)
        # self.lg.info(content)

        return content

    @staticmethod
    async def unify_wash_article_content(short_name: str, content) -> str:
        """
        统一清洗
        :param content:
        :return:
        """
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('今日头条', '优秀网'),
                ('头条', '优秀'),
                ('\，{2}', '，'),
                ('\。{2}', '。'),
            ],
            add_sensitive_str_list=[
                '<br>',
                '禁止转[发载]{1}',
                '私自转载',
                '禁止搬运',
                '追究法律责任',
                '图片[均]{0,1}来[源自]{1}[于]{0,1}网络',
                '如有侵权请联系删除',
                '版权归[于]{0,1}原作者所有',
                '图文原创',
                '搬运必究',
                '转载此文是出于传递更多信息之目的',
                '若有来源标注错误或侵犯了您的合法权益',
                '请作者持权属证明与本网联系',
                '我们将及时更正、删除，谢谢。',
                '部分图片来自网络',
                '转载抄袭必究',
                '未经[许授]{1}[可权]{1}',
                '[本独]{1}[人家]{1}原创',
                '请勿转载',
                '声明：本文章内容或视频素材来源于网络，如有侵权请联系删除！',
                '该文章为优秀网首发，其他平台转载必须私信作者，取得授权。',
                '\#月薪万元\—新作者扶植计划开启\#',
                '\（点击可放大看\）',
                '禁止一切搬运行为',
                '侵删',
                '免责声明[\：\:]{0,1}',
                '本文部分内容来自互联网',
                '如不慎侵害的您的权益,请告知,我们将尽快删除',
                '文章中的，，文字为。',
                '阅读原文',
                '领取更多京东优惠',
                '欢迎你关注我',
                '我们下期再见',
                '\：\，\，\。',
                '\:\,\,\.',
                '[\[\(\【]{1}[\]\)\】]{1}',
                '本文著作权归作者所有',
                '并授权\w+独家使用',
                '未经\w+官方许可',
                '不得转载使用',
                '本文文字为原创',
                '文字属于作者原创',
                '配图来源[于]{0,1}网络',
                '欢迎大家转发关注',
                '文字原创',
                '文章系原创',
                '版权受保护',
                '严禁任何形式的抄袭、搬运',
                '如有侵权',
                '请联系我们删除',
                '禁止抄袭',
                '和搬运等行为',
                '声明：。，，',
                '声明：，，。',
            ],
            is_default_filter=False,
            is_lower=False,)
        if content != '':
            content += '<br><p><strong>免责声明: 文章来源于网络, 仅供个人研究学习, 不涉及商业盈利目的, 如有侵权请及时联系管理员删除! 谢谢!</strong></p>'
        else:
            pass

        return content

    @staticmethod
    async def _wash_my_style_in_content(content: str) -> str:
        """
        清洗掉自己的样式
        :param self:
        :param content:
        :return:
        """
        content = wash_sensitive_info(
            data=content,
            replace_str_list=None,
            add_sensitive_str_list=[
                '<meta name=\"referrer\" content=\"never\">',
                # 图片居中, p, 原生style
                '<style type=\"text/css\">.*?</style>',
            ],
            is_default_filter=False,
            is_lower=False,)

        return content

    async def _get_amz_video_iframe(self, parse_obj, target_obj) -> str:
        """
        获取amz video_iframe
        :param parse_obj:
        :param target_obj:
        :return:
        """
        video_iframe = await async_parse_field(
            parser=parse_obj['video_iframe'],
            target_obj=target_obj,
            logger=self.lg, )
        if video_iframe == '':
            # 第二种情况视频处理, 生成iframe(eg: 优酷视频云)
            client_id = await async_parse_field(
                parser=parse_obj['client_id'],
                target_obj=target_obj,
                logger=self.lg, )
            assert client_id != ''
            vid = await async_parse_field(
                parser=parse_obj['vid'],
                target_obj=target_obj,
                logger=self.lg, )
            assert vid != ''
            # eg: https://player.youku.com/embed/XNDExMjEzMzMxNg==?client_id=53c06c7e23bff2b5&amp;password=&amp;autoplay=true#aimozhen.com
            iframe_src = 'https://player.youku.com/embed/{vid}?client_id={client_id}&amp;password=&amp;autoplay=true#aimozhen.com'.format(
                vid=vid,
                client_id=client_id, )
            self.lg.info('生成的iframe_src: {}'.format(iframe_src))
            video_iframe = '<iframe width=\"100%\" height=\"100%\" allow=\"autoplay\" src=\"{iframe_src}\" name=\"iframeId\" id=\"iframeId\" frameborder=\"0\" allowfullscreen=\"true\" scrolling=\"no\"></iframe>'.format(
                iframe_src=iframe_src, )
        else:
            pass
        assert video_iframe != '', 'amz的video_iframe不为空值!'

        return video_iframe

    async def _wash_article_content(self, short_name: str, content: str) -> str:
        """
        清洗content
        :param short_name:
        :param content:
        :return:
        """
        if short_name == 'tt':
            # html乱码纠正
            content = await self._wash_tt_article_content(content=content)

        elif short_name == 'js':
            # 图片处理
            content = await self._wash_js_article_content(content=content)

        elif short_name == 'kd':
            # 图片处理
            content = await self._wash_kd_article_content(content=content)

        elif short_name == 'kb':
            # css 处理为原生的
            content = await self._wash_kb_article_content(content=content)

        elif short_name == 'wx':
            content = await self._wash_wx_article_content(content=content)

        elif short_name == 'df':
            content = await self._wash_df_article_content(content=content)

        elif short_name == 'sg':
            content = await self._wash_sg_article_content(content=content)

        elif short_name == 'bd':
            content = await self._wash_bd_article_content(content=content)

        elif short_name == 'zq':
            content = await self._wash_zq_article_content(content=content)

        elif short_name == 'fh':
            content = await self._wash_fh_article_content(content=content)

        elif short_name == 'ys':
            content = await self._wash_ys_article_content(content=content)

        elif short_name == 'cn':
            content = await self._wash_cn_article_content(content=content)

        elif short_name == 'if':
            content = await self._wash_if_article_content(content=content)

        elif short_name == 'ss':
            content = await self._wash_ss_article_content(content=content)

        elif short_name == 'jm':
            content = await self._wash_jm_article_content(content=content)

        elif short_name == 'pp':
            content = await self._wash_pp_article_content(content=content)

        elif short_name == 'hx':
            content = await self._wash_hx_article_content(content=content)

        elif short_name == 'nfzm':
            content = await self._wash_nfzm_article_content(content=content)

        elif short_name == 'hqx':
            content = await self._wash_hqx_article_content(content=content)

        elif short_name == 'ck':
            content = await self._wash_ck_article_content(content=content)

        elif short_name == 'lsp':
            content = await self._wash_lsp_article_content(content=content)

        elif short_name == 'amz':
            content = await self._wash_amz_article_content(content=content)

        elif short_name == 'mp':
            content = await self._wash_mp_article_content(content=content)

        elif short_name == '7y7':
            content = await self._wash_7y7_article_content(content=content)

        elif short_name == 'qqbb':
            content = await self._wash_qqbb_article_content(content=content)

        elif short_name == 'ft':
            content = await self._wash_ft_article_content(content=content)

        elif short_name == '91mt':
            content = await self._wash_91mt_article_content(content=content)

        elif short_name == 'xq':
            content = await self._wash_xq_article_content(content=content)

        elif short_name == '5h':
            content = await self._wash_5h_article_content(content=content)

        elif short_name == 'bdj':
            content = await self._wash_bdj_article_content(content=content)

        elif short_name == 'jd':
            content = await self._wash_jd_article_content(content=content)

        elif short_name == 'lfd':
            content = await self._wash_lfd_article_content(content=content)

        elif short_name == 'blbl':
            content = await self._wash_blbl_article_content(content=content)

        elif short_name == 'gxg':
            content = await self._wash_gxg_article_content(content=content)

        elif short_name == 'kr':
            content = await self._wash_kr_article_content(content=content)

        elif short_name == 'dfsp':
            content = await self._wash_dfsp_article_content(content=content)

        elif short_name == 'ky':
            content = await self._wash_ky_article_content(content=content)

        elif short_name == 'dy':
            content = await self._wash_dy_article_content(content=content)

        elif short_name == 'jhgzw':
            content = await self._wash_jhgzw_article_content(content=content)

        elif short_name == 'jhrx':
            content = await self._wash_jhrx_article_content(content=content)

        elif short_name == 'jhwb':
            content = await self._wash_jhwb_article_content(content=content)

        elif short_name == 'jhbdsv':
            content = await self._wash_jhbdsv_article_content(content=content)

        elif short_name == 'bdqmxsv':
            content = await self._wash_bdqmxsv_article_content(content=content)

        elif short_name == 'jhyw18q':
            content = await self._wash_jhyw18q_article_content(content=content)

        elif short_name == 'jhzjol':
            content = await self._wash_jhzjol_article_content(content=content)

        else:
            pass

        return content

    @staticmethod
    async def _wash_jhzjol_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                # 加上http避免cp 服务端无法上传
                ('src=\"\/\/img\.zjol\.com\.cn', 'src=\"http://img.zjol.com.cn')
            ],
            add_sensitive_str_list=[
                '浙江在线-金华频道\d+月\d+日',
                '请输入图片描述',
                '详见今日浙江日报\d+版',
            ],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_jhyw18q_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('义乌十八腔', '优秀网'),
            ],
            add_sensitive_str_list=[
            ],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_bdqmxsv_article_content(content: str) -> str:
        return content

    @staticmethod
    async def _wash_jhbdsv_article_content(content: str) -> str:
        return content

    @staticmethod
    async def _wash_jhwb_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
            ],
            add_sensitive_str_list=[
                '金华晚报',
                '<div class=\"article-social\">.*</script></div>',
                '<div class=\"article-weixin\">.*?</div>',
                '\d+月\d+日消息',
            ],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_jhrx_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('金华热线', '优秀网'),
                ('浙中在线', '优秀网'),
            ],
            add_sensitive_str_list=[
                # 去除表情包
                r'<img src="http://bbs.0579.cn/images/post/smile/pig/daku.gif">',
                # 去除金华热线二维码
                '<img src=\"images/inapp\.jpg\?id=\\d+\" alt=\"\">',
            ],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_jhgzw_article_content(content: str) -> str:
        if 'livmedia.php' in content:
            # 表示是js的视频文章, 此处pass, 因为这种都只有一个视频且为js
            # 金华广众网较多都是含有js视频文章的会导致较多的发布失败, 所以考虑放到后面去
            raise AssertionError('js视频文章, pass')
        else:
            pass

        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                # 去除无线金华二维码, 都已'TiEL'结尾的图片
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.png\?TiEL\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.png\?YfBN\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.png\?dJAq\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.png\?jJ3h\"', 'src=""'),

                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.[jp][pn]g\?RFZU\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.[jp][pn]g\?9kzt\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.[jp][pn]g\?cIFA\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.[jp][pn]g\?zUBO\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.[jp][pn]g\?bp7w\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.[jp][pn]g\?G4Z\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.[jp][pn]g\?1GOQ\"', 'src=""'),
                ('src=\"http:\/\/imgs.jinhua.com.cn/material/news/img/640x/\d+/\d+/\w+\.[jp][pn]g\?14e\"', 'src=""'),
            ],
            add_sensitive_str_list=[
                '无[线限]金华客户端',
                '金华广众网',
                # 去掉开头的时间点消息
                '\d+月\d+日消息',
            ],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)
        content = modify_body_p_typesetting(content=content)

        return content

    @staticmethod
    async def _wash_dy_article_content(content: str) -> str:
        return content

    @staticmethod
    async def _wash_ky_article_content(content: str) -> str:
        return content

    @staticmethod
    async def _wash_dfsp_article_content(content: str) -> str:
        content = fix_text(text=content)

        return content

    @staticmethod
    async def _wash_kr_article_content(content: str) -> str:
        return content

    @staticmethod
    async def _wash_gxg_article_content(content: str) -> str:
        return content

    @staticmethod
    async def _wash_blbl_article_content(content: str) -> str:
        return content

    @staticmethod
    async def _wash_lfd_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
            ],
            add_sensitive_str_list=[
                # 洗掉二维码
                '<section class=\"show-code\".*?><label>扫描到手机：.*?</section>'
                '<section class=\"post-share\">.*?</section>',
                '<section class=\"post-likes\">.*?</section>'
            ],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_jd_article_content(content: str) -> str:
        # 把查看图片替换成img标签, 下面匹配url较为通用
        _ = '<a target=\"_blank\" href=\"((https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|])\">\[点击查看图片\]</a>'
        look_img_url_list = re.compile(_).findall(content)
        # pprint(look_img_url_list)
        for item in look_img_url_list:
            img_url = item[0]
            # 依次替换, img_url地址存在.html这种不处理
            content = re.compile(_)\
                .sub(repl='<img src=\"{}\">'.format(img_url), string=content, count=1)

        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                # 点赞数字清洗
                ('<div class=\"clearfix\"></div>\d+</div>', '</div>'),
            ],
            add_sensitive_str_list=[
                '<em>本文译自.*?</em>',
                # 打赏
                '<div class=\"shang\"><hr>.*<hr></div>',
                # 赞
                '<span class="zan-text">.*?</span>',
                '<a id=\"jandan-zan-\d+\" class=\"jandan-zan\".*?></a>',
                '<div style=\".*?\" class=\"wechat-hide\">.*?</div>',
                '<div class=\"social-share\" data-disabled=\".*?\"></div>',
                # 洗掉js
                '<script.*?>.*?</script>',
                '<link rel=\"stylesheet\" href=\".*?\">',
                # 洗掉注释
                '<!--.*?-->',
            ],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_bdj_article_content(content: str) -> str:
        if '<img' in content:
            # 有图的文章, 则把文章标题过滤
            content = re.compile('<h1>.*?</h1>').sub('', content)
        else:
            pass
        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_5h_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                # 图片替换
                ('<img src=\"', '<img src=\"http://www.5h.com'),
            ],
            add_sensitive_str_list=[],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_xq_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=None,
            add_sensitive_str_list=[
                '<p>作者：\w+</p>',
                '<p>编辑：\w+</p>',
                '<p><b>作者：\w+</b></p>',
                '<p>来源：.*?</p>',
                '<p><b>免责申明：以上内容仅供参考，不作为买卖依据，据此操作，盈亏自负！</b></p>',
                '<p><a href=\"http://xueqiu\.com/n/今日话题\" target=\"_blank\">@今日话题</a> </p>',
                '<p>原文链接：<a href=\"http.*?\" title=\"http.*?\" target=\"_blank\" class=\"status-link\">网页链接</a></p>',
            ],
            is_default_filter=False,
            is_lower=False,)

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_91mt_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                # 视频详情介绍
                ('<mip-img popup', '<img'),
                ('</mip-img>', '</img>'),
            ],
            add_sensitive_str_list=None,
            is_default_filter=False,
            is_lower=False,)

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_ft_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=None,
            add_sensitive_str_list=[
                '<em>查看全部<i class=\"iconfont icon-xiajiantou\"></i></em>',
            ],
            is_default_filter=False,
            is_lower=False,)

        content = modify_body_img_centering(content=content)

        return content

    async def _wash_qqbb_article_content(self, content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=None,
            add_sensitive_str_list=[
                # 洗掉下一页或上一页
                '<div class=\"detail_page\">.*?</div>',
                # 洗掉推荐
                '<section class=\"hotwrap about-rec-ul dis-bot tab-box\">.*?</section>',
                # 查看更多
                '<div class=\"art-body-fold-\d+\">查看全文</div>',
                # 洗掉视频文章中的额查看更多
                '<div class=\"more\">展开查看全文<img src=\"http.*?\" alt=\"\"></div>',
                # 洗掉脚本
                '<script type=\"text/javascript\" src=\".*?\"></script>',
                '<footer><footer>©2019 QBAOBEI.COM</footer>.*?</footer>',
            ],
            is_default_filter=False,
            is_lower=False,)

        # 把下一页中的div.item-nub em.nub替换成正确的顺序
        em_nub_list_sel = {
            'method': 'css',
            'selector': 'div.item-nub em.nub ::text',
        }
        em_nub_list = await async_parse_field(
            parser=em_nub_list_sel,
            target_obj=content,
            is_first=False,
            # 不打印
            logger=None,)
        # eg: ['1', '2', '3', '4', '1', '2']
        # pprint(em_nub_list)
        index = 1
        replace_str_list = []
        for num in em_nub_list:
            # self.lg.info(num, index)
            replace_str_list.append([
                '<em class=\"nub\">{}</em>'.format(num), '<em class=\"nub\" id=\"fz\">{}</em>'.format(index),
            ])
            index += 1
        # pprint(replace_str_list)
        for item in replace_str_list:
            content = content.replace(item[0], item[1], 1)

        # item 的css
        content = '<style type="text/css">.art-body .item {position: relative;background-color: #fff;border-radius: 5px;border: 1px solid #e9ebed; padding: 10px;margin-top: 10px;overflow: hidden;}</style>'\
            + content if content != '' else content

        ## dl dd ul的css
        content = '<style type="text/css">ul {display: block;list-style-type: disc;margin-block-start: 1em;margin-block-end: 1em;margin-inline-start: 0px;margin-inline-end: 0px;padding-inline-start: 40px;} dl {display: block;margin-block-start: 1em;margin-block-end: 1em;margin-inline-start: 0px;margin-inline-end: 0px;} dd {line-height: 25px;}</style>'\
            + content if content != '' else content

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_7y7_article_content(content: str) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('<p><br></p>', '<br>'),
            ],
            add_sensitive_str_list=[
                # 洗掉下一页或上一页
                '<div class=\"detail_page\">.*?</div>',
                '<div class=\"adver\"></div>',
                # 洗掉推荐
                '<section id=\"related\" class=\"y7-sec y7-sec-3\">.*</div>',
                # 洗掉了解更多
                '<div class=\"box gzh_div\" style=\"display: none\">.*?</div>',
                # 洗掉展开更多
                '<div onclick=\"showfullcontent\(\)\" id=\"show_more\">.*?</div>',
                '<div class=\"befo_fa\"><div class=\"beforead\"></div></div>',
                '<div class=\"relativ\"></div>',
                # 洗掉脚本
                '<script type=\"text/javascript\" src=\".*?\"></script>',
            ],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_mp_article_content(content) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[],
            add_sensitive_str_list=[
                '美拍小助手'
                '美拍',
                'meipai',
                '\#\#',
            ],
            is_default_filter=False,
            is_lower=False, )

        return content

    @staticmethod
    async def _wash_amz_article_content(content) -> str:
        # firefox上正常显示, chrome变形, 后台可以改下iframe的属性, 使其自适应
        return content

    @staticmethod
    async def _wash_lsp_article_content(content) -> str:
        return content

    @staticmethod
    async def _wash_ck_article_content(content) -> str:
        return content

    @staticmethod
    async def _wash_hqx_article_content(content) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('好奇心日报', '优秀网'),
                # figure 里面img src处理
                ('data-format=\"jpeg\" class=\"lazyload\" data-src=', 'data-format=\"jpeg\" class=\"lazyload\" src='),
                # a标签跳转处理
                ('<a href=\".*?\">', '<a href=\"\">'),
            ],
            add_sensitive_str_list=[
                '<p class=\"\"><br></p>',
                '<p>题图来源：<a href=\".*?\" rel=\"nofollow\">pixabay</a></p>',
                '<p>题图来自.*?</p>',
                '<p class=\"\">题图：<a href=\"\">.*?</a>.*?<a href=\"\">.*?</a>  <br></p>',
                '<p>翻译：.*?</p>',
            ],
            is_default_filter=False,
            is_lower=False,)

        content = modify_body_img_centering(content=content)
        content = modify_body_p_typesetting(content=content)

        return content

    @staticmethod
    async def _wash_nfzm_article_content(content) -> str:
        content = re.compile('\n').sub('', content)

        content = modify_body_img_centering(content=content)
        content = modify_body_p_typesetting(content=content)

        return content

    @staticmethod
    async def _wash_hx_article_content(content) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                # 去除图片惰性加载
                ('<img class=\"lazy\" data-original=', '<img class=\"lazy\" src='),
                ('虎嗅网', '优秀网'),
                ('虎嗅', '优秀'),
            ],
            add_sensitive_str_list=[
                # 去除段落空行
                '<p><br></p>',
                '<p></p>',
                '<p class=\"img-center-box\"><br></p>',
                '<p label=\"正文\" class=\"text-normal\"><br></p>',
                # 立场去除
                '<div class=\"neirong-shouquan\">.*?</div>',
                # 引用去除
                '<span class=\"text-remarks\" label=\"备注\">.*?</span>',
                '<span class=\"text-remarks\">.*?</span>',
                # 去除点击展开全文
                '<divclass js-hmt-detection data-detection=\"文章详情页,展开全文,点击\">.*?</divclass>',
                # 去除尾部作者盒子图片
                '<img src=\"https://img.huxiucdn.com/authorCard/\d+.jpg\?\d+\">',
                # 去除不让转载
                '<span style=\".*?\">本文首发于腾讯科技，未经授权，不得转载。</span>',
            ],
            is_default_filter=False,
            is_lower=False,)

        content = modify_body_img_centering(content=content)
        content = modify_body_p_typesetting(content=content)

        return content

    @staticmethod
    async def _wash_pp_article_content(content) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                # 清洗末尾额外补充说明
                ('<div class=\"news_infor_extra\">.*</div> <div class=\"relations_div\">', '<div class="relations_div">'),
                ('澎湃新闻', '优秀网'),
                ('湃客', '秀客'),
            ],
            add_sensitive_str_list=[
                '<strong>“湃客·镜相”栏目首发独家非虚构作品，版权所有，任何媒体或平台不得未经许可转载。</strong>',
                '<a href=\".*?\" target=\"_blank\">阅读原文</a>',
            ],
            is_default_filter=False,
            is_lower=False,)

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_jm_article_content(content) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('界面新闻', '优秀网'),
            ],
            add_sensitive_str_list=[
                # 洗掉末尾广告
                '<div id=\"ad_content\">.*?</div>',
                '<div class=\"article-source\">.*?</div>',
                # 洗掉图片来源
                '<span>图片来源：.*?</span>',
                '<p>图片来源：.*?</p>',
                '<figcaption>图片来源：.*?</figcaption>',
                # 洗掉摄影
                '<span>摄影：.*?</span>',
                # 洗掉记者
                '<p>记者 \| .*?</p>',
                # 洗掉撰文
                '<p>撰文 \| .*?</p>',
            ],
            is_default_filter=False,
            is_lower=False,)

        content = modify_body_img_centering(content=content)
        content = modify_body_p_typesetting(content=content)

        return content

    @staticmethod
    async def _wash_ss_article_content(content) -> str:
        # 洗掉本文禁止商业转载
        content = re.compile('<blockquote>.*?</blockquote>').sub('', content)
        content = re.compile('<strong>为您推荐</strong>').sub('', content)
        # 洗掉推荐文章
        content = re.compile('<div class=\"my-related-posts-box\".*?>.*?</div>').sub('', content)
        # 洗掉图片来源
        content = re.compile('<p class=\"wp-caption-text\">图片来源：.*?</p>').sub('', content)
        # 把img标签原先的固定大小置空
        content = re.compile('width=\"\d+\" height=\"\d+\" class=\"size-large wp-image-')\
            .sub('class=\"size-large wp-image-', content)
        # 并且把img src的url, 改成非固定大小(测试发现没用, pass)
        # content = re.compile('-\d+x\d+\.jpg')\
        #     .sub('.jpg', content)
        # 洗掉分享标签
        content = re.compile('<div class=\"bshare-custom icon-medium\">.*?</div>')\
            .sub('', content)

        content = modify_body_img_centering(content=content,)

        return content

    @staticmethod
    async def _wash_if_article_content(content) -> str:
        # 避免a标签调转
        content = re.compile('<a href=\".*?\">').sub('<a href=\"\">', content)
        content = modify_body_img_centering(content=content)
        content = modify_body_p_typesetting(content=content)

        return content

    @staticmethod
    async def _wash_cn_article_content(content) -> str:
        content = re.compile('<mip-img').sub('<img', content)
        content = re.compile('</mip-img>').sub('</img>', content)
        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_ys_article_content(content) -> str:
        """
        51健康养生网
        :param content:
        :return:
        """
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('alt=\".*?\" src=\"\/\/', 'alt=\"\" src=\"http://'),
            ],
            add_sensitive_str_list=[],
            is_default_filter=False,
            is_lower=False,)
        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_fh_article_content(content) -> str:
        content = re.compile('凤凰网汽车讯').sub('', content)
        # TODO chrome 显示content时会带上手机默认客户端的css样式, 导致显示异常, 用firefox查看是正常的!!
        content = modify_body_img_centering(content=content)
        content = modify_body_p_typesetting(content=content)

        return content

    @staticmethod
    async def _wash_zq_article_content(content) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('<img data-src=', '<img src='),
                ('data-width=\"\d+\" data-height=\"\d+\" data-src=', 'src='),
            ],
            add_sensitive_str_list=[
                '<br>',
            ],
            is_default_filter=False,
            is_lower=False, )

        if '<video' in content:
            print('zq 不允许发布图文详情中, 带有视频的')
            return ''

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_bd_article_content(content) -> str:
        # TODO firefox正常显示, 但是chrome无图, 原因图片地址无响应!
        # 顶部空白替换
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('<div style=\"padding-top:\d+\.\d+%\">', '<div>'),
                ('<div style=\"padding-top:\d+%\">', '<div>'),
                ('&amp;', '&'),
            ],
            add_sensitive_str_list=[],
            is_default_filter=False,
            is_lower=False, )

        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_sg_article_content(content) -> str:
        content = modify_body_img_centering(content=content)

        return content

    @staticmethod
    async def _wash_df_article_content(content) -> str:
        content = re.compile('<p class=\"section txt\">对此你怎么看，欢迎大家在评论区留言！</p>').sub('', content)

        return content

    @staticmethod
    async def _wash_wx_article_content(content: str) -> str:
        # print(content)
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                ('<p><br></p>', '<br>'),
            ],
            add_sensitive_str_list=[
                # 洗掉编辑, 校对
                '<span style=\"max-width: 100%;.*?\">编辑：.*?</span>',
                '<span style=\"max-width: 100%;.*?\">校对：.*?</span>',
                # 空行
                '<p><span style=\"color: rgb\(217, 33, 66\);font-size: 14px;\"><strong><br></strong></span></p>',
                # 空行过多, 洗掉
                '<br>',
                # 最下方a标签: 洗掉往期回顾 or 推荐内容
                '<p style=\".*?\"><a href=\".*?mp.weixin.qq.com/s.*?\" target=\"_blank\" data-itemshowtype=\"0\" data-linktype=\"2\".*?>.*?</a>.*?</p>',

                # todo section容易错洗, 导致正常内容无法显示, 不处理
                # '<section .*? data-tools=\"新媒体排版\".*?>.*?</section>',
            ],
            is_default_filter=False,
            is_lower=False,)

        return content

    @staticmethod
    async def _wash_kd_article_content(content) -> str:
        content = wash_sensitive_info(
            data=content,
            replace_str_list=[
                # 替换掉img 标签中src为svg的
                (' src=\"data:image/svg\+xml;.*?\" ', ' '),
                # 处理图片
                (' data-src=', ' src='),
                ('data-lazy=\"\d+\"', 'style=\"height:auto;width:100%;\"'),
            ],
            add_sensitive_str_list=[
                '<svg .*?>.*?</svg>',
                '<a class=\"jubao\"><i></i>举报内容</a>',
            ],
            is_default_filter=False,
            is_lower=False,)

        # 给与原装的css
        content = '<link rel="stylesheet" href="//mp.gtimg.cn/themes/default/client/article/article.css?_bid=2321&v=2017082501">' + \
            content if content != '' else ''

        return content

    @staticmethod
    async def _wash_kb_article_content(content) -> str:
        # 给与原生的css
        content = r'<link href="//mat1.gtimg.com/www/cssn/newsapp/cyshare/cyshare_20181121.css" type="text/css" rel="stylesheet">' + \
            content if content != '' else content
        content = modify_body_img_centering(content=content)
        content = modify_body_p_typesetting(content=content)

        return content

    async def is_child_can_debug(self, article_url) -> bool:
        """
        判断是否是子对象, 以及是否debug是打开
        :return:
        """
        if 'www.iesdouyin.com' in article_url:
            # 单独处理抖音排行榜的视频地址
            return True

        for item in ARTICLE_ITEM_LIST:
            item_debug = item.get('debug', False)
            if item.get('short_name', '') == 'df':
                if 'mini.eastday.com' in article_url:
                    if item_debug:
                        return True

            elif item.get('short_name', '') == 'bd':
                if 'mbd.baidu.com' in article_url\
                        or 'sv.baidu.com' in article_url:
                    if item_debug:
                        return True
                else:
                    if item.get('obj_origin', '') in article_url:
                        if item_debug:
                            return True

            elif item.get('short_name', '') == 'fh':
                if await self._in_fh_two_level_domain_name(article_url):
                    if item_debug:
                        return True
                else:
                    if item.get('obj_origin', '') in article_url:
                        if item_debug:
                            return True

            else:
                if item.get('obj_origin', '') in article_url:
                    if item_debug:
                        return True

        return False

    async def _in_fh_two_level_domain_name(self, article_url) -> bool:
        """
        是否在可抓取的fh 的二级域名里
        :param article_url:
        :return:
        """
        if 'news.ifeng.com' in article_url\
                or 'feng.ifeng.com' in article_url\
                or 'finance.ifeng.com' in article_url\
                or 'ent.ifeng.com' in article_url\
                or 'sports.ifeng.com' in article_url\
                or 'fashion.ifeng.com' in article_url\
                or 'auto.ifeng.com' in article_url\
                or 'tech.ifeng.com' in article_url\
                or 'culture.ifeng.com' in article_url\
                or 'history.ifeng.com' in article_url\
                or 'mil.ifeng.com' in article_url\
                or 'travel.ifeng.com' in article_url\
                or 'fo.ifeng.com' in article_url\
                or 'health.ifeng.com' in article_url\
                or 'guoxue.ifeng.com' in article_url\
                or 'v.ifeng.com' in article_url:
            return True

        else:
            return False

    async def _get_site_id(self, article_url_type) -> int:
        """
        获取文章的site_id
        :return:
        """
        # 肯定在里面, 否则无法走到这一步
        return self.obj_origin_dict.get(article_url_type, {}).get('site_id', '')

    async def _judge_url_type(self, article_url) -> str:
        """
        判断url类别
        :return:
        """
        if 'www.iesdouyin.com' in article_url:
            # 单独处理抖音排行榜的视频
            return 'dy'

        # 提前处理并返回的, 避免二级域名冲突
        for key, value in self.obj_origin_dict.items():
            if key == 'jhbdsv':
                # todo jhbdsv文章的地址也是'sv.baidu.com'与下方百度m站部分地址冲突, 此处直接在其前面进行处理
                if 'sv.baidu.com' in article_url:
                    return key
            else:
                pass

        for key, value in self.obj_origin_dict.items():
            if key == 'df':
                if 'mini.eastday.com' in article_url:
                    return key

            elif key == 'bd':
                if 'mbd.baidu.com' in article_url\
                        or 'sv.baidu.com' in article_url:
                    return key

                else:
                    if value.get('obj_origin') in article_url:
                        return key

            elif key == 'fh':
                if await self._in_fh_two_level_domain_name(article_url):
                    return key

            else:
                if value.get('obj_origin',) in article_url:
                    return key

        raise ValueError('未知的文章url!')

    def __del__(self):
        try:
            del self.lg
            del self.user_agent_type
            del self.ip_pool_type
            del self.request_num_retries
            del self.hook_target_api_data
            del self.concurrency
        except:
            pass
        try:
            del self.loop
        except:
            pass
        try:
            self.obj_origin_dict
        except:
            pass
        collect()

def modify_body_img_centering(content: str,) -> str:
    """
    修改body图片居中
    :param content:
    :return:
    """
    # 图片居中, 放前后作用一样, img里面的实际值还是会被加载, 故统一放最前面
    content = '<style type="text/css">img {visibility: visible !important;height: auto !important;width: 100% !important;}</style>' + \
              content if content != '' else ''

    return content

def modify_body_p_typesetting(content: str) -> str:
    """
    修改body p标签的排版
    :param content:
    :return:
    """
    # p标签文字修饰(自己添加, 目的: 让其自适应phone端, 添加在后端以覆盖原有p标签属性)
    content = '<style type="text/css">p {width: 100%; height: auto; word-wrap:break-word; word-break:break-all; overflow: hidden;}</style>' + \
              content if content != '' else ''

    return content

def main():
    _ = ArticleParser()
    loop = get_event_loop()
    # wx公众号
    # 存在链接过期的情况
    # https://mp.weixin.qq.com/s?__biz=MzA4MjQxNjQzMA==&mid=2768396229&idx=1&sn=&scene=0#wechat_redirect
    # url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1542166201&ver=1243&signature=qYsoi7Sn3*tmw9x-lXxo6sJfSYDGGyHewzZyJCjgovA8taCXuTtENN7X2d4dPnOz1TvEnO2LsYJR1W3IwozcIzLyfhcdcZgOoqyzPLhz469ssieB15ojFrdtA2y83*As&new=1'
    # url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1564036201&ver=1749&signature=XCTMLVFytVL3FzjyURHVRICZb2bM1kLWhSpUrNeb8SGD1jvxgHkJgicFiMNBOl6W0Ow6m*Gzke*tlPVCzOJTcDx4WYv2FyOsY1FtMzB-pHIOErSsuq4H3T-yUeyMq9vg&new=1'
    # url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1565314201&ver=1779&signature=3RxHcLiybXKqNJH95V5UekL6udEBs6tZFNnqPKCxEbXHOWcnQ2djUfXBA1hrMOerxiKAIKVyvPOYW9Frj-rwmPDpnzZE8WuiSZWZCFhIoLUKVRHD5AfsH90C1vupHvUH&new=1'
    url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1568689203&ver=1857&signature=2ABS59Q9ciRvm27MYTS694lYxq1qsyp1KUJ9AU6oqFREk8-en2OeSbE9jLKFGwGSHIj*C9CmVeJxD6ImtYgs18bluEISV8o2rEZM-WUzwWTYCcdF*mSyQeAmleT4lwOz&new=1'
    # 含视频
    # url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1563850802&ver=1745&signature=kF7BFCtTqr9OlfBzqLSgUfnD413Ig9JfMVKCc1ew8YQ8maPdhL8zFXgrctDdl5Z3HfI0ZOb7yThhKR1QHrtuUjVQE*gTTPBvBOTagAA5wN*bylpMTtwBqwv7ctFh-j5P&new=1'
    # url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1567476001&ver=1829&signature=WRtVmIbd-R3jJmAMe4ILMN2C12-Yd7QRJhZbZLLle7NmAyLSLTooaJqQPjtb0WHH288LVqanz2vvl0wmIpVNyL-iG5zNwGDsl4oZt4lXXZGXNv7*aQ7sy8ZgyS7l0kTU&new=1'

    # 今日头条(视频切入到content中了)    [https://www.toutiao.com/]
    # url = 'https://www.toutiao.com/a6623290873448759815/'
    # url = 'https://www.toutiao.com/a6623125148088140291/'
    # url = 'https://www.toutiao.com/a6694437682031886852/'
    # url = 'https://www.toutiao.com/a6707502560892158468/'
    # url = 'https://www.toutiao.com/a6714969589630894605/'
    # url = 'https://www.toutiao.com/a6716696808971567630/'
    # url = 'https://www.toutiao.com/a6716489299614761484/'
    # 问答不采集
    # url = 'https://www.toutiao.com/a6661496988099412238/'
    # 含视频
    # url = 'https://www.toutiao.com/a6623325882381500931/'

    # 简书
    # url = 'https://www.jianshu.com/p/ec1e9f6129bd'
    # url = 'https://www.jianshu.com/p/a02313dd3875'
    # url = 'https://www.jianshu.com/p/1a60bdc3098b'
    # url = 'https://www.jianshu.com/p/2876ca9e3ae7'
    # url = 'https://www.jianshu.com/p/9ba3eb7bc524'
    # url = 'https://www.jianshu.com/p/675bf3a17d54'
    # url = 'https://www.jianshu.com/p/dceebde3caf8'

    # QQ看点
    # url = 'https://post.mp.qq.com/kan/article/2184322959-232584629.html?_wv=2147483777&sig=24532a42429f095b9487a2754e6c6f95&article_id=232584629&time=1542933534&_pflag=1&x5PreFetch=1&web_ch_id=0&s_id=gnelfa_3uh3g5&share_source=0'
    # url = 'https://post.mp.qq.com/kan/article/3082663893-394335551.html?sig=8807b10464215f5eac164824c23729c1&article_id=394335551&_pflag=1&_wv=2147483777&x5PreFetch=1&time=1558074607'
    # url = 'https://post.mp.qq.com/kan/article/1001000209370-558421494.html?sig=cce26570d9dd6093f0416112420b6c07&article_id=558421494&_pflag=1&_wv=2147483777&x5PreFetch=1&time=1565108260'
    # url = 'https://post.mp.qq.com/kan/article/3341167918-561135106.html?_wv=2147483777&sig=2005d9c1366770c1de75f447d143f9a6&article_id=561135106&time=1565237253&_pflag=1&x5PreFetch=1&web_ch_id=0&sourcefrom=6'
    # todo 含视频(本地可以, server也可以)
    #  server失败[原因原先以为是selenium版本 在linux中与firefox和geckodriver不兼容导致启动geckodriver失败, 即使firefox和geckodriver皆为最新版本])
    #  后来发现是headless=True导致无法启动驱动
    # geckodriver download_url: https://github.com/mozilla/geckodriver/releases
    # url = 'http://post.mp.qq.com/kan/video/201271541-2525bea9bc8295ah-x07913jkmml.html?_wv=2281701505&sig=50b27393b64a188ffe7f646092dbb04f&time=1542102407&iid=Mjc3Mzg2MDk1OQ==&sourcefrom=0'
    # url = 'http://post.mp.qq.com/kan/video/200553568-1375d3f1b48697ah-j0906gh4g62.html?_wv=2281701505&sig=e1dfb38fc2d5eaa0fd4400b05c94d17c&time=1564417414&iid=Mjc3Mzg2MDk1OQ==&sourcefrom=6'

    # 天天快报
    # url = 'https://kuaibao.qq.com/s/NEW2018120200710400?refer=kb_news&titleFlag=2&omgid=78610c582f61e3b1f414134f9d4fa0ce'
    # url = 'https://kuaibao.qq.com/s/20181201A0VJE800?refer=kb_news&titleFlag=2&omgid=78610c582f61e3b1f414134f9d4fa0ce'
    # url = 'https://kuaibao.qq.com/s/20190515A06XAW00?refer=kb_news&coral_uin=ec30afdb64e74038ca7991e4e282153af308670081f17d0ee4fc3e473b0b5dda2f&omgid=22c4ac23307a6a33267184cafd2df8b6&chlid=news_news_top&atype=0&from=groupmessage&isappinstalled=0'
    # url = 'https://kuaibao.qq.com/s/20190908AZPIWP00?refer=kb_news&amp;titleFlag=2&amp;coral_uin=ec2fef55983f2b0f322a43dc540c8dda94190bf70c60ca0d998400a23f576204fb&amp;omgid=7a157262f3d303c6f2d089446406d22e&from=groupmessage&isappinstalled=0'
    # 第二类图文文章
    # url = 'https://kuaibao.qq.com/s/20190710AZOJ0B00?from=groupmessage&isappinstalled=0'
    # 第三类图文文章(跟第二类是同一接口但是字段不同)
    # url = 'https://kuaibao.qq.com/s/20190708A0INL100?refer=kb_news&amp;coral_uin=ec30afdb64e74038ca7991e4e282153af308670081f17d0ee4fc3e473b0b5dda2f&amp;omgid=22c4ac23307a6a33267184cafd2df8b6&amp;chlid=daily_timeline&amp;atype=0&from=groupmessage&isappinstalled=0'
    # url = 'https://kuaibao.qq.com/s/20190721A0JCZT00?refer=kb_news&amp;coral_uin=ec30afdb64e74038ca7991e4e282153af308670081f17d0ee4fc3e473b0b5dda2f&amp;omgid=22c4ac23307a6a33267184cafd2df8b6&amp;chlid=daily_timeline&amp;atype=0&from=groupmessage&isappinstalled=0'
    # url = 'https://kuaibao.qq.com/s/20190723A0IRBX00?refer=kb_news&amp;titleFlag=2&amp;coral_uin=ec30afdb64e74038ca7991e4e282153af308670081f17d0ee4fc3e473b0b5dda2f&amp;omgid=22c4ac23307a6a33267184cafd2df8b6&from=groupmessage&isappinstalled=0'
    # TODO 含视频(本地可以，server也成功[firefox失败, 用的chrome]) [有一定失败率多尝试]
    # url = 'https://kuaibao.qq.com/s/20180906V1A30P00?refer=kb_news&titleFlag=2&omgid=78610c582f61e3b1f414134f9d4fa0ce'
    # url = 'https://kuaibao.qq.com/s/20191028V044PD00?refer=kb_news&amp;omgid=7a157262f3d303c6f2d089446406d22e&amp;chlid=daily_timeline&amp;atype=4&from=groupmessage&isappinstalled=0'
    # 第一种类型
    # url = 'https://kuaibao.qq.com/s/20190322V0DCSY00?refer=kb_news&amp;coral_uin=ec2fef55983f2b0f322a43dc540c8dda94190bf70c60ca0d998400a23f576204fb&amp;omgid=7a157262f3d303c6f2d089446406d22e&amp;chlid=daily_timeline&amp;atype=4&from=groupmessage&isappinstalled=0'
    # 第二种类型
    # url = 'https://kuaibao.qq.com/s/20190221V170RM00?refer=kb_news&amp;titleFlag=2&amp;coral_uin=ec2fef55983f2b0f322a43dc540c8dda94190bf70c60ca0d998400a23f576204fb&amp;omgid=7a157262f3d303c6f2d089446406d22e&from=groupmessage&isappinstalled=0'
    # url = 'https://kuaibao.qq.com/s/20190505V0FMTX00?refer=kb_news&amp;titleFlag=2&amp;coral_uin=ec2fef55983f2b0f322a43dc540c8dda94190bf70c60ca0d998400a23f576204fb&amp;omgid=7a157262f3d303c6f2d089446406d22e&from=groupmessage&isappinstalled=0'
    # url = 'https://kuaibao.qq.com/s/20190509V0JOTG00?refer=kb_news&amp;titleFlag=2&amp;coral_uin=ec2fef55983f2b0f322a43dc540c8dda94190bf70c60ca0d998400a23f576204fb&amp;omgid=7a157262f3d303c6f2d089446406d22e&from=groupmessage&isappinstalled=0'
    # url = 'https://kuaibao.qq.com/s/20190328V0E9OX00?refer=kb_news&amp;titleFlag=2&amp;omgid=7a157262f3d303c6f2d089446406d22e&amp;coral_uin=ec2fef55983f2b0f322a43dc540c8dda94190bf70c60ca0d998400a23f576204fb&from=groupmessage&isappinstalled=0'
    # url = 'https://kuaibao.qq.com/s/20191016V04YLD00?refer=kb_news&amp;titleFlag=2&amp;coral_uin=ec2fef55983f2b0f322a43dc540c8dda94190bf70c60ca0d998400a23f576204fb&amp;omgid=7a157262f3d303c6f2d089446406d22e&from=groupmessage&isappinstalled=0'

    # 东方头条新闻
    # url = 'https://mini.eastday.com/mobile/190505214138491.html?qid=null&idx=1&recommendtype=crb_a579c9a168dd382c_1_1_0_&ishot=1&fr=toutiao&pgnum=1&suptop=0'
    # url = 'https://mini.eastday.com/mobile/190507061239214.html?qid=null&idx=2&recommendtype=-1_a579c9a168dd382c_1_2_0_&ishot=1&fr=toutiao&pgnum=1&suptop=0001'
    # 含视频
    # url = 'https://mini.eastday.com/video/vgaoxiao/20190506/190506045241686142077.html?qid=null&idx=6&recommendtype=-1_a579c9a168dd382c_1_6_0_&ishot=1&fr=toutiao&pgnum=1&suptop=0'
    # url = 'https://mini.eastday.com/video/vgaoxiao/20190425/190425154440387159259.html?qid=null&idx=2&fr=https://mini.eastday.com/video/vgaoxiao/20190506/190506045241686142077.html&ishot=0&recommendtype=vs'

    # 搜狗新闻资讯
    # url = 'https://sa.sogou.com/sgsearch/sgs_tc_news.php?req=gNWjMh9kjpEtYgjReTdUXZS0Q2CO6DjsS87Col9-QZE=&user_type=wappage'
    # url = 'https://sa.sogou.com/sgsearch/sgs_tc_news.php?req=xtgTQEURkeIQnw4p57aSHd9gihe6nAvIBk6JzKMSwdJ_9aBUCJivLpPO9-B-sc3i&user_type=wappage'
    # url = 'https://sa.sogou.com/sgsearch/sgs_tc_news.php?req=SKbJyHwsObNfXcwSUF_VoWrnmpkThJtfiHZ54FsQFNk=&user_type=wappage'
    # url = 'https://sa.sogou.com/sgsearch/sgs_tc_news.php?req=35zB-k94kWvc1SfKHhqXM1_UEnQCOA83_2msaXw6lPs=&user_type=wappage'
    # 含视频
    # url = 'http://sa.sogou.com/sgsearch/sgs_video.php?mat=11&docid=sf_307868465556099072&vl=http%3A%2F%2Fsofa.resource.shida.sogoucdn.com%2F114ecd2b-b876-46a1-a817-e3af5a4728ca2_1_0.mp4'
    # url = 'http://sa.sogou.com/sgsearch/sgs_video.php?mat=11&docid=286635193e7a63a24629a1956b3dde76&vl=http%3A%2F%2Fresource.yaokan.sogoucdn.com%2Fvideodown%2F4506%2F557%2Fd55cd7caceb1e60a11c8d3fff71f3c45.mp4'
    # url = 'http://sa.sogou.com/sgsearch/sgs_video.php?mat=11&docid=open_doc_prod6562107&vl=http%3A%2F%2F1400094915.vod2.myqcloud.com%2F3df4ea08vodtransgzp1400094915%2Feb5e8f815285890789528268277%2Fv.f20.mp4'

    # 百度m站
    # url = 'https://mbd.baidu.com/newspage/data/landingpage?s_type=news&dsp=wise&context=%7B%22nid%22%3A%22news_9512351987809643964%22%7D&pageType=1&n_type=1&p_from=-1'
    # url = 'https://mbd.baidu.com/newspage/data/landingpage?s_type=news&dsp=wise&context=%7B%22nid%22%3A%22news_9423330273641956666%22%7D&pageType=1&n_type=1&p_from=-1'
    # url = 'https://mbd.baidu.com/newspage/data/landingshare?context=%7B%22nid%22%3A%22news_8934756170017529467%22%2C%22ssid%22%3A%22%22%7D&pageType=1'
    # url = 'https://m.baidu.com/#iact=wiseindex%2Ftabs%2Fnews%2Factivity%2Fnewsdetail%3D%257B%2522linkData%2522%253A%257B%2522name%2522%253A%2522iframe%252Fmib-iframe%2522%252C%2522id%2522%253A%2522feed%2522%252C%2522index%2522%253A0%252C%2522url%2522%253A%2522https%253A%252F%252Fmbd.baidu.com%252Fnewspage%252Fdata%252Flandingpage%253Fs_type%253Dnews%2526dsp%253Dwise%2526context%253D%25257B%252522nid%252522%25253A%252522news_8934756170017529467%252522%25257D%2526pageType%253D1%2526n_type%253D1%2526p_from%253D-1%2526innerIframe%253D1%2522%252C%2522isThird%2522%253Afalse%252C%2522title%2522%253Anull%257D%257D'
    # url = 'https://m.baidu.com/#iact=wiseindex%2Ftabs%2Fnews%2Factivity%2Fnewsdetail%3D%257B%2522linkData%2522%253A%257B%2522name%2522%253A%2522iframe%252Fmib-iframe%2522%252C%2522id%2522%253A%2522feed%2522%252C%2522index%2522%253A0%252C%2522url%2522%253A%2522https%253A%252F%252Fmbd.baidu.com%252Fnewspage%252Fdata%252Flandingpage%253Fs_type%253Dnews%2526dsp%253Dwise%2526context%253D%25257B%252522nid%252522%25253A%252522news_9292806054300264081%252522%25257D%2526pageType%253D1%2526n_type%253D1%2526p_from%253D-1%2526innerIframe%253D1%2522%252C%2522isThird%2522%253Afalse%252C%2522title%2522%253Anull%257D%257D'
    # url = 'https://m.baidu.com/#iact=wiseindex%2Ftabs%2Fnews%2Factivity%2Fnewsdetail%3D%257B%2522linkData%2522%253A%257B%2522name%2522%253A%2522iframe%252Fmib-iframe%2522%252C%2522id%2522%253A%2522feed%2522%252C%2522index%2522%253A0%252C%2522url%2522%253A%2522https%253A%252F%252Fmbd.baidu.com%252Fnewspage%252Fdata%252Flandingpage%253Fs_type%253Dnews%2526dsp%253Dwise%2526context%253D%25257B%252522nid%252522%25253A%252522news_10217781133566637087%252522%25257D%2526pageType%253D1%2526n_type%253D1%2526p_from%253D-1%2526innerIframe%253D1%2522%252C%2522isThird%2522%253Afalse%252C%2522title%2522%253Anull%257D%257D'
    # url = 'https://m.baidu.com/#iact=wiseindex%2Ftabs%2Fnews%2Factivity%2Fnewsdetail%3D%257B%2522linkData%2522%253A%257B%2522name%2522%253A%2522iframe%252Fmib-iframe%2522%252C%2522id%2522%253A%2522feed%2522%252C%2522index%2522%253A0%252C%2522url%2522%253A%2522https%253A%252F%252Fmbd.baidu.com%252Fnewspage%252Fdata%252Flandingpage%253Fs_type%253Dnews%2526dsp%253Dwise%2526context%253D%25257B%252522nid%252522%25253A%252522news_9575607690617582637%252522%25257D%2526pageType%253D1%2526n_type%253D1%2526p_from%253D-1%2526innerIframe%253D1%2522%252C%2522title%2522%253Anull%257D%257D'
    # 含视频(好看视频)
    # url = 'https://m.baidu.com/#iact=wiseindex%2Ftabs%2Fnews%2Factivity%2Fnewsdetail%3D%257B%2522linkData%2522%253A%257B%2522name%2522%253A%2522iframe%252Fmib-iframe%2522%252C%2522id%2522%253A%2522feed%2522%252C%2522index%2522%253A0%252C%2522url%2522%253A%2522https%253A%252F%252Fhaokan.baidu.com%252Fvideoui%252Fpage%252Fsearchresult%253Fpd%253Dwise%2526vid%253D15928130604529794109%2526is_invoke%253D1%2526innerIframe%253D1%2522%252C%2522isThird%2522%253Afalse%252C%2522title%2522%253Anull%257D%257D'
    # url = 'https://m.baidu.com/#iact=wiseindex%2Ftabs%2Fnews%2Factivity%2Fnewsdetail%3D%257B%2522linkData%2522%253A%257B%2522name%2522%253A%2522iframe%252Fmib-iframe%2522%252C%2522id%2522%253A%2522feed%2522%252C%2522index%2522%253A0%252C%2522url%2522%253A%2522https%253A%252F%252Fhaokan.baidu.com%252Fvideoui%252Fpage%252Fsearchresult%253Fpd%253Dwise%2526vid%253D12574625425386503733%2526is_invoke%253D1%2526innerIframe%253D1%2522%252C%2522isThird%2522%253Afalse%252C%2522title%2522%253Anull%257D%257D'
    # url = 'https://m.baidu.com/#iact=wiseindex%2Ftabs%2Fnews%2Factivity%2Fnewsdetail%3D%257B%2522linkData%2522%253A%257B%2522name%2522%253A%2522iframe%252Fmib-iframe%2522%252C%2522id%2522%253A%2522feed%2522%252C%2522index%2522%253A0%252C%2522url%2522%253A%2522https%253A%252F%252Fhaokan.baidu.com%252Fvideoui%252Fpage%252Fsearchresult%253Fpd%253Dwise%2526vid%253D5077289958594474520%2526is_invoke%253D1%2526innerIframe%253D1%2522%252C%2522isThird%2522%253Afalse%252C%2522title%2522%253Anull%257D%257D'
    # url = 'https://m.baidu.com/#iact=wiseindex%2Ftabs%2Fnews%2Factivity%2Fnewsdetail%3D%257B%2522linkData%2522%253A%257B%2522name%2522%253A%2522iframe%252Fmib-iframe%2522%252C%2522id%2522%253A%2522feed%2522%252C%2522index%2522%253A0%252C%2522url%2522%253A%2522https%253A%252F%252Fhaokan.baidu.com%252Fvideoui%252Fpage%252Fsearchresult%253Fpd%253Dwise%2526vid%253D8197562812859491736%2526innerIframe%253D1%2522%252C%2522isThird%2522%253Afalse%252C%2522title%2522%253Anull%257D%257D'
    # 推荐栏上边点击视频进入的tab, 所得的到视频地址
    # url = 'https://sv.baidu.com/videoui/page/videoland?context=%7B%22nid%22%3A%22sv_7865563634675285012%22%7D&pd=feedtab_h5&pagepdSid='
    # url = 'https://sv.baidu.com/videoui/page/videoland?context=%7B%22nid%22%3A%22sv_2051009680729321124%22%7D&pd=feedtab_h5&pagepdSid='

    # 中青看点(左上角点击全部进行文章类型选择, 因为其只显示前2页, 下滑点击加载更多, 会被跳转到https://cpu.baidu.com, 只需要回退页面直接返回)
    # url = 'https://focus.youth.cn/mobile/detail/id/15547200#'
    # url = 'https://focus.youth.cn/mobile/detail/id/15561509#'
    # url = 'https://focus.youth.cn/mobile/detail/id/17240154#'
    # url = 'https://focus.youth.cn/mobile/detail?id=17197839#'
    # 带有视频的不允许发布
    # url = 'https://focus.youth.cn/mobile/detail/id/21760591#'

    # 阳光宽频网(短视频)
    # 旧版
    # url = 'https://www.365yg.com/a6693050837997978126/#mid=1568175129542657'
    # url = 'https://www.365yg.com/a6689279176827994638/#mid=1607129585526787'
    # 新版(即西瓜视频)
    # url = 'https://www.ixigua.com/i6711509850636943876/'

    # 西瓜视频(短视频)
    # url = 'https://www.ixigua.com/i6711509850636943876/'
    # url = 'https://www.ixigua.com/i6693050837997978126/#mid=1568175129542657'
    # url = 'https://www.ixigua.com/i6689557180368028173/'
    # url = 'https://www.ixigua.com/i6623552886510977540/'

    # 凤凰网
    # 资讯
    # url = 'https://news.ifeng.com/c/7nDvcZ4NtW1'
    # url = 'https://news.ifeng.com/c/7nEJ63GSOWW'
    # url = 'https://news.ifeng.com/c/7nEFqgSjZiq'
    # url = 'https://news.ifeng.com/c/7nE9cR3x2VH'
    # url = 'https://news.ifeng.com/c/7pdYc1BqNgY'
    # url = 'https://news.ifeng.com/c/7q1JRd1MzcO'
    # 大风号
    # url = 'https://feng.ifeng.com/c/7nE6wahrgJg'
    # url = 'https://feng.ifeng.com/c/7nE8Gmm6iR4'
    # 财经
    # url = 'http://finance.ifeng.com/c/7nEMfALohyC'
    # 娱乐
    # url = 'https://ent.ifeng.com/c/7nESdTWykLm'
    # url = 'https://ent.ifeng.com/c/7nDvPWE79UF'
    # 体育
    # url = 'https://sports.ifeng.com/c/7nDzc9Lrspg'
    # 时尚
    # url = 'https://fashion.ifeng.com/c/7nDykbExSVc'
    # url = 'https://fashion.ifeng.com/c/7nDxh4ZgED2'
    # url = 'https://fashion.ifeng.com/c/7q0a30KckYy'
    # 汽车
    # url = 'https://auto.ifeng.com/c/7nE86ZB9Y3s'
    # url = 'https://auto.ifeng.com/c/7nEFmnQAbiK'
    # TODO 房产未实现, 页面结构完全不同
    # 科技
    # url= 'https://tech.ifeng.com/c/7nE6KwElcwq'
    # 文化
    # url = 'http://culture.ifeng.com/c/7nDOfYV9Ma2'
    # 历史
    # url = 'https://history.ifeng.com/c/7n9wJLKFkKx'
    # 军事
    # url = 'https://mil.ifeng.com/c/7nD84weEtS9'
    # 旅游
    # url = 'https://travel.ifeng.com/c/7nDM9G2yG5A'
    # 佛教
    # url = 'https://fo.ifeng.com/c/7nE4JqoNnIu'
    # url = 'https://fo.ifeng.com/c/7nCq7vTkOjj'
    # 健康
    # url = 'https://health.ifeng.com/c/7n7k5Gc95yC'
    # url = 'https://health.ifeng.com/c/7nD69v4BFqk'
    # TODO 家居未实现, 页面结构非文章格式, 全是图片
    # 国学
    # url = 'https://guoxue.ifeng.com/c/7nCOLefbTeq'
    # 视频
    # url = 'https://v.ifeng.com/c/7n9OP680pzt'
    # url = 'https://v.ifeng.com/c/7msqjIm1dUe'
    # url = 'https://v.ifeng.com/c/7nEV3crGcwC'
    # url = 'https://v.ifeng.com/c/7nE1XJY8fL6'

    # 51健康养生网
    # url = 'http://www.51jkst.com/article/275371/index.html'
    # url = 'http://www.51jkst.com/article/275373/index.html'
    # url = 'http://www.51jkst.com/article/252943/index.html'
    # url = 'http://www.51jkst.com/article/275308/index.html'

    # 彩牛养生网(权威医生解说的短视频)
    # 视频
    # url = 'http://m.cnys.com/yiliao/1784.html'
    # url = 'http://m.cnys.com/yiliao/1783.html'
    # url = 'http://m.cnys.com/yiliao/1376.html'
    # url = 'http://m.cnys.com/yiliao/1202.html'
    # 文章
    # url = 'http://m.cnys.com/yangshengzixun/2178.html'
    # url = 'http://m.cnys.com/yangshengzixun/2167.html'
    # url = 'http://m.cnys.com/yangshengzixun/2157.html'
    # url = 'http://m.cnys.com/yangshengzixun/2158.html'

    # 爱范儿
    # url = 'https://www.ifanr.com/1226698'
    # url = 'https://www.ifanr.com/1226793'
    # 生活
    # url = 'https://www.ifanr.com/1226718'
    # 早报
    # url = 'https://www.ifanr.com/1227727'
    # 公司(行业)
    # url = 'https://www.ifanr.com/1227626'
    # 评测
    # url = 'https://www.ifanr.com/1227452'
    # 董车会
    # url = 'https://www.ifanr.com/1227475'
    # appSo
    # url = 'https://www.ifanr.com/app/1216511'
    # url = 'https://www.ifanr.com/app/1257907'
    # 人物
    # url = 'https://www.ifanr.com/1227137'
    # url = 'https://www.ifanr.com/1227137'
    # 小程序
    # url = 'https://www.ifanr.com/minapp/1225964'
    # 汽车
    # url = 'https://www.ifanr.com/1226588'
    # 产品(新锐产品)
    # url = 'https://www.ifanr.com/1227642'
    # 玩物志
    # url = 'https://www.ifanr.com/coolbuy/1227328'
    # 游戏
    # url = 'https://www.ifanr.com/1223605'
    # 视频(其视频都为内切的bilibili页面, 拿到iframe其中的代码即可, 但是原始video_url还存在问题, 先不处理)
    # url = 'https://www.ifanr.com/video/1227199'
    # url = 'https://www.ifanr.com/video/1201702'
    # url = 'https://www.ifanr.com/video/1195120'

    # 科学松鼠会
    # 工程
    # url = 'https://songshuhui.net/archives/105917'
    # 心理
    # url = 'https://songshuhui.net/archives/105965'
    # 健康
    # url = 'https://songshuhui.net/archives/105900'
    # 生物
    # url = 'https://songshuhui.net/archives/105950'
    # 医学
    # url = 'https://songshuhui.net/archives/105960'
    # 化学
    # url = 'https://songshuhui.net/archives/105163'
    # 天文
    # url = 'https://songshuhui.net/archives/105581'
    # 数学
    # url = 'https://songshuhui.net/archives/102949'
    # 环境
    # url = 'https://songshuhui.net/archives/104506'
    # 计算机
    # url = 'https://songshuhui.net/archives/104767'
    # 松鼠快评
    # url = 'https://songshuhui.net/archives/82224'
    # 少儿科普
    # url = 'https://songshuhui.net/archives/88788'
    # 媒体导读
    # url = 'https://songshuhui.net/archives/56553'
    # 活动
    # url = 'https://songshuhui.net/archives/103225'
    # 其他
    # url = 'https://songshuhui.net/archives/101270'

    # 界面新闻
    # url = 'https://www.jiemian.com/article/3265195.html'
    # url = 'https://www.jiemian.com/article/3267594.html'
    # url = 'https://www.jiemian.com/article/3503663.html'
    # 天下
    # url = 'https://www.jiemian.com/article/3267499.html'
    # url = 'https://www.jiemian.com/article/3262717.html'
    # 中国
    # url = 'https://www.jiemian.com/article/3266951.html'
    # 地方
    # url = 'https://www.jiemian.com/article/3267357.html'
    # 宏观
    # url = 'https://www.jiemian.com/article/3267391.html'
    # 数据
    # url = 'https://www.jiemian.com/article/3264008.html'
    # url = 'https://www.jiemian.com/article/3252963.html'
    # url = 'https://www.jiemian.com/article/3227712.html'
    # 评论
    # url = 'https://www.jiemian.com/article/3265615.html'
    # 文娱
    # url = 'https://www.jiemian.com/article/3265618.html'
    # 体育
    # url = 'https://www.jiemian.com/article/3267782.html'
    # 时尚
    # url = 'https://www.jiemian.com/article/3267630.html'
    # 文化
    # url = 'https://www.jiemian.com/article/3263646.html'
    # 旅行
    # url = 'https://www.jiemian.com/article/3264141.html'
    # 生活
    # url = 'https://www.jiemian.com/article/3263390.html'
    # 游戏
    # url = 'https://www.jiemian.com/article/3263543.html'
    # 歪楼
    # url= 'https://www.jiemian.com/article/3263035.html'
    # 影像
    # url = 'https://www.jiemian.com/article/3259950.html'
    # 商业
    # url = 'https://www.jiemian.com/article/3267974.html'
    # 科技
    # url = 'https://www.jiemian.com/article/3267974.html'
    # 交通
    # url = 'https://www.jiemian.com/article/3266169.html'
    # 投资
    # url = 'https://www.jiemian.com/article/3267363.html'
    # 管理
    # url = 'https://www.jiemian.com/article/3265243.html'
    # 健康
    # url = 'https://www.jiemian.com/article/3266728.html'
    # 视频
    # url = 'https://www.jiemian.com/video/AGQCNwhhB24BP1Vq.html'
    # url = 'https://www.jiemian.com/video/AGQCNwhhB24BPlVi.html'
    # url = 'https://www.jiemian.com/video/AGQCNwhhB24BPFVq.html'
    # 箭厂视频
    # url = 'https://www.jiemian.com/video/AGQCNwhhB2ABOVVi.html'
    # 面谈视频
    # url = 'https://www.jiemian.com/video/AGQCNwhhB2MBPVVk.html'
    # 歪楼小分队
    # url = 'https://www.jiemian.com/video/AGQCNwhnB2YBPFVn.html'
    # 番茄社视频
    # url = 'https://www.jiemian.com/video/AGQCNwhhB2EBMFVk.html'
    # 观见直播
    # url = 'https://www.jiemian.com/video/AGQCNwhhB24BP1Vh.html'

    # 澎湃网
    # 财经
    # url = 'https://m.thepaper.cn/newsDetail_forward_3839103'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3839853'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3846838'
    # 时事
    # url = 'https://m.thepaper.cn/newsDetail_forward_3840446'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3838988'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3846825'
    # TODO 时事中的这个不支持
    # url = 'http://news.cctv.com/2019/07/04/ARTIF52wrNXdxkXpjQYgWUp7190704.shtml'
    # 湃客
    # url = 'https://m.thepaper.cn/newsDetail_forward_3838888'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3840135'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3783807'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3840119'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3839964'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3835189'
    # 思想
    # url = 'https://m.thepaper.cn/newsDetail_forward_3817762'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3846862'
    # 问政
    # url = 'https://m.thepaper.cn/newsDetail_forward_3842458'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3845652'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3845265'
    # 生活
    # url = 'https://m.thepaper.cn/newsDetail_forward_3846718'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3838792'
    # 问吧
    # TODO 问吧不支持
    # url = 'https://m.thepaper.cn/asktopic_detail_10016331'
    # 媒体
    # url = 'https://m.thepaper.cn/newsDetail_forward_3846513'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3847138'
    # 视频
    # url = 'https://m.thepaper.cn/newsDetail_forward_3771975'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3846917'
    # 七环视频
    # url = 'https://m.thepaper.cn/newsDetail_forward_3847170'
    # url = 'https://m.thepaper.cn/newsDetail_forward_3844360'
    # 一级视场
    # url = 'https://m.thepaper.cn/newsDetail_forward_3840047'
    # 温度计
    # url = 'https://m.thepaper.cn/newsDetail_forward_3838786'
    # world湃
    # url = 'https://m.thepaper.cn/newsDetail_forward_3844360'
    # 澎湃科技
    # url = 'https://m.thepaper.cn/newsDetail_forward_3840018'
    # 健寻记
    # url = 'https://m.thepaper.cn/newsDetail_forward_3829764'
    # 城市漫步
    # url = 'https://m.thepaper.cn/newsDetail_forward_3778088'
    # 大都会
    # url = 'https://m.thepaper.cn/newsDetail_forward_3790389'
    # @所有人
    # url = 'https://m.thepaper.cn/newsDetail_forward_3839854'

    # 虎嗅网
    # url = 'https://m.huxiu.com/article/312411.html'
    # url = 'https://m.huxiu.com/article/309642.html'
    # url = 'https://m.huxiu.com/article/312390.html'
    # url = 'https://m.huxiu.com/article/314704.html'
    # 医疗健康
    # url = 'https://m.huxiu.com/article/308324.html'
    # url = 'https://m.huxiu.com/article/308204.html'
    # url = 'https://m.huxiu.com/article/307905.html'
    # url = 'https://m.huxiu.com/article/307743.html'
    # 电商消费
    # url = 'https://m.huxiu.com/article/308473.html'
    # url = 'https://m.huxiu.com/article/308467.html'
    # url = 'https://m.huxiu.com/article/308442.html'
    # 娱乐淘金
    # url = 'https://m.huxiu.com/article/308523.html'
    # url = 'https://m.huxiu.com/article/308340.html'
    # 车与出行
    # url = 'https://m.huxiu.com/article/308465.html'
    # url = 'https://m.huxiu.com/article/308022.html'
    # 人工智能
    # url = 'https://m.huxiu.com/article/307650.html'
    # 年轻一代
    # url = 'https://m.huxiu.com/article/308441.html'
    # 智能终端
    # url = 'https://m.huxiu.com/article/308527.html'
    # 文化教育
    # url = 'https://m.huxiu.com/article/308471.html'
    # 金融地产
    # url = 'https://m.huxiu.com/article/308425.html'
    # 企业服务
    # url = 'https://m.huxiu.com/article/308152.html'
    # 创业维艰
    # url = 'https://m.huxiu.com/article/308496.html'
    # 社交通讯
    # url = 'https://m.huxiu.com/article/308505.html'
    # 全球热点
    # url = 'https://m.huxiu.com/article/308509.html'
    # 生活腔调
    # url = 'https://m.huxiu.com/article/308510.html'
    # 视频
    # url = 'https://m.huxiu.com/article/308402.html'
    # url = 'https://m.huxiu.com/article/307339.html'
    # todo collection非图文, pass
    # url = 'https://m.huxiu.com/collection/381.html'

    # 南方周末(其中只有部分文章可用, 不推荐使用)
    # url = 'http://www.infzm.com/wap/#/content/153845'
    # url = 'http://www.infzm.com/wap/#/content/153862'
    # url = 'http://www.infzm.com/wap/#/content/158165'
    # TODO 无法查看文章内容:
    #  1. 含有redirect为非正常url
    #  2. or 包括部分文章只能在app内打开(即标题边上有南方周末小img的，即会员才能查看), 这部分url无法处理
    # url = 'http://www.infzm.com/wap/#/content/153536?redirect=%2Fcontent%2F153500'
    # 新闻
    # url = 'http://www.infzm.com/wap/#/content/153500'
    # url = 'http://www.infzm.com/wap/#/content/153849'
    # url = 'http://www.infzm.com/wap/#/content/153851'
    # url = 'http://www.infzm.com/wap/#/content/153760'
    # 文化
    # url = 'http://www.infzm.com/wap/#/content/153854'
    # 人物
    # url = 'http://www.infzm.com/wap/#/content/153334'
    # 生活
    # url = 'http://www.infzm.com/wap/#/content/152879'
    # 社会
    # url = 'http://www.infzm.com/wap/#/content/153416'
    # 教育
    # url = 'http://www.infzm.com/wap/#/content/152819'
    # 财富
    # url = 'http://www.infzm.com/wap/#/content/147544'

    # 好奇心日报
    # todo 文章为书的介绍的不做采集
    # 商业
    # url = 'http://m.qdaily.com/mobile/articles/64092.html'
    # url = 'http://m.qdaily.com/mobile/articles/64087.html'
    # url = 'http://m.qdaily.com/mobile/articles/64084.html'
    # 时尚
    # url = 'http://m.qdaily.com/mobile/articles/64089.html'
    # 智能
    # url = 'http://m.qdaily.com/mobile/articles/64078.html'
    # 娱乐
    # url = 'http://m.qdaily.com/mobile/articles/64072.html'
    # 文化
    # url = 'http://m.qdaily.com/mobile/articles/64060.html'
    # url = 'http://m.qdaily.com/mobile/articles/63484.html'
    # 文化长文章
    # url = 'http://m.qdaily.com/mobile/articles/63974.html'
    # 设计
    # url = 'http://m.qdaily.com/mobile/articles/64056.html'
    # 游戏
    # url = 'http://m.qdaily.com/mobile/articles/64050.html'

    # 场库(cp服务器无法上传视频)
    # url = 'https://www.vmovier.com/57050?from=index_new_title'
    # url = 'https://www.vmovier.com/57057?from=index_new_title'
    # url = 'https://www.vmovier.com/57035?from=index_new_title'
    # url = 'https://www.vmovier.com/56985?from=index_hot_week_title'
    # url = 'https://www.vmovier.com/57028?from=index_hot_week_title'
    # url = 'https://www.vmovier.com/56442?from=index_rand_title'
    # url = 'https://www.vmovier.com/57696?from=index_new_title'
    # url = 'https://www.vmovier.com/57669?from=index_new_img'

    # 梨视频
    # url = 'https://www.pearvideo.com/video_1584072'
    # url = 'https://www.pearvideo.com/video_1583852'
    # 新知
    # url = 'https://www.pearvideo.com/video_1584002'
    # url = 'https://www.pearvideo.com/video_1583149'
    # 社会
    # url = 'https://www.pearvideo.com/video_1583889'
    # 世界
    # url = 'https://www.pearvideo.com/video_1584109'
    # 体育
    # url = 'https://www.pearvideo.com/video_1584079'
    # 生活
    # url = 'https://www.pearvideo.com/video_1570493'
    # 科技
    # url = 'https://www.pearvideo.com/video_1584259'
    # 娱乐
    # url = 'https://www.pearvideo.com/video_1584141'
    # 财富
    # url = 'https://www.pearvideo.com/video_1584122'
    # 汽车
    # url = 'https://www.pearvideo.com/video_1584113'
    # 美食
    # url = 'https://www.pearvideo.com/video_1584089'
    # 音乐
    # url = 'https://www.pearvideo.com/video_1584314'
    # 拍客
    # url = 'https://www.pearvideo.com/video_1584404'
    # todo 万象, 图文文章(多为国家相关, 不采集)
    # todo 直播不采集
    # url = 'https://www.pearvideo.com/living_1583854'

    # 艾墨镇(视频是iframe)
    # url = 'https://aimozhen.com/view/15994/'
    # url = 'https://aimozhen.com/view/15770/'
    # url = 'https://aimozhen.com/view/15537/'
    # url = 'https://aimozhen.com/view/15505/'
    # url = 'https://aimozhen.com/view/15996/'
    # url = 'https://aimozhen.com/view/15993/'
    # url = 'https://aimozhen.com/view/2789/'
    # url = 'https://aimozhen.com/view/10345/'
    # url = 'https://aimozhen.com/view/15620/'
    # url = 'https://aimozhen.com/view/15960/'

    # 美拍
    # url = 'https://www.meipai.com/media/1129488204'
    # url = 'https://www.meipai.com/media/1119174156'
    # url = 'https://www.meipai.com/media/1131644923'
    # url = 'https://www.meipai.com/media/1133207409'
    # url = 'https://www.meipai.com/media/1132365942'
    # url = 'https://www.meipai.com/media/1131644923'
    # url = 'https://www.meipai.com/media/1188897814'
    # todo 直播不采集

    # 百度好看视频
    # 推荐
    # url = 'https://haokan.baidu.com/v?vid=4136323293933620725&tab=recommend'
    # url = 'https://haokan.baidu.com/v?vid=13905274734303307712&tab=recommend'
    # 影视
    # 音乐
    # url = 'https://haokan.baidu.com/v?vid=15566590767854893570&tab=yinyue'
    # 搞笑
    # url = 'https://haokan.baidu.com/v?vid=11049055717053789925&tab=gaoxiao'
    # vlog
    # url = 'https://haokan.baidu.com/v?vid=18364192214912567672&tab=vlog'
    # 娱乐
    # url = 'https://haokan.baidu.com/v?vid=2039585784239075755&tab=yule'
    # 动漫
    # url = 'https://haokan.baidu.com/v?vid=13669502144755223017&tab=dongman'
    # 生活
    # url = 'https://haokan.baidu.com/v?vid=6013186501247664939&tab=shenghuo'
    # 小品
    # url = 'https://haokan.baidu.com/v?vid=1950334490626075127&tab=xiaopin'
    # 综艺
    # url = 'https://haokan.baidu.com/v?vid=3543129372355380096&tab=zongyi'
    # 游戏
    # url = 'https://haokan.baidu.com/v?vid=16045267043621223572&tab=youxi'
    # 秒懂
    # url = 'https://haokan.baidu.com/v?vid=8764292721309064181&tab=miaodong'
    # 教育
    # url = 'https://haokan.baidu.com/v?vid=13019064242738140769&tab=jiaoyu'
    # 军事
    # url = 'https://haokan.baidu.com/v?vid=9293974956392010975&tab=junshi'
    # 科技
    # url = 'https://haokan.baidu.com/v?vid=3788911623189008455&tab=keji'
    # 汽车
    # url = 'https://haokan.baidu.com/v?vid=8655585633607378937&tab=qiche'
    # 纪录片
    # url = 'https://haokan.baidu.com/v?vid=11997191395202643272&tab=record'
    # 体育
    # url = 'https://haokan.baidu.com/v?vid=16107732794840639604&tab=tiyu'
    # 文化
    # url = 'https://haokan.baidu.com/v?vid=7456588810512052606&tab=wenhua'
    # 亲子
    # url = 'https://haokan.baidu.com/v?vid=15546006886814520106&tab=qinzi'
    # 社会
    # url = 'https://haokan.baidu.com/v?vid=648167893261511164&tab=shehui'
    # 三农
    # url = 'https://haokan.baidu.com/v?vid=4161801005423552525&tab=sannong'
    # 宠物
    # url = 'https://haokan.baidu.com/v?vid=9740175951467494081&tab=chongwu'
    # 美食
    # url = 'https://haokan.baidu.com/v?vid=11754326304031754679&tab=meishi'
    # 时尚
    # url = 'https://haokan.baidu.com/v?vid=17448170737812377575&tab=shishang'

    # 七丽女性网
    # url = 'https://i.7y7.com/hufu/84/385784.html'
    # url = 'https://i.7y7.com/remenzixun/31/386631.html'
    # url = 'https://i.7y7.com/hufu/42/386542.html'
    # 时尚
    # url = 'https://i.7y7.com/fushi/04/386404.html'
    # url = 'https://i.7y7.com/fushi/62/385562.html'
    # 护肤
    # url = 'https://i.7y7.com/hufu/35/386635.html'
    # url = 'https://i.7y7.com/hufu/37/385737.html'
    # 彩妆
    # url = 'https://i.7y7.com/caizhuang/36/386636.html'
    # 减肥
    # url = 'https://i.7y7.com/shoushen/93/386493.html'
    # 美发
    # url = 'https://i.7y7.com/meifa/28/386628.html'
    # 医美
    # url = 'https://i.7y7.com/yimei/91/386491.html'
    # 博主
    # url = 'https://i.7y7.com/bozhu/93/338893.html'
    # 街拍
    # url = 'https://i.7y7.com/jiepai/34/383734.html'
    # 星座
    # url = 'https://i.7y7.com/xingzuo/05/386605.html'
    # 情感
    # url = 'https://i.7y7.com/qinggan/24/384924.html'
    # 健康
    # url = 'https://i.7y7.com/jiankang/36/386536.html'
    # 亲子
    # url = 'https://i.7y7.com/qinzi/37/386237.html'
    # 美甲
    # url = 'https://i.7y7.com/meijia/60/386260.html'
    # 时装
    # url = 'https://i.7y7.com/shizhuang/77/386177.html'
    # 优品
    # url = 'https://i.7y7.com/youpin/13/384213.html'
    # 秀场
    # url = 'https://i.7y7.com/xiuchang/84/364884.html'
    # 明星
    # url = 'https://i.7y7.com/mingxing/25/384425.html'
    # 大片(多为纯图, 不提取)
    # 影视
    # url = 'https://i.7y7.com/yingshi/48/381648.html'
    # 家居
    # url = 'https://i.7y7.com/jiaju/97/386197.html'
    # todo 广场不采集, 纯图文章不采集

    # 亲亲宝贝
    # todo 听声音cp后台无法转, pass
    # url = 'https://m.qbaobei.com/a/1372873.html'
    # 备孕
    # url = 'https://m.qbaobei.com/a/1372711.html'
    # url = 'https://m.qbaobei.com/a/1365780.html'
    # 怀孕
    # url = 'https://m.qbaobei.com/a/1145214.html'
    # 分娩
    # url = 'https://m.qbaobei.com/a/1103497.html'
    # 产后
    # url = 'https://m.qbaobei.com/a/1064188.html'
    # 新生儿
    # url = 'https://m.qbaobei.com/a/1372717.html'
    # url = 'https://m.qbaobei.com/a/387813.html'
    # 0-1岁
    # url = 'https://m.qbaobei.com/a/470111.html'
    # 1-3岁
    # url = 'https://m.qbaobei.com/a/807352.html'
    # 3-6岁
    # url = 'https://m.qbaobei.com/a/442792.html'
    # 早教
    # url = 'https://m.qbaobei.com/a/1192626.html'
    # 食谱
    # url = 'https://m.qbaobei.com/a/1191509.html'
    # 百科
    # url = 'https://m.qbaobei.com/a/439598.html'
    # url = 'https://m.qbaobei.com/a/671501.html'
    # 用品
    # url = 'https://m.qbaobei.com/a/1000502.html'
    # 奶粉
    # url = 'https://m.qbaobei.com/a/1361544.html'
    # 视频
    # url = 'https://m.qbaobei.com/v/video_2972.html'
    # url = 'https://m.qbaobei.com/v/video_8.html'
    # url = 'https://m.qbaobei.com/v/video_25.html'
    # todo 小时光, 听听 不采集

    # 发条网
    # 视频
    # url = 'https://mart.fatiao.pro/detail/1522.html'
    # url = 'https://mart.fatiao.pro/detail/2268.html'
    # url = 'https://mlive.fatiao.pro/detail/8755.html'
    # url = 'https://mlive.fatiao.pro/detail/8909.html'
    # url = 'https://mlive.fatiao.pro/detail/8772.html'
    # url = 'https://mnatural.fatiao.pro/detail/4194.html'
    # url = 'https://mqtwj.fatiao.pro/detail/8937.html'
    # url = 'https://mdiet.fatiao.pro/detail/1041.html'
    # 图文
    # url = 'https://mpet.fatiao.pro/article/7858.html'
    # url = 'https://mpet.fatiao.pro/article/1093.html'
    # url = 'https://mpet.fatiao.pro/article/5137.html'
    # url = 'https://mpet.fatiao.pro/article/9477.html'
    # url = 'https://mbeauty.fatiao.pro/article/52633.html'
    # url = 'https://mbeauty.fatiao.pro/article/28785.html'
    # url = 'https://mlive.fatiao.pro/article/52761.html'

    # 觅糖
    # 视频
    # url = 'https://www.91mitang.com/pages/2019011772010'
    # 时尚
    # url = 'https://www.91mitang.com/pages/81047'
    # 美食
    # url = 'https://www.91mitang.com/pages/2019011771915'
    # 生活百科
    # url = 'https://www.91mitang.com/pages/2019011751000'
    # 教育
    # url = 'https://www.91mitang.com/pages/2019011772120'
    # 其他
    # url = 'https://www.91mitang.com/pages/2019011761003'
    # 诗词朗诵
    # url = 'https://www.91mitang.com/pages/71225'
    # 节日风俗
    # url = 'https://www.91mitang.com/pages/70006'
    # 课程学习
    # url = 'https://www.91mitang.com/pages/71115'
    # 家常菜谱
    # url = 'https://www.91mitang.com/pages/72014'
    # 风味小吃
    # url = 'https://www.91mitang.com/pages/72176'
    # 旅游出行
    # url = 'https://www.91mitang.com/pages/83527'
    # 美妆护肤
    # url = 'https://www.91mitang.com/pages/81047'
    # 娱乐
    # url = 'https://www.91mitang.com/pages/91022'
    # 图文文章
    # url = 'https://www.91mitang.com/pages/2106103'
    # url = 'https://www.91mitang.com/pages/2106106'

    # 雪球网
    # 推荐
    # url = 'https://xueqiu.com/8036802659/131021825'
    # url = 'https://xueqiu.com/3075122481/131022515'
    # 沪深
    # url = 'https://xueqiu.com/S/SH600309/131099947'
    # url = 'https://xueqiu.com/8992033978/131027969'
    # url = 'https://xueqiu.com/9220236682/131126259'
    # 科创板
    # url = 'https://xueqiu.com/1896346964/130972987'
    # 港股
    # url = 'https://xueqiu.com/1055336715/129835730'
    # 基金
    # url = 'https://xueqiu.com/7298671747/131128718'
    # 美股
    # url = 'https://xueqiu.com/S/DL/131099586'
    # url = 'https://xueqiu.com/8041756563/131102425'
    # 房产
    # url = 'https://xueqiu.com/1428373799/130981044'
    # 私募
    # url = 'https://xueqiu.com/3186487370/130986249'
    # 汽车
    # url = 'https://xueqiu.com/4828772707/130482225'
    # 保险
    # url = 'https://xueqiu.com/5157574024/130400677'

    # 5号女性网
    # url = 'http://m.5h.com/mr/161290.html'
    # url = 'http://m.5h.com/mr/140547.html'
    # 化妆
    # url = 'http://m.5h.com/mr/152296.html'
    # url = 'http://m.5h.com/mr/157448.html'
    # 护肤
    # url = 'http://m.5h.com/mr/152431.html'
    # 减肥
    # url = 'http://m.5h.com/mr/151883.html'
    # 发型
    # url = 'http://m.5h.com/mr/157448.html'
    # 时尚
    # url = 'http://m.5h.com/mr/152413.html'
    # 情感
    # url = 'http://m.5h.com/ys/152131.html'
    # 亲子
    # url = 'http://m.5h.com/qz/153147.html'
    # 整形
    # url = 'http://m.5h.com/mr/152342.html'
    # 饮食
    # url = 'http://m.5h.com/ys/152432.html'
    # 养生
    # url = 'http://m.5h.com/ys/153185.html'
    # 医疗
    # url = 'http://m.5h.com/yl/153612.html'
    # 看病
    # url = 'http://m.5h.com/yl/148912.html'
    # todo 不支持专题,

    # 百思不得姐
    # url = 'http://www.budejie.com/detail-29745738.html'
    # url = 'http://www.budejie.com/detail-29752780.html'
    # url = 'http://www.budejie.com/detail-29752170.html'
    # url = 'http://www.budejie.com/detail-29752481.html'
    # url = 'http://www.budejie.com/detail-29752617.html'
    # url = 'http://www.budejie.com/detail-29160596.html'
    # 纯文字
    # url = 'http://www.budejie.com/detail-29752862.html'
    # todo 声音不支持

    # 煎蛋网
    # url = 'http://i.jandan.net/2019/09/26/alcohol-facts.html'
    # url = 'http://i.jandan.net/2019/09/27/dark-skin-2.html'
    # 健康
    # url = 'http://jandan.net/2019/09/27/hand-sanitizer.html'
    # 故事
    # url = 'http://jandan.net/2019/09/26/truck-drivers.html'
    # url = 'http://jandan.net/2019/09/24/cockroach-milk.html'
    # 科学
    # url = 'http://jandan.net/2019/09/26/music-impairs.html'
    # 技术
    # 下方url含点击查看图片的情况
    # url = 'http://jandan.net/2019/09/03/photorealistic-emojis.html'
    # 脑洞
    # url = 'http://jandan.net/2019/05/01/non-toxic-spray.html'
    # url = 'http://jandan.net/2017/08/17/love-power.html'
    # 人类
    # url = 'http://jandan.net/2019/09/26/korea-angry-young.html'
    # 折腾
    # url = 'http://jandan.net/2019/07/13/circumcision-season.html'
    # url = 'http://jandan.net/2019/05/02/six-pack-abs.html'
    # 心理学
    # url = 'http://jandan.net/2019/09/26/first-date-5.html'
    # 走近科学
    # url = 'http://jandan.net/2019/09/25/sinking-beach.html'
    # todo 极客中含视频的还未处理
    # url = 'http://jandan.net/2019/09/12/exercise-hard.html'
    # todo 问答不采集

    # 来福岛爆笑娱乐网
    # 图片
    # url = 'http://www.laifudao.com/tupian/87076.htm?xid=tupian87076'
    # url = 'http://www.laifudao.com/tupian/87080.htm?xid=tupian87080'
    # url = 'http://www.laifudao.com/tupian/87109.htm?xid=tupian87109'
    # url = 'http://www.laifudao.com/tupian/87108.htm?xid=tupian87108'
    # url = 'http://www.laifudao.com/tupian/87100.htm?xid=tupian87100'
    # url = 'http://www.laifudao.com/tupian/86778.htm'
    # 纯文字
    # url = 'http://www.laifudao.com/wangwen/214763.htm?xid=wangwen214763'
    # url = 'http://www.laifudao.com/wangwen/4223.htm'
    # todo 铃声不支持

    # bilibili
    # url = 'https://www.bilibili.com/video/av60965559?spm_id_from=333.334.b_62696c695f67756f636875616e67.42'
    # 动画
    # url = 'https://www.bilibili.com/video/av70120885?spm_id_from=333.334.b_62696c695f646f756761.3'
    # 国产原创
    # url = 'https://www.bilibili.com/video/av60965559?spm_id_from=333.334.b_62696c695f67756f636875616e67.42'
    # 音乐
    # url = 'https://www.bilibili.com/video/av50549725?spm_id_from=333.334.b_62696c695f6d75736963.3'
    # 舞蹈
    # url = 'https://www.bilibili.com/video/av71057920?spm_id_from=333.334.b_62696c695f64616e6365.3'
    # 游戏
    # url = 'https://www.bilibili.com/video/av71180658?spm_id_from=333.334.b_62696c695f67616d65.3'
    # 科技
    # url = 'https://www.bilibili.com/video/av48880721?spm_id_from=333.334.b_62696c695f746563686e6f6c6f6779.3'
    # 数码
    # url = 'https://www.bilibili.com/video/av70969651?spm_id_from=333.334.b_62696c695f6469676974616c.3'
    # 生活
    # url = 'https://www.bilibili.com/video/av68706390?spm_id_from=333.334.b_62696c695f6c696665.3'
    # 鬼畜
    # url = 'https://www.bilibili.com/video/av70836260?spm_id_from=333.334.b_62696c695f6b696368696b75.3'
    # 时尚
    # url = 'https://www.bilibili.com/video/av64328457?spm_id_from=333.334.b_62696c695f66617368696f6e.3'
    # 广告
    # url = 'https://www.bilibili.com/video/av71183384?spm_id_from=333.334.b_62696c695f6164.3'
    # 娱乐
    # url = 'https://www.bilibili.com/video/av67337245?spm_id_from=333.334.b_62696c695f656e74.3'
    # 影视
    # url = 'https://www.bilibili.com/video/av62093677?spm_id_from=333.334.b_62696c695f63696e657068696c65.3'
    # 纪录片
    # url = 'https://www.bilibili.com/video/av70033425?spm_id_from=333.334.b_62696c695f646f63756d656e74617279.6'
    # todo 番剧, 国创url含'/play/'的, 漫画, 专栏图文, 电影(1-2小时), 电视剧, 直播不支持

    # 快音视(全网短视频集合)
    # 快手
    # url = 'https://kuaiyinshi.com/?video_id=BMjAxOTA3MDUxMzA4MTdfMTIwMDU4MjA4N18xNDgwNTM0NzQ3NV8xXzM=_b_Ba9cd9e5539759a6b73d0e2b400cc9dc9&source=kuai-shou#search-form'
    # url = 'https://kuaiyinshi.com/?video_id=BMjAxODA5MjAxODE2MjZfMTA4OTc1MDA5OV84MTA5Nzc4MDI5XzFfMw==_b_B5b668e696fc5f8fead97cbb251c4ac02&source=kuai-shou#search-form'
    # url = 'https://kuaiyinshi.com/?video_id=BMjAxOTA2MDUwODU4MTNfOTE2MjUxOTkyXzEzNzQwNjQwMzk1XzFfMw==_b_B61fab60021d32b77d20c34cec02798ee&source=kuai-shou#search-form'
    # 美拍(存在大量无title的)
    # 无title
    # url = 'https://kuaiyinshi.com/?video_id=5c3de5f1d71cb2ckucyf6p1502_H264_1_62f1d90b99edf1&source=mei-pai#search-form'
    # url = 'https://kuaiyinshi.com/?video_id=5c3de5f1d71cb2ckucyf6p1502_H264_1_62f1d90b99edf1&source=mei-pai#search-form'
    # 有title
    # url = 'https://kuaiyinshi.com/?video_id=5c4b4102ab7612595&source=mei-pai#search-form'

    # 搞笑gif图片集
    # url = 'https://m.gaoxiaogif.com/dongwugif/12298.html'
    # url = 'https://m.gaoxiaogif.com/zhenrengif/12297.html'
    # url = 'https://m.gaoxiaogif.com/meinvgif/12289.html'

    # 酷燃视频
    # url = 'https://krcom.cn/6357210927/episodes/2358773:4435230858126303'
    # url = 'https://krcom.cn/6056657061/episodes/2358773:4415767190436583'
    # url = 'https://krcom.cn/6135166906/episodes/2358773:4275862502049689'
    # url = 'https://krcom.cn/1729930211/episodes/2358773:4276593313415601'
    # url = 'https://krcom.cn/6511520515/episodes/2358773:673bb576ece8d9291562459596cee095'

    # 东方视频(热门视频)
    # url = 'http://imedia.eastday.com/node2/2015imedia/rmsp/u8i790954.html'
    # url = 'http://imedia.eastday.com/node2/2015imedia/i/20191117/u8i790911.html'
    # url = 'http://imedia.eastday.com/node2/2015imedia/i/20191114/u8i790718.html'

    # 腾讯微视
    # url = 'https://h5.weishi.qq.com/weishi/feed/6YfJpqYl21IysAVgg/wsfeed?wxplay=1&id=6YfJpqYl21IysAVgg&spid=1556715970981610&qua=v1_and_weishi_6.1.5_588_312026001_d&chid=100000014&pkg=3670&attach=cp_reserves3_1000000012&from=groupmessage&isappinstalled=0'
    # url = 'https://h5.weishi.qq.com/weishi/feed/6ZWI9iM5q1Ipfc65v/wsfeed?wxplay=1&id=6ZWI9iM5q1Ipfc65v&spid=1556715970981610&qua=v1_and_weishi_6.1.5_588_312026001_d&chid=100000014&pkg=3670&attach=cp_reserves3_1000000012&from=groupmessage&isappinstalled=0'
    # url = 'https://h5.weishi.qq.com/weishi/feed/771Jznds31IrthMbv/wsfeed?wxplay=1&id=771Jznds31IrthMbv&spid=1556715970981610&qua=v1_and_weishi_6.1.5_588_312026001_d&chid=100000014&pkg=3670&attach=cp_reserves3_1000000012&from=groupmessage&isappinstalled=0'
    # url = 'https://h5.weishi.qq.com/weishi/feed/7723Eht791IwmCuXW/wsfeed?wxplay=1&id=7723Eht791IwmCuXW&spid=1556715970981610&qua=v1_and_weishi_6.1.5_588_312026001_d&chid=100000014&pkg=3670&attach=cp_reserves3_1000000012&from=groupmessage&isappinstalled=0'
    # url = 'https://h5.weishi.qq.com/weishi/feed/76q06teUr1IJyDKND/wsfeed?attach=cp_reserves3_1000020006&wxplay=1&qua=v1_iph_weishi_6.4.0_606_app_a&id=76q06teUr1IJyDKND&spid=8045329248462745600&chid=100002010&pkg=3670'
    # 视频原声
    # url = 'https://h5.weishi.qq.com/weishi/feed/7cGkLgNTS1Iva9REP/wsfeed?wxplay=1&id=7cGkLgNTS1Iva9REP&spid=1556715970981610&qua=v1_and_weishi_6.1.5_588_312026001_d&chid=100000014&pkg=3670&attach=cp_reserves3_1000000012&from=groupmessage&isappinstalled=0'

    # 看了吗视频聚合网
    # 小视频
    # url = 'http://www.klm123.com/share/5b399af6d947'
    # url = 'http://www.klm123.com/share/3c4e443bb39f'
    # 短视频
    # url = 'http://www.klm123.com/share/4260e78cad8f'
    # url = 'http://www.klm123.com/share/93e219fa9a2e'

    # 开眼小视频
    # url = 'https://www.kaiyanapp.com/detail.html?vid=52619'
    # url = 'https://www.kaiyanapp.com/detail.html?vid=52618'
    # url = 'https://www.kaiyanapp.com/detail.html?vid=4000'

    # 抖音
    # url = 'https://v.douyin.com/pnxxaH/'
    # url = 'https://v.douyin.com/sdLYWJ/'
    # url = 'https://v.douyin.com/se3wkb/'
    # url = 'https://v.douyin.com/nXCh6q/'
    # 下方为不是app里面分享的地址, 如排行榜的地址
    # url = 'https://www.iesdouyin.com/share/video/6818874977903824128/?region=&mid=6818874986108603143&u_code=0&titleType=title'

    # 今日小视频(它们网站偶尔不稳定)
    # url = 'http://m.jrtb.net/shenghuo/xhyljjtzxjdpjmmhzpysdxjzcr.html'
    # url = 'http://m.jrtb.net/yingshi/dxhyjgfzgypcdzlyglkqwwzlxs.html'
    # url = 'http://m.jrtb.net/shenghuo/11sxnhzgyyzzjdycqsxlwdyklldrz.html'
    # url = 'http://m.jrtb.net/yingshi/zdqwcrzzzgzzbmxltzfywrtdzjj.html'

    # 金华广众网(即金华广电网)(目前只做里面的图文文章)
    # todo 有些文章无权限访问, 要账号登录论坛, pass
    # 美食
    # 美食快讯里的文章(但是官网不更新)
    # url = 'https://food.jinhua.com.cn/mskx/2018-06-07/348820.html'
    # 美食里的舌尖上的金华(含视频, 视频在js中, 自己会切入, 是m3u8的格式, 目前cp后台不支持下载, pass)
    # url = 'https://food.jinhua.com.cn/sjjh/2019-03-11/458177.html'
    # url = 'https://food.jinhua.com.cn/sjjh/2019-02-01/450063.html'
    # 饮食健康
    # url = 'https://food.jinhua.com.cn/ysjk/2016-12-02/234967.html'
    # 活动(活动里面含有一些规格正确的地址但是非文章内容, 此处做成获取接口时, pass)
    # url = 'https://www.jinhua.com.cn/activity/2019-12-13/521841.html'
    # url = 'https://www.jinhua.com.cn/app/zhuanti/2018-06-14/352998.html'
    # 资讯(即金华24小时)(其中地址如浙江新闻网的地址, 微信分享的地址, 就pass)
    # url = 'https://news.jinhua.com.cn/shishi/2020-03-26/543480.html'
    # url = 'https://news.jinhua.com.cn/shishi/2020-03-25/543470.html'
    # url = 'https://news.jinhua.com.cn/shishi/2020-03-25/543469.html'
    # 资讯里的生活
    # url = 'https://news.jinhua.com.cn/shenghuo/2020-03-26/543486.html'
    # 资讯里的奇闻(不更新)
    # url = 'https://news.jinhua.com.cn/qiwen/2017-07-04/278236.html'
    # 资讯里的突发(含js切入的视频图文, 如上[舌尖上的金华])
    # url = 'https://www.jinhua.com.cn/topics/qtzt/xgwz/2019-09-02/498875.html'
    # url = 'https://news.jinhua.com.cn/tufa/2018-07-05/355326.html'
    # 咨询里的广播(含上述切入的视频)
    # url = 'https://news.jinhua.com.cn/guangbo/jgzxw/2019-12-26/524156.html'
    # 摄影
    # url = 'https://photo.jinhua.com.cn/slys/2019-12-12/521505.html'
    # 摄影里的摄影技巧
    # url = 'https://photo.jinhua.com.cn/xuexi/syjq/2018-04-11/335061.html'
    # 摄影里的作品欣赏, pass
    # url = 'https://photo.jinhua.com.cn/zpxs/xwjs/2019-12-04/519814.html'
    # todo 主页里的视频(获取到的视频播放地址都为m3u8格式的, cp 目前不支持上传, pass)
    # 视频里面的直播回顾
    # url = 'https://www.jinhua.com.cn/video/zhibo/2020-02-29/537613.html'
    # url = 'https://www.jinhua.com.cn/video/zhibo/2019-11-08/527712.html'
    # 视频里面的原创短片
    # url = 'https://www.jinhua.com.cn/video/yuanchuang/2018-04-08/536933.html'
    # 舌尖上的金华再上方处理了
    # 无线金华, pass
    # url = 'https://tv1.jinhua.com.cn/wxjh/2020-03-24/543065.html'
    # 含有无线金华二维码的且(含有视频的处理 or 图文)
    # url = 'https://news.jinhua.com.cn/shishi/2020-04-26/549659.html'
    # url = 'https://news.jinhua.com.cn/shishi/2020-04-25/549601.html'
    # url = 'https://news.jinhua.com.cn/shishi/2020-04-29/550345.html'
    # url = 'https://news.jinhua.com.cn/shishi/2020-04-28/550341.html'
    # url = 'https://news.jinhua.com.cn/shishi/2020-04-28/550302.html'
    # url = 'https://news.jinhua.com.cn/shishi/2020-04-28/550303.html'
    # url = 'https://news.jinhua.com.cn/shishi/2020-04-28/550155.html'
    # url = 'https://news.jinhua.com.cn/shishi/2020-05-16/553957.html'

    # 金华热线
    # url = 'http://m.0579.cn/read.php?tid=3138997'
    # url = 'http://m.0579.cn/read.php?tid=3138827'
    # url = 'http://m.0579.cn/read.php?tid=3138994'
    # url = 'http://m.0579.cn/read.php?tid=3138573'
    # url = 'http://m.0579.cn/read.php?tid=3136901'

    # 金华晚报
    # url = 'https://www.96356.in/articles/75359'
    # url = 'https://www.96356.in/articles/75345'
    # url = 'https://www.96356.in/articles/75301'

    # 百度app金华本地的短视频解析
    # url = 'https://sv.baidu.com/videoui/page/videoland?&context=%7B%22nid%22%3A%22sv_13449568219241582441%22%2C%22sourceFrom%22%3A%22bjh%22%2C%22poster_big%22%3A%22https%3A%5C%2F%5C%2Fpic.rmb.bdstatic.com%5C%2F613230305e3b9c62c8b66bb2e1bda612.jpeg%40s_1%2Cw_660%2Ch_370%22%7D'
    # url = 'https://sv.baidu.com/videoui/page/videoland?&context=%7B%22nid%22%3A%22sv_711599875470459459%22%2C%22sourceFrom%22%3A%22bjh%22%2C%22poster_big%22%3A%22https%3A%5C%2F%5C%2Fpic.rmb.bdstatic.com%5C%2F4b6343c1864151170561b0d9ca23f595.jpeg%40s_1%2Cw_660%2Ch_370%22%7D'
    # url = 'https://sv.baidu.com/videoui/page/videoland?&context=%7B%22nid%22%3A%22sv_17635889761783462064%22%2C%22sourceFrom%22%3A%22bjh%22%2C%22poster_big%22%3A%22https%3A%5C%2F%5C%2Fpic.rmb.bdstatic.com%5C%2Fb968eea9c83d089a2986e3b8ca8093ab.jpeg%40s_1%2Cw_660%2Ch_370%22%7D'
    # url = 'https://sv.baidu.com/videoui/page/videoland?&context=%7B%22nid%22%3A%22sv_5599335408583823355%22%2C%22sourceFrom%22%3A%22bjh%22%2C%22poster_big%22%3A%22http%3A%5C%2F%5C%2Fpic.rmb.bdstatic.com%5C%2F1fc5d9fe736de4d9326bcf272a15fc45.jpeg%40s_1%2Cw_660%2Ch_370%22%7D'

    # 百度app中全屏小视频页面解析
    # url = 'https://quanmin.baidu.com/sv?source=share-h5&pd=qm_share_mvideo&vid=4538982913039184503&shared_cuid=AqqqB#/'
    # url = 'https://quanmin.baidu.com/sv?source=share-h5&pd=qm_share_mvideo&vid=5015163600876926622&shared_cuid=AqqqB'
    # url = 'https://quanmin.baidu.com/sv?source=share-h5&pd=qm_share_mvideo&vid=3982527886437173468&shared_cuid=AqqqB'
    # url = 'https://quanmin.baidu.com/sv?source=share-h5&pd=qm_share_mvideo&vid=3276059148537518865&shared_cuid=AqqqB'

    # 义乌18腔
    # url = 'https://m.18qiang.com/read.php?tid=697605'
    # url = 'https://m.18qiang.com/read.php?tid=697467'

    # 浙江在线金华频道
    # url = 'http://jinhua.zjol.com.cn/jsbd/202004/t20200425_11911752.shtml'
    # url = 'http://jinhua.zjol.com.cn/jsbd/202004/t20200425_11911741.shtml'
    # url = 'http://jinhua.zjol.com.cn/jsbd/202004/t20200425_11911732.shtml'

    # 文章url 测试
    print('article_url: {}'.format(url))
    article_parse_res = loop.run_until_complete(
        future=_._parse_article(article_url=url))
    pprint(article_parse_res)
    # print(dumps(article_parse_res))

    # article spiders intro
    # tmp = loop.run_until_complete(_.get_article_spiders_intro())
    # print(tmp)

    # 文章列表
    # article_type = 'zq'
    # article_type = 'hk'
    # article_type = 'lfd'
    # article_type = 'gxg'
    # article_type = 'pp'
    # article_type = 'kr'
    # article_type = 'dfsp'
    # article_type = 'lsp'
    # mp pc站官网503
    # article_type = 'mp'
    # article_type = 'klm'
    # article_type = 'jrxsp'
    # article_type = 'jhgzw'
    # article_type = 'jhrx'
    # article_type = 'jhwb'
    # article_type = 'jhbdsv'
    # article_type = 'bdqmxsv'
    # article_type = 'dy0'
    # article_type = 'jhzjol'
    # tmp = loop.run_until_complete(_.get_article_list_by_article_type(
    #     article_type=article_type,))
    # pprint(tmp)

if __name__ == '__main__':
    main()