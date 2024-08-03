import pyperclip as cb
from glob import glob

txtFiles = glob('*.txt')
copyText = ""
print(f"已识别到{len(txtFiles)}个相关文件")

for filePath in txtFiles:
    readFile = open(filePath, 'r')
    readList = readFile.read().splitlines()
    readFile.close()

    copyText += readList[6] + " " + readList[0] + "\n"

cb.copy(copyText)
input("ender to exit...")
