
filePath = %1%
quotedFilePath := ""

Loop, Parse, filePath, "\"
{
  IfInString, A_LoopField, %A_Space%
  {
    quotedFilePath = %quotedFilePath%"%A_LoopField%"\
    Continue
  }
  quotedFilePath = %quotedFilePath%%A_LoopField%\
}

StringTrimRight, quotedFilePath, quotedFilePath, 1

Run, com.bat %quotedFilePath%
