import json
import mysql.connector
import pymongo
from scrapy import Request,Spider
from douban.items import DoubanItem,DoubanProfession
from douban import settings

"""
这个网页有几类信息，这里爬取的是台词、演员导演、电影信息3类，分别存储到mysql数据库和mongodb数据库。
因为网页是动态加载的，这里用的是分析ajax的方法爬取的。

"""

class thespider(Spider):
    name = 'douban'
    allowed_domains = ["www.douban.com"]
    url = 'https://movie.douban.com/ithil_j/activity/movie_annual2016/widget/1'

    def start_requests(self):
        yield Request(self.url,callback=self.get_items)
        for i in range(2, 71):
            url = 'https://movie.douban.com/ithil_j/activity/movie_annual2016/widget/{0}'.format(i)
            yield Request(url, callback=self.get_items)


    def get_items(self,response):
        result =json.loads(response.text)
        if result.get('res').get('subjects') == []:#这个if获取的是台词
            text = result.get('res').get('payload').get('text')
            title = result.get('res').get('subject').get('title')
            s = Sql()
            s.save_to_mysql(title,text)
            pass

        elif result.get('res').get('subjects') == None:#这个if获取的是演员、导演
            itemslist = result.get('res').get('people')
            print(response.url)
            print(itemslist)
            item = DoubanProfession()
            item['category'] = result.get('res').get('payload').get('title')
            s = Sql
            for items in itemslist:
                for field in item.fields:
                    if field in items.keys():
                        item[field] = items.get(field)
                print(item)
                s.save_to_mongo2(item)

        else:
            itemslist = result.get('res').get('subjects')#最后这里获取的是电影信息
            item = DoubanItem()
            item['category'] = result.get('res').get('payload').get('title')
            for items in itemslist:
                for field in item.fields:
                    if field in items.keys():
                        item[field] = items.get(field)
                yield item

cnx = mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='test')
cur = cnx.cursor(buffered=True)
class Sql:
    @classmethod
    def save_to_mysql(cls,title,text):#台词保存到了mysql数据库
        sql = 'INSERT INTO doubandianying(`title`,`text`) VALUES (%(title)s,%(text)s)'
        value = {
            'title':title,
            'text':text
        }
        cur.execute(sql,value)
        cnx.commit()

    @classmethod
    def save_to_mongo2(cls,result):#演员、导演保存到mongodb数据库
        client = pymongo.MongoClient(settings.MONGO_URL)
        db = client[settings.MONGO_DB]
        MONGO_TABLE = 'doubanyanyuan'
        try:
            if db[MONGO_TABLE].update({'name': result['name']}, {'$set': dict(result)}, True):
                print('{0} 存储成功。'.format(result['name']))
        except:
            print('{0}存储失败。'.format(result['name']))











