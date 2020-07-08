from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, DateTime, String


Base = declarative_base()

class Book(Base):
    __tablename__ = 'test_3'
    url = Column(String(100), primary_key=True)
    title = Column(Text)
    author = Column(Text)
    timedate = Column(DateTime)
    done = Column(Integer)

    def __init__(self, url, title, author, timedate, done):
        if isinstance(title, tuple) or isinstance(title, set) or isinstance(title, list):
            title = ','.join(title)
        if isinstance(author, tuple) or isinstance(author, set) or isinstance(author, list):
            author = ','.join(author)

        self.url = url
        self.title = title
        self.author = author
        self.timedate = timedate
        self.done = done
        pass

    def __repr__(self):
        return "<User('%s','%s','%s','%d','%d')>" % (self.url, self.title, self.author, self.timedate, self.done)


class Writer_DB(object):

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/test?charset=utf8mb4', echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save_item(self, ent_list):
        for ent in ent_list:
            ent = Book(ent['url'],ent['title'],ent['author'],ent['timedate'],ent['done'])
            self.session.add(ent)
            self.session.commit()

    def update_item(self, ent_list):
        for ent in ent_list:

            if isinstance(ent['title'], tuple) or isinstance(ent['title'], set) or isinstance(ent['title'], list):
                ent['title'] = ','.join(ent['title'])

            if isinstance(ent['author'], tuple) or isinstance(ent['author'], set) or isinstance(ent['author'], list):
                ent['author'] = ','.join(ent['author'])

            r = self.session.query(Book).filter(Book.url == ent['url']).first()
            r.title = ent['title']
            r.author = ent['author']
            r.timedate = ent['timedate']
            r.done = ent['done']
            self.session.commit()

    def close_db(self):
        self.session.close()
