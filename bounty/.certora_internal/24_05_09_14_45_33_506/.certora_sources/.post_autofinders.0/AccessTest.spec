/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier(env e, method f) {
    calldataarg args;

    bool isGovernorBefore = msg.sender == governor;
    f(e, args);
    bool isGovernorAfter = msg.sender == governor;

    assert (
        isGovernorBefore &&
        isGovernorAfter
    ) => (
        f.selector == methodWithOnlyGovernorModifier().selector
    );

    assert (
        !isGovernorBefore &&
        !isGovernorAfter
    ) => (
        f.selector != methodWithOnlyGovernorModifier().selector
    );
}

