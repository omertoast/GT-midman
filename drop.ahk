CoordMode, Pixel, Client
ControlClick, X102 Y431, ahk_exe Growtopia.exe, , LEFT,, D ;sola yürüme iki
Sleep, 10
ControlClick, X102 Y431, ahk_exe Growtopia.exe, , LEFT,,U ;sola yürümeyi durdurma
Sleep, 1000

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
				break	
			}
		}
		
		else
		{
			xpos3 := xpos3 + 80
		}
	}
}

ControlClick, X%DLkorX% Y%DLkorY% , ahk_exe Growtopia.exe, , LEFT ;DL
Sleep, 1000
ControlClick, X930 Y649, ahk_exe Growtopia.exe, , LEFT ;drop
Sleep, 1500
ControlClick, X515 Y469, ahk_exe Growtopia.exe, , LEFT ;drop ok
ControlClick, X515 Y469, ahk_exe Growtopia.exe, , LEFT ;drop ok
ControlClick, X515 Y469, ahk_exe Growtopia.exe, , LEFT ;drop ok
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

ControlClick, X%DLkorX% Y%DLkorY% , ahk_exe Growtopia.exe, , LEFT ;DL

Sleep, 1000
ControlClick, X930 Y649, ahk_exe Growtopia.exe, , LEFT ;drop
Sleep, 1500
ControlClick, X515 Y469, ahk_exe Growtopia.exe, , LEFT ;drop ok
ControlClick, X515 Y469, ahk_exe Growtopia.exe, , LEFT ;drop ok 
ControlClick, X515 Y469, ahk_exe Growtopia.exe, , LEFT ;drop ok

ControlClick, X250 Y435, ahk_exe Growtopia.exe, , LEFT,, D ;sağa yürüme iki
Sleep, 10
ControlClick, X250 Y435, ahk_exe Growtopia.exe, , LEFT,,U ;sağa yürümeyi durdurma