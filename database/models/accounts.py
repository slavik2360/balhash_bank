# Local
from database.core import Connection
from database.models.users import User


class Account:
    """Object from db. Accounts"""

    id: int
    number: str
    owner: User
    balance: str
    my_type: str

    @staticmethod
    def create(
        conn: Connection,
        number: str,
        owner: int,
        balance: str,
        my_type: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO users(
                    number,
                    owner_id,
                    balance,
                    type
                )
                VALUES (
                    '{number}',
                    '{owner.id}',
                    '{balance}',
                    '{my_type}'
                )
                """
            )

    @staticmethod
    def get_all(conn: Connection) -> 'Account':

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM accounts
                """
            )
            return cur.fetchall()
        
    @staticmethod
    def search_by_columnName(conn: Connection, nameColumn: str, data:any) -> 'Account':
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