;Send {Left}
;ControlSend, ahk_parent,{Blind}{Left}, ahk_exe Growtopia.exe
;Sleep, 10000

[::
loop, 10000000000000000
	
{
Send {Left}
sleep 5
Send {Up}
sleep 10000000000000000
}

]::
pause 