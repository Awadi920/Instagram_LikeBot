import pyautogui as pt
import time
import schedule

class GuiCommands:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def navigate_to_heart(self, speed):
            position = pt.locateOnScreen("capture.png", confidence=.8) # Locate the heart icon on the screen by searching for the capture.png image, which represents the save icon
            self.x = position[0] - 550  # Update the x-coordinate based on each computer's display settings
            self.y = position[1] + 10  # Update the y-coordinate based on each computer's display settings
            pt.moveTo(self.x, self.y, duration=speed) # Move the cursor to the updated position
            print("Navigating to heart!")
            time.sleep(.3) # Pause for 3 seconds
             

def like_posts():
    commands = GuiCommands(0, 0) # Create an instance of the GuiCommands class with initial coordinates
    for i in range(1):  
        try:
            commands.navigate_to_heart(-1)  # Call the navigate_to_heart method with a speed of -1
            if pt.pixelMatchesColor(pt.position().x, pt.position().y, (255, 48, 64), tolerance=10): # Check if the pixel at the current position matches a specific color
                pt.scroll(-920)  # Scroll the screen up by -920 pixels
                time.sleep(.3)  
            else:
                pt.click()  # Click at the current position
                time.sleep(.3)  
                pt.scroll(-920)  # Scroll the screen up by -920 pixels
        except Exception as e:
            print(e)  # Print the exception message
            pt.scroll(-600)  # Scroll the screen up by -600 pixels
            time.sleep(.3)  


# Schedule task to run every 5 seconds
schedule.every(5).seconds.do(like_posts)


# Run the scheduled tasks
while True:
    schedule.run_pending()  
    time.sleep(1)  