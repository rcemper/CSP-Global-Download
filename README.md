This is the Python client for IRIS NativeAPI Command extension   
It demonstrates using the extension without ObjectScript   

Vou have to prepare   
- your credentials for server access    
- your level of error handling
   
First,    
you make a connection to the target SuperServer Port    
````   
do ##class(nacl.Client).Connect("192.168.0.99",41773)   
````    
Then you launch your command for remote execution      
<p><pre>USER>write ##class(nacl.Client).Do(" quit $now() ")
66698,68259.396554358
USER>write ##class(nacl.Client).Do(" quit $ZV ")
IRIS for UNIX (Ubuntu Server LTS for x86-64 Containers) 2023.2 (Build 227U) Mon Jul 31 2023 18:04:28 EDT   
</pre></p>

### Prerequisites    
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.    

On your target server, you need to install    
https://github.com/rcemper/native-api-command-line-extension    

### Installation   
Clone/git pull the repo into any local directory  

````    
git https://github.com/rcemper/native-api-command-line-client    
````    
   
Run the IRIS container with your project:   

````
docker-compose up -d --build    
````
## How to Test it    

<p><pre>
docker-compose exec iris bash python3 src/rcc.py  

>>> serverIP [127.0.0.1]:
>>> serverPORT [1972]:
>>> namespace [USER]:
>>> username [_SYSTEM]:
>>> password [SYS]:

Connected to Instance IRIS on Server 1C09927CAE60

Select Demo to exercise
 0 = free ObjectScript
 1 = $ZV from Server
 2 = Actual Time in Server
 3 = TimeZone Offset of Server
 4 = Server Architecture*Vendor*Model
 5 = List Global in ZWRITE style
 * = Terminate demo
>>> take a choice [1]:
         IRIS for UNIX (Ubuntu Server LTS for x86-64 Containers) 2023.2 (Build 227U) Mon Jul 31 2023 18:04:28 EDT
>>> take a choice [1]: 5
>>> Your Global [^dc.MultiD]:
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
>>> take a choice [1]:

</pre></p>

[Article in DC](https://community.intersystems.com/post/remote-global-listing-using-nativeapi-objectscript-2)
  
        
