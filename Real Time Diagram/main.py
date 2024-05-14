import subprocess

proc = subprocess.Popen(['C:/Users/Ehsan/Desktop/EMDTools/sensor-cli.exe','en acc'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(proc)

import os

os.startfile("C:/Users/Ehsan/Desktop/EMDTools/sensor-cli.exe")


import subprocess

# subprocess.Popen(['C:\Users\Ehsan\Desktop\EMDTools\sensor-cli.exe port \\.\COM7', 'en acc'], shell=True, capture_output=True, universal_newlines=True)


proc = subprocess.Popen(['cd C:\TDK-InvenSense\"SmartMotion Platform 4.2.15"\EMDTools','sensor-cli.exe port \\.\COM7','en acc'], shell=True, stdout=subprocess.PIPE)
proc.communicate()
proc.stdout.readlines()
out, err = proc.communicate(input='en acc')
out.decode(), err.decode()


result = subprocess.run(['C:\TDK-InvenSense\SmartMotion Platform 4.2.15\EMDTools\sensor-cli.exe port \\.\COM7', 'en acc'], shell=True, stdout=subprocess.PIPE)
# result = subprocess.run(['en acc'], shell=True, stdout=subprocess.PIPE)
result.stdout

import subprocess

proc = subprocess.Popen(['C:\TDK-InvenSense\"SmartMotion Platform 4.2.15"\EMDTools\sensor-cli.exe port \\.\COM7'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
proc = proc.Popen(['en acc'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if not line:
        break
    else: 
        # Do whathever you need to do with the last line written on 
        # stdout by your_process
        print("doing some stuff with...", line)
        print("done for this line!")


import subprocess

p = subprocess.Popen(['C:\TDK-InvenSense\"SmartMotion Platform 4.2.15"\EMDTools\sensor-cli.exe port \\.\COM7'],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE)
while True:
    out, _ = p.communicate(input().encode())
    print(out.decode())


import os 

t = os.system('cmd')


import commands
status, output = commands.getstatusoutput("cat /etc/services")