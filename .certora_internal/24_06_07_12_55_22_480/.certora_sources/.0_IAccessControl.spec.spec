methods {
    function hasRole(bytes32, address) returns(bool) envfree;
    function getRoleAdmin(bytes32) returns(bytes32) envfree;
    function grantRole(bytes32, address)  returns address envfree;
    function revokeRole(bytes32, address) returns address envfree;
    function renounceRole(bytes32, address) returns address envfree;
}
