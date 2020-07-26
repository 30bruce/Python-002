# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Homework2Pipeline:
    def process_item(self, item, spider):
        title, movie_type, plan_date = map(item.get, ('title', 'movie_type', 'plan_date'))
        output = f'{title}\n{movie_type}\n{plan_date}\n\n'
        with open('./maoyantop10_2.csv', 'a+', encoding='utf-8') as f:
            f.write(output)
        return item
