send_and_let_go() ->
    Pid = spawn(fun() -> receive {Message, From} -> From ! {ack, Message} end end),
    Pid ! {self(), "Embrace change and move forward"},
    receive {ack, _} -> "Message sent, moving on" end.
