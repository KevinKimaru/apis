from peewee import *
#db = SqliteDatabase("C:\\Users\Kevin Kimaru Chege\\Desktop\\db\\apis.db")
from  os import path
ROOT= path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT,"apis.db"))

class User(Model):
    names = CharField()
    email = CharField(unique=True)
    age = IntegerField()
    class Meta:
        database = db

# User.create_table()
# User.create(names="Kevin", email="kkc@gail.com", age=18)
# User.create(names="Liz", email="liz@gail.com", age=16)
# User.create(names="Eric", email="eric@gail.com", age=19)