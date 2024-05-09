// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @author Obingo76
/// @title reentrancy attack test
import "forge-std/Test.sol";
import { TargetContract } from "certora/contracts/SoftBank.sol";
import { BadContract } from "certora/contracts/BadBoy.sol";

contract ReentrancyAttackTest is Test {
    TargetContract public targetContract;
    BadContract public badContract;
    
    address public  INNOCENT = vm.addr(0x01);
    address public ATTACKER = vm.addr(0x02);
    
    function setUp() public {
        targetContract = new TargetContract();
        badContract = new BadContract(address(targetContract));
        
        vm.deal(INNOCENT, 10 ether);
        vm.deal(ATTACKER, 2 ether);
    }

    function testInnocentTransfer() public {
        vm.startPrank(INNOCENT);
        targetContract.addBalance{value: 10 ether}();
        vm.stopPrank();
        uint targetContractBalance = address(targetContract).balance;
        emit log_named_uint("target Contract Balance: ", targetContractBalance);
        assertEq(targetContractBalance, 10 ether);
    }

    
    /// @notice 
        function testBadContract() public {
        testInnocentTransfer();
        vm.startPrank(ATTACKER);
        badContract.attack{value: 2 ether}();
        uint targetContractBalanceAfterAttack = address(targetContract).balance;
        emit log_named_uint("targetContract After Attack: ", targetContractBalanceAfterAttack);
        assertEq(targetContractBalanceAfterAttack, 0 ether);
        
    }
}