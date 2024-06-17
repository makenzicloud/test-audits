
rule targetCallRevertConditions()
{
    env e;

    changeOwner@withrevert(e);
    bool isReverted = lastReverted;

    assert !isReverted <=> e.msg.value == 0;
}