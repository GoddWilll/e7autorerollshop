import pyautogui
import time
import os

"""class Script():
    def __init__(self):
        self.name = "Script"
        self.counter = 0
        
    def update(self):
        self.counter += 1"""
    

def main():
    
     # initialized refresh counter variable
    refreshCounter = 0
    
    while(True):
        
        # initialized pyautogui
        pyautogui.FAILSAFE = True

        # geting the position for the bm
        get_bm_pos()
        
        # waiting 
        time.sleep(1)
        
        # getting the position + refreshing
        refresh_click()
        
        # udpdating the refresh counter
        refreshCounter +=1
        
        # waiting
        time.sleep(1)
        
        # getting the position + refreshing    
        confirm_click()
        
        # print how many times we refreshed the shop
        print(f"We refreshed {refreshCounter} times.")
    
    
def initialize():
    print("Starting the count", end="")
    for i in range(0, 3):
        print(".", end="")
        time.sleep(1)
    print("Go")
    
    """Function made to test if the element exists on the page
    """
def exists(element):
    script_dir = os.path.dirname(__file__)
    item_path = os.path.join(
        script_dir,
        'imgs',
        element
    )
    researched_elem = pyautogui.locateOnScreen(item_path, confidence=0.9)
    if researched_elem == None:
        return False
    else : 
        return researched_elem

def price_check():
    location = exists('price.png')
    if location !=False:
        script_dir = os.path.dirname(__file__)
        item_path = os.path.join(
            script_dir,
            'imgs',
            'price.png'
        )
        x,y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
        pyautogui.click(x, y+50)
    
def confirm_click():
    location = exists('confirm_button.png')
    if location != False:
        script_dir = os.path.dirname(__file__)
        item_path = os.path.join(
            script_dir,
            'imgs',
            'confirm_button.png'
        )
        x,y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
        pyautogui.click(x,y)
        

def get_bm_pos():
    location = exists('part_bm.png')
    if location != False:
        time.sleep(0.5)
        price_check()
    else :
        time.sleep(1)
        move_page()
        if exists('part_bm.png') != False:
            price_check()
            
            """"script_dir = os.path.dirname(__file__)
            item_path = os.path.join(
            script_dir,
            'imgs',
            'part_bm.png'
            )
            x, y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
            pyautogui.moveTo(x,y)
            time.sleep(0.5)
            pyautogui.click(x+300,y)"""
        

def refresh_click():
    location = exists('refresh.png')
    if location != False:
        script_dir = os.path.dirname(__file__)
        item_path = os.path.join(
            script_dir,
            'imgs',
            'refresh.png'
        )
        x, y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
        pyautogui.click(x, y)
    
    
def py_screenshot():
    im = pyautogui.screenshot('Screenshot_test.png')

def move_page():
    location = exists('pos_calibration.png')
    if location != False:
        script_dir = os.path.dirname(__file__)
        item_path = os.path.join(
            script_dir,
            'imgs',
            'pos_calibration.png'
        )    
        x, y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
        pyautogui.moveTo(x,y+100)
        pyautogui.dragTo(x, y-150,1, pyautogui.easeInQuad, button='left')

        
        
if __name__ == '__main__':
    
    # initialize the app
    initialize()
    
    # execute the script
    main()