# coding=utf-8

"""
@author: Reggie
@time:   2018/08/10 20:29
"""

import MySQLdb
import logging


class DB():
    """Common Mysql method"""

    def __init__(self, config):
        config = self.__parse_config(config)
        print("\r\nMysql Config::::", config, '\r\n')

        try:
            self.conn = self.connection(config)
        except Exception as e:
            logging.error(e)

    def __parse_config(self, config):
        alias = {'database': "db", 'password': "passwd"}

        for k, v in alias.items():
            if config.get(k):
                config[v] = config[k]
                del config[k]
        config["connect_timeout"] = 3

        return config

    @staticmethod
    def connection(config):
        """
        Create mysql connection
        """
        return MySQLdb.Connect(**config)

    def query(self, sql):
        """
        Query from mysql

        Args:
            sql:    sql language

        Returns:
             1:    data.
             0:    Failed.
        """
        cursor = self.conn.cursor()

        # cursor.execute(sql)
        cursor.execute(sql)

        ret = cursor.fetchall()
        cursor.close()
        # self.conn.close()
        return ret

    def update(self, sql):
        """
        Update mysql data

        Args:
            sql:    sql language

        Returns:
             1:    Success.
             0:    Failed.
        """
        cursor = self.conn.cursor()

        cursor.execute(sql)

        self.conn.commit()
        cursor.close()
        # self.conn.close()
        return 0

    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    """Demo"""
    from conf.config import Config

    db = DB(Config.DB_CONFIG)
    print(db.query("show tables;"))
