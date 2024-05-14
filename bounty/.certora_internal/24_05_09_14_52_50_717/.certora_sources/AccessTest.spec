/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier(env e, method f) {
    calldataarg args;

    bool isGovernorBefore = e.msg.sender == governor;
    f(e, args);
    bool isGovernorAfter = e.msg.sender == governor;

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
