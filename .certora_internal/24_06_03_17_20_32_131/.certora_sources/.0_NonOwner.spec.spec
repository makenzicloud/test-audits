rule accessControl(method f, address nonOwner) {
    // Define the environment and set up the initial state
    env e;

    // Assume `nonOwner` is not the owner
    assume nonOwner != DegenDealer.owner();

    // Set the sender to `nonOwner`
    e.msg.sender = nonOwner;

    // Try to call the restricted function with the non-owner address
    calldataarg args;
    f(e, args);

    // Assert that the call reverts
    assert lastReverted, "Access control violation: non-owner was able to call a restricted function";
}
