This level cannot be solved directly through reverse engineering inside the VM.
I downloaded the getflag binary to my local machine using:
"rsync -avz -e "ssh -p 4242" level14@10.12.179.172:/bin/getflag ~/Downloads/"

I decompiled the binary into C code (ft_dest.c).

I found the hexadecimal UID for level14, which is 0xBC6.

I searched for this UID in the decompiled function.

I located the encrypted flag for this user.

I passed the encrypted string into the f_des() function.

The function returned the decrypted flag:
"7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ"
I then used this result with getflag to obtain the final flag.
