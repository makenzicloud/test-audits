// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts v4.3.2 (token/ERC20.sol)

pragma solidity ^0.8.0;

import "./IERC20.sol";
import "./IERC20Metadata.sol";

/**
 * @dev Implementation of the {IERC20} interface.
    *
    * This implementation is agnostic to the way tokens are created. This means
    * that a supply mechanism has to be added in a derived contract using {_mint}.
    * For a generic mechanism see {ERC20PresetMinterPauser}.

    * TIP: For a detailed writeup see our guide
    * https://forum.zeppelin.solutions/t/how-to-implement-erc20-supply-mechanisms/226[How to implement supply mechanisms].
    *
    * We have followed general OpenZeppelin guidelines: functions revert instead
    * of returning `false` on failure. This behavior is nonetheless conventional
    * and does does not conflict with the expectations of ERC20 applications.
    *
    * Additionally, an {Approval} event is emitted on calls to {transferFrom}.
    * This allows applications to reconstruct the allowance for all accounts just
    * by listening to said events. Other implementations of the EIP may not emit
    * these events, as it isn't required by the specification.
    *
    * Finally, the non-standard {decreaseAllowance} and {increaseAllowance}
    * functions have been added to mitigate the well-known issues around setting
    * allowances. See {IERC20-approve}.
    */


contract ERC20 is IERC20, IERC20Metadata {
    mapping (address => uint256) private _balances;

    mapping (address => mapping (address => uint256)) private _allowances;

    uint256 private _totalSupply;

    address public owner;

    constructor() {

    }

    modifier onlyOwner() {
        require(msg.sender == owner, "ERC20: caller is not the owner");
        _;
    }

    /**
     * @dev Return name of token.
     */
     function name() public view virtual override returns (string memory) {
         return "";
     }

        /**
        * @dev Return symbol of token.
        */
        function symbol() public view virtual override returns (string memory) {
            return "";
        }

        


}