import irisnative

def cmd(what,default):
    prompt=">>> "+what+" ["+default+"]: "
    ans=input(prompt)
    if (ans=="") :
        ans=default
    return ans

# init connection
ip   = cmd("serverIP","127.0.0.1")
port = cmd("serverPORT","1972")
nspc = cmd("namespace","USER")
user = cmd("username","_SYSTEM")
pwd  = cmd("password","SYS")
# get connected
conn = irisnative.createConnection(ip,int(port),nspc,user,pwd)
iris = irisnative.createIris(conn)

# talk to NativeAPI Extension
def act(what):
    ans=iris.function("","%ZX",what+" quit 0")
    return ans

inst=act("quit ##class(%SYS.System).GetInstanceName()")
node=act("quit ##class(%SYS.System).GetNodeName()")
print("\nConnected to Instance "+inst+" on Server "+node+"\n")

# demo menue
print("Select Demo to exercise")
print(" 0 = free ObjectScript")
print(" 1 = $ZV from Server")
print(" 2 = Actual Time in Server")
print(" 3 = TimeZone Offset of Server")
print(" 4 = Server Architecture*Vendor*Model")
print(" 5 = List Global in ZWRITE style")
print(" * = Terminate demo")

# show Global + Content
def dzr(glob):
    res=act('q ##class(%Utility).FormatString(@$zr)')
    print("\t",glob," = ",res)
    return
# scan Global
def gdemo(glob):
    if len(glob)>0 :
        dd=act("q $d("+glob+")")
        if dd%10>0 :
            dzr(glob)
    else:
        return
    while dd>9 :
        glob=act("q $q(@$zr)")
        if glob==None:
            dd=0
            break
        dzr(glob)
    return
# demo selection
while True :
    demo=cmd("take a choice","1")
    if (demo=="*") :
        break
    try :
        demo=int(demo)
    except ValueError :
        print("\tDemo '",demo,"' not implemented")
        continue   
    if (demo==0) :
        void=cmd("Your ObjectScript",' quit "?"')
        res=act(void)
    if (demo==1) :
        res=act("quit $ZV")
    if (demo==2) :
        res=act("quit $ZDT($h,3)")
    if (demo==3) :
        res=act("quit $ZTZ")
    if (demo==4) :
        void=act("set cp=$system.CPU.%New()")
        res=act("quit cp.Arch") 
        res=res+" * "+act("quit cp.Vendor") 
        res=res+" * "+act("quit cp.Model") 
        void=act("kill cp")
    if (demo==5) :
        void=cmd("Your Global","^dc.MultiD")
        gdemo(void)
        res="**** done ***"
    print("\t",res)
    continue
	# done
print("\nThank you for trying the demo\n")
iris.close()
conn.close()
