#!/usr/bin/env python3
"""Decode base64 encoded contract sources and save to files."""
import base64, json, os, sys

OUT_DIR = r"C:\Users\Administrator\.qclaw\workspace\contracts\0x7e199fc\src"

FILE_NAMES = [
    "ATokenInstance.sol",
    "interfaces/IPool.sol",
    "interfaces/IInitializableAToken.sol",
    "protocol/libraries/helpers/Errors.sol",
    "misc/aave-upgradeability/VersionedInitializable.sol",
    "protocol/tokenization/AToken.sol",
    "interfaces/IPoolAddressesProvider.sol",
    "protocol/libraries/types/DataTypes.sol",
    "interfaces/IAaveIncentivesController.sol",
    "openzeppelin-contracts/contracts/utils/math/SafeCast.sol",
    "openzeppelin-contracts/contracts/utils/cryptography/ECDSA.sol",
    "dependencies/openzeppelin/contracts/IERC20.sol",
    "dependencies/gnosis/contracts/GPv2SafeERC20.sol",
    "interfaces/IAToken.sol",
    "protocol/tokenization/base/ScaledBalanceTokenBase.sol",
    "protocol/tokenization/base/IncentivizedERC20.sol",
    "protocol/tokenization/base/EIP712Base.sol",
    "protocol/libraries/helpers/TokenMath.sol",
    "interfaces/IScaledBalanceToken.sol",
    "protocol/libraries/math/WadRayMath.sol",
    "protocol/tokenization/base/MintableIncentivizedERC20.sol",
    "dependencies/openzeppelin/contracts/Context.sol",
    "dependencies/openzeppelin/contracts/IERC20Detailed.sol",
    "interfaces/IACLManager.sol",
    "misc/DelegationMode.sol",
]

SEPARATOR = "\n<<FILE_BREAK>>\n"

# Read chunks from command line arguments
chunks = []
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        with open(arg, "r") as f:
            chunks.append(f.read().strip())
else:
    print("Usage: python decode_sources.py chunk1.txt chunk2.txt ...")
    sys.exit(1)

full_b64 = "".join(chunks)
print(f"Total base64 length: {len(full_b64)}")

# Decode
decoded = base64.b64decode(full_b64).decode("utf-8")
print(f"Decoded length: {len(decoded)}")

# Split by file separator
files = decoded.split(SEPARATOR)
print(f"Number of files: {len(files)}")

# Save each file
for i, content in enumerate(files):
    if i >= len(FILE_NAMES):
        print(f"Warning: more files than names, skipping file {i}")
        break
    
    name = FILE_NAMES[i]
    content = content.strip()
    
    if not content:
        print(f"  [{i}] {name}: EMPTY")
        continue
    
    fpath = os.path.join(OUT_DIR, name)
    os.makedirs(os.path.dirname(fpath), exist_ok=True)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"  [{i}] {name}: {len(content)} bytes -> {fpath}")

print(f"\nDone! Saved {len(files)} files to {OUT_DIR}")
