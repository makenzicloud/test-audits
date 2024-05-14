/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Modifier: onlyGovernor                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyGovernorModifier(env e, method f) {
    bool isGovernorBefore = e.contract.governor == e.msg.sender;
    f(e);
    bool isGovernorAfter = e.contract.governor == e.msg.sender;

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
