/*
*No double withdrawal
*/

methods {
    function totalSupply()                          external returns(uint) envfree;
    function balanceOf(address)                     external returns(uint) envfree;
    function allowance(address,address)             external returns(uint) envfree;
    function transfer(address,uint)                 external;
    function deposit(uint256)                        external returns(uint256);
    function withdraw(uint256)                       external returns(uint256);
}

rule noDoubleWithdraw(address account) {
    // uint256 amount = allBalancesOf(user);
    uint256 amount = getCreditOf(account);
    uint256 id;
    address to;
    // bool;

    env e;
    require e.msg.sender == account;
    withdraw(e, address, uint256, uint256);
    uint256 x;
    withdraw@withrevert(e, x);
    assert lastReverted;
}
