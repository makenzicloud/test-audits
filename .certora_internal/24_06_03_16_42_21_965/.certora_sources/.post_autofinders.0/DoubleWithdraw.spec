/*
*No double withdrawal
*/

methods {
 
    function deposit(uint256)                        external returns(uint256);
    function withdraw(uint256)                       external returns(uint256);
}

rule noDoubleWithdraw(address account) {
    // uint256 amount = allBalancesOf(user);
    // uint256 amount = getCreditOf(account);
    uint256 id;
    address to;
    uint256 amount;
    require amount > 0;
    uint256 amountMinted = deposit(e, amount);
    // bool;

    env e;
    require e.msg.sender == account;
    withdraw(e, uint256);
    uint256 x;
    withdraw@withrevert(e, x);
    assert lastReverted;
}
