import subprocess


class PackageControl:
    def __init__(self, params, package, mode):
        pass


class CheckResidualPackage:
    def __init__(self, autoremove=False):
        self.residuals_pkg: list = []
        self.autoremove = autoremove

    def check_residual_config(self):
        check = self.get_residual()
        if check:
            if len(self.residuals_pkg) > 0:
                for pkg in self.residuals_pkg:
                    print("\t[+]", pkg)
        else:
            print("[+] Congratulations, the system package status appears to be ok!")
            return False
        return True

    def get_residual(self):
        result = subprocess.run(['dpkg', '-l'], stdout=subprocess.PIPE)
        are_in = False
        for line in result.stdout.splitlines():
            line_pkg = line.split()
            if len(line_pkg) > 1:
                status = line_pkg[0].decode()
                if status == "rc":
                    self.residuals_pkg.append(line_pkg[1].decode())
                    if not are_in:
                        are_in = True
        return are_in

    def do_autoremove(self):
        for pkg in self.residuals_pkg:
            result = subprocess.run(['dpkg', '--purge', pkg], stdout=subprocess.PIPE)
            print(result.stdout.decode())
