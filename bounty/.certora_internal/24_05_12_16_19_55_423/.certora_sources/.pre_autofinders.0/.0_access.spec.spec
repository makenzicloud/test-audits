/*
* Test acces control
*/

invariant governorConsistency(env e) 
    getGovernor(e) == owner();


rule  governorConsistencyAsRule(env e, method f) {
    // Precondition
    require getGovernor() == owner(e);

    
    calldataarg args;
    f(e, args);

    // Postcondition
    assert getGovernor() == owner(),
        "Governor should be equal to owner";
}


  