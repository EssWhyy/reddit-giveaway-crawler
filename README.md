# reddit-giveaway-crawler
## Post and link crawler &amp; sorter for r/giveaways 
Video Demonstration of Program: (TO BE UPDATED)

Reddit Giveaway Crawler is a simple regex search web scraper which collects data from r/giveaways with many giveaway contest posts (r/giveaways) and organises them into a spreadsheet. Made so that one can efficiently enter applicable contests and therefore increase chances of winning.

Filters out only entries with a certain location tag, and for a certain deadline as indicated on the post title. It then quotes the title, contest url, deadline date; entry by entry into the sheet.

There is the option to include any additional items to search for, if any of their desired items is included in post title, it will be highlighted at the end of the sheet for one to take note of.

##Here's an example of the output data of the program:
<img width="1275" alt="Screenshot 2021-11-28 at 12 13 31 PM" src="https://user-images.githubusercontent.com/39799639/143729386-0ba14748-8324-4702-bba2-991d4150162a.png">


### Requirements:

- Python 3 with PRAW, XLUTILS installed 
- A Reddit Account 
- Microsoft Excel or equivalent

### How to use:

- Go to reddit/preferences and create a script application, check the included screeenshot and link below. (https://praw.readthedocs.io/en/latest/getting_started/quick_start.html)

- Clone/download repo, edit file in notepad or an IDE and edit the portions under the commented portions (\# lines beginning with hashtags) Do NOT edit any other lines.

- Run Program “Giveaway Crawler” on Python and follow the on-screen instructions.

- View the newly created sheet to see a list of contests filtered and format as necessary.

### Notes:

- You have to install PRAW and XLUTILS in Python3 using (pip install xxx)

- XLUTILS only saves in 2003 Excel Format (.xls) as of v0.8 so it would be wise to create a separate sheet to import data there, and keep any filters/formulas/formatting if used.


