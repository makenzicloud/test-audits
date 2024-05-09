/*
*/

ghost bool called_extcall;
ghost bool g_reverted;
ghost uint g_sighash;

// Hook on "CALL" opcodes to simulate reentrancy
hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    called_extcall = true;
    env e;
    bool cond;
    
    if (g_sighash == sig:withdraw(uint256).selector) {
        calldataarg args;
        withdraw@withrevert(e); // concrete name
        g_reverted = lastReverted;
    }

    else {
        // Fallback case
        g_reverted = true;
    }
}

// Rule filtering for non-view functions
rule no_reentrancy(method f, method g) filtered { f->!f.isView, g ->!g.isView } {
    require!called_extcall;
    require!g_reverted;
    env e; calldataarg args;
    
    // Place the assertion here to verify the function signature before the function call
    assert_uint32(g_sighash) == g.selector, "Incorrect function signature";

    f@withrevert(e, args);
    
    // Main assert here - we expect that if an external function is called
    // any reentrancy to a non-view function will revert
    assert called_extcall => g_reverted, "Reentrancy weakness exists";
}
