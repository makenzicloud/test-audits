/*
* Test access control
*/

// invariant governorConsistency(env e) 
//     getGovernor(e) == owner(e);


rule governorConsistencyAsRule( env e, method f) {
    // Precondition
    require getGovernor(e) == owner(e);

   
    calldataarg args;
    f(e, args);

    // Postcondition
    assert getGovernor() == owner(),
        "Governor should be equal to owner";
}
