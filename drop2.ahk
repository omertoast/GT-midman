CoordMode, Pixel, Client

filewl := FileOpen("mod_control.txt", "w")

PixelGetColor, color, 770, 72, RGB
if (color = "0xF9362D")
{
	DLsonuc := 0
}

else
{
	DLsonuc := 1
}

if (DLsonuc = "0")
{
filewl.Write("0")
filewl.Close()
}

if (DLsonuc = "1")
{
filewl.Write("1")
filewl.Close()
}