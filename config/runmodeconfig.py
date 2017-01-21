#!/usr/bin/env python
# -*- coding:utf-8 -*-
import configparser
from globalpkg.log import logger


class RunModeConfig:
    """
    日志配置类 configparser
    配置文件的格式是： []包含的叫section,section 下有option=value这样的键值
    如果section下有多个键值对，调用的写法：self.projects = config['PROJECTS']['projects']
    自带自省功能
    """
    def __init__(self, run_mode_conf):
        config = configparser.ConfigParser()

        # 从配置文件中读取运行模式
        config.read(run_mode_conf, encoding='utf-8-sig')
        try:
            self.run_mode = config['RUNMODE']['runmode']
            self.project_mode = int(config['PROJECTS']['project_mode'])
            self.projects = config['PROJECTS']['projects']
            self.testplans = config['PLANS']['plans']
            self.project_of_plans = config['PLANS']['project']
            self.testsuites = config['TESTSUITES']['testsuites']
        except Exception as e:
            logger.error('读取运行模式配置失败：%s' % e)
            exit()

    def get_run_mode(self):
        return  self.run_mode

    def get_project_mode(self):
        return self.project_mode

    def get_projects(self):
        return self.projects

    def get_testplans(self):
        return self.testplans

    def get_project_of_testplans(self):
        return  self.project_of_plans

    def get_testsuits(self):
        return self.testsuites

    #新增
    def get_testcases(self):
        return self.get_testsuits()

    # def get_testcases_id_list(self):
    #     return self.testcases_id_list




