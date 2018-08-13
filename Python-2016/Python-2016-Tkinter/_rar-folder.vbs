dim wsh
set wsh=wscript.createobject("wscript.shell")

set fso = createobject("scripting.filesystemobject")
set objFolder = fso.getfolder(".")
Set objFolders = objFolder.SubFolders

For Each objFolder In objFolders
    m_strFolder = objFolder.name
    If m_strFolder<>"." And m_strFolder<>".." Then
        m_strFolder_base = m_strFolder'fso.GetBaseName(m_strFolder)
        'm_strCommand = """%ProgramFiles%\WinRAR\WinRAR.exe"" a -df -hpwww """ & m_strFolder_base & ".rar"" """ & m_strFolder_base & """"
        m_strCommand = """%ProgramFiles%\WinRAR\WinRAR.exe"" a -hpwww """ & m_strFolder_base & ".rar"" """ & m_strFolder_base & """"
        'MsgBox(m_strCommand)
        wsh.run m_strCommand, 1, true
    End If
Next

MsgBox ("Done.")
