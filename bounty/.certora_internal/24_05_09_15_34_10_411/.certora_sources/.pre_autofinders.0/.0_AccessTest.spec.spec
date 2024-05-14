/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier {
    env e;
    
    address governor;

    // Initialize the governor to the contract caller.
    governor = e.governor;

    assert e.msg.sender == e.governor,
    "Only Governor can call";
    







    
}
