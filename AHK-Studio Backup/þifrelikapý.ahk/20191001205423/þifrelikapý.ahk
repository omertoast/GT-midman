;Send {Left}
;ControlSend, ahk_parent,{}, ahk_exe Growtopia.exe


;ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,, D ;remove items

ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,,D
Sleep, 200
ControlClick, X100 Y537, ahk_exe Growtopia.exe, , LEFT,,U
Sleep, 500
ControlClick, X350 Y280, ahk_exe Growtopia.exe, , LEFT
Sleep, 16000
ControlClick, X365 Y450, ahk_exe Growtopia.exe, , LEFT