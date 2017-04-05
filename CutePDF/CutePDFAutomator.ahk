;Automation for CutePDF installer

SetTitleMatchMode, 2

;Initiate CutePDF installer by proxy of bat file
;This negates the need to bypass the Open File - Security Warning if the install
;is performed from the built-in admin account
SetWorkingDir .
#Include ComScripts\com.ahk

;Chooses initial Next button of the CutePDF installer
WinWait, ahk_class TWizardForm, Welcome to the CutePDF
TrayTip, Info, Selecting Next button
ControlSend, TNewButton1, {Space}, ahk_class TWizardForm

;Chooses Accept radio button for License Agreement
WinWait, ahk_class TWizardForm, License Agreement
TrayTip, Info, Selecting Accept
Send {Tab}
Send {Up}

;Chooses Next button for License Agreement
TrayTip, Info, Selecting Next button
ControlSend, TNewButton2, {Space}, ahk_class TWizardForm

;Chooses Install button
WinWait, ahk_class TWizardForm, Ready to Install
TrayTip, Info, Selecting Install button
ControlSend, TNewButton2, {Space}, ahk_class TWizardForm

;Chooses Yes button fo download of PS2PDF converter
WinWait, ahk_class #32770, PS2PDF
TrayTip, Info, Selecting Yes button
ControlSend, Button1, {Space}, ahk_class #32770
