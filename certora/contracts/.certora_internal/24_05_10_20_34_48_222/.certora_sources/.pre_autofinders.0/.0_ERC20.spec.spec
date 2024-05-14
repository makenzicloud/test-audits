methods {
    function balanceOf(address) external returns (uint256) envfree;
    
}

// Transfer must move `amount` tokens from
// the caller's account to `recipient`.

rule transferSpec{
    
    address recipient;
    uint256 amount;

    env e;
   

    mathint balance_sender_before = balanceOf(e.msg.sender);
    mathint balance_recipient_before = balanceOf(recipient);

    transfer(e, recipient, amount); 

    mathint balance_sender_after = balanceOf(e.msg.sender);
    mathint balance_recipient_after = balanceOf(recipient);

    address sender = e.msg.sender;

    require sender != recipient;

    assert recipient != sender => balance_sender_after == balance_sender_before - amount,
        "sender balance should decrease by amount";

    assert recipient != sender => balance_recipient_after == balance_recipient_before + amount,
        "recipient balance should increase by amount";

    assert recipient == sender => balance_sender_after == balance_sender_before,
        "sender balance should not change if sender == recipient";        
}
