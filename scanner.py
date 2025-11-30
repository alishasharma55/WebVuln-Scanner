import os
import time

TARGET_IP = "192.168.60.129"
TARGET_URL = f"http://{TARGET_IP}"

print("[+] Target:", TARGET_URL)

print("[+] Starting DB...")
os.system("sudo service postgresql start")
time.sleep(2)

print("[+] Running WMAP scan...")
os.system(f'''
sudo msfconsole -q -x "
load wmap;
wmap_sites -a {TARGET_URL};
wmap_targets -t {TARGET_URL};
wmap_run -e;
exit"
''')

print("[+] Scan finished."
