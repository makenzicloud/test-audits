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
   

    f(e, args);

    // Check that the function is only callable by the governor
    assert oldPendingGovernor != NewOwnership => owner ==e.msg.sender,
        "The caller of the function must be the governor";
    
}







    

