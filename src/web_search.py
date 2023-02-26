import urllib3
import certifi
import ssl
import os
import sys

CA_CERTS = certifi.where()
CERT_REQS = ssl.CERT_REQUIRED
FILE_PATH = os.environ['HOME']


class Searcher:
    def __init__(self):
        self.pool = urllib3.PoolManager(cert_reqs=CERT_REQS, ca_certs=CA_CERTS)

    def search(self, args):
        resp = self.pool.request("GET", "https://google.it/search?q=" + args)

        print("Response Code:", resp.status, "\n")

        for k, v in resp.headers.items():
            print(k, v)

        print(resp.data)
        f = open(os.path.join(FILE_PATH, "Desktop/google.html"), "wb")
        f.write(resp.data)
        f.close()


if __name__ == '__main__':
    Searcher().search(sys.argv[1])
