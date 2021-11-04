import urllib3
import certifi
import ssl
import os

CA_CERTS = certifi.where()
CERT_REQS = ssl.CERT_REQUIRED
FILE_PATH = os.environ['HOME']

pool = urllib3.PoolManager(cert_reqs=CERT_REQS, ca_certs=CA_CERTS)
resp = pool.request("GET", "https://google.it/search?q=asd")

print("Response Code:", resp.status, "\n")

for k, v in resp.headers.items():
    print(k, v)

f = open(os.path.join(FILE_PATH, "Desktop/google.html"), "wb")
f.write(resp.data)
f.close()
