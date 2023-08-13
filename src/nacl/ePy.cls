Class nacl.ePy
{
ClassMethod Connect(
	serverIP = "192.168.0.9",
	serverPORT = 1972,
	namespace = "USER",
	username = "_SYSTEM",
	password = "SYS") As %Net.DB.Iris
{
  try {
    set %rccon=##class(%Net.DB.DataSource).CreateConnection(serverIP
                           ,serverPORT,namespace,username,password)
    set %rccdb=%rccon.CreateIris()
    }
  catch { zw  b  }  ;; do some error handling
  quit %rccdb
}

ClassMethod Do(
	request As %String,
	rccdb As %Net.DB.Iris = {%rccdb}) As %String
{
  set req=request_"  quit 0"   
  set res=rccdb.Function("%ZX","",req)
  quit res
}
}
