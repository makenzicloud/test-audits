methods {
    // owner() returns (address) envfree
    // pendingOwner() returns (address) envfree
    // transferOwnership(address)
    // acceptOwnership()
    // renounceOwnership()
}

methods {
    function acceptOwnership()                                                 external returns();
    function renounceOwnership()                                               external returns();
    function owner()                                                           external returns address envfree;
    function pendingowner()                                                    external returns address envfree;
    function transferOwnership()                                               external returns address envfree;
}