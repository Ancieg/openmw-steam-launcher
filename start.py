#!/usr/bin/env python                                                           
import os, sys
from ctypes import CDLL

# Steam Application Identifier for Morrowind                                    
os.environ['SteamAppId'] = '22320'

# Steam Overlay                                                                 
# It is made to make Steam track played time                                    
home_dir = os.getenv('HOME')
ubuntu12_64_dir = os.popen('find $HOME -name ubuntu12_64').read()
overlay_path = ubuntu12_64_dir + '/gameoverlayrenderer.so'
os.environ['LD_PRELOAD'] = home_dir + overlay_path

# Load special library for Morrowind                                            
steam_api = CDLL('./libsteam_api.so')
try:
    steam_api.SteamAPI_Init()
except:
    print('Failed to initialize Steam API')
    sys.exit(1)

# When all of preparations are ready, start openmw                              
os.system('openmw')
