from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, DateTime, String
from sqlalchemy.orm.strategy_options import load_only

Base = declarative_base()

class Company(Base):
    __tablename__ = 'test_3'
    url = Column(String(100), primary_key=True)
    inn = Column(Text)
    ogrn = Column(Text)
    phones = Column(String())
    emails = Column(String())
    sites = Column(String())
    title = Column(String())
    description = Column(String())
    viber = Column(String())
    whatsapp = Column(String())
    telegram = Column(String())
    facebook = Column(String())
    instagram = Column(String())
    vk = Column(String())
    youtube = Column(String())
    regions = Column(String())
    http_status = Column(Integer())
    updated = Column(DateTime())
    done = Column(Integer())

    def __init__(self, item):
        for key in item.__dict__.keys():
            if item.__dict__[key]:
                tt = item.__dict__[key]
                if isinstance(item.__dict__[key],(list, set)):
                    self.__dict__[key] =','.join(item.__dict__[key])
                else:
                    self.__dict__[key] = item.__dict__[key]


class database_Alchemy(object):
    def __enter__(self):
        self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/test?charset=utf8mb4', echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/test?charset=utf8mb4', echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save_item(self, entity_list):
        for entity in entity_list:
            self.session.add(Company(entity))
            self.session.commit()



    def clean_dict(self, ent):
        dict((k,v) for k,v in ent.items() if v)
        for k, v in ent.items():
            if isinstance(v,(list,set)):
                ent[k] = ','.join(v)
        return ent


    def update_item(self, ent_list):
        for ent in ent_list:
            url = ent.pop('url')
            s = self.clean_dict(ent)
            r = self.session.query(Company).filter(Company.url == url).update(s)
            self.session.commit()

    def get_unchecked(self, limit: int):
        return self.session.query(Company.url).filter(Company.done == 1).limit(limit).all()


    def close_db(self):
        self.session.close()
