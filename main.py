import pyautogui
import time
import os
import keyboard

exitProgram = False 

def quit():
    global exitProgram
    exitProgram = True


    
def main():
    
    # creating the hotkey
    keyboard.add_hotkey('q', lambda: quit())
    
    # initialized refresh counter variable
    refreshCounter = 0
    itemsCounter = 0
    
    # calibrating the autoclicker
    calibration()
    
    # loop
    while not exitProgram:
        
        # initialized pyautogui
        pyautogui.FAILSAFE = True
        
        pyautogui.screenshot("VERIFY.png")

        # geting the position for the bm
        itemsCounter += price_check(0)
        
        # getting the position + refreshing
        refreshCounter = refresh_click(refreshCounter)        

        # getting the position + refreshing    
        confirm_click()
        
        # print how many times we refreshed the shop
        # print(f"We refreshed {refreshCounter} times.")
        
    print(f"""
        ----------------------------------------
                    STATISTICS
        ----------------------------------------
        Number or refreshes : {refreshCounter}
        ----------------------------------------
        Number of bought items : {itemsCounter}
          """)
    
    
def initialize():
    print("""
        AUTOMATIC REROLL SHOP v0.1 by Godwill#9999
        ----------------------------------------
        Use the hotkey 'a' to quit the loop. 
        ----------------------------------------
          """)
    print("Starting the script ", end="")
    for i in range(0, 3):
        print(". ", end="")
        time.sleep(1)
    print("Go")
    
    
def calibration():
    location = exists('pos_calibration.png')
    if location != False:
        script_dir = os.path.dirname(__file__)
        item_path = os.path.join(
            script_dir,
            'imgs',
            'pos_calibration.png'
        )
        x,y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
        pyautogui.click(x,y)
 
 
def exists(element):
    script_dir = os.path.dirname(__file__)
    item_path = os.path.join(
        script_dir,
        'imgs',
        element
    )
    researched_elem = pyautogui.locateOnScreen(item_path, confidence=0.99)
    if researched_elem == None:
        #print(element + " not found!")
        return False
    else : 
        #print("I found " + element)
        return researched_elem


def bought():
    location = exists('bought.png')
    if location !=False:
        return True
    else : 
        return False
        
        
def buy_item():
    location = exists('buy_cov.png')
    location2 = exists('buy_myst.png')
    
    if location2 != False:
        script_dir = os.path.dirname(__file__)
        item_path = os.path.join(
            script_dir,
            'imgs',
            'buy_myst.png'
        )
        x,y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
        pyautogui.click(x, y)
        price_check(0)
        
    if location !=False:
        script_dir = os.path.dirname(__file__)
        item_path = os.path.join(
            script_dir,
            'imgs',
            'buy_cov.png'
        )
        x,y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
        pyautogui.click(x, y)
        price_check(0)
        

def price_check(num):
    time.sleep(0.5)
    location = exists('5bm.png')
    location2 = exists('50bm.png')
    if location == False and location2 == False:
        if num == 0:
            move_page()
            time.sleep(0.5)
            price_check(1)
            return 0
        else :
            return 0
    else:
        script_dir = os.path.dirname(__file__)
        if location != False:  
            item_path = os.path.join(
                script_dir,
                'imgs',
                '5bm.png'
            )
            x,y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
            pyautogui.click(x + 500, y+40)
            buy_item()
            if bought() == False:
                buy_item()
                return 1
            else : 
                return 1
                
        if location2 != False:
            script_dir = os.path.dirname(__file__)
            item_path = os.path.join(
                script_dir,
                'imgs',
                '50bm.png'
            )
            x,y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
            pyautogui.click(x + 500, y+40)
            buy_item()
            if bought() == False:
                buy_item()
                return 1
            else :
                return 1
    
        
       
                
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
        

def refresh_click(rc):
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
        time.sleep(1)
        return rc+1
    
    
def move_page():
    pyautogui.scroll(-10)
    time.sleep(1)

        
if __name__ == '__main__':
    
    # initialize the app
    initialize()
    
    # execute the script
    main()