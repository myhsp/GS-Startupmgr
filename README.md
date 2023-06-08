# GS-Startupmgr
启动项管理

### 用法:

```python
from Startup import Startup
with Startup.openFile("C:\\scripts\\startup.bat") as s:
    s.delItem("APP1")
    s.findItem("APP1")
    s.addItem("C:\\scripts\\APP1.exe", "APP2")
```

```python
s=Startup.openFile("C:\scripts\startup.bat")
s.saveFile()
s.closeFile()
```