import os
import unittest
import tempfile
import sys
import inspect
# inspired by https://stackoverflow.com/a/11158224
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import readport


def head(filename, n):
    with open(filename) as f:
        h = [next(f) for x in range(n)]
    return h


class ReadportTestCase(unittest.TestCase):

    def test_read_var_factor_file__file_is_none(self):
        config = readport.Config()
        with self.assertRaisesRegex(TypeError, "^Invalid type of config.varFactorFile$"):
            readport.read_var_factor_file(config)

    def test_read_var_factor_file__file_is_missing(self):
        config = readport.Config()
        config.varFactorFile = "x"
        with self.assertRaisesRegex(FileNotFoundError, "No such file or directory: 'x'"):
            readport.read_var_factor_file(config)

    def test_read_var_factor_file_base_case(self):
        config = readport.Config()
        config.varFactorFile = "../data/input/var_factor"
        factor_ids = readport.read_var_factor_file(config)
        self.assertTrue(factor_ids)
        self.assertGreater(len(factor_ids), 15_000)
        self.assertEqual(factor_ids["USD_3m"], 1)

    def test_readport_invalid_var_factor_file(self):
        with self.assertRaisesRegex(SystemExit, "2"):
            readport.main(["--var_factor_file", "x"])

    def test_readport_missing_var_factor_file(self):
        with self.assertRaisesRegex(SystemExit, "2"):
            readport.main([])

    def test_readport_base_case(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            readport.main(["--var_factor_file", "../data/input/var_factor",
                           "--out_dir", temp_dir,
                           "-l",
                           "../data/input/exposures-small-sample.txt"])
            exp_file = f"{temp_dir}/Exp.csv"
            self.assertTrue(os.path.isfile(exp_file))
            self.assertListEqual(head(exp_file, 2),
                                 ["e_cusip_id,cusip,dt,purpose,base_ccy,mkt_value,notional\n",
                                  "1,00037BAB8,2019-09-27,P100,USD,12854.1,12854.1\n"])
            sys_file = f"{temp_dir}/Sys.csv"
            self.assertTrue(os.path.isfile(sys_file))
            self.assertListEqual(head(sys_file, 2),
                                 ["s_cusip_id,fid,exp\n",
                                  "1,1657,6916.1249\n"])
            idio_file = f"{temp_dir}/Idio.csv"
            self.assertTrue(os.path.isfile(idio_file))
            self.assertListEqual(head(idio_file, 2),
                                 ["i_cusip_id,issuer,issue,model,sp_exp,idio_risk\n",
                                  "1,F75317,00037BAB8,5957,12854.1,359.4441\n"])


if __name__ == '__main__':
    unittest.main()
