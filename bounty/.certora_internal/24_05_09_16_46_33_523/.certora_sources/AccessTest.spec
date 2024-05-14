/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier {
    method f;
    env e;
    calldataarg args;
    
   
    address oldPendingGovernor = e.contract.pendingGovernor;

    f(e, args);

    address NewOwnership = e.contract.pendingGovernor;

    // Check that the function is only callable by the governor
    assert oldPendingGovernor != NewOwnership =>  e.msg.sender == e.contract.governor,
        "The caller of the function must be the governor";
    
}







    

