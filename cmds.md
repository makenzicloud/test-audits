 # certoraRun  Controller.sol:Controller --verify  Controller:access.spec 

 # certoraRun  BondManager.sol  --verify  BondManager:ZeroAddress.spec  --optimistic_loop --optimistic_hashing 

 # certoraRun  Lib_AddressManager.sol --verify  Lib_AddressManager:ZeroAddress.spec   --optimistic_hashing --optimistic_loop 

 # certoraRun  glodollar.sol:RabbitHabit --verify RabbitHabit:BurnMint.spec --optimistic_hashing --optimistic_loop 

 certoraRun DegenDealer.sol --verify  DegenDealer:Balances.spec  --optimistic_loop --optimistic_hashing 

 #  certoraRun DegenDealer.sol:DegenDealer  --verify DegenDealer:Benchmarking.spec --optimistic_loop --optimistic_hashing 

  certoraRun THORChain_Router.sol:THORChain_Router --verify THORChain_Router:Benchmarking.spec --optimistic_loop --optimistic_hashing 
  
  # certoraRun Dispenser.sol:Dispenser --verify Dispenser:TargetCall.spec --optimistic_loop --optimistic_hashing 