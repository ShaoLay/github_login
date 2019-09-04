# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']

    def start_requests(self):
        str_cookies = '_octo=GH1.1.2033338529.1562826053; _ga=GA1.2.2037473805.1562826059; _device_id=41b736d6e784c0aac9726648c0761359; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; user_session=6H-uhP_EbLot2QkU2An5wJCrK8I2mm8bKRMiwNU4a7lDBgvy; __Host-user_session_same_site=6H-uhP_EbLot2QkU2An5wJCrK8I2mm8bKRMiwNU4a7lDBgvy; logged_in=yes; dotcom_user=ShaoLeei; _gh_sess=TWRSNVZRdXVzVlJGZXNkSDVSSG1CSHpxbnNvTGQ4YWZKRmlHUnowRVlwemZQUkVTTkF4OG9kR205UjRQL09CV2xZcnBtV3ZKK2NEeENSdXprcVhXRm1zS0tWRlQ4Rno0TUgxUjRzOTloVHpiclY5SnRFalBwVlZwODJMalN2V0NXZFhESWlBdmp0U3paK2h6VnZQb2hjL0oyOS9sc2Q4M3hleW95L1JjNUk3azQ2R0o2a3lzZk9ZaG9aM1pyT3lkOG1uL09reHFURHA3QUdhS0hFb3FCajdtdlVVQ2psR2FwZGtHMngwTzBudDNqMzF6MHFndlg3WDFSMVhaZE9ZQzRnOFpTMHBSQ1ZubjlrR1Q5QkQ3TVVGbllmWmlMSFFKVHZFcndDdTlLRjR5YUJ1dUFQYmRhR3BJR3FMaTRzWnR5V3JXOFcvTmNaU05aU1FWQmhzVVU2aWJxQmk3MTNOakFVQkdJZi9SaS9vPS0tR3dpM2szUmZKbXhpR0QrRWp1M3c0dz09--7e9299d913f1a67c452b41d18e97d25598f74471'
        dict_cookies = {
            i.split('=')[0]: i.split('=')[1] for i in str_cookies.split("; ")
        }

        for url in self.start_urls:
            yield scrapy.Request(url, cookies=dict_cookies)

    def parse(self, response):

        with open("login.html", 'w') as f:
            f.write(response.body.decode())

