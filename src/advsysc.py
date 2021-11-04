import apt


class AdvSysApt:
    def __init__(self):
        self.cache = apt.Cache()

    def do_update(self):
        self.cache.update()
        self.cache.open(None)

    def do_upgrade(self):
        self.cache.upgrade(True)
        chgs = self.cache.get_changes()
        print(chgs)
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
