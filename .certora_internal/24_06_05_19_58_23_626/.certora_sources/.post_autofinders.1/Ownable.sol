// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Context.sol";

/**
 * @dev Contract module which provides a basic access control mechanism, where
 * there is an account (an owner) that can be granted exclusive access to
 * specific functions.
 *
 * By default, the owner account will be the one that deploys the contract. This
 * can later be changed with {transferOwnership}.
 *
 * This module is used through inheritance. It will make available the modifier
 * `onlyOwner`, which can be applied to your functions to restrict their use to
 * the owner.
 */
abstract contract Ownable is Context {
    address private _owner;

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Initializes the contract setting the deployer as the initial owner.
     */
    constructor() {
        _setOwner(_msgSender());
    }

    /**
     * @dev Returns the address of the current owner.
     */
    function owner() public view virtual returns (address) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00100000, 1037618708496) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00100001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00100004, 0) }
        return _owner;
    }

    /**
     * @dev Throws if called by any account other than the owner.
     */
    modifier onlyOwner() {
        require(owner() == _msgSender(), "Ownable: caller is not the owner");
        _;
    }

    /**
     * @dev Leaves the contract without owner. It will not be possible to call
     * `onlyOwner` functions anymore. Can only be called by the current owner.
     *
     * NOTE: Renouncing ownership will leave the contract without an owner,
     * thereby removing any functionality that is only available to the owner.
     */
    function renounceOwnership() public virtual logInternal21()onlyOwner {
        _setOwner(address(0));
    }modifier logInternal21() { assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00150000, 1037618708501) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00150001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00150004, 0) } _; }

    /**
     * @dev Transfers ownership of the contract to a new account (`newOwner`).
     * Can only be called by the current owner.
     */
    function transferOwnership(address newOwner) public virtual logInternal20(newOwner)onlyOwner {
        require(newOwner != address(0), "Ownable: new owner is the zero address");
        _setOwner(newOwner);
    }modifier logInternal20(address newOwner) { assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00140000, 1037618708500) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00140001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00140005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00146000, newOwner) } _; }

    function _setOwner(address newOwner) private {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00130000, 1037618708499) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00130001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00130005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00136000, newOwner) }
        address oldOwner = _owner;
        _owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }
}