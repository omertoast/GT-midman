;Send {Left}
;ControlSend, ahk_parent,{ESC}, ahk_exe Growtopia.exe

loop, 100
{
	ControlClick, X100 Y4530, ahk_exe Growtopia.exe, , LEFT ;remove items
}