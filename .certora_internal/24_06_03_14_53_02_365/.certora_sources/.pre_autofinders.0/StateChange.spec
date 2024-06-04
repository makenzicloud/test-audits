/*
* check for state changes in deposits
*/

rule depositTransition(method f) {
    calldataarg args;
    env e;
    address from;
    address to;
    uint256 amount;

    uint256 deposits_before = deposit(from, to);

    f(e, args);

    uint256 deposits_after = deposit(from, to);

    assert deposits_before != deposits_after,
    "Balance must change after deposits";

}