/*
* Test access control
*/

invariant governorConsistency(env e) 
    getGovernor(e) == governor(e);


rule governorConsistencyAsRule( env e, method f) {
    // Precondition
    require getGovernor(e) == governor(e);

   
    calldataarg args;
    f(e, args);

    // Postcondition
    assert getGovernor(e) == governor(e),
        "Governor should be equal to governor";
}
