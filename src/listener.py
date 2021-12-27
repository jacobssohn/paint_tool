import struct
import time
import subprocess
import sys
import os

class Listener():
    '''
    This class is supposed to be running in the background and listen whether the keyboard shortcut
    has been triggered. If so, it should run the necessary scripts which will do the rest of the work.
    '''
    def __init__(self):
        #subprocess.run(['sudo', 'python3', '-S Pn4n4m4p4nny', *sys.argv])
        start = time.time()
        with open('/dev/input/event4', 'rb') as stream:
            print(time.time())
            while True and time.time() - start < 10:
                #print(time.time())
                data = stream.read(24)
                print(struct.unpack('4IHHI', data))
                print()
                #FORMAL = (Time Stamp_INT, 0, Time Stamp_DEC, 0,
                ######   type , code ( key pressed ) , value (press/release) )
            stream.close()
Listener()