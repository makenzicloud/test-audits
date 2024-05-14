/*
* Test access control
*/

invariant governorConsistency(env e) 
    getGovernor() == owner();


rule governorConsistencyAsRule(method f) {
    // Precondition
    require getGovernor() == owner();

    env e;
    calldataarg args;
    f(e, args);

    // Postcondition
    assert getGovernor() == owner(),
        "Governor should be equal to owner";
}
