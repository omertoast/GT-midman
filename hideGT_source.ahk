#CommentFlag //
#MaxThreadsPerHotkey 2 // Without this the loop won't work
#Persistent
SetWorkingDir, %A_Temp% // Save location to temp folder

show = 0

Menu, tray, Add, Growtopia'yı Göster, HideGT

WinShow, ahk_exe Growtopia.exe
DetectHiddenWindows, on

HideGT: // Toggles Growtopia window visibility
    if (show = 1) {
        WinWait, ahk_exe Growtopia.exe, , 1
        WinHide, ahk_exe Growtopia.exe
        if ErrorLevel {
            TrayTip, Error, Growtopia is closed, cannot hide it!, 4, 3
        } else {
            WinHide, ahk_exe Growtopia.exe
            show = 0
            Menu, tray, Uncheck, Growtopia'yı Göster
        }
    } else {
        WinWait, ahk_exe Growtopia.exe, , 1
        if ErrorLevel {
            TrayTip, Error, Growtopia is closed, cannot show it!, 4, 3
        } else {
            WinShow, ahk_exe Growtopia.exe
            show = 1
            Menu, tray, Check, Growtopia'yı Göster
        }
    }
    Return
       