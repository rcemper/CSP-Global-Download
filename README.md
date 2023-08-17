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

</pre></p>

[Article in DC](https://community.intersystems.com/post/download-globals-xml-using-csp)
