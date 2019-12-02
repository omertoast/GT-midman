wl_miktari = 3
ControlClick, X169 Y549, ahk_exe Growtopia.exe, , LEFT ;wrench
CoordMode, Pixel, Client

DLsonuc := 0
xpos := 60
ypos := 520
xposF := 60
yposF := 520
ypos3 := 600
xpos3 := 60

Loop, 10
{
	PixelGetColor, color, %xpos%, %ypos%, RGB
	if (color = "0xD8F4F8")
	{
		xpos2 := xpos
		ypos2 := ypos + 20
		PixelGetColor, color2, %xpos2%, %ypos2%, RGB
		if (color2 = "0xD8F4F8")
		{
;			MsgBox %xpos2% %ypos2%
			DLsonuc := 1
            DLkorX := xpos2
            DLkorY := ypos2
			ControlClick, X%DLkorX% Y%DLkorY% , ahk_exe Growtopia.exe, , LEFT ;DL
			ControlClick, X%DLkorX% Y%DLkorY% , ahk_exe Growtopia.exe, , LEFT ;DL
			break	
		}
	}
	
	else
	{
		xpos := xpos + 80
	}
}

if (DLsonuc = "0")
{
	Loop, 10
	{
		PixelGetColor, color3, %xpos3%, %ypos3%, RGB
		if (color3 = "0xD8F4F8")
		{
			xpos4 := xpos3
			ypos4 := ypos3 + 20
			PixelGetColor, color4, %xpos3%, %ypos4%, RGB
			if (color4 = "0xD8F4F8")
			{
	;			MsgBox %xpos2% %ypos2%
				DLsonuc := 1
				DLkorX := xpos4
				DLkorY := ypos4
				ControlClick, X%DLkorX% Y%DLkorY% , ahk_exe Growtopia.exe, , LEFT ;DL
				ControlClick, X%DLkorX% Y%DLkorY% , ahk_exe Growtopia.exe, , LEFT ;DL
				break
			}
		}
		
		else
		{
			xpos3 := xpos3 + 80
		}
	}
}

Sleep, 100
ControlClick, X169 Y549, ahk_exe Growtopia.exe, , LEFT ;wrench
Sleep, 100
ControlClick, X570 Y233, ahk_exe Growtopia.exe, , LEFT ;kasa
Sleep,1500
ControlClick, X351 Y419, ahk_exe Growtopia.exe, , LEFT ; deposit
Sleep, 1000

xpos := 60
ypos := 520
xposF := 60
yposF := 520
WLsonuc := 0
ypos3 := 600
xpos3 := 60

Loop, 10
{
	PixelGetColor, color, %xpos%, %ypos%, RGB
	if (color = "0xFFF115")
	{
		xpos2 := xpos
		ypos2 := ypos + 20
		PixelGetColor, color2, %xpos2%, %ypos2%, RGB
		if (color2 = "0xFFF115")
		{
;			MsgBox %xpos2% %ypos2%
			WLsonuc := 1
            DLkorX := xpos2
            DLkorY := ypos2
			break	
		}
	}
	
	else
	{
		xpos := xpos + 80
	}
}

if (WLsonuc = "0")
{
	Loop, 10
	{
		PixelGetColor, color3, %xpos3%, %ypos3%, RGB
		if (color3 = "0xFFF115")
		{
			xpos4 := xpos3
			ypos4 := ypos3 + 20
			PixelGetColor, color4, %xpos3%, %ypos4%, RGB
			if (color4 = "0xFFF115")
			{
	;			MsgBox %xpos2% %ypos2%
				WLsonuc := 1
				DLkorX := xpos4
				DLkorY := ypos4
				break	
			}
		}
		
		else
		{
			xpos3 := xpos3 + 80
		}
	}
}

ControlClick, X%DLkorX% Y%DLkorY% , ahk_exe Growtopia.exe, , LEFT ;WL

Sleep,500
Loop, 3
	ControlSend, ahk_parent,{BackSpace},ahk_exe Growtopia.exe
ControlSend,, %wl_miktari%, ahk_exe Growtopia.exe
Sleep, 1000
ControlClick, X281 Y464, ahk_exe Growtopia.exe, , LEFT ;store items
Sleep,1000
ControlSend, ahk_parent,{ESC},ahk_exe Growtopia.exe
Sleep, 500


xpos := 60
ypos := 520
xposF := 60
yposF := 520
WLsonuc := 0
ypos3 := 600
xpos3 := 60

Loop, 10
{
	PixelGetColor, color, %xpos%, %ypos%, RGB
	if (color = "0xFFF115")
	{
		xpos2 := xpos
		ypos2 := ypos + 20
		PixelGetColor, color2, %xpos2%, %ypos2%, RGB
		if (color2 = "0xFFF115")
		{
;			MsgBox %xpos2% %ypos2%
			WLsonuc := 1
            DLkorX := xpos2
            DLkorY := ypos2
			break	
		}
	}
	
	else
	{
		xpos := xpos + 80
	}
}

if (WLsonuc = "0")
{
	Loop, 10
	{
		PixelGetColor, color3, %xpos3%, %ypos3%, RGB
		if (color3 = "0xFFF115")
		{
			xpos4 := xpos3
			ypos4 := ypos3 + 20
			PixelGetColor, color4, %xpos3%, %ypos4%, RGB
			if (color4 = "0xFFF115")
			{
	;			MsgBox %xpos2% %ypos2%
				WLsonuc := 1
				DLkorX := xpos4
				DLkorY := ypos4
				break	
			}
		}
		
		else
		{
			xpos3 := xpos3 + 80
		}
	}
}

ControlClick, X%DLkorX% Y%DLkorY% , ahk_exe Growtopia.exe, , LEFT ;WL
ControlClick, X%DLkorX% Y%DLkorY% , ahk_exe Growtopia.exe, , LEFT ;WL

ControlClick, X169 Y549, ahk_exe Growtopia.exe, , LEFT ;wrench