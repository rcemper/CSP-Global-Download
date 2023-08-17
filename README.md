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

in your browser call  (http://192.168.0.9:42773/csp/user/dc.Gdown.cls?GBL=dc.MultiD)    
and you get the file select menue for the download    
<img width="50%" src="https://github.com/rcemper/CSP-Global-Download/assets/31236645/1b9e68f8-31af-4bd4-a5ab-d31fd8cdaa35">



[Article in DC](https://community.intersystems.com/post/download-globals-xml-using-csp)
