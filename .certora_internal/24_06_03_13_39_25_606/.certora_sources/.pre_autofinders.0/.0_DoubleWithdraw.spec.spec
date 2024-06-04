rule noDoubleWithdraw(address user) {
    // uint256 amount = allBalancesOf(user);
    uint256 amount = getCreditOf(user);
    env e;
    require e.msg.sender == user;
    withdraw(e, amount);
    uint256 x;
    withdraw@withrevert(e, x);
    assert lastReverted;
}
