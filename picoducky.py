import time
import keyboard
import mouse

def type_window_update():
    keyboard.write("control update", delay=0.05)
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('win + up arrow')
    time.sleep(0.5)

def open_run_dialog():
    keyboard.press_and_release('win+r')
    time.sleep(0.5)

def move_to_update_button():
    mouse.move(1375, 160, absolute=True)
    time.sleep(0.2)
    mouse.click(button='left')
    time.sleep(0.5)

def move_to_auto_update_switch():
    mouse.move(1375, 280, absolute=True)
    time.sleep(0.2)
    mouse.click(button='left')
    time.sleep(0.5)

def open_advanced():
    mouse.move(1375, 500, absolute=True)
    time.sleep(0.2)
    mouse.click(button='left')
    time.sleep(0.5)

def move_to_microsoft_updates():
    mouse.move(1375, 145, absolute=True)
    time.sleep(0.2)
    mouse.click(button='left')
    time.sleep(0.5)

def free_advertising():
    keyboard.write("https://www.youtube.com/watch?v=iKnqjtLeWmg", delay=0.05)
    keyboard.press_and_release('enter')
    time.sleep(1)

def move_privacy():
    mouse.move(25, 560, absolute=True)
    time.sleep(0.2)
    mouse.click(button='left')
    time.sleep(0.5)

def move_speech_privacy():
    mouse.move(500, 500, absolute=True)
    time.sleep(0.2)
    mouse.click(button='left')
    time.sleep(0.5)

def move_to_speech_recognition():
    mouse.move(430, 340, absolute=True)


def type_end():
    keyboard.write("notepad")
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('win + up arrow')
    time.sleep(0.5)
    keyboard.write("Script Completed :D \nThanks for using it", delay=0.05)

if __name__ == "__main__":
    input("Switch to a text editor, then press ENTER to start...")
    #move_speech_privacy()
    #move_to_speech_recognition()
    open_run_dialog()
    free_advertising()
    #open_run_dialog()
    #type_window_update()
    #move_to_update_button()
    #move_to_auto_update_switch()
    #open_advanced()
    #move_to_microsoft_updates()
    #open_run_dialog()
    #type_end()