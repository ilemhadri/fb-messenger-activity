# fb-messenger-activity: Monitoring your friends' activity on Messenger

![Messenger activity screenshot](https://i0.wp.com/ilemhadri.files.wordpress.com/2017/07/log.png)

Read the blog post: https://ilemhadri.wordpress.com/2017/07/01/visualizing-your-friends-activity-on-messenger/

## Installation

**Pre-requisites**
- Git ([how to install](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
- Python with the packages pandas, numpy, selenium, yaml, matplotlib
- A Selenium webbrowser instance. I recommend [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) or using the new [headless feature in Chrome](https://intoli.com/blog/running-selenium-with-headless-chrome/).

**Clone repository**
```
git clone https://github.com/sqren/fb-sleep-stats.git
```

**Configuration**

Open the source code folder:
```
cd fb-messenger-activity
```

Setup the database and save your Facebook login credentials.
*Note:* You may need to install a compatible selenium webbrowser in case "chromedriver.exe" is not compatible with your OS.
```
python init.py
```

Launch the scraper (and keep it active for as long as needed)
```
python scrape.py
```

Generate the PDF report
```
usage: main.py [-h] [--userid USERID] [--name NAME [NAME ...]] [--all]

Generates the user activity report

optional arguments:
  -h, --help            show this help message and exit
  --userid USERID       the user's facebook id
  --name NAME [NAME ...]
                        the user's full name
  --all                 generate reports for all users on file
```


## Disclaimer
#### 1)
I do not encourage personal use of this tool. I have decided to publish it for educational purposes only. Most of my friends and family are simply not aware of how much of their private information is being shared online without their knowledge. As such, the goal of this utility is certainly not to spy on your friends but to raise awareness about privacy concerns on Facebook.
#### 2)
This tool has not been updated since June 2017. The author does NOT intend to keep it up to date in case of updates to the Messenger internals.
