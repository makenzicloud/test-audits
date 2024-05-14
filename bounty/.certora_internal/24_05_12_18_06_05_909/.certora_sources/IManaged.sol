// SPDX-License-Identifier: MIT

// pragma solidity ^0.7.3;
pragma solidity >=0.6.12 <0.8.0;

interface IManaged {
    function setController(address _controller) external;
}