// Verifacation of the MulWadUp contract using Certora Prover

method {
    function mulWadUp(uint256 x, uint256 y) external pure returns uint256 envfree {
}

rule check_testMulWadUpFuzz(x: uint256, y: uint256) {
    if (x == 0 || y == 0 || y <= type(uint256).max / x) {
        uint256 result = MathMasters.mulWadUp(x, y);
        uint256 expected = x * y == 0 ? 0 : x * y;
        assert(result == expected);
        
    }

}