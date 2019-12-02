#NoEnv
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%
;Send {Left}
;ControlSend, ahk_parent,{}, ahk_exe Growtopia.exe

^!f::
{
	Send, My First Script
	return
}


ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,, D ;sola yürüme bir
ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,, D ;sola yürüme iki
Sleep, 200
ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,,U ;sola yürümeyi durdurma 
Sleep, 500
ControlClick, X350 Y280, ahk_exe Growtopia.exe, , LEFT
Sleep, 1000
ControlClick, X355 Y447, ahk_exe Growtopia.exe, , LEFT ;password 
Sleep, 1000
;ControlSend, ahk_parent,{^!f}, ahk_exe Growtopia.exe

;ControlClick, X395 Y580, ahk_exe Growtopia.exe, , LEFT

;MouseMove, 426, 449

;ControlClick, X426 Y449, ahk_exe Growtopia.exe, , Right,
;ControlSend, ahk_parent,{LButton}, ahk_exe Growtopia.exe
;Click, Left, 578 