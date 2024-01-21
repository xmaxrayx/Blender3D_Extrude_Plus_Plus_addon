#Requires AutoHotkey v2.0
#SingleInstance Force

;[Laptop HQ] @xMaxrayx @Unbreakable-ray [Code : ReBorn]   at 10:42:51  on 18/1/2024   (24H Format)  (UTC +2) 	 {Can we prove we are stronger than before?}


InstallKeybdHook(true,true)
;==========change this if you want==========
global time := 0.4 ;only numbers
;global key := winKeyCombo("{F8}")
;global key := '{F2}'
;global key := "{LWin Down}{F8}{LWin Up}"
;================================

#HotIf WinActive("ahk_exe blender.exe")

$E::{

global time
isKeyPressedTooLong := KeyWait("e" , "T" time)

if isKeyPressedTooLong == true {
    SendInput("#{F8}")
    MsgBox
    return
}else{
    SendInput("e")
    KeyWait("e" , "L")
    return
}


}




winKeyCombo(key){
return "{LWin Down}{" key "}{LWin Up}"
}

#HotIf WinActive("ahk_exe blender.exe")
