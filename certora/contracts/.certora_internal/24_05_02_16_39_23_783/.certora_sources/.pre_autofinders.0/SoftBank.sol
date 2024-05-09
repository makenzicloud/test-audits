// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

// import "@openzeppelin/contracts/security/ReentrancyGuard.sol"; 
// Use the nonReentrant modifier in the withdraw function if you wanna try the ReentrancyGuard contract.

contract TargetContract {
    mapping(address => uint256) public balances;

    // Update the `balances` mapping to include the new ETH deposited by msg.sender
    function addBalance() public payable {
        balances[msg.sender] += msg.value;
    }

    // Send ETH worth `balances[msg.sender]` back to msg.sender
    function withdraw() public {
        // Ensure the sender has a balance to withdraw
        require(balances[msg.sender] != 0);
        // Attempt to transfer
        (bool sent, ) = msg.sender.call{value: balances[msg.sender]}("");// This is the vulnerable line
        require(sent, "Failed to send Ether");
        // Update the balance to reflect the transfer after being drained
        balances[msg.sender] = 0; 
    }

    
}
