CoordMode, Pixel, Client

filewl := FileOpen("serialWL.txt", "w")
filedl := FileOpen("serialDL.txt", "w")
xpos := 60
ypos := 520
xposF := 60
yposF := 520
WLsonuc := 0
ypos3 := 600
xpos3 := 60
ControlClick, X169 Y549, ahk_exe Growtopia.exe, , LEFT ;wrench

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

if (WLsonuc = "1")
{
filewl.Write("1")
filewl.Close()
}

if (WLsonuc = "0")
{
filewl.Write("0")
filewl.Close()
}

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

if (DLsonuc = "1")
{
filedl.Write("1")
filedl.Close()
}

if (DLsonuc = "0")
{
filedl.Write("0")
filedl.Close()
}