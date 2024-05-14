/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier {
    env e;
    
    address governor;

    // Initialize the governor to the contract caller.
    governor = e.s.governor;

    assert e.msg.sender == e.s.governor,
    "Only Governor can call";
    







    
}
