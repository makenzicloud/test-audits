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
    // Ensure the sender is not the zero address
    require e.msg.sender != 0x0;
    
    // Record the governor before executing the method
    address governorBefore = getGovernor(e);

    
    // Execute the method
    f(e, args);
    
    // Record the governor after executing the method
    address governorAfter = getGovernor(e);

    // Check if the governor changed
    assert governorBefore != governorAfter => (f.selector == Governor.acceptOwnership.selector),
    "Governor can only change through acceptOwnership";


     // Condition
    // assert governorBefore != governorAfter => (
    //     f.selector == Controller.acceptOwnership.selector),
    //     "Ownership is only affected by accepting an Ownership transfer";    
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

//     // New state
//     new_state {
//         Governance.acceptOwnership(e);
//     }

//     // Condition
//     require pendingGovernor != address(0) && sender == pendingGovernor;
// }

// assert {
//     env e;
//     address governorBefore;
//     address governorAfter;
//     any f;

//     // Old state
//     old_state {
//         governorBefore = Governance.getGovernor(e);
//     }

//     // New state
//     new_state {
//         Governance.acceptOwnership(e);
//         governorAfter = Governance.getGovernor(e);
//     }

//     // // Condition
//     // assert governorBefore != governorAfter => (
//     //     f.selector == Controller.acceptOwnership.selector),
//     //     "Ownership is only affected by accepting an Ownership transfer";
// }