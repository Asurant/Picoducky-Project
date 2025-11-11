import time
import keyboard
import mouse

def type_window_update():
    keyboard.write("control update", delay=0.05)
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('win + up arrow')
    time.sleep(0.7)

def open_run_dialog():
    keyboard.press_and_release('win+r')
    time.sleep(0.7)

def move_to_update_button():
    mouse.move(1375, 160, absolute=True)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_auto_update_switch():
    mouse.move(1375, 280, absolute=True)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def open_advanced():
    mouse.move(1375, 500, absolute=True)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_microsoft_updates():
    mouse.move(1375, 145, absolute=True)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def free_advertising():
    keyboard.write("https://www.youtube.com/watch?v=iKnqjtLeWmg", delay=0.05)
    keyboard.press_and_release('enter')
    time.sleep(1)

def move_privacy():
    mouse.move(25, 560, absolute=True)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_speech_privacy():
    mouse.move(500, 500, absolute=True)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_speech_recognition():
    mouse.move(430, 340, absolute=True)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_inking():
    mouse.move(1000, 570)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_custom_inking():
    mouse.move(1380, 210)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_recs():
    mouse.move(500, 425)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_ads():
    mouse.move(1350, 140)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_disallow_language():
    mouse.move(1375, 225)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_disallow_start():
    mouse.move(1375, 290)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_disallow_recs():
    mouse.move(1375, 440)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def move_to_ad_ID():
    mouse.move(1375, 510)
    time.sleep(0.5)
    mouse.click(button='left')
    time.sleep(0.7)

def type_end():
    keyboard.write("notepad")
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('win + up arrow')
    time.sleep(0.7)
    keyboard.write("Script Completed :D \nThanks for using it", delay=0.05)

if __name__ == "__main__":
    input("Switch to a text editor, then press ENTER to start...")
    open_run_dialog()
    free_advertising()
    open_run_dialog()
    type_window_update()
    move_to_update_button()
    move_to_auto_update_switch()
    open_advanced()
    move_to_microsoft_updates()
    move_privacy()
    move_speech_privacy()
    move_to_speech_recognition()
    move_privacy()
    move_to_inking()
    move_to_custom_inking()
    move_privacy()
    move_to_recs()
    move_to_ads()
    move_to_disallow_language()
    move_to_disallow_start()
    move_to_disallow_recs()
    move_to_ad_ID()
    open_run_dialog()
    type_end()