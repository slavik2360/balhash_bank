# Local
from database.core import Connection
from database.models.accounts import Account
import datetime


class Card:
    """Object from db. Cards"""

    id: int
    ccv: str
    number: str
    account: Account
    is_active: str
    date_end: str
    pin: str

    @staticmethod
    def create(
        conn: Connection,
        number: str,
        account: Account,
        cvv: str,
        date_end: str,
        is_active: str,
        pin: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO users(
                    number,
                    account_id,
                    cvv,
                    date_end,
                    is_active,
                    pin
                )
                VALUES (
                    '{number}',
                    '{account.id}',
                    '{cvv}',
                    '{date_end}',
                    '{is_active}',
                    '{pin}'
                )
                """
            )
    @staticmethod
    def get_all(conn: Connection) -> 'Card':

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM cards
                """
            )
            return cur.fetchall()
        
    @staticmethod
    def search_by_columnName(conn: Connection, nameColumn: str, data: any) -> 'Card':
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