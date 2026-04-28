#!/usr/bin/env python3
"""Save all contract source files from browser-extracted base64 data."""
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

# The full base64 was returned by the browser evaluate call
# We'll read it from stdin or a file
b64_path = r"C:\Users\Administrator\.qclaw\workspace\contracts\_sources.b64"

# If the b64 file doesn't exist yet, we need to get it from browser
# For now, let's just write a manifest and use the browser to save files directly
print(f"Output dir: {OUT_DIR}")
print(f"Files to save: {len(FILE_NAMES)}")

# Write the file list as JSON for the browser script to use
manifest = {"names": FILE_NAMES, "outDir": OUT_DIR}
manifest_path = os.path.join(os.path.dirname(OUT_DIR), "_manifest.json")
os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
with open(manifest_path, "w") as f:
    json.dump(manifest, f, indent=2)
print(f"Manifest written to: {manifest_path}")
