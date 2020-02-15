from peewee import *

#
# instalacja peewee:
# `conda install -c conda-forge peewee `
# trzeba też doinstalować driver do postgres:
# ` conda install -c anaconda psycopg2`


db_host = '10.10.0.33'
db_db = 'student'
db_user = 'student'
db_pass = 'wsiz#1234'

db = PostgresqlDatabase(db_db, user=db_user, password=db_pass, host=db_host, port=5432)
print(f'Using database [{db_db}] on {db_user}@{db_host}')


class BaseModel(Model):
    class Meta:
        database = db
        schema = 'xxx'


class FakeUser(BaseModel):
    id = AutoField()
    name = TextField()
    city = TextField()
    country = TextField()
    phone = TextField()
    img_url = TextField()


rrr = FakeUser.select().where(FakeUser.id == 6).get()
print(rrr.name)
