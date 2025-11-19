in this level we have token of flag09 in token file but it is already encoded , 
so to get the token we shoould decoded using script, but to run the script , i used scp to transfer 
the file from my localhost to the vm ;

command used 

"scp -P 4242 script.py level09@ipaddrOfthemachine:/tmp" (from the localhost)
"/tmp/script.py"

after executing the command i got as flag : "f3iji1ju5yuevaus41q1afiuq"

"su flag09"

"getflag"


    
