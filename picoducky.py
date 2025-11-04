import time
import keyboard
import mouse

def type_window_update():
    keyboard.write("control update", delay=0.05)
    keyboard.press_and_release('enter')
    time.sleep(5)

def open_run_dialog():
    keyboard.press_and_release('win+r')
    time.sleep(0.5)

def move_to_button():
    mouse.move(1350, 160, absolute=True)
    time.sleep(0.2)
    mouse.click(button='left')
    time.sleep(0.2)

if __name__ == "__main__":
    input("Switch to a text editor, then press ENTER to start...")
    open_run_dialog()
    type_window_update()
    move_to_button()
    print("Keyboard demo complete.")