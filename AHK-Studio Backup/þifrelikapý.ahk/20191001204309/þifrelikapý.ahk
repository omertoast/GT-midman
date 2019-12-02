;Send {Left}
;ControlSend, ahk_parent,{}, ahk_exe Growtopia.exe


;ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,, D ;remove items

Loop, 1
{
	ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,,D
}