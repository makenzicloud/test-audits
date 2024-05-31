#!/bin/bash

for FILE in Controller.sol /* 
do 
  echo $FILE 
  contract=`echo ${FILE} | perl -0777 -pe 's/.*\///g' | awk -F'.' '{print $1}'` 
  echo $contract
  certoraRun ${FILE} \
      --verify ${contract}:Reentrancy.spec \
      --optimistic_loop --loop_iter 3 \
      --prover_args "-enableStorageSplitting false" \
      --msg "${contract} : NoGuardSafety"
      --solc_args "--solidity-version=0.7.3"
  
  certoraRun ${FILE} \
      --verify ${contract}:Reentrancy.spec \
      --optimistic_loop --loop_iter 3 \
      --msg "${contract} : Reentrancy"
      --solc_args "--solidity-version=0.7.3"

  certoraRun ${FILE} \
      --verify ${contract}:Reentrancy.spec \
      --optimistic_loop --loop_iter 3 \
      --msg "${contract} : ROReentrancy"
      --solc_args "--solidity-version=0.7.3"
done