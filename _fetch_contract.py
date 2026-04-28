#!/usr/bin/env python3
"""Fetch BSC contract source code from BSCScan using web scraping."""
import urllib.request, json, re, os, sys, time

PROXY = "http://127.0.0.1:7890"
ADDRESS = "0x7e199fc666368d95b9eaefa7d2d8081acab74134"
OUT_DIR = r"C:\Users\Administrator\.qclaw\workspace\contracts\0x7e199fc"

proxy = urllib.request.ProxyHandler({"https": PROXY, "http": PROXY})
opener = urllib.request.build_opener(proxy)

# BSCScan loads contract code via a separate API call
# Let's try the contract verification API
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"https://bscscan.com/address/{ADDRESS}#code",
}

# Try to get the contract details via the BSCScan internal page API
print("Trying BSCScan contract page API...")
urls_to_try = [
    # Standard etherscan-compatible format (no API key, rate limited)
    f"https://api.bscscan.com/api?module=contract&action=getsourcecode&address={ADDRESS}",
    # Alternative: try without any API params  
    f"https://api.etherscan.io/v2/api?chainid=56&module=contract&action=getsourcecode&address={ADDRESS}",
]

for url in urls_to_try:
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = opener.open(req, timeout=15)
        text = resp.read().decode("utf-8")
        data = json.loads(text)
        print(f"URL: {url[:80]}...")
        print(f"Status: {data.get('status')}, Message: {data.get('message')}")
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
                # Save files
                os.makedirs(OUT_DIR, exist_ok=True)
                
                # Handle multi-file source (JSON array format)
                if source.startswith("[{") or source.startswith("{"):
                    try:
                        sources = json.loads(source)
                        if isinstance(sources, dict) and "sources" in sources:
                            # Standard JSON format
                            for fname, fdata in sources["sources"].items():
                                content = fdata.get("content", "")
                                fpath = os.path.join(OUT_DIR, fname)
                                os.makedirs(os.path.dirname(fpath), exist_ok=True)
                                with open(fpath, "w", encoding="utf-8") as f:
                                    f.write(content)
                                print(f"  Saved: {fname} ({len(content)} bytes)")
                        elif isinstance(sources, list):
                            # BSCScan multi-file format
                            for item in sources:
                                fname = item.get("FileName", item.get("filename", "contract.sol"))
                                content = item.get("Content", item.get("content", ""))
                                fpath = os.path.join(OUT_DIR, os.path.basename(fname))
                                with open(fpath, "w", encoding="utf-8") as f:
                                    f.write(content)
                                print(f"  Saved: {fname} ({len(content)} bytes)")
                        else:
                            # Single source
                            fpath = os.path.join(OUT_DIR, f"{contract_name}.sol")
                            with open(fpath, "w", encoding="utf-8") as f:
                                f.write(source)
                            print(f"  Saved: {contract_name}.sol ({len(source)} bytes)")
                    except json.JSONDecodeError:
                        # Raw Solidity source
                        fpath = os.path.join(OUT_DIR, f"{contract_name}.sol")
                        with open(fpath, "w", encoding="utf-8") as f:
                            f.write(source)
                        print(f"  Saved: {contract_name}.sol ({len(source)} bytes)")
                else:
                    fpath = os.path.join(OUT_DIR, f"{contract_name}.sol")
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(source)
                    print(f"  Saved: {contract_name}.sol ({len(source)} bytes)")
                
                # Save ABI
                if abi and abi != "Contract source code not verified":
                    abi_path = os.path.join(OUT_DIR, f"{contract_name}.abi.json")
                    with open(abi_path, "w", encoding="utf-8") as f:
                        f.write(abi)
                    print(f"  Saved ABI: {contract_name}.abi.json")
                
                print(f"\nAll files saved to: {OUT_DIR}")
                sys.exit(0)
        else:
            print(f"Result: {str(data)[:200]}")
    except Exception as e:
        print(f"Error: {e}")

# If all API attempts fail, try scraping the rendered page
print("\nAPI attempts exhausted. The contract may not be verified on BSCScan.")
print("Please check if the contract is verified at:")
print(f"https://bscscan.com/address/{ADDRESS}#code")
