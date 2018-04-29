import os
import re
from time import strftime
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
reg0=re.compile(r' +get +it')
os.chdir(r'C:\temp')
results=open('result.csv','a')

for root,subfolders,filenames in os.walk(os.getcwd()):
    print("当前目录为："+root)
    for subfolder in subfolders:
        print(root+'的子目录：'+subfolder)
    for filename in filenames:
        print('文件夹'+root+'内的文件名为：'+filename)
        if filename=='goal.txt':
            file=open(os.path.join(root,'goal.txt'),'r')
            strings=file.read()
            result=reg0.search(strings).group()
            results.write(os.path.dirname(os.path.dirname(root))+strftime(',Time:%Y%m%d%H%M%S,')+result+'\n')
            file.close()
            logging.debug('file closed')
results.close()
logging.debug('End of program')
