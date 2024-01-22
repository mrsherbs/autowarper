#SingleInstance force
#include MouseDelta.ahk

md := new MouseDelta("MouseEvent").Start()
 
md.SetState(true)

DllCall("mouse_event",uint,1,int,0,int,5,uint,0,int,0)
ExitApp