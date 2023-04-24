# About Anti-Lock 5000

![Anti-Lock 5000 in action](https://github.com/xlaech/Anti-Lock-5000/blob/master/screenshot.png)

This program ensures, that Windows computers stay awake even, when the battery configuration is set otherwise and can not be changed.
The program works in a 2 step process:
- If the system has been idle for more than 60 seconds, the mouse is moved to the top left corner and one click is performed
- If the system has been idle for less than 60 seconds, the program waites for 60-idletime seconds

# How to install

The program is written, such that it only uses out-of-the-box python libraries.
You only need any (even portable) installation of Python.
The default installation can be performed without administration rights if you run the installer for the local user (%appdata%).

After this just copy the "Anti-Lock 5000.py" file to any location.

# How to run

Open the cmd or Powershell in the directory you copied the file (shift+rightclick in any empty area of the explorer -> Open Powershell Window) and type:
```bash
python '.\Anti-Lock 5000.py'
```
# Mac OS

You got the same issue on mac os? Here is someone who did the same thing - just way more advanced:
https://github.com/bhaller/Jiggler
