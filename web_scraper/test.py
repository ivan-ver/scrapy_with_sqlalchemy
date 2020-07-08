from web_scraper.other.db import Writer_DB
from datetime import datetime

ent1 = {
    'url':'http://python-3.ru/page/instrukcija-with-as-v-python',
    'title':('кортеж','кортеж'),
    'author':'sdfsef1',
    'timedate': datetime.now(),
    'done': 1
}

ent2 = {
    'url':'https://mail.ru/',
    'title':['список','список'],
    'author':'sdfsef2',
    'timedate': datetime.now(),
    'done': 2
}

ent3 = {
    'url':'https://mail.ru/4564813/',
    'title':[],
    'author':'',
    'timedate': datetime.now(),
    'done': 3
}

ent4 = {
    'url':'https://docs.sqlalchemy.org/en/13/errors.html#error-9h9h',
    'title':set(),
    'author':'sdfsef4',
    'timedate': datetime.now(),
    'done': 4
}

ent5 = {
    'url':'https://sqla3/err5555555555',
    'title':('11111111','111111'),
    'author':'11111111',
    'timedate': datetime.now(),
    'done': 11
}

ent6 = {
    'url':'https://66666666666666666666',
    'title':('11111111','111111'),
    'author':'11111111',
    'timedate': datetime.now(),
    'done': 11
}

ent7 = {
    'url':'https://77777777777777',
    'title':('fasrg','111111','gdsrg','rw4g'),
    'author':['11111111', '34wfasdf','3wrasdf'],
    'timedate': datetime.now(),
    'done': 11
}

ent8 = {
    'url':'https://8888888888',
    'title':'',
    'author':'',
    'timedate': datetime.now(),
    'done': 11
}

ent9 = {
    'url':'https:9999999',
    'title':None,
    'author':set(),
    'timedate': datetime.now(),
    'done': 11
}



db = Writer_DB()
# db.save_item([ent1, ent2, ent3, ent4, ent5, ent6, ent7, ent8, ent9])
db.update_item([ent1, ent2, ent3, ent4, ent5, ent6, ent7, ent8, ent9])
db.close_db()


