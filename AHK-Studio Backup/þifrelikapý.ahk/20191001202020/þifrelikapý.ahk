;Send {Left}
ControlSend, ahk_parent,{Blind}{Left}, ahk_exe Growtopia.exe
Sleep, 10000

[::
loop, 10000000000000000
	
{
ControlSend, ahk_parent,{Left}, ahk_exe Growtopia.exe
sleep 10000000000000000
}

]::
pause 