# coding:utf-8

'''
@author = super_fazai
@File    : tmux_ops_server.py
@connect : superonesfazai@gmail.com
'''

"""
自动化tmux 脚本
"""

from sys import path as sys_path
sys_path.append('..')
from fzutils.spider.async_always import *

class TmuxOps(AsyncCrawler):
    def __init__(self):
        AsyncCrawler.__init__(
            self,
        )
        self.python_version_cmd = 'python3'
        self.spike_path = '~/myFiles/python/my_flask_server/spike_everything'
        self.pintuan_path = '~/myFiles/python/my_flask_server/pintuan_script'
        self.real_path = '~/myFiles/python/my_flask_server/real-times_update'
        self.logs_path = '~/myFiles/python/my_flask_server/logs'
        self.zwm_path = '~/myFiles/python/my_flask_server'
        self.ip_pool_path = '~/myFiles/tri_party_agent_ip_pool'
        self.fck_run_path = '~/myFiles/python/my_flask_server/just_fuck_run'
        self.dcs_path = '~/myFiles/python/my_flask_server/distribute_jobs'
        self.cp_path = '~/myFiles/python/my_flask_server/cp'

    async def _fck_run(self):
        print('开始执行tmux 命令集合...')
        tmux_cmd_list = await self.get_tmux_cmd_list()
        bulk_execute_order_cmd_by_tmux_cmd_list(
            tmux_cmd_list=tmux_cmd_list,)
        print('执行完毕!')

    async def get_tmux_cmd_list(self) -> list:
        """
        :return:
        """
        return [
            {
                'page_name': 'ip_pool',
                'cmd': 'cd {} && {} proxy_checker_plus.py'.format(
                    self.ip_pool_path,
                    self.python_version_cmd,
                ),
                'delay_time': 2,
            },
            {
                'page_name': 'ip_server',
                'cmd': 'cd {} && {} server.py'.format(
                    self.ip_pool_path,
                    self.python_version_cmd,
                ),
                'delay_time': 20,
            },
            {
                'page_name': 'new_my_server',
                'cmd': 'cd {} && {} new_my_server.py'.format(
                    self.zwm_path,
                    self.python_version_cmd,
                ),
                'delay_time': 2,
            },
        ]

    def __del__(self):
        collect()

def main():
    tmux_ops = TmuxOps()
    loop = get_event_loop()
    loop.run_until_complete(tmux_ops._fck_run())

if __name__ == '__main__':
    main()