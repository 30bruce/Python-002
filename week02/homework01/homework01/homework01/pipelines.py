# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from homework01.db_conf import db_info
from homework01.mysql_helper import ConnDB


class Homework01Pipeline:
    def process_item(self, item, spider):
        origin_ip = item.get('origin_ip')
        print('process_item', item)
        if origin_ip:
            db = ConnDB(db_info)
            db.insert_data(origin_ip)
        return item
