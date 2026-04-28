#!/usr/bin/env python3
"""Extract all contract source files from BSCScan via browser CDP."""
import json, os, sys

OUT_DIR = r"C:\Users\Administrator\.qclaw\workspace\contracts\0x7e199fc"
os.makedirs(OUT_DIR, exist_ok=True)

# Read the snapshot data - we already have all 25 files from the browser snapshot
# File list extracted from the snapshot:
files = [
    ("ATokenInstance.sol", r"""// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.0;

import {IPool} from '../interfaces/IPool.sol';
import {IInitializableAToken} from '../interfaces/IInitializableAToken.sol';
import {Errors} from '../protocol/libraries/helpers/Errors.sol';
import {VersionedInitializable} from '../misc/aave-upgradeability/VersionedInitializable.sol';
import {AToken} from '../protocol/tokenization/AToken.sol';

/**
 * @title Aave ERC20 AToken Instance
 * @author BGD Labs
 * @notice Instance of the interest bearing token for the Aave protocol
 */
contract ATokenInstance is AToken {
    uint256 public constant ATOKEN_REVISION = 5;

    constructor(
        IPool pool,
        address rewardsController,
        address treasury
    ) AToken(pool, rewardsController, treasury) {}
"""),
]

# We'll use the browser to get all files. For now, let's create a script
# that will be run via browser evaluate to extract all source code.
print("Please use browser evaluate to extract source code.")
print("Files saved to:", OUT_DIR)
