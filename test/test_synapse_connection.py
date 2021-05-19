import unittest
import pyodbc
import keyring
import socket


class TestSynapseConnection(unittest.TestCase):
    @unittest.skipUnless(socket.gethostname() == "portrisk-vm-2", "run this in vm only")
    def test_first_ever(self):
        # given
        dsn = 'PortriskSynapse'
        user = 'sqladminuser'
        pwd = keyring.get_password("synapse", user)
        # when
        conn_str = 'DSN={}; UID={}; PWD={}'.format(dsn, user, pwd)
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT cusip from dbo.exp where cusip='00037BAB8'")
        # then
        cusips = [row.cusip for row in cursor.fetchall()]
        self.assertListEqual(cusips, ["00037BAB8"])


if __name__ == '__main__':
    unittest.main()
