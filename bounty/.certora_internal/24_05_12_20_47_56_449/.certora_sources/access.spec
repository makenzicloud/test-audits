/*
* Test access control
*/


rule governorConsistencyAsRule( env e, method f) {
    // Precondition
    require getGovernor(e) == governor(e);

   
    calldataarg args;
    f(e, args);

    // Postcondition
    assert getGovernor(e) == governor(e),
        "Governor should be equal to governor";
}









// Rule to prevent changes to the governor except for accepting an admin transfer
rule noGovernorChange(env e, method f, calldataarg args) {
    address governorBefore = getGovernor;
    address governorAfter = getGovernor;
    // Ensure the sender is not the zero address
    require e.msg.sender != 0x0;
    
    // Record the governor before executing the method
    address governorBefore = getGovernor(e);

    
    // Execute the method
    f(e, args);
    
    // Record the governor after executing the method
    address governorAfter = getGovernor(e);

    // Check if the governor changed

    //  Condition
    assert governorBefore != governorAfter => (
        f.selector == transferOwnership().selector),
        "Ownership is only affected by accepting an Ownership transfer";    
}

// rule acceptOwnership {
//     env e;
//     address pendingGovernor;
//     address sender;

//     // Old state
//     old_state {
//         pendingGovernor = Governance.getPendingGovernor(e);
//         sender = env.msg.sender(e);
//     }



