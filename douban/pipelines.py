# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from douban import settings

class DoubanPipeline(object):
    def process_item(self, item, spider):
        self.save_to_mongo1(item)

    def save_to_mongo1(self,result):#这里保存的是电影的信息
        client = pymongo.MongoClient(settings.MONGO_URL)
        db = client[settings.MONGO_DB]
        try:
            if db[settings.MONGO_TABLE].insert(result):
                print('{0} 存储成功。'.format(result['title']))
        except:
            print('{0}存储失败。'.format(result['title']))


