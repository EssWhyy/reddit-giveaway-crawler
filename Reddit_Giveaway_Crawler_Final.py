'''EssWhyy/Giveaway_Prawer_Final'''

import praw
import xlwt
import re
from xlutils.copy import copy
from xlrd import open_workbook

print('Reddit Giveaway Prawer')

desireditemslist = []
item = ''

print("If there are any items which you wish to win, type them out, one by one and press enter to key in")
print("Type done to proceed")
print("Type clear to reset the list")


while item.lower() != 'done':
    try:
        item = input()
        desireditemslist.append(item.lower())
    except TypeError:
        print("Key in letters only")
    if item == 'clear':
        del desireditemslist[:]
    print('items listed:'+ str(desireditemslist))


USA = ''

while USA != 'y' and USA != 'n':
    try:
        print("Search for USA posts only? y/n")
        USA = input()
        USA = USA.lower()

    except TypeError:
        print("Enter y or n please.")



n = 0
while n not in range(10,1001):
    print("Search for how many new posts? Type a number from 10-1000")
    try:
        n = input()
        n = int(n)
    except TypeError:
        print("Enter numbers only please.")


desireditems = ''.join(desireditemslist)
parentheses1 = r"[0-9]+/[0-9]+/[0-9]+"
parentheses2 = r"[0-9]+/[0-9]+"


#Create a new workbook to save info in, then enter the sheet path here
rb = open_workbook("/Users/Giveaway_Sheet.xls",formatting_info=True)

r_sheet = rb.sheet_by_index(0)
wb = copy(rb)
w_sheet = wb.get_sheet(0)
rowx = 0
col_indexnumber = 0
col_title = 1
col_url = 2
col_date = 3
col_indicator = 4

number = 0
list4 = []

#Creates a script program to run the praw web crawler, see screenshot for example

reddit = praw.Reddit(client_id='xxxxxxxxxxxx',
 client_secret='xxxxxxxxxxxxxxxxxxxxxxxxx',
 user_agent='Whatever you named your script program')


subreddit = reddit.subreddit('giveaways')


for submission in subreddit.new(limit=n):

    if 'WW' in submission.title:
        rowx += 1
        w_sheet.write(rowx,col_indexnumber,str(col_indexnumber))
        w_sheet.write(rowx,col_title, submission.title)
        w_sheet.write(rowx,col_url, submission.url)


        list1 = re.findall(parentheses1, submission.title)
        if len(list1) > 0:
            w_sheet.write(rowx,col_date, list1[0])
        else:
            list1 = re.findall(parentheses2, submission.title)
            if len(list1) > 0:
                w_sheet.write(rowx,col_date,list1[0])


        for item in desireditemslist:
            list3 = re.findall(item, (submission.title).lower())
            if len(list3) > 0:
                for entry in list3:
                    list4.append(entry)
                w_sheet.write(rowx,col_indicator,','.join(list4))

#Change path if needed.
wb.save("/Users/Giveaway_Sheet.xls")
