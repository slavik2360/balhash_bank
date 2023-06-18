# Python
from decouple import config
import datetime

# Local
from database.core import Connection
from database.models.users import User
from database.models.accounts import Account
from database.models.cards import Card


my_connection: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)


if __name__ == '__main__':
    my_connection.create_tables()
    # User.create(
    #     conn=my_connection.conn,
    #     first_name='Bob',
    #     last_name='Flint',
    #     date_of_birth=datetime.datetime(
    #         year=1998,
    #         month=5,
    #         day=15
    #     ),
    #     iin='980515123234',
    #     phone_number='7009006050'
    # )

    print(User.get_all(conn=my_connection.conn))
    # print(User.search_by_columnName(conn=my_connection.conn, nameColumn='iin', data='980515123234'))
    # print(User.search_by_columnName(conn=my_connection.conn, nameColumn='id', data='1'))

    # print(Account.get_all(conn=my_connection.conn))
    # print(Account.search_by_columnName(conn=my_connection.conn, nameColumn='balance', data='100'))

    # print(Card.get_all(conn=my_connection.conn))
    # print(Card.search_by_columnName(conn=my_connection.conn, nameColumn='cvv', data='123'))