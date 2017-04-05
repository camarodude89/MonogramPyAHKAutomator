;Automation for ShoreTel Communicator installer

SetTitleMatchMode, 2

;Initiate ShoreTel Communicator installer by proxy of bat file
;This negates the need to bypass the Open File - Security Warning if the install
;is performed from the built-in admin account
SetWorkingDir .
#Include ComScripts\com.ahk

;Chooses initial Next button of the ShoreTel Communicator installer
WinWait, ahk_class MsiDialogCloseClass, To continue
TrayTip, Info, Selecting Next button
ControlSend, Button1, {Space}, ahk_class MsiDialogCloseClass

;Chooses Accept radio button for License Agreement
WinWait, ahk_class MsiDialogCloseClass, License Agreement
TrayTip, Info, Selecting Accept
Send {Up}

;Chooses Next button for License Agreement
ControlSend, Button5, {Space}, ahk_class MsiDialogCloseClass

;Chooses Next button for Installation warning
WinWait, ahk_class MsiDialogCloseClass, Installation warning
TrayTip, Info, Selecting Next for Installation warning
ControlSend, Button1, {Space}, ahk_class MsiDialogCloseClass

;Chooses Next button for Destination Folder
WinWait, ahk_class MsiDialogCloseClass, Destination Folder
TrayTip, Info, Selecting Next for Destination Folder
ControlSend, Button1, {Space}, ahk_class MsiDialogCloseClass

;Chooses Install button
WinWait, ahk_class MsiDialogCloseClass, Install the Program
TrayTip, Info, Selecting Install
ControlSend, Button1, {Space}, ahk_class MsiDialogCloseClass

;Chooses Finish button
WinWait, ahk_class MsiDialogCloseClass, Completed
TrayTip, Info, Selecting Finish
ControlSend, Button1, {Space}, ahk_class MsiDialogCloseClass
