#!/usr/bin/env python3
import apt
from src.packages_tool import CheckResidualPackage
from src.tools import build_options

if __name__ == '__main__':
    parser = build_options()
    args = parser.parse_args()
    if args.a:
        args.p = True
        args.sub = True
    if args.p:
        print("[+] Checking: Packages")
        crp = CheckResidualPackage()
        if crp.check_residual_config():
            print("[!] Found residual configuration")
            crp.do_autoremove()
        print("[+] Cleaning apt")
        apt.Cache().clear()
    if args.sub:
        print("[+] Checking: Update")
        cache = apt.Cache()
        cache.update()
        cache.fetch_archives()
        print(cache.get_changes())
        if len(cache.get_changes()) > 0:
            print("[+] Upgrade system")
            cache.upgrade()
    if True not in args.__dict__.values():
        parser.print_help()
