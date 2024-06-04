/*
* check for state changes in deposits
*/

rule depositTransition(method f) {
    calldataarg args;
    env e;
    uint256 deposits_before = deposit(e);

    f(e, args);

    uint256 deposits_after = deposit(e);

    assert deposits_before != deposits_after,
    "Balance must change after deposits";

}