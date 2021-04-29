# -*- coding: utf-8 -*-

import allure

from Params.params import Personal
from Config.Config import Config
from Commom import Request
from Commom import Consts


class TestPersonal:

    @allure.feature('Personal')
    @allure.severity('blocker')
    @allure.story('Personal')
    def test_personal_01(self, action):
        """
            用例描述：未登陆状态下更新Personal个人简介
        """
        conf = Config()
        data = Personal()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://'+host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url+urls[0]
        response = request.post_request(api_url, params[0][0], headers[0])
        assert response['code'] == 200
        Consts.RESULT_LIST.append('True')

    @allure.feature('Personal')
    @allure.severity('blocker')
    @allure.story('Personal')
    def test_personal_02(self, action):
        """
            用例描述：登陆状态下更新Personal个人简介
        """
        conf = Config()
        data = Personal()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://'+host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url+urls[1]
        response = request.post_request(api_url, params[1][0], headers[1])
        assert response['code'] == 200
        Consts.RESULT_LIST.append('True')
