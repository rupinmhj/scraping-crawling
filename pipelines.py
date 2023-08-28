# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

# scraped data-> Item container ->Pipeline ->Sql/Mongo database

import mysql.connector
class QuotetutorialPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="20771006",
            database="myquotes"
        )
        self.curr=self.conn.cursor()

    def create_table(self):
       self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")

       self.curr.execute("""
    CREATE TABLE IF NOT EXISTS quotes_tb (
        title TEXT,
        author TEXT,
        tag TEXT
    )
""")

      
    def store_db(self,item):
        self.curr.execute("""insert into quotes_tb values (%s,%s,%s)""",(
            item['title'][0],
            item['author'][0],

         
            item['tags'][0:5],

        ))   
        self.conn.commit() 
    def process_item(self, item, spider):
        self.store_db(item)
        return item
