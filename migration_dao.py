import pymysql.cursors
from conf import config


class Dao:
    def __init__(self):

        pass

    def is_exist_table(self, table_name):

        result = False
        tables = self.show_tables()

        for i in tables:
            if table_name in i.values():
                result = True
                break
        return result

    def show_tables(self):
        results = []
        # Connect to the database
        connection = pymysql.connect(host=config.DATABASE_CONFIG['host'],
                                     user=config.DATABASE_CONFIG['user'],
                                     password=config.DATABASE_CONFIG['password'],
                                     db=config.DATABASE_CONFIG['db'],
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = 'show tables'
                cursor.execute(sql)
                results = cursor.fetchall()

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        finally:
            connection.close()

        return results

    def trucate(self, table_name):

        result = 0

        # Connect to the database
        connection = pymysql.connect(host=config.DATABASE_CONFIG['host'],
                                     user=config.DATABASE_CONFIG['user'],
                                     password=config.DATABASE_CONFIG['password'],
                                     db=config.DATABASE_CONFIG['db'],
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = 'truncate ' + table_name
                result = cursor.execute(sql)
                print('result: ' + str(result))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        finally:
            connection.close()

        return result

    def insert(self, query_sql, values):

        result = 0

        # Connect to the database
        connection = pymysql.connect(host=config.DATABASE_CONFIG['host'],
                                     user=config.DATABASE_CONFIG['user'],
                                     password=config.DATABASE_CONFIG['password'],
                                     db=config.DATABASE_CONFIG['db'],
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = query_sql
                result = cursor.execute(sql, values)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        finally:
            connection.close()

        return result

    def create_table(self, table_name, columns, column_type="VARCHAR(1000)"):

        columns_str = (" " + column_type + ", ").join(columns) + (" " + column_type + " ")
        # print(columns_str)

        result = 0

        # Connect to the database
        connection = pymysql.connect(host=config.DATABASE_CONFIG['host'],
                                     user=config.DATABASE_CONFIG['user'],
                                     password=config.DATABASE_CONFIG['password'],
                                     db=config.DATABASE_CONFIG['db'],
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = """
                    CREATE TABLE """ + table_name + """ (
                           """ + columns_str + """
                    );
                    """
                # print(sql)

                result = cursor.execute(sql)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print("--- table(" + table_name + ") created!")
        finally:
            connection.close()

        return result