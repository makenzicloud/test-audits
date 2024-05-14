methods {
    function balanceOf(address) external returns (uint256) envfree;
    
}

// Transfer must move `amount` tokens from
// the caller's account to `recipient`.

rule transferSpec{
    address sender;
    address recipient;
    uint256 amount;

    env e;
    require e.sender == sender;

    mathint balance_sender_before = e.balanceOf(sender);
    mathint balance_recipient_before = e.balanceOf(recipient);

    transfer(e, recipient, amount); 

    mathint balance_sender_after = e.balanceOf(sender);
    mathint balance_recipient_after = e.balanceOf(recipient);

    require sender != recipient;

    assert balance_sender_after == balance_sender_before - amount,
        "sender balance should decrease by amount";

    assert balance_recipient_after == balance_recipient_before + amount,
        "recipient balance should increase by amount";    
}
