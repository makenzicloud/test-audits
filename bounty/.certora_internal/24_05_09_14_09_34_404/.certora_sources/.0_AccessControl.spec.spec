import "./helpers.spec";

definition DEFAULT_ADMIN_ROLE() returns bytes32 = 0x0000000000000000000000000000000000000000000000000000000000000000;

rule onlyGovernorCanTransferOwnership(env e, method f) {
    calldataarg args;

    address oldGovernor = governor;
    address oldPendingGovernor = pendingGovernor;

    f(e, args);

    assert (
        oldGovernor != pendingGovernor
    ) => (
        f.selector == sig:transferOwnership(address)
    );
}

rule onlyPendingGovernorCanAcceptOwnership(env e, method f) {
    calldataarg args;

    address oldGovernor = governor;
    address oldPendingGovernor = pendingGovernor;

    f(e, args);

    assert (
        pendingGovernor == address(0) || oldPendingGovernor == pendingGovernor
    ) => (
        f.selector == sig:acceptOwnership()
    );
}
