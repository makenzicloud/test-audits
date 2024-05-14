/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier {
    method f;
    env e;
    calldataarg args;
    address owner
   
    address oldPendingGovernor = e.contract.pendingGovernor;

    f(e, args);

    address NewOwnership = e.contract.pendingGovernor;

    // Check that the function is only callable by the governor
    assert oldPendingGovernor != NewOwnership => owner ==e.msg.sender,
        "The caller of the function must be the governor";
    
}







    

