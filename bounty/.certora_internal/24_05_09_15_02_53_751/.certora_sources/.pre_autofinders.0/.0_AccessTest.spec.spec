/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier(env e, method f) {
    calldataarg args;

    bool isGovernorBefore = e.contract.state.governor == e.msg.sender;
    f(e, args);
    bool isGovernorAfter = e.contract.state.governor == e.msg.sender;

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
