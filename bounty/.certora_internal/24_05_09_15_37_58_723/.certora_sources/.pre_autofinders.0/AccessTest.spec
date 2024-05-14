/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier {
    env e;
    method f;
    calldataarg args;
    address governor;

    governor = getGovernor();
    f(e, args);
    assert !lastReverted => hasRole(getRoleAdmin(ROLE_GOVERNOR), governor);
}

    








    

