// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TargetContract {
    mapping(address => uint256) public balances;

    // Update the `balances` mapping to include the new ETH deposited by msg.sender
    function addBalance() public payable {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000000, 1037618708480) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000004, 0) }
        balances[msg.sender] += msg.value;
    }

    // Send ETH worth `balances[msg.sender]` back to msg.sender
    function withdraw() public {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010000, 1037618708481) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00010004, 0) }
        // Ensure the sender has a balance to withdraw
        require(balances[msg.sender] != 0);
        // Attempt to transfer
        (bool sent, ) = msg.sender.call{value: balances[msg.sender]}("");// This is the vulnerable line
        require(sent, "Failed to send Ether");
        // Update the balance to reflect the transfer after being drained
        balances[msg.sender] = 0; 
    }

    function withdrawAll() external {
        uint256 amount = balances[msg.sender];
        balances[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed.");
    }

    
}
