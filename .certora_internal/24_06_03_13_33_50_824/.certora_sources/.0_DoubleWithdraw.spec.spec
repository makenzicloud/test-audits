rule noDoubleWithdraw(address user) {
    // uint256 amount = allBalancesOf(user);
    uint256 initialBalance = degenDealer.getUserBalance(user);
    env e;
    require e.msg.sender == user;
    claim(e, amount);
    uint256 x;
    withdraw@withrevert(e, x);
    assert lastReverted;
}
