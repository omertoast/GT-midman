ControlClick, X169 Y649, ahk_exe Growtopia.exe, , LEFT ;wrench
ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,, D ;sola yürüme iki
Sleep, 200
ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,,U ;sola yürümeyi durdurma 
Sleep, 500
ControlClick, X350 Y280, ahk_exe Growtopia.exe, , LEFT
Sleep, 750
ControlClick, X355 Y447, ahk_exe Growtopia.exe, , LEFT ;password 
Sleep, 250
Loop, 23 {
	ControlSend, ahk_parent,{BackSpace},ahk_exe Growtopia.exe
Send, MAVIBALINA33
Sleep, 250
ControlClick, X400 Y600, ahk_exe Growtopia.exe
Sleep, 500
ControlClick, X250 Y523, ahk_exe Growtopia.exe, , LEFT,, D ;sağaa yürüme iki
Sleep, 300
ControlClick, X250 Y523, ahk_exe Growtopia.exe, , LEFT,,U ;sağaa yürümeyi durdurma
ControlClick, X169 Y649, ahk_exe Growtopia.exe, , LEFT 