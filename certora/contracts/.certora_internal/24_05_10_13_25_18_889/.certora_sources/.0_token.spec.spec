// erc20 methods
methods {
    function addBalance()  public                             returns (uint256) => DISPATCHER(true);
    function withdraw()    public                            returns (uint256) => DISPATCHER(true);
    function withdrawAll() public                         returns (uint256) => DISPATCHER(true);


}