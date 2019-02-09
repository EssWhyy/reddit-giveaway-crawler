# reddit-giveaway-crawler
Post and link crawler &amp; sorter for r/giveaways 
Made using the PRAW and XLUTILS modules in Python 3. A simple regex search web scraper which collects data from a site with many giveaway contest posts (r/giveaways) and organises them into a spreadsheet. Made so that I can efficiently enter the relevant applicable contests to win the stuff I want.

It filters out only entries with a certain location tag, and for a certain deadline as indicated on the post title. It then quotes the title, contest url, deadline date - entry by entry into the sheet.

Users also have the option to include any items which they want, if any of their desired items shows up in post title, it will be highlighted at the end of the sheet.

Requirements:

Python 3 with PRAW, XLUTILS installed (pip install module) A Reddit Account Spreadsheet Manager (Like Microsoft Excel)

How to use:

Go to reddit/preferences and create a script application (https://praw.readthedocs.io/en/latest/getting_started/quick_start.html)
Save files to computer, edit file in notepad and edit the portions under the #commented portions (lines with hashtags, read the instructions in itif you are unsure.) Do not edit any other lines.
Run Program “Giveaway Crawler” and follow the on-screen instructions.
View the newly created sheet to see a list of contests filtered and format as necessary.
Notes:

•	You have to install python PRAW using (pip install praw)

•	XLUTILS only saves in 2003 Excel Format (.xls) as of v0.8 so it would be wise to create a separate sheet to import data there, and keep any filters/formulas/formatting.

CHECK THE SCREENSHOT INCLUDED IN THE REPO FOR AN EXAMPLE OF THE REDDIT SCRIPT PROGRAM.
