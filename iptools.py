import requests, random

def randip():
    rn = lambda: random.randint(0, 255)
    return f"{rn()}.{rn()}.{rn()}.{rn()}"

def testip(session, IP):
    target = f"http://{IP}:80/"
    print(f"[.] Testing {target}")
    try:
        response = session.get(
            target,
            timeout=1
        )
        print("[+] Target is up")
        open("active.targets", "a").write(f"{response.status_code} {target}\n")
        return True
    except requests.ConnectTimeout:
        print("[-] Connection timed out")
    except requests.ConnectionError:
        print("[!] Connection error")
    except Exception as error:
        print(f"[!] {error}")
    return False