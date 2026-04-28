#!/usr/bin/env python3
"""Fetch contract source from BSCScan API (old V1 endpoint on bscscan.com domain)."""
import urllib.request, json, os, base64

PROXY = "http://127.0.0.1:7890"
ADDRESS = "0x7e199fc666368d95b9eaefa7d2d8081acab74134"
API_KEY = "U3R1EDSVYX45FQBR3VTB555QG9971WHZEH"
OUT_DIR = r"C:\Users\Administrator\.qclaw\workspace\contracts\0x7e199fc"

proxy = urllib.request.ProxyHandler({"https": PROXY, "http": PROXY})
opener = urllib.request.build_opener(proxy)

# Try bscscan.com/api (may still work even if api.bscscan.com is deprecated)
url = f"https://bscscan.com/api?module=contract&action=getsourcecode&address={ADDRESS}&apikey={API_KEY}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

try:
    req = urllib.request.Request(url, headers=headers)
    resp = opener.open(req, timeout=15)
    text = resp.read().decode("utf-8")
    data = json.loads(text)
    
    print(f"Status: {data.get('status')}")
    print(f"Message: {data.get('message')}")
    
    if data.get("status") == "1" and isinstance(data.get("result"), list) and len(data["result"]) > 0:
        result = data["result"][0]
        contract_name = result.get("ContractName", "Unknown")
        compiler = result.get("CompilerVersion", "Unknown")
        source = result.get("SourceCode", "")
        abi = result.get("ABI", "")
        
        print(f"Contract: {contract_name}")
        print(f"Compiler: {compiler}")
        print(f"Source length: {len(source)}")
        print(f"ABI length: {len(abi)}")
        
        if source:
            os.makedirs(OUT_DIR, exist_ok=True)
            
            # Save raw source
            raw_path = os.path.join(OUT_DIR, f"{contract_name}_raw_source.json")
            with open(raw_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"Saved raw source to: {raw_path}")
            
            # Parse and save individual files
            src_dir = os.path.join(OUT_DIR, "src")
            os.makedirs(src_dir, exist_ok=True)
            
            if source.startswith("[{") or source.startswith("{"):
                try:
                    sources = json.loads(source)
                    if isinstance(sources, dict) and "sources" in sources:
                        # Standard JSON format
                        for fname, fdata in sources["sources"].items():
                            content = fdata.get("content", "")
                            fpath = os.path.join(src_dir, fname)
                            os.makedirs(os.path.dirname(fpath), exist_ok=True)
                            with open(fpath, "w", encoding="utf-8") as f:
                                f.write(content)
                            print(f"  Saved: {fname} ({len(content)} bytes)")
                    elif isinstance(sources, list):
                        for item in sources:
                            fname = item.get("FileName", item.get("filename", "contract.sol"))
                            content = item.get("Content", item.get("content", ""))
                            fpath = os.path.join(src_dir, os.path.basename(fname))
                            with open(fpath, "w", encoding="utf-8") as f:
                                f.write(content)
                            print(f"  Saved: {fname} ({len(content)} bytes)")
                except json.JSONDecodeError:
                    fpath = os.path.join(src_dir, f"{contract_name}.sol")
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(source)
                    print(f"  Saved: {contract_name}.sol ({len(source)} bytes)")
            else:
                fpath = os.path.join(src_dir, f"{contract_name}.sol")
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(source)
                print(f"  Saved: {contract_name}.sol ({len(source)} bytes)")
            
            # Save ABI
            if abi and abi != "Contract source code not verified":
                abi_path = os.path.join(OUT_DIR, f"{contract_name}.abi.json")
                with open(abi_path, "w", encoding="utf-8") as f:
                    json.dump(json.loads(abi), f, ensure_ascii=False, indent=2)
                print(f"  Saved ABI: {contract_name}.abi.json")
    else:
        print(f"Result: {str(data.get('result'))[:500]}")
        
except Exception as e:
    print(f"Error: {e}")
