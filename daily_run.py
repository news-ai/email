# -*- coding: utf-8 -*-
# Stdlib imports
import time

# Third-party app imports
import schedule

# Local app imports
from daily import process


def run_emails():
    print 'Running daily process'
    process()

schedule.every().day.at("5:00").do(run_emails)

print 'Starting schedule'

while True:
    schedule.run_pending()
    time.sleep(1)
