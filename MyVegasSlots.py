from ppadb.client import Client
from PIL import Image
import numpy
import time

adb = Client()
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

def screencap(x, y):
    image = device.screencap()
    with open('/home/pi/test.png', 'wb') as f:
        f.write(image)
    image = Image.open('test.png')
    image = numpy.array(image, dtype=numpy.uint8)

    pixel = image[y, x]
    pixel_red = pixel[2]
    # print(pixel_red)
    return pixel_red

def open_app():
    # Wake up the device
    device.shell('input keyevent 26')
    print('Waking up the device...')
    time.sleep(2)  # Wait for the device to wake up
    
    # Swipe to unlock
    device.shell('input swipe 350 1220 350 500')
    print('Swiping to unlock...')
    time.sleep(2)  # Wait for the swipe gesture to complete
    
    device.shell('input keyevent KEYCODE_HOME')
    print('Home Button')
    
    device.shell('input tap 81 648')
    print('Open MyVegas App...')
    time.sleep(135)
    
def device_sleep():
    device.shell('input swipe 1275 398 630 398') # Swipe to reveal Home Buttons
    device.shell('input tap 1259 163') # Click Windows Button
    device.shell('input tap 850 115') # Clear All Button
    time.sleep(2)
    device.shell('input keyevent 26') # Lock the device's screen
    time.sleep(5)

def skip_ads():
    print('Checking for Ads')
    while True:       
        pixel_red = screencap(1235, 40) # Check first potential ad position
        if 212 < pixel_red < 216:
            print(f'Exit Type 1: {pixel_red}')
            device.shell('input tap 1236 39')
            time.sleep(30)
            continue
        
        pixel_red = screencap(1038, 165) # Check second potential ad position
        if 212 < pixel_red < 216:
            print(f'Exit Type 2: {pixel_red}')
            device.shell('input tap 1038 165')
            time.sleep(30)
            continue
        
        pixel_red = screencap(1175, 40) # Check third potential ad position
        if 226 < pixel_red < 230:
            print(f'Exit Type 3: {pixel_red}')
            device.shell('input tap 1173 43')
            time.sleep(30)
            continue
        
        pixel_red = screencap(1175, 40) # Check third potential ad position
        if 204 < pixel_red < 208:
            print(f'Exit Type 4: {pixel_red}')
            device.shell('input tap 1173 43')
            time.sleep(30)
            continue
        
        break # No ads detected, exit loop
    
def restart_app():
    device_sleep()
    open_app()
    time.sleep(135)
    skip_ads()
        
def purple_coins():
    print('Checking for Purple Coins...')            
    pixel_red = screencap(120, 693) # Screenshot checks for purple coins
    if 253 < pixel_red < 257:
        print('Collecting Purple Coins...')
        device.shell('input tap 68 644')
        time.sleep(10)
        
def game_start():
    print('Checking for Server Error...')
    pixel_red = screencap(725, 520)
    if 22 < pixel_red < 26:
        print('Server Error...')
        device.shell('input tap 725 520')
        time.sleep(7)
    
    print('Checking for Connect Accounts Request...')
    pixel_red = screencap(932, 150)
    if 217 < pixel_red < 221:
        print('"Connect Now" Closed...')
        device.shell('input tap 932 150')
        time.sleep(7)
    
    print('Checking for daily bonus...')
    pixel_red = screencap(938, 510)
    if 34 < pixel_red < 38:
        print('Collecting Daily Bonus...')
        device.shell('input tap 642 463')
        time.sleep(10)
        device.shell('input tap 641 644')
        time.sleep(20)
        device.shell('input tap 641 644')
        time.sleep(15)

def system_fail():
    pixel_red = screencap(938, 510)
    if 34 < pixel_red < 38:
        device_sleep()
        open_app()
        pass

############################# ADVERTS #############################
# def watch_ads():
#     print('Checking if there are ads to watch...')
#     pixel_red = screencap(15, 699) # Screenshot to capture pixel colour of 'Watch Ads' icon
#     if 253 < pixel_red < 257: # Run code below if pixel is between 253 and 257
#         advert = True
#         print('Watching Ad')
#         while advert:
#             device.shell('input tap 72 651') # Taps the watch ad button
#             time.sleep(60) # Watches ad for 60 seconds
            
#             pixel_red = screencap(0, 0)
#             if 253 < pixel_red < 257:
#                 print('Tapping top right X...')
#                 device.shell('input tap 1222 58')
#                 time.sleep(20)
            
#             pixel_red = screencap(1222, 58)
#             if 253 < pixel_red < 257:
#                 print('Tapping top right X...')
#                 device.shell('input tap 1222 58')
#                 time.sleep(20)
#                 print('Tapping top right X...')
#                 device.shell('input tap 1222 58')
#                 time.sleep(10)
#                 print('Collecting coins...')
#                 device.shell('input tap 640 632')
#                 time.sleep(5)
                
#             pixel_red = screencap(48, 49)
#             if 36 < pixel_red < 40:
#                 print('Tapping top left X...')
#                 device.shell('input tap 48 49')
#                 time.sleep(20)
#                 print('Tapping Rewards granted X...')
#                 device.shell('input tap 1136 49')
#                 time.sleep(8)
#                 print('Collecting coins...')
#                 device.shell('input tap 640 632')
#                 time.sleep(5)
            
#             pixel_red = screencap(1064, 89)
#             if 68 < pixel_red < 72:
#                 print('Tapping top right X...')
#                 device.shell('input tap 1064 89')
#                 time.sleep(8)
#                 print('Collecting coins...')
#                 device.shell('input tap 640 632')
#                 time.sleep(5)
            
#             pixel_red = screencap(1227, 31)
#             if 202 < pixel_red < 206:
#                 print('Skipping ad...')
#                 device.shell('input tap 1241 33')
#                 time.sleep(5)
#                 device.shell('input tap 1240 70')
#                 time.sleep(5)
#                 device.shell('input tap 1241 33')
#                 time.sleep(15)
#                 print('Collect...')
#                 device.shell('input tap 640 632')
            
#             pixel_red = screencap(1141, 43)
#             if 122 < pixel_red < 126:
#                 print('Tapping X...')
#                 device.shell('input tap 1141 43')
#                 time.sleep(15)
#                 print('Collecting coins...')
#                 device.shell('input tap 640 632')
#             else:
#                 break
#     else:
#         print('No more ads to watch...')
#         return

while True:
    open_app()
    # system_fail()
    game_start()
    skip_ads() # Initial Adverts
        
    tap_num = 1
    while True:
        # Check for 'Connection Timeout'
        print('Checking for Connection Issue...')
        pixel_red = screencap(956, 248) # Screenshot checks for green tick on yellow coins
        if 212 < pixel_red < 216:
            print('Closing Connection Timeout...')
            device.shell('input tap 956 248')
            time.sleep(15)
            
        purple_coins()
        
        print('Checking for Green Tick...')
        pixel_red = screencap(396, 53) # Screenshot checks for green tick on yellow coins
        if 12 < pixel_red < 16:
            print('Green tick: YES...') 
            
            purple_coins()
            
            ############################# COINS ADVERTS #############################
            # watch_ads()
            
            print('Everything collected. Nothing left to do...')
            device_sleep()
            # Sleep for X hours
            print('Sleeping...')
            time.sleep(2 * 60 * 60)  # Sleep for 2 hours before running the code again
            # When code resumes, it will run from the beginning
            break
        
        else:
            # Keep time Running
            device.shell('input tap 136 46')
            print(f'Time Bonus Tap {[tap_num]}...')
            tap_num += 1
            time.sleep(5)
                
