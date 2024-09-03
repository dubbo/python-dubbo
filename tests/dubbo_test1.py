# -*- coding: utf-8 -*-
"""
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""

import json
import logging
import unittest
from dubbo.common.loggers import init_log
from dubbo.client import DubboClient, ZkRegister

logger = logging.getLogger('python-dubbo')


def pretty_print(value):
    logger.debug(json.dumps(value, ensure_ascii=False, indent=4, sort_keys=True))


class TestDubbo(unittest.TestCase):
    def setUp(self):
        init_log()  # 初始化日志配置，调用端需要自己配置日志属性

        zk = ZkRegister('127.0.0.1:2181')
        self.dubbo = DubboClient('org.apache.dubbo.springboot.demo.DemoService', zk_register=zk)
        # self.dubbo = DubboClient('me.hourui.echo.provider.Echo', host='127.0.0.1:20880')

    def tearDown(self):
        # Do something to clear the test environment here.
        pass

    # @unittest.skip('skip base test')
    def test(self):
        dubbo = self.dubbo
        pretty_print(dubbo.call('sayHello', '张老师'))



if __name__ == '__main__':
    test = TestDubbo()
    test.test()
    # test.test_performance()
    # unittest.main()
