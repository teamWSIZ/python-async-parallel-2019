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


def as_list_dict(entities):
    return [e.__dict__['__data__'] for e in entities]


def as_dict(entity):
    """
        Converts a single Entity to json
    """
    return entity.__dict__['__data__']


def get_all_users():
    return as_list_dict(FakeUser.select().where(FakeUser.id < 30))


def get_all_users_with_name_prefix(prefix):
    return as_list_dict(FakeUser.select().where(FakeUser.name.startswith(prefix)))

# print(get_all_users())

# user6 = FakeUser.select().where(FakeUser.id == 6).get()
# print(as_dict(user6))
# update:
# user6.city = 'Katowice'
# user6.save()


# users = FakeUser.select().where(FakeUser.country == 'Austria',
#                                 FakeUser.phone.startswith('52-'))
# for u in as_list_dict(users):
#     print(u)

# create
# user_x = FakeUser(name='Alpa',city='Katowice',country='Poland',phone='+666')
# user_x.save()

# saved_user = FakeUser.select().where(FakeUser.name == 'Alpa').get()
# print(as_dict(saved_user))


# FakeUser.delete_by_id(6)  # wycinanie usera po unikalnum id
# w = FakeUser.delete().where(FakeUser.phone.startswith('84-')).execute()
# print(w)    # liczba usuniętych rekordów
