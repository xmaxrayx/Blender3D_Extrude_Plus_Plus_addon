#Requires AutoHotkey v2.0
#SingleInstance Force

;[Laptop HQ] @xMaxrayx @Unbreakable-ray [Code : ReBorn]   at 10:42:51  on 18/1/2024   (24H Format)  (UTC +2) 	 {Can we prove we are stronger than before?}



;==========change this if you want==========
global time := 0.4 ;only numbers
global key := winKeyCombo("F11")
;================================

#HotIf WinActive("ahk_exe blender.exe")

$e::{

global time
isKeyPressedTooLong := !KeyWait("e" , "T" time)

if isKeyPressedTooLong == true {
    Send(key)
}else{
    ; Send("{e}")
    Send("e")
    KeyWait("e" , "L")
}
return

}




winKeyCombo(key){
return "{LWin Down}{" key "}{LWin Up}"
}

