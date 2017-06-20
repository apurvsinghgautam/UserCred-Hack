import pyperclip
import time

list = []  # List to store the clipboard content

while True: 
    
    if pyperclip.paste() != 'None':    # If the clipboard content is not empty 
        value = pyperclip.paste()      # value will take the clipboard content
        #print pyperclip.paste()


        if value not in list:    # To ensure no duplicate characters in the list
            list.append(value)
        fp=open("clipboard.txt","w")
    	fp.write(list)
    	fp.close()

        time.sleep(3)

