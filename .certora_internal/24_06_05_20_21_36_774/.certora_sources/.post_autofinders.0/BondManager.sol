// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/* Interface Imports */
import { IBondManager } from "./IBondManager.sol";

/* Contract Imports */
import { Lib_AddressResolver } from "./Lib_AddressResolver.sol";

/**
 * @title BondManager
 * @dev This contract is, for now, a stub of the "real" BondManager that does nothing but
 * allow the "OVM_Proposer" to submit state root batches.
 *
 * Runtime target: EVM
 */
contract BondManager is IBondManager, Lib_AddressResolver {
    /**
     * @param _libAddressManager Address of the Address Manager.
     */
    constructor(address _libAddressManager) Lib_AddressResolver(_libAddressManager) {}

    /**
     * Checks whether a given address is properly collateralized and can perform actions within
     * the system.
     * @param _who Address to check.
     * @return true if the address is properly collateralized, false otherwise.
     */
    function isCollateralized(address _who) public view returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010000, 1037618708481) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00016000, _who) }
        // Only authenticate sequencer to submit state root batches.
        return _who == resolve("OVM_Proposer");
    }
    
    function isCollateralizedByChainId(
        uint256 _chainId,
        address _who,
        address _prop
    ) override public view returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00020000, 1037618708482) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00020001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00020005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00026002, _prop) }
        require(_who==_prop,"sender must the proposer!");
        return true;
        //return bonds[_who].state == State.COLLATERALIZED;
    }
    
    function registerSequencerByChainId(
        uint256 _chainId,
        address _sequencer,
        address _proposer
    ) public {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00030000, 1037618708483) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00030001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00030005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00036002, _proposer) }
    }
}