;Send {Left}
ControlSend, ahk_parent,{ESC}, ahk_exe Growtopia.exe

loop, 100000000
{
	ControlSend, ahk_parent,{Right}, ahk_exe Growtopia.exe
}