import report
report=0
import os
import yaml
import argparse
import sys

if not (os.path.exists("data/lastActiveTimes.json") and os.path.exists("data/shortProfiles.json")):
    print("data missing. Please run init.py and scrape.py")
    sys.exit()

times=yaml.safe_load(open('data/lastActiveTimes.json','rb'))
profiles=yaml.safe_load(open('data/shortProfiles.json','rb'))

if not os.path.exists("out"):
    os.makedirs("out")
    
parser=argparse.ArgumentParser(description='Generates the user activity report')
parser.add_argument('--userid',nargs=1,help='the user\'s facebook id')
parser.add_argument('--name',nargs='+',help='the user\'s full name')
parser.add_argument('--all',action='store_const',const=True,help="generate reports for all users on file")
args = parser.parse_args()

if args.all:
    for userid in profiles:
        report.reportid(str(userid),profiles,times)
    sys.exit()
    
if args.userid:
    report.reportid(args.userid[0],profiles,times)
    sys.exit()
    
if args.name:
    report.report(' '.join(args.name),profiles,times)
    sys.exit()