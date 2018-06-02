from scrapy import cmdline
import os
from datetime import datetime
import time
import json

#while True:
filelist=[]  
rootdir="/yjdata/www/xs/database"
filelist=os.listdir(rootdir)  
for f in filelist:  
    filepath = os.path.join( rootdir, f )  
    if os.path.isfile(filepath):  
        os.remove(filepath)  
os.system("scrapy crawl xs -o database/menu.json")
f = open('/yjdata/www/xs/database/menu.json',encoding = 'utf-8')
content = json.load(f)
name = "scrapy crawl xs_content -o database/"+content[0]['chapter'][0]+".json"
print(name)
os.system(name)
#    time.sleep(1800)


