/*
* check for state changes in deposits
*/

rule depositTransition(method f) {
    calldataarg args;
    env e;
    address from;
    address to;
    uint256 amount;

    uint256 deposits_before = deposit(from, to, amount);

    f(e, args);

    uint256 deposits_after = deposit(from, to, amount);

    assert deposits_before != deposits_after,
    "Balance must change after deposits";

}