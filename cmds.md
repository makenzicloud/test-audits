 # certoraRun  Controller.sol:Controller --verify  Controller:access.spec 

 # certoraRun  BondManager.sol  --verify  BondManager:ZeroAddress.spec  --optimistic_loop --optimistic_hashing 

 # certoraRun  Lib_AddressManager.sol --verify  Lib_AddressManager:ZeroAddress.spec   --optimistic_hashing --optimistic_loop 

 # certoraRun DegenDealer.sol --verify  DegenDealer:Reentrancy.spec   --solc solc8.0

 certoraRun DegenDealer.sol --verify  DegenDealer:Balances.spec  --optimistic_loop --optimistic_hashing 

 #  certoraRun DegenDealer.sol --verify  DegenDealer:Ownable.spec --optimistic_loop --optimistic_hashing 

  certoraRun ERC20.sol --verify  ERC20:Token.spec  --optimistic_loop --optimistic_hashing