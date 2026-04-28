#!/usr/bin/env python3
"""Decode and save all contract source files from the base64 data."""
import base64, os

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

# Read the base64 data from file
b64_path = r"C:\Users\Administrator\.qclaw\workspace\contracts\_sources.b64"
with open(b64_path, "r") as f:
    full_b64 = f.read().strip()

print(f"Base64 length: {len(full_b64)}")
decoded = base64.b64decode(full_b64).decode("utf-8")
print(f"Decoded length: {len(decoded)}")

files = decoded.split(SEPARATOR)
print(f"Number of files: {len(files)}")

saved = 0
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
    saved += 1
    print(f"  [{i}] {name}: {len(content)} chars ✓")

print(f"\nDone! Saved {saved}/{len(files)} files to {OUT_DIR}")
