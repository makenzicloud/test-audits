// erc20 methods
methods {
    function addBalance()  external                             returns (uint256) => DISPATCHER(true);
    function withdraw()    external                            returns (uint256) => DISPATCHER(true);
    function withdrawAll() external                         returns (uint256) => DISPATCHER(true);


}