# What's this
This is a news push program.  
This program collect news from RSS of https://campus.nutn.edu.tw/newsPost3/Default.aspx and the news will send to specific email address.

# Pre-requirements

- Software
  - Linux based OS
    - *Note: This program may run on Windows by modifying some codes.*
  - Python 3
  - Python 3 Library - feedparser, smtplib, email
    - *Note: You can install them by pip.*
  - Mail Trasfer Agent
  - cron

# Install

## Install cron
Please install main.py to cron.

Example config:
```
# m  h  dom mon dow   command
  0  *   *   *   *    python3 /home/user/Routine/nutn_news/main.py
```

## Change mail info
Use text editor to open main.py and edit the following code:
```
mail['To'] = 'user@example.com'
mail['From'] = 'sender@example.com'
```
Please change 'user@example.com' and 'sender@example.com' to the correct mail sender and receiver.


# Changelog
- 02 / 18 2022
  - First commit.
  - Program is ready to use.

# Copyright
This program is written by [haward79](https://www.haward79.tw/).  
All rights reserved by haward79.

