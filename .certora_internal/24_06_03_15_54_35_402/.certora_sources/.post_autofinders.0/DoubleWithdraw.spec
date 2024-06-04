rule noDoubleWithdraw(address account) {
    // uint256 amount = allBalancesOf(user);
    uint256 amount = getCreditOf(account);
    uint256 id;
    env e;
    require e.msg.sender == account;
    withdraw(e, address,uint256,uint256,bool);
    uint256 x;
    withdraw@withrevert(e, x);
    assert lastReverted;
}
