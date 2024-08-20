#! /usr/bin/env python
import sqlite3
import base64
from cryptography.fernet import Fernet
from getpass import getpass
database = sqlite3.connect("edelweiss.sqlite")
sq = database.cursor()
def main():
    #f = "YOUR KEY HERE"
    sq.execute("CREATE TABLE IF NOT EXISTS edelweiss(origin, username, password)")
    #key = f.encode('utf-8')[:32].ljust(32,b'H')
    #key = base64.b64encode(key)
    #f = Fernet(key)
    #pw = f.encrypt(b"PASSWORD HERE")
    #un = f.encrypt(b"USERNAME HERE")
    #query = "INSERT INTO edelweiss (origin, username, password) VALUES (?, ?, ?)"
    #data = ('Sinclair', un, pw)
    #sq.execute(query, data)
    #database.commit()
    password = getpass("Password>>>")
    key = password.encode('utf-8')[:32].ljust(32,b'H')
    key = base64.b64encode(key)
    f = Fernet(key)
    query = "SELECT password FROM edelweiss WHERE origin = 'Sinclair'"
    EnPass = sq.execute(query)
    EnPass = EnPass.fetchone()
    if(f.decrypt(EnPass[0]) != password.encode('utf-8')):
        print("Wrong Password")
        exit()
    action = input("Action>>>")
    if(action == "reset"):
        username = input("Username>>>")
        query = "SELECT username FROM edelweiss WHERE origin = 'Sinclair'"
        query = sq.execute(query)
        query = query.fetchone()
        if(f.decrypt(query[0]) != username.encode("utf-8")):
            print("Wrong Username")
            exit()
        newPass = getpass("New Password>>>")
        j = getpass("Re-Enter Password>>>")
        while(newPass != j):
            newPass = getpass("New Password>>>")
            j = getpass("Re-Enter Password>>>")
        query = f"UPDATE edelweiss SET password = {newPass} WHERE username = {username}"
        sq.execute(query)
        database.commit()
        print("Password Reset!")
        exit()
    elif(action == "set"):
        origin = input("Origin>>>")
        username = input("Username>>>")
        username = username.encode('utf-8')
        username = f.encrypt(username)
        password = input("Password>>>")
        password = password.encode('utf-8')
        password = f.encrypt(password)
        query = "INSERT INTO edelweiss (origin, username, password) VALUES (?, ?, ?)"
        data = (origin, username, password)
        sq.execute(query, data)
        database.commit()
        print(f"Saved Login Information For {origin}")
        exit()
    elif(action == "get"):
        origin = input("Origin>>>")
        print("Origin:", origin)
        query = f"SELECT username FROM edelweiss WHERE origin = '{origin}'"
        query = sq.execute(query)
        query = query.fetchone()
        query = f.decrypt(query[0])
        query = query.decode('utf-8')
        print("Username:", query)
        query = f"SELECT password FROM edelweiss WHERE origin = '{origin}'"
        query = sq.execute(query)
        query = query.fetchone()
        query = f.decrypt(query[0])
        query = query.decode('utf-8')
        print("Password:",query)
    elif(action == "delete"):
        origin = input("Origin>>>")
        query = f"DELETE FROM edelweiss WHERE origin = '{origin}'"
        sq.execute(query)
        database.commit()
        print(f"deleted {origin}")
        exit()

if __name__ == "__main__":
    main()