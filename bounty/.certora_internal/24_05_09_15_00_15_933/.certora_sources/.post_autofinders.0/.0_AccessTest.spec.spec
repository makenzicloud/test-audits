/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier(env e, method f) {
    calldataarg args;

    bool isGovernorBefore = e.contractState.governor == e.msg.sender;
    f(e, args);
    bool isGovernorAfter = e.contractState.governor == e.msg.sender;

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

