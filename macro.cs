using Microsoft.Office.Interop.Word;
using Microsoft.Vbe.Interop;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Create a new Word application
        Microsoft.Office.Interop.Word.Application wordApp = new Microsoft.Office.Interop.Word.Application();
        Document doc = wordApp.Documents.Add();

        // Add a paragraph with the text "Test"
        Paragraph paragraph = doc.Content.Paragraphs.Add();
        paragraph.Range.Text = "Test";

        // Add VBA code to a new module
        VBProject vbProject = doc.VBProject;
        VBComponent module = vbProject.VBComponents.Add(vbext_ComponentType.vbext_ct_StdModule);
        module.CodeModule.DeleteLines(1, module.CodeModule.CountOfLines); // Clear existing code
        module.CodeModule.AddFromString(@"
Sub AutoOpen()
    MsgBox ""Hello"", vbInformation, ""Welcome Message""
End Sub");

        // Save the document as a macro-enabled document (.docm)
        string filePath = @"C:\users\ds_wa\desktop\test.doc";
        doc.SaveAs2(filePath, WdSaveFormat.wdFormatDocument97);

        // Close and release resources
        doc.Close();
        System.Runtime.InteropServices.Marshal.ReleaseComObject(doc);
        wordApp.Quit();
        System.Runtime.InteropServices.Marshal.ReleaseComObject(wordApp);

        Console.WriteLine("Document created successfully at: " + filePath);
    }
}
