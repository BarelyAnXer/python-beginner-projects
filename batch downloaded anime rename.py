import os
import re


# dapat yung file name eh yung unang number eh dapat yun yung episode number nya kung iba eh
# magkakanda letse letse ayos lng na meron mga number na kasunod basta yung unang number eh yung nnumber ng epsiode nya


os.chdir(r"C:\Users\63966\Desktop\New folder")

print(os.listdir())
files = os.listdir()

regex = re.compile(r'\d+')

mylist = []
for i in files:

    if i == "desktop.ini":
        continue
    else:
        temp = regex.findall(i)[0]
        os.rename(i, f"todardora ep {temp}.mp4")
