from scrapy import cmdline
import os
from datetime import datetime
import time

#while True:
dir_name = datetime.now().strftime("%Y%m%d_%H%M%S") 
os.rename('database',dir_name)
os.makedirs('database')
os.system("scrapy crawl xs_content -o database/content.json")
#os.system("scrapy crawl xs -o database/xs.json")
#    time.sleep(1800)


