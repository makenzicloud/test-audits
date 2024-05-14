// Import the Controller contract
// import "./Controller.sol";

// Ensure governor consistency
invariant governorConsistency(env e) 
    getGovernor(e) == governor(e);

// Rule to ensure governor consistency after method execution
rule governorConsistencyAsRule(env e, method f) {
    // Precondition: Check governor consistency before method execution
    require getGovernor(e) == governor(e);

    calldataarg args;
    f(e, args); // Execute the method

    // Postcondition: Check governor consistency after method execution
    assert getGovernor(e) == governor(e), "Governor should remain consistent";
}

// Rule to prevent changes to the governor except for accepting an admin transfer
rule noGovernorChange(env e, method f, calldataarg args) {
    // Ensure the sender is not the zero address
    require e.msg.sender != 0x0;
    
    // Ensure governor consistency before method execution
    require governorConsistency(e);
    
    // Record the governor before executing the method
    address governorBefore = getGovernor(e);
    
    // Execute the method
    f(e, args);
    
    // Record the governor after executing the method
    address governorAfter = getGovernor(e);

    // Check if the governor changed
    assert governorBefore == governorAfter || 
           (f.selector == Controller(f.contract).acceptOwnership.selector),
           "Governor is only affected by accepting an admin transfer";
}
