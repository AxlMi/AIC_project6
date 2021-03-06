#!/usr/bin/python3
# coding: utf-8
from crontab import CronTab

# this function will create new cron if he does not exist, the username variable concerns the user who will perform this function
# and launch time corresponds to the time between each launch of the script
def create_cron(username, launch_time):
    cron = CronTab(user=username)

    crontab = []

    line_cron = "0 */"+str(launch_time)+" * * * cd /home/axel/projet6/AIC_project6 && /usr/bin/python3 main.py >> /home/cron3.log 2>&1"
    """ I check that the crontab does not already exist, else i add him"""
    for line in cron.lines:
        crontab.append(str(line))
    """i make a comparison betwen the crontab and the line i want to execute"""
    if line_cron in crontab:
        print("le cron existe déja")
    else:
        job = cron.new(command="cd /home/axel/projet6/AIC_project6 && /usr/bin/python3 main.py >> /home/cron3.log 2>&1")
        job.every(launch_time).hours()
        cron.write()
        print("le cron a été mis en place")
