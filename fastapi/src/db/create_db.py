import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from core.config import settings

try:
    # Подключение к существующей базе данных
    conn = psycopg2.connect(user=settings.postgres.user,
                            password=settings.postgres.password,
                            host=settings.postgres.host,
                            port=settings.postgres.port)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()
    sql_create_database = f'create database {settings.postgres.dbname}'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
