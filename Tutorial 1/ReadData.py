import pandas as pd
import os
import time
from datetime import datetime

# Path to the folder
path = "D:\Python Projects\SVM Practice\Tutorial 1\intraQuarter"

def key_stats(gather="Total Debt/Equity (mrq)"):
    statspath = path + '/_KeyStats'
    # Each directory is a stock
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio'])

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[1]

        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html') # Specify structure of date time
                unix_time = time.mktime(date_stamp.timetuple())
                # We have stock name and time for it
                full_file_path = each_dir + '/' + file
                print full_file_path
                source = open(full_file_path,'r').read()
                value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                print ticker+":", value

            time.sleep(15)


key_stats()