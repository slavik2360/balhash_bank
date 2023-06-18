# Python
import datetime

# Local
from database.core import Connection


class User:
    """Object from db. User."""

    id: int
    first_name: str
    last_name: str
    date_of_birth: datetime.datetime
    iin: str
    phone_number: str

    @staticmethod
    def create(
        conn: Connection,
        first_name: str,
        last_name: str,
        date_of_birth: datetime,
        iin: str,
        phone_number: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO users(
                    first_name,
                    last_name,
                    date_of_birth,
                    iin,
                    phone_number
                )
                VALUES (
                    '{first_name}',
                    '{last_name}',
                    '{date_of_birth}',
                    '{iin}',
                    '{phone_number}'
                )
                """
            )

    @staticmethod
    def get_all(conn: Connection) -> 'User':

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM log
                """
            )
            return cur.fetchall()
        
    @staticmethod
    def search_by_columnName(conn: Connection, nameColumn: str, data: any) -> 'User':
        try:
            with conn.cursor() as cur:
                if isinstance(nameColumn, str):
                    cur.execute(
                        f"""
                        SELECT * FROM users WHERE {nameColumn} = '{data}'
                        """
                    )
                    return cur.fetchall()
        except Exception as e:
            print(f'ERROR--> {e}')