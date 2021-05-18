import unittest
import pyodbc

class TestStringMethods(unittest.TestCase):

    def test_first_ever(self):
        # given
        dsn='PortriskSynapse'
        db='portrisk_synapse_workspace_sql_pool'
        user='sqladminuser'
        pwd='PortriskSqlPool!'
        # when
        connStr='DSN={}; UID={}; PWD={}'.format(dsn, user, pwd)
        conn=pyodbc.connect(connStr)
        cursor = conn.cursor()
        cursor.execute("SELECT cusip from dbo.exp where cusip='00037BAB8'")
        # then
        cusips = [row.cusip for row in cursor.fetchall()]
        self.assertListEqual(cusips, ["00037BAB8"])

if __name__ == '__main__':
    unittest.main()
