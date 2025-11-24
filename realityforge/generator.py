from __future__ import annotations
import random
import uuid
from datetime import datetime
from typing import List, Dict, Any
from .data import DESTINATIONS, PUBLIC_KEYS, SHORT_IDS, FINGERPRINTS
import os
import sys
if __name__ == "__main__" and __package__ is None:
    __package__ = "realityforge"
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def generate_configs(count: int = 50) -> List[Dict[str, Any]]:
    if not 1 <= count <= 1000:
        raise ValueError("تعداد باید بین ۱ تا ۱۰۰۰ باشد")

    configs = []
    flow_options = ["xtls-rprx-vision", "xtls-rprx-vision-udp443", ""]

    for i in range(count):
        dest = random.choice(DESTINATIONS)
        domain = dest.split(":")[0]
        fp_name = random.choice(list(FINGERPRINTS.keys()))
        fp_display = fp_name.split("_", 1)[0] if "_" in fp_name else fp_name
        raw_flow = random.choice(flow_options)

        config = {
            "name": f"RF-{datetime.now():%m%d}-{i+1:02d}",
            "server": domain,
            "port": 443,
            "uuid": str(uuid.uuid4()),
            "flow": raw_flow if raw_flow else None,
            "fp": fp_display,
            "publicKey": random.choice(PUBLIC_KEYS),
            "shortId": random.choice(SHORT_IDS),
            "sni": domain,
            "spiderX": random.choice(["", "/", "/video", "/download", "/cdn", "/api/v1", "/stream", "/live"]),
            "fullFingerprint": FINGERPRINTS[fp_name],
            "generated_at": datetime.now().isoformat(),
        }
        configs.append(config)
    return configs
