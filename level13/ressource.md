In this reverse engineering challenge, the level13 binary implements a security 
  mechanism that verifies the user's UID before revealing the access token.
The program expects to be executed by a specific user with UID 4242,
  denying access to all other users. To bypass this protection,
I employed dynamic analysis using GDB by setting a breakpoint on the getuid function call.
After allowing the function to complete execution using the 'finish' command,
I intercepted and modified the return value stored in the EAX register to match the expected UID 4242.


tools i used :
"gdb ./level13"
"b getuid"
  "run"
 "finish"
 "set $eax = 4242"
 "continue"
