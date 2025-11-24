#!/usr/bin/env python3
import argparse
from .generator import generate_configs
from .exporter import export_to_nekobox, export_to_clash
import os
import sys
if __name__ == "__main__" and __package__ is None:
    __package__ = "realityforge"
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
def main():
    parser = argparse.ArgumentParser(description="RealityForge – ژنراتور Reality")
    parser.add_argument("-c", "--count", type=int, default=50, help="تعداد کانفیگ (پیش‌فرض: 50)")
    args = parser.parse_args()

    print(f"در حال تولید {args.count} کانفیگ Reality خفن...")
    configs = generate_configs(args.count)
    export_to_nekobox(configs)
    export_to_clash(configs)
    print("تموم شد! کانفیگ‌ها در پوشه RealityForge_Output ذخیره شدن")

if __name__ == "__main__":
    main()
