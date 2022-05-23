#!/usr/bin/env python3
from src.packages_tool import CheckResidualPackage
from src.tools import build_options
from src.advsysc import AdvSysApt

if __name__ == '__main__':
    parser = build_options()
    args = parser.parse_args()
    advsys = AdvSysApt()
    if args.a:
        args.p = True
        args.sub = True
    if args.p:
        print("[+] Cleaning apt")
        advsys.cache.clear()
        print("[+] Checking: Packages")
        crp = CheckResidualPackage()
        if crp.check_residual_config():
            print("[!] Found residual configuration")
            crp.do_autoremove()
    if args.sub:
        print("[+] Checking: Update")
        if advsys.do_update():
            advsys.do_upgrade()
    if True not in args.__dict__.values():
        parser.print_help()
