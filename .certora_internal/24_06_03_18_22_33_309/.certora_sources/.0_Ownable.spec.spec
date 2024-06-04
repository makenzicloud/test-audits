import "./helpers.spec";
import "./IOwnable.spec";

methods {
    // Declare methods that exist in the DegenDealer contract
    function transferOwnership(address newOwner) external;
    function renounceOwnership() external;
    function withdraw(address to, uint256 amount, uint256 id, bool isInternal) external;
    function batchUpdatePosition((address, int256, int256, int256, int256, string)[] calldata positionDatas) external;
    function deposit(address from, address to, uint256 amount) external;
    function owner() external returns (address envfree);
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Function correctness: transferOwnership changes ownership                                                           │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule transferOwnership(env e) {
    require nonpayable(e);

    address newOwner;
    address current = owner();

    transferOwnership@withrevert(e, newOwner);
    bool success = !lastReverted;

    assert success <=> (e.msg.sender == current && newOwner != address(0)), "unauthorized caller or invalid arg";
    assert success => owner() == newOwner, "current owner changed";
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Function correctness: renounceOwnership removes the owner                                                           │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule renounceOwnership(env e) {
    require nonpayable(e);

    address current = owner();

    renounceOwnership@withrevert(e);
    bool success = !lastReverted;

    assert success <=> e.msg.sender == current, "unauthorized caller";
    assert success => owner() == address(0), "owner not cleared";
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Access control: only current owner can call restricted functions                                                    │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyCurrentOwnerCanCallRestricted(env e, method f) {
    require nonpayable(e);

    address current = owner();

    calldataarg args;
    f@withrevert(e, args);

    assert !lastReverted <=> e.msg.sender == current, "access control failed";
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Rule: ownership can only change in specific ways                                                                    │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule onlyOwnerOrPendingOwnerCanChangeOwnership(env e) {
    address oldCurrent = owner();

    method f; calldataarg args;
    f(e, args);

    address newCurrent = owner();

    // If owner changes, must be either transferOwnership or renounceOwnership
    assert oldCurrent != newCurrent => (
        (e.msg.sender == oldCurrent && newCurrent != address(0) && f.selector == sig:transferOwnership(address)) ||
        (e.msg.sender == oldCurrent && newCurrent == address(0) && f.selector == sig:renounceOwnership())
    );
}
