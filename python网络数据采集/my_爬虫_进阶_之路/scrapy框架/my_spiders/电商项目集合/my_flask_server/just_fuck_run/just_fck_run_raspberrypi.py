# coding:utf-8

'''
@author = super_fazai
@File    : just_fck_run_raspberrypi.py
@connect : superonesfazai@gmail.com
'''

from sys import path as sys_path
sys_path.append('..')
from os import system
from fzutils.spider.async_always import *

if get_system_type() == 'Darwin':
    python_version_cmd = 'python3'
    logs_path = '/Users/afa/myFiles/codeDoc/pythonDoc/python/python网络数据采集/my_爬虫_进阶_之路/scrapy框架/my_spiders/电商项目集合/my_flask_server/logs'
    zwm_path = '/Users/afa/myFiles/codeDoc/pythonDoc/python/python网络数据采集/my_爬虫_进阶_之路/scrapy框架/my_spiders/电商项目集合/my_flask_server'
    dcs_path = '/Users/afa/myFiles/codeDoc/pythonDoc/python/python网络数据采集/my_爬虫_进阶_之路/scrapy框架/my_spiders/电商项目集合/my_flask_server/distribute_jobs'

else:
    python_version_cmd= 'python3.6'
    logs_path = '~/myFiles/python/my_flask_server/logs'
    zwm_path = '~/myFiles/python/my_flask_server'
    dcs_path = '~/myFiles/python/my_flask_server/distribute_jobs'

logs_file_name_list = [
    # 'expired_logs_deal_with',
]

zwm_file_name_list = [
    # 只监控new_my_server
    # 'new_my_server',
]

dcs_file_name_list = [
    # 只监控distributed_tasks_producer
    'distributed_tasks_producer',
]

# 只在晚上run
night_run_file_name_list = []
night_run_time = ['21', '22', '23', '00', '01', '02', '03', '04', '05', '06',]

def run_one_file_name_list(path, file_name_list):
    for item in file_name_list:
        if item in night_run_file_name_list \
                and str(get_shanghai_time())[11:13] not in night_run_time:
            print('{0}.py不在运行时间点...此处跳过!'.format(item))
            pass
        else:
            process_name = item + '.py'
            if process_exit(process_name) == 0:
                if 'distributed_tasks_producer' in item:
                    system('cd {0} && {1} -X faulthandler {2}.py'.format(
                        path,
                        python_version_cmd,
                        item))
                else:
                    # 如果对应的脚本没有在运行, 则运行之
                    system('cd {0} && {1} {2}.py'.format(
                        path,
                        python_version_cmd,
                        item))
                sleep(2.5)  # 避免同时先后启动先sleep下
            else:
                print(process_name + '脚本已存在!')

def auto_run(*params):
    print('开始执行监控脚本'.center(60, '*'))

    run_one_file_name_list(path=params[0], file_name_list=logs_file_name_list)
    run_one_file_name_list(path=params[1], file_name_list=zwm_file_name_list)
    run_one_file_name_list(path=params[2], file_name_list=dcs_file_name_list)

    if str(get_shanghai_time())[11:13] not in night_run_time:
        # kill冲突process
        [kill_process_by_name(process_name) for process_name in night_run_file_name_list]

    print('监控脚本执行完毕'.center(60, '*'))

def main_2():
    while True:
        auto_run(logs_path, zwm_path, dcs_path)
        print(' Money is on the way! '.center(100, '*'))
        sleep(15)

if __name__ == '__main__':
    main_2()