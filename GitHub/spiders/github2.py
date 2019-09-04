#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Hamdi
import scrapy


class GitHubSpider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login/']

    def parse(self, response):
        utf8 = response.xpath('//*[@id="login"]/form/input[1]/@value').extract_first()
        commit = response.xpath('//*[@id="login"]/form/div[3]/input[3]/@value').extract_first()
        authenticity_token = response.xpath('//*[@id="login"]/form/input[2]/@value').extract_first()
        login = 'javs_shao@163.com'
        password = 'QWERTY0202sl'

        form_data = {
            "utf8": utf8,
            "commit": commit,
            "authenticity_token": authenticity_token,
            "login": login,
            "password": password,
        }

        login_url = 'https://github.com/session'

        yield scrapy.FormRequest(login_url, formdata=form_data, callback=self.home_parse)

    def home_parse(self, response):
        with open("login2.html", 'w') as f:
            f.write(response.body.decode())
