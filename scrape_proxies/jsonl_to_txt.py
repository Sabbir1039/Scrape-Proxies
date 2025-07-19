import json

with open("proxies.jsonl", "r") as fin, open("proxies.txt", "w") as fout:
    for line in fin:
        proxy = json.loads(line.strip())
        ip = proxy["ip_address"]
        port = proxy["port"]

        fout.write(f"https://{ip}:{port}\n")
