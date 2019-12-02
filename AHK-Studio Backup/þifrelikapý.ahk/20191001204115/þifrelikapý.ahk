;Send {Left}
;ControlSend, ahk_parent,{}, ahk_exe Growtopia.exe


;ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,, D ;remove items

Loop, 5
{
	ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT
}