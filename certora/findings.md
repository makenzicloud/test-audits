### Root cause + impact


# Description
The root cause of the vulnerability lies in the vulnerable implementation of the withdraw and withdrawAll functions in the VulnerableBank contract. Both functions allow an external entity to call them and then transfer Ether to another address using the call function. However, the contract updates the user's balance after the external call, creating a window of opportunity for reentrancy attacks. An attacker can recursively call these functions before the balance update, leading to unexpected behavior and potential loss of funds.
#####
Reentrancy in VulnerableBank.withdraw(uint256) (SoftBank.sol#10-17):
        External calls:
        - (success,None) = msg.sender.call{value: amount}() (SoftBank.sol#13)
        State variables written after the call(s):
        - userBalances[msg.sender] -= amount (SoftBank.sol#14)
        VulnerableBank.userBalances (SoftBank.sol#7) can be used in cross function reentrancies:
        - VulnerableBank.getUserBalance(address) (SoftBank.sol#31-33)
        - VulnerableBank.withdraw(uint256) (SoftBank.sol#10-17)
        - VulnerableBank.withdrawAll() (SoftBank.sol#19-25)
Reentrancy in VulnerableBank.withdrawAll() (SoftBank.sol#19-25):
        External calls:
        - (success,None) = msg.sender.call{value: balance}() (SoftBank.sol#22)
        State variables written after the call(s):
        - userBalances[msg.sender] = 0 (SoftBank.sol#24)
        VulnerableBank.userBalances (SoftBank.sol#7) can be used in cross function reentrancies:
        - VulnerableBank.getUserBalance(address) (SoftBank.sol#31-33)
        - VulnerableBank.withdraw(uint256) (SoftBank.sol#10-17)
        - VulnerableBank.withdrawAll() (SoftBank.sol#19-25)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities

#Impact
The impact of this vulnerability is severe as it can lead to financial losses for users of the contract. An attacker can exploit the reentrancy vulnerability to drain the contract's funds or manipulate the contract's state in unintended ways. This could result in the loss of user funds or disrupt the intended functionality of the contract.

#Mitigation
To mitigate this vulnerability, you should:

Update State Before External Calls: Ensure that state changes are made before any external calls to prevent reentrancy attacks. Update the user's balance before interacting with external contracts or transferring Ether.
Use Safe Ether Transfer Functions: Replace the use of call with safer alternatives like transfer or send to transfer Ether. These functions limit the gas forwarded and reduce the risk of reentrancy attacks.
Apply Checks-Effects-Interactions (CEI) Pattern: Follow the CEI pattern to ensure that checks are performed, state changes are made, and interactions with external contracts occur in the correct order. This helps prevent reentrancy vulnerabilities by ensuring that state changes are finalized before interacting with external contracts.
By implementing these mitigation strategies, you can significantly reduce the risk of reentrancy attacks and enhance the security of your smart contract.





