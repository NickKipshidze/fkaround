import time
from multiprocessing import Pool
import tor, iptools

session = tor.torsession()

def wrapper(ip):
    iptools.testip(
        session, ip
    )

ips = [iptools.randip() for _ in range(8192)]

start_time = time.time()

with Pool(processes=64) as pool:
    results = pool.map(wrapper, ips)

end_time = time.time()

duration = end_time - start_time
print(f"[+] Execution took: {duration} seconds")
