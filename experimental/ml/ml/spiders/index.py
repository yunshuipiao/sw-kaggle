#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: index.py

@desc:

@hint:
"""
import scrapy
import json
from scrapy.http import FormRequest
import pandas as pd
from bs4 import BeautifulSoup
from scrapy import signals


class ML(scrapy.Spider, object):
    page = 1
    name = 'ml'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true',
    }
    citys = ['101010100', '101280600', '101280100', '101020100', '101210100']
    filename = './boss/first.csv'
    result_row = []

    def start_requests(self):
        for city in self.citys:
            url = 'https://www.zhipin.com/c' + city + '/?query=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0'
            request = scrapy.Request(url=url, callback=self.parse, headers=self.headers)
            yield request

    def parse(self, response):
        print(response.url)
        soup = BeautifulSoup(response.body, 'lxml')
        for s in soup.select('.item'):
            position = s.select_one('div > div > h4').text
            salary = s.select_one('div > div > span').text
            company = s.select_one('div > div:nth-of-type(2)').text
            location = s.select_one('div > div:nth-of-type(3) > em:nth-of-type(1)').text
            experience = s.select_one('div > div:nth-of-type(3) > em:nth-of-type(2)').text
            education = s.select_one('div > div:nth-of-type(3) > em:nth-of-type(3)').text
            df = pd.DataFrame({
                'position': position,
                'company': company,
                'salary': salary,
                'location': location,
                'experience': experience,
                'education': education,
            }, index=[0])
            self.result_row.append(df)





    @classmethod
    def from_crawler(cls, crawler, **kwargs):
        # This method is used by Scrapy to create your spiders.
        print('from_crawler')
        s = cls()
        crawler.signals.connect(s.spider_close, signal=signals.spider_closed)
        return s

    def spider_close(self):
        print('spider  close--------')
        result = pd.concat(self.result_row)
        print("result")
        result.to_csv(self.filename, index=False)






