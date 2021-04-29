# -*- coding: utf-8 -*-

import allure

from Params.params import Basic
from Config.Config import Config
from Commom import Request
from Commom import Consts
from Commom import Assert


class TestBasic:

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Basic')
    def test_basic_01(self, action):
        """
            用例描述：未登陆状态下查看基础设置
        """
        conf = Config()
        data = Basic()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        response = request.get_request(api_url, params[0], headers[0])

        assert test.assert_code(response['code'], 401)
        assert test.assert_body(response['body'], 'error', u'继续操作前请注册或者登录.')
        assert test.assert_time(response['time_consuming'], 100)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Basic')
    def test_basic_02(self, action):
        """
            用例描述：登陆状态下查看基础设置
        """
        conf = Config()
        data = Basic()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[1]
        response = request.post_request(api_url, params[1], headers[1])

        assert test.assert_code(response['code'], 401)
        assert test.assert_text(response['text'], '{"error":"继续操作前请注册或者登录."}')
        Consts.RESULT_LIST.append('True')
