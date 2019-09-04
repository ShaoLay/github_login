#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Hamdi
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github3'
    allowed_domains = ['github.com']

    start_urls = ['https://github.com/login']

    def __init__(self, name=None, **kwargs):
        super(GithubSpider, self).__init__(name=None, **kwargs)
        self.home_parse = None

    def parse(self, response):
        login = "javs_shao@163.com"
        password = "QWERTY0202sl"

        formdata = {
            "login": login,
            "password": password,
        }

        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//*[@id="login"]/form',
            formdata=formdata,
            callable=self.home_parse,
        )

    def home_parse(self, response):
        with open("login3.html", 'w') as f:
            f.write(response.body.decode())