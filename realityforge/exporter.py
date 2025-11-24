import os
from typing import List, Dict
import sys
if __name__ == "__main__" and __package__ is None:
    __package__ = "realityforge"
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
def export_to_nekobox(configs: List[Dict], path: str = "RealityForge_Output/nekobox.txt"):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for c in configs:
            flow = f"&flow={c['flow']}" if c['flow'] else ""
            link = f"vmess://{c['uuid']}@{c['server']}:443?encryption=none&security=reality{flow}&fp={c['fp']}&pbk={c['publicKey']}&sid={c['shortId']}&sni={c['sni']}&type=tcp&spiderX={c['spiderX']}#{c['name']}"
            f.write(link + "\n")
    print(f"نکو باکس: {len(configs)} کانفیگ → {path}")

def export_to_clash(configs: List[Dict], path: str = "RealityForge_Output/clash.yaml"):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("proxies:\n")
        for c in configs:
            flow = f", flow: {c['flow']}" if c['flow'] else ""
            f.write(f"  - {{name: {c['name']}, type: vmess, server: {c['server']}, port: 443, uuid: {c['uuid']}, alterId: 0, cipher: auto, tls: true, network: tcp, skip-cert-verify: true, udp: true{flow}, reality-opts: {{public-key: {c['publicKey']}, short-id: {c['shortId']}, fingerprint: {c['fp']}, spider-x: \\\"{c['spiderX']}\\\"}}}}\n")
    print(f"کلش/سینگ‌باکس: {len(configs)} کانفیگ → {path}")
