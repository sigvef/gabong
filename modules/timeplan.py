#coding=utf-8

import urllib
import datetime

def timeplan(phenny,input):
    try:
        today = datetime.datetime.today()
        nick = input.group(2)
        if nick:
            nick = nick.split(" ")[0]
        if not nick:
            nick = input.nick
        ical = urllib.urlopen(r'http://ntnu.1024.no/2014/spring/'+nick.lower()+'/ical/')
        found = False
        difference = datetime.timedelta.max
        info = ""
        countdown = -1
        for line in ical:
            if line[:17] == "DTSTART;TZID=CET:":
                testdate = datetime.datetime.strptime(line[17:].strip(),"%Y%m%dT%H%M%S")
                if testdate > today:
                    if testdate-today < difference:
                        founddate = testdate
                        countdown = 1
                        difference = founddate - today
            else:
                if countdown == 0:
                    info = line[12:]
                    countdown = -1
                elif countdown > 0:
                    countdown -= 1

        td = founddate-today
        s = td.seconds
        d = td.days
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        timestring = ""
        if d == 1:
            timestring += "1 day"
        elif d > 1:
            timestring += str(d)+" days"
        if hours == 1:
            if d:
                timestring += ", "
            timestring += "1 hour"
        elif hours > 1:
            if d:
                timestring += ", "
            timestring += str(hours)+" hours"
        if minutes == 1:
            if hours:
                timestring += " and "
            elif d:
                timestring += ", "
            timestring += "1 minute"
        elif minutes > 1:
            if hours:
                timestring += " and "
            elif d:
                timestring += ", "
            timestring += str(minutes)+" minutes"
        phenny.reply(timestring+' until: ' + info.strip("\/"))

    except:
        phenny.reply("Could not find any information.")



timeplan.commands=['timeplan']
