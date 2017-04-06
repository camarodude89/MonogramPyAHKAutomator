;Automation for Adobe Reader Installer

SetTitleMatchMode, 2

;Initiate Adobe Reader installer by proxy of bat file
;This negates the need to bypass the Open File - Security Warning if the install
;is performed from the built-in admin account
SetWorkingDir .
#Include ComScripts\com.ahk

;Bypasses Open File - Security Warning window if it appears
;IfWinExist, Open File - Security Warning
;{
;  TrayTip, Info, Bypassing Security Window
;  WinActivate
;  Sleep 500
;  Send {Shift Right}
;  Send {R}
;}

;Wait for extraction process to complete
WinWait, ahk_class #32770, Preparing installation
TrayTip, Info, Waiting on extraction process
WinWaitClose, ahk_class #32770, Preparing installation

;Chooses Next button of Adobe Reader installer
WinWait, ahk_class MsiDialogCloseClass, Destination
TrayTip, Info, Selecting Next button
ControlSend, Button1, {Space}, ahk_class MsiDialogCloseClass

;Chooses Install button of Adobe Reader installer
WinWait, ahk_class MsiDialogCloseClass, automatically
TrayTip, Info, Selecting Install button
ControlSend, Button1, {Space}, ahk_class MsiDialogCloseClass

;Wait for installation process to complete
WinWait, ahk_class MsiDialogCloseClass, are being installed
TrayTip, Info, Waiting on installation process

;Chooses Finish button of Adobe Reader installer
WinWait, ahk_class MsiDialogCloseClass, successfully
TrayTip, Info, Selecting Finish button
ControlSend, Button1, {Space}, ahk_class MsiDialogCloseClass
WinWaitClose, ahk_class MsiDialogCloseClass, successfully
