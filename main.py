import os

server_address = r"\\10.1.10.52\d\ "   #location of remote server

app_type = "java"               #app type:  java, exe
app_name = "server.jar"         #
app_dir = "1.18\\"
app_params = "-Xmx8G"

print(server_address)
def StartApp():
    if app_type == "java":
        os.popen("java " + app_params + " -jar " + server_address + app_dir + app_name)


StartApp()