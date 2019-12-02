CoordMode, Pixel, Client
MouseGetPos, xpos, ypos

^!z::
PixelGetColor, color , %xpos% , %ypos%, RGB
if(color = 3192FF)
{
	msgBox, sex
}