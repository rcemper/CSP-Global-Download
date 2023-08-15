This is the Python client for IRIS NativeAPI Command Extension   
It demonstrates using the extension without ObjectScript   

For easy testing an IRIS instance with a demo Global and    
a pre-installed NativeAPI Command Line Extension is added. 
### Prerequisites    
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.    
### Installation   
Clone/git pull the repo into any local directory  

````    
git https://github.com/rcemper/native-api-command-line-client    
````    
   
Run the IRIS container with your project:   

````
docker-compose up -d --build    
````
### How to Test it    
<p><pre>docker-compose exec iris python3 src/rcc.py
  
\>\>\> serverIP [127.0.0.1]:
\>\>\> serverPORT [1972]:
\>\>\> namespace [USER]:
\>\>\> username [_SYSTEM]:
\>\>\> password [SYS]:
Connected to Instance IRIS on Server 1C09927CAE60    

Select Demo to exercise
 0 = free ObjectScript
 1 = $ZV from Server
 2 = Actual Time in Server
 3 = TimeZone Offset of Server
 4 = Server Architecture*Vendor*Model
 5 = List Global in ZWRITE style
 \* = Terminate demo
\>\>\> take a choice [1]:
         IRIS for UNIX (Ubuntu Server LTS for x86-64 Containers) 2023.2 (Build 227U) Mon Jul 31 2023 18:04:28 EDT
\>\>\> take a choice [1]: 2
         2023-08-15 07:42:16
\>\>\> take a choice [1]: 3
         0
\>\>\> take a choice [1]: 4
         x86_64 * Intel * Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz
\>\>\> take a choice [1]: 0
\>\>\> Your ObjectScript [ quit "?"]: quit $ZTS
         66701,27813.678790226
\>\>\> take a choice [1]: 0
\>\>\> Your ObjectScript [ quit "?"]: quit 17/4
         4.250000000000000000
\>\>\> take a choice [1]: 0
\>\>\> Your ObjectScript [ quit "?"]: quit 17/0
         <DIVIDE\> 18 x^%ZX
\>\>\> take a choice [1]: 5
\>\>\> Your Global [^dc.MultiD]:
         ^dc.MultiD  =  5
         ^dc.MultiD(1)  =  $lb("Braam,Ted Q.",51353)
         ^dc.MultiD(1,"mJSON")  =  "{}"
         ^dc.MultiD(2)  =  $lb("Klingman,Uma C.",62459)
         ^dc.MultiD(2,2,"Multi","a")  =  1
         ^dc.MultiD(2,2,"Multi","rob",1)  =  "rcc"
         ^dc.MultiD(2,2,"Multi","rob",2)  =  2222
         ^dc.MultiD(2,"Multi","a")  =  1
         ^dc.MultiD(2,"Multi","rob",1)  =  "rcc"
         ^dc.MultiD(2,"Multi","rob",2)  =  2222
         ^dc.MultiD(2,"mJSON")  =  "{""A"":""ahahah"",""Rob"":""VIP"",""Rob2"":1111,""Rob3"":true}"
         ^dc.MultiD(3)  =  $lb("Goldman,Kenny H.",45831)
         ^dc.MultiD(3,"mJSON")  =  "{}"
         ^dc.MultiD(4)  =  $lb("","")
         ^dc.MultiD(4,"mJSON")  =  "{""rcc"":122}"
         ^dc.MultiD(5)  =  $lb("","")
         ^dc.MultiD(5,"mJSON")  =  "{}"
         **** done ***
\>\>\> take a choice [1]: *

Thank you for trying the demo
</pre></p>

[Article in DC](https://community.intersystems.com/post/using-nativeapi-extension-python)

[Video](https://youtu.be/-rtJ0lNHuvk)

