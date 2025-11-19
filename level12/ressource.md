We have a script level12.pl that listens on port 4646. It takes two parameters x and y via the function n(t(param("x"), param("y"))).
The parameter x undergoes two transformations: conversion to uppercase and removal of spaces. Next, 
it is used in an egrep command with backticks that searches for the pattern in /tmp/xd.
The vulnerability lies in the shell's interpretation of backticks. We exploit this by creating an uppercase GETFLAG script in /tmp,
and injecting it via wildcards to bypass case restrictions.
Although egrep fails (file /tmp/xd does not exist), our command in backticks executes before this failure.
  
Result will be broadcasted to all terminals using wall

COMMAND USED:

echo 'getflag | wall' > /tmp/GETFLAG
chmod +x /tmp/GETFLAG
curl 'http://127.0.0.1:4646/?x=`/*/GETFLAG`'




  
