/*
* Test access control
*/

invariant governorConsistency(env e) 
   getGovernor(e) == owner(e);


rule governorConsistencyAsRule( env e, method f) {
    // Precondition
    require getGovernor(e) == governor(e);

   
    calldataarg args;
    f(e, args);

    // Postcondition
    assert getGovernor(e) == governor(e),
        "Governor should be equal to governor";
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Rule: Governer is only affected by accepting an admin transfer or renoucing                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/

rule noDefaultAdminChange(env e, method f, calldataarg args) {
    // Ensure the sender is a non-zero account
    require e.msg.sender != address(0);
    
    // Ensure default admin consistency
    requireInvariant governorConsistencyAsRule(getGovernor(), governor());
    
    // Ensure single default admin
    requireInvariant singleGovernor(e.msg.sender, getGovernor());

    // Record the default admin before executing the method
    address adminBefore = getGovernor();
    
    // Execute the method
    f(e, args);
    
    // Record the default admin after executing the method
    address adminAfter = getGovernor();

    // Check if the default admin changed
    assert adminBefore != adminAfter => (
        // Check if the method is either accepting an admin transfer or renouncing the role
        f.selector == acceptOwnership().selector ||
        f.selector == renounceOwnership().selector
    ), "Governor is only affected by accepting an admin transfer or renouncing";
}
