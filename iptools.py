import requests, random, json

SETTINGS = json.load(open("./settings.json", "r"))

def randip():
    rn = lambda: random.randint(0, 255)
    return f"{rn()}.{rn()}.{rn()}.{rn()}"

def checktarget(session, target):
    try:
        response = session.get(
            target,
            timeout=1
        )
        print("[+] Target is up")
        open(SETTINGS["output"]["ok-targets"] if response.ok else SETTINGS["output"]["active-targets"], "a").write(
            f"{response.status_code} {target}\n" if SETTINGS["output"]["append-status-code"] else
            f"{target}\n"
        )
        return True
    except requests.ConnectTimeout:
        print("[-] Connection timed out")
    except requests.ConnectionError:
        print("[!] Connection error")
    except Exception as error:
        print(f"[!] {error}")
    return False

def testip(session, IP):
    for port in SETTINGS["target"]["open-ports"]:
        target = f"http://{IP}:{port}/"
        print(f"[.] Testing {target}")
        checktarget(session, target)