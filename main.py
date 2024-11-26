import time                         # Delays
import ctypes                       # Windows API Input
from pynput import keyboard         # Keyboard Input

# Mouse event constant for Windows API
MOUSEEVENTF_LEFTDOWN = 0x0002       # Left Mouse Click
MOUSEEVENTF_LEFTUP = 0x0004         # Left Mouse Release

class AutoClicker:
    def __init__(self):             # Initialization
        self.running = False                                                    # Declare running(bool) status variable
        self.listener = keyboard.Listener(on_release=self.on_release)           # Declare keyboard listener (will run on_release function when a key is released)
        self.listener.start()                                                   # Start listener in separate thread to not block the clicking function
        self.delay = 0.001                                                      # Delay default var        

    def on_release(self, key):      # Function when released
        if key == keyboard.Key.esc:                                             # Detecting what key that is released
            print("Thank you for using this application. Exiting...")
            self.running = False                                                # Changing running status to false
            return False                                                        # Stops listener

    def start_clicking(self):       # Main function?
        while True:                                                             # Loop Forever
            if not self.running:                                                # Detecting running status
                break                                                           # Stops loop when running status is false
            self.click()                                                        # Run click function
            time.sleep(self.delay)                                              # Delay before running another clicking function

    def click(self):                # Clicking function
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)      # Simulate left click (event, X, Y, data, info)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)        # Simulate left release (event, X, Y, data, info)


print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print('CLICK!')
auto_clicker = AutoClicker()
auto_clicker.start_clicking()