# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String


Base = declarative_base()


class EntityBook(Base):
    __tablename__ = 'entitybooks'
    id = Column(Integer, primary_key=True)
    title = Column(String(60))
    author = Column(String(30))

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return "<Data %s, %s, %s>" % (self.title, self.author)


class WebScraperPipeline(object):
    def __init__(self):
        self.engine = create_engine('mysql://root:root@localhost:3306/examle?charset=utf8', echo=True)
        Base.metadata.create_all(self.engine)

    def process_item(self, item, spider):
        book = EntityBook(item['title'], item['author'])
        self.session.add(book)
        print('процесс записи запущен')

    def close_spider(self, spider):
        print('паук закрыт')
        self.session.commit()
        self.session.close()

    def open_spider(self, spider):
        print('паук открыт')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

