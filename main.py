import os
import subprocess
server_address = '\\\\10.1.10.52\\d\\'   #location of remote server

app_type = "java"               #app type:  java, exe
app_name = "server.jar"         #
app_dir = "1.18\\"
app_params = "-Xmx8G"

print(server_address+app_dir)
def StartApp():
    if app_type == "java":
        os.system('powershell -Command "cd ' + server_address + app_dir + ' ; java ' + app_params + ' ' '-jar ' + app_name + '"')


StartApp()