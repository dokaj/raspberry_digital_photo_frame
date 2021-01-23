import datetime
import os
import time
from workalendar.europe import Hungary
import logging as log

time.sleep(30)
command = "vcgencmd display_power 0"
os.system(command)
ON = False
cal = Hungary()

while True:
    now = datetime.datetime.now().hour
    # cal.holiday(datetime.datetime.now().year)

    if cal.is_working_day(datetime.datetime.now()):
        # workdays
        if ON == False and (now == 7 or now == 12 or (now >= 17 and now <= 21)):
            log.info("holiday, ON")
            slideshow_command = "DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority /usr/bin/feh -q -p -Z -z -x -F -R 1200 -Y -D 50 /home/pi/Pictures/ &"
            os.system(slideshow_command)
            ON = True
            command = "vcgencmd display_power 1"
            os.system(command)
        elif ON == True and (now < 7 or now > 21 or (now > 7 and now < 12) or (now > 12 and now < 17)):
            log.info("holiday, OFF")
            try:
                stop_command = "sudo pkill feh"
                os.system(stop_command)
            except:
                print("cant kill feh")
            ON = False
            command = "vcgencmd display_power 0"
            os.system(command)
    else:
        # holiday or weekend
        if ON == False and now >= 8 and now <= 21:
            log.info("holiday, ON")
            slideshow_command = "DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority /usr/bin/feh -q -p -Z -z -x -F -R 1200 -Y -D 50 /home/pi/Pictures/ &"
            os.system(slideshow_command)
            ON = True
            command = "vcgencmd display_power 1"
            os.system(command)
        elif ON == True and (now < 8 or now > 21):
            log.info("holiday, OFF")
            try:
                stop_command = "sudo pkill feh"
                os.system(stop_command)
            except:
                print("cant kill feh")
            ON = False
            command = "vcgencmd display_power 0"
            os.system(command)
    time.sleep(60)
