#!/usr/bin/env python3
"""Save extracted contract source files to disk."""
import json, os, sys

OUT_DIR = r"C:\Users\Administrator\.qclaw\workspace\contracts\0x7e199fc\src"
os.makedirs(OUT_DIR, exist_ok=True)

# Known file names from BSCScan page (File 1-25)
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

# This script will be called from the browser context via JS
# Sources are stored in window._contractSources array (0-indexed)
print("File names prepared:", len(FILE_NAMES))
for i, name in enumerate(FILE_NAMES):
    path = os.path.join(OUT_DIR, name)
    print(f"  [{i}] {name}")
