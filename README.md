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

</pre></p>

[Article in DC](https://community.intersystems.com/post/remote-global-listing-using-nativeapi-objectscript-2)
  
        
