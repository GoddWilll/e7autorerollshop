import pyautogui
import time
import os


def main():

    # initialized refresh counter variable
    refreshCounter=0
    
    # initialized pyautogui
    pyautogui.FAILSAFE = True

    # Countdown timer
    print("Starting the count", end="")
    for i in range(0, 3):
        print(".", end="")
        time.sleep(1)
    print("Go")

    # geting the position for the bm
    get_bm_pos()
    
    # waiting 
    time.sleep(1)
    
    # getting the position + refreshing
    get_refresh_pos()
    
    # waiting
    time.sleep(1)
    
    # getting the position + refreshing    
    get_confirm_pos(refreshCounter)
    
    # print how many times we refreshed the shop
    print(f"We refreshed {refreshCounter} times.")
    
    # done
    print("Done")
    
    

    
    """
    Used to get the position of the confirm button, and to hit it
    """

def get_confirm_pos(rc):
    script_dir = os.path.dirname(__file__)
    item_path = os.path.join(
        script_dir,
        'imgs',
        'confirm_button.png'
    )
    image_pos = pyautogui.locateOnScreen(item_path, confidence=0.9)
    print("Here are the coordinates for the confirm button:")
    print(image_pos)
    x, y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
    pyautogui.click(x,y)
    rc+=1

def get_bm_pos():
    script_dir = os.path.dirname(__file__)
    item_path = os.path.join(
        script_dir,
        'imgs',
        'part_bm.png'
    )
    image_pos = pyautogui.locateOnScreen(item_path, confidence=0.9)
    print("Here are the coordinates for the cov bookmark:")
    print(image_pos)
    if image_pos == None:
        time.sleep(1)
        movePage()
        image_pos = pyautogui.locateOnScreen(item_path, confidence=0.9)
        print("Here are the coordinates for the cov bookmark:")
        print(image_pos)

def get_refresh_pos():
    script_dir = os.path.dirname(__file__)
    item_path = os.path.join(
        script_dir,
        'imgs',
        'refresh.png'
    )
    image_pos = pyautogui.locateOnScreen(item_path, confidence=0.9)
    x, y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
    pyautogui.click(x,y)
    print("Here are the coordinates for the refresh button:")
    print(image_pos)

def py_screenshot():
    im = pyautogui.screenshot('Screenshot_test.png')

def movePage():
    script_dir = os.path.dirname(__file__)
    item_path = os.path.join(
        script_dir,
        'imgs',
        'pos_calibration.png'
    )    
    image_pos = pyautogui.locateOnScreen(item_path, confidence=0.9)
    x, y = pyautogui.locateCenterOnScreen(item_path, confidence=0.9)
    pyautogui.dragTo(x, y-150,1, pyautogui.easeInQuad, button='left')
    
if __name__ == '__main__':
    while(True):
        main()
