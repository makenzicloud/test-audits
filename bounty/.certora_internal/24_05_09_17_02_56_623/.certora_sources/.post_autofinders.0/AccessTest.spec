/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier {
    method f;
    env e;
    calldataarg args;
    address governor;
    address transferOwnership;

    address oldGovernor = oldPendingGovernor(governor, transferOwnership);

    f(e, args);

    address NewOwnership = pendingGovernor(governor, transferOwnership);

    // Check that the function is only callable by the governor
    assert oldGovernor != NewOwnership =>  e.msg.sender == e.contract.governor,
        "The caller of the function must be the governor";
    
   
    
}







    

