"""
Example:
    with Startup.openFile("C:\\scripts\\startup.bat") as s:
        s.delItem("APP1")
        s.findItem("APP1")
        s.addItem("C:\\scripts\\APP1.exe", "APP1")
     
    s=Startup.openFile("C:\scripts\startup.bat")
    s.saveFile()
    s.closeFile()
    
"""


import os
import argparse

class Startup:
    def openFile(filename):
        if not os.path.isfile(filename):
            print(f"[-] Cannot find '{filename}'.No such file.")
        new = Startup()
        new.file = open(filename, "r+", encoding="utf-8")
        new.filename = filename
        new.loadFile()
        print(f"[+] '{filename}' is loaded successfully.")
        return new

    def closeFile(self):
        if self.file:
            self.file.close()
            print(f"[+] '{self.filename}' is closed.")

    def loadFile(self):
        self.items = []
        lines = self.file.readlines()
        for now, line in enumerate(lines, start=1):
            flag, path, app = (0, "", "")
            try:
                path, app = [s.strip("start").strip() for s in line.split("rem")]
            except:
                flag |= 1
            if flag | Startup.checkStr(path) | Startup.checkStr(app):
                print(f"[-] Invalid formatting. Line {now}")
            else:
                self.items.append((path, app))
        print(f"[+] '{self.filename}' is loaded with {len(self.items)} items.")

    def addItem(self, path=None, app=None):
        if path is None or app is None:
            print("[-] Please provide path and app.")
            return
        self.items.append((path, app))
        print(f"[+] Added '{path}' with app '{app}'.")
        
    def addItem(self, path=None, app=None):
        if path is None or app is None:
            print("[-] Please provide path and app.")
            return
        self.items.append((path, app))
        print(f"[+] Added '{path}' with app '{app}'.")

    def delItem(self, appName=None):
        if appName is None:
            print("[-] Please provide appName.")
            return
        self.items = list(filter(lambda x: x[1] != appName, self.items))
        print(f"[+] Deleted item: '{appName}'.")
        
    def findItem(self,appName):
        if appName is None:
            print("[-] Please provide appName.")
            return
        filtered = list(filter(lambda x: x[1] == appName, self.items))
        print(f"[+] Found {len(self.items)} items.")
        return len(filtered)
        
    def saveFile(self):
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(
            ["start %s rem %s\n" % (item[0], item[1]) for item in self.items]
        )
        print(f"[+] '{self.filename}' is saved with {len(self.items)} items.")

    @staticmethod
    def checkStr(str):
        return " " in str or "\n" in str or "rem" in str or len(str) == 0 or str == None

    def __enter__(self):
        return self

    def __exit__(self, excType, excVal, excTb):
        self.saveFile()
        self.closeFile()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Startup Manager')
    parser.add_argument('-f', default="C:\\scripts\\startup.bat", type=str, help='File Path')
    parser.add_argument('-a', default=[], type=str, help='Add Item',nargs='+')
    parser.add_argument('-d', type=str, help='Del Item')
    parser.add_argument('-c', type=str, help='Count Item')
    opt=parser.parse_args()
    with Startup.openFile(opt.f) as s:
        if len(opt.a):
            s.addItem(opt.a[0], opt.a[1])
        if opt.d!=None:
            s.delItem(opt.d)
        if opt.c!=None:
            s.findItem(opt.c)
