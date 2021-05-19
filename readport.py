#!/usr/bin/env python3
#
"""readport.py
blah
"""

import argparse
import csv
import datetime
import json
import logging.config
import sys
import time
from datetime import datetime
import pathlib as pl
import errno
import os

# %% Logging
# log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
# logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logger = logging.getLogger('readport')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class Config:
    """
    Configuration defaults.  Overridable.
    """
    nLim = None
    lSep = True
    infile = ''
    agg = "vector"
    varFactorFile = None
    outDir = None


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def cli_parse(argv):
    """
    Parse commandline.
    """
    config = Config()
    parser = argparse.ArgumentParser(add_help=False, description='bcm Neural Style Transfer')
    parser.add_argument('-l', '--lSep', action='store_true')
    parser.add_argument('-n', '--nLim', dest='nLim', action='store')
    parser.add_argument('--var_factor_file', dest='varFactorFile', action='store',
                        type=argparse.FileType('r'), required=True)
    parser.add_argument('--out_dir', dest='outDir', action='store', type=dir_path, default=".")
    parser.add_argument('Infile',
                        type=argparse.FileType('r'),
                        help='the portfolio input file (json)')
    args = parser.parse_args(argv)

    config.infile = args.Infile.name
    config.lSep = args.lSep
    config.nLim = 0 if (args.nLim is None) else int(args.nLim)
    config.varFactorFile = args.varFactorFile.name
    config.outDir = args.outDir

    args.Infile.close()
    args.varFactorFile.close()
    return config


def read_portfolios(config):
    dicts = []
    file_name = config.infile
    lsep = config.lSep

    with open(file_name) as f:
        if lsep:
            for line in f:
                dicts.append(json.loads(line))
        else:
            s = f.read().split('}{')
            # noinspection PyTypeChecker
            for i in range(len(s)):
                dicts.append(json.loads(s[i]))
    logger.debug("ReadPortfolios: len(dicts) = {}".format(len(dicts)))
    return dicts


def parse_portfolios(dicts, fids):
    v_exp = []
    v_sys = []
    v_idio = []

    eid = 1
    for d in dicts:
        cusip = d.get("cusip")
        dt = datetime.strptime(d.get("date"), '%Y%m%d').strftime('%Y-%m-%d')
        purpose = d.get("purpose")
        base_ccy = d.get("base_ccy")
        mkt_value = d.get("mkt_value")
        notional = d.get("notional")
        cusip_id = eid
        eid += 1
        tup = (cusip_id, cusip, dt, purpose, base_ccy, mkt_value, notional)
        v_exp.append(tup)

        systematic = d.get("systematic")
        systematic_cnt = len(systematic)
        # noinspection PyTypeChecker
        for i in range(systematic_cnt):
            si = systematic[i]
            sys_ftag = si.get("ftag")
            sys_exp = si.get("exposure")
            sys_fid = fids[sys_ftag]
            systup = (cusip_id, sys_fid, sys_exp)
            v_sys.append(systup)

        idio = d.get("idio")
        idio_cnt = len(idio)
        # noinspection PyTypeChecker
        for i in range(idio_cnt):
            ii = idio[i]
            issuer = ii.get("issuer")
            sp_risk = ii.get("sp_risk")
            sp_risk_cnt = len(sp_risk)

            # noinspection PyTypeChecker
            for j in range(sp_risk_cnt):
                sprj = sp_risk[j]
                issue = sprj.get("issue")
                model = sprj.get("model")
                sp_exp = sprj.get("sp_exp")
                idio_risk = sprj.get("idio_risk")

                idiotup = (cusip_id, issuer, issue, model, sp_exp, idio_risk)
                v_idio.append(idiotup)

    return v_exp, v_sys, v_idio


def dump_csv_files(config, v_exp, v_sys, v_idio):
    with open(f"{config.outDir}/Exp.csv", "w") as f:
        f.write("e_cusip_id,cusip,dt,purpose,base_ccy,mkt_value,notional\n")
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(v_exp)

    with open(f"{config.outDir}/Sys.csv", "w") as f:
        f.write("s_cusip_id,fid,exp\n")
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(v_sys)

    with open(f"{config.outDir}/Idio.csv", "w") as f:
        f.write("i_cusip_id,issuer,issue,model,sp_exp,idio_risk\n")
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(v_idio)


def read_var_factor_file(config):
    if not isinstance(config.varFactorFile, str):
        raise TypeError("Invalid type of config.varFactorFile")

    if not pl.Path(config.varFactorFile).is_file():
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), config.varFactorFile)
    fids = {}
    with open(config.varFactorFile) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        fid_index = None
        for row in rd:
            if fid_index is None:
                if len(row) > 0 and row[0] == "ftag":
                    x = {k: v for v, k in enumerate(row)}
                    fid_index = x["fid"]
            else:
                if row[0].startswith("ZZ"):
                    continue
                fids[row[0]] = int(row[fid_index])
    return fids


def main(argv):
    config = cli_parse(argv)
    factor_ids = read_var_factor_file(config)
    t1 = time.time()
    dicts = read_portfolios(config)
    t2 = time.time()
    logger.info("ReadPortfolios elapsed = {}".format(t2 - t1))

    logger.debug(dicts)
    n_ports = len(dicts)
    # noinspection PyTypeChecker
    if n_ports == 0:
        print("no portfolios found in {} or missing -l\n".format(config.infile))
        return 1
    print("found {} portfolios\n".format(n_ports))
    # %% Parse Portfolios
    t1 = time.time()
    v_exp, v_sys, v_idio = parse_portfolios(dicts, factor_ids)
    logger.info("Parsed: len(v_exp) = {}, len(v_sys) = {}, len(v_idio) = {}".format(len(v_exp), len(v_sys), len(v_idio)))
    t2 = time.time()
    logger.info("ParsePortfolios elapsed = {}".format(t2 - t1))
    if config.nLim != 0:
        for i in range(config.nLim):
            print("{}".format(v_exp[i]))
    # %% DumpCSVs
    t1 = time.time()
    dump_csv_files(config, v_exp, v_sys, v_idio)
    t2 = time.time()
    logger.info("DumpCSVs elapsed = {}".format(t2 - t1))


# %% main
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
