// SPDX-License-Identifier: MIT
pragma solidity 0.8.25;

import {MathMasters} from "../src/MathMasters.sol";

contract Base {
    function mulWad(uint256 x, uint256 y) public pure returns (uint256) {
        return MathMasters.mulWad(x, y);
    }
}