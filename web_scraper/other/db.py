from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Book(Base):
    __tablename__ = 'entbooks'
    id = Column(Integer, primary_key=True)
    url = Column(String(100))
    title = Column(String(20))
    author = Column(String(20))

    def __init__(self, url, title, author):
        self.url = url
        self.title = title
        self.author = author

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.url, self.title, self.author)


class writer_db(object):

    def __init__(self):
        self.engine = create_engine('mysql://root:root@localhost:3306/examle', echo=True)
        Base.metadata.create_all(self.engine)

    def process_item(self):
        new_book = Book('123', '123', '123')
        self.session.add(new_book)
        print('процесс записи запущен')

    def close_spider(self):
        print('паук закрыт')
        self.session.commit()
        self.session.close()

    def open_spider(self):
        print('паук открыт')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


wdb = writer_db()
wdb.open_spider()
wdb.process_item()
wdb.close_spider()
