import apt


class AdvSysApt:
    def __init__(self):
        self.cache = apt.Cache()

    def do_update(self):
        try:
            self.cache.update()
            self.cache.open(None)
        except apt.cache.LockFailedException:
            print("[!] Privilege required root")
            return False
        return True

    def do_upgrade(self):
        self.cache.upgrade(True)
        self.cache.cache_pre_change()
        chgs = self.cache.get_changes()
        for items in chgs:
            print(items)
        if len(chgs) > 0:
            ans = input("Do you want upgrade system? (y/[n]) > ")
            if ans in ['y', 's', 'Y', 'S']:
                print("[+] Upgrade system")
                self.cache.fetch_archives()
                self.cache.commit(apt.progress.base.AcquireProgress(),
                                  apt.progress.base.InstallProgress())
            else:
                self.cache.clear()
                self.cache.close()
