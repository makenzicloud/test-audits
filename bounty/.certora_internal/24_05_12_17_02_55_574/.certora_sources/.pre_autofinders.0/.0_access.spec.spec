/*
* Test access control
*/

// invariant governorConsistency(env e) 
//     getGovernor(e) == owner(e);


rule governorConsistencyAsRule( env e, method f) {
    // Precondition
    require getGovernor(e) == getOwner(e);

   
    calldataarg args;
    f(e, args);

    // Postcondition
    assert getGovernor(e) == getOwner(e),
        "Governor should be equal to owner";
}
