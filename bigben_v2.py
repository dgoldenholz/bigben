#!/usr/bin/python
# Will play grandfather clcok sounds
# Version 1.4
# Daniel Goldenholz

# Library calls
from datetime import datetime,timedelta
from time import sleep
import simpleaudio as sa


# MAIN CODE

# constants
# smallTIME is how many secs to wait
smallTIME = 10
okToTic = False

last_check = datetime.now()

# Initialize sound
clocklist = ['01','02','03','04','05','06','07','08','09','10','11','12']
quarterlist = ['quarter','half','3quarter']
ticname = 'tic2.wav'
wobj=[]
print('loading hours...')
for counter in range(12):
    print(counter+1)
    wobj.append(sa.WaveObject.from_wave_file(clocklist[counter] + '.wav'))

# load the quarter hours
qwobj=[]
print('loading quarters...')
for counter in range(3):
    print(counter+1)
    qwobj.append(sa.WaveObject.from_wave_file(quarterlist[counter] + '.wav'))

if okToTic==True:
    print('loading tic.')
    twobj=sa.WaveObject.from_wave_file(ticname)
    last_tic_check = last_check

print('Loaded.')

# create a timedelta of 1 second
delta = timedelta(seconds=1)

while 1:
    now = datetime.now()
    delta_t = now - last_check
    delta_t_sec = delta_t.total_seconds()
    if okToTic:
        delta_t_tic = now - last_tic_check
        delta_t_tic_sec = delta_t_tic.total_seconds()
    
    current_HR = now.strftime("%H")
    current_T = now.strftime("%H%M")
    oktoplay = (now.hour>=8) and (now.hour<=21)
    # are we allowed to play anything currently?
    if oktoplay==True:
        # if a quarter hour has passed, do something here
        if delta_t_sec > 900:
            if now.minute==0:
                H = now.hour % 12
                if H==0:
                    H=12
                play_obj = wobj[H-1].play()
                play_obj.wait_done()

                print('%s - %d' % (current_T,H))
                last_check = now

            if now.minute==15:
                play_obj = qwobj[0].play()
                play_obj.wait_done()
                dotic=0
                print('%s - quarter' % current_T)
                last_check = now

            if now.minute==30:
                play_obj = qwobj[1].play()
                play_obj.wait_done()
                dotic=0
                print('%s - half' % current_T)
                last_check = now

            if now.minute==45:
                play_obj = qwobj[2].play()
                play_obj.wait_done()
                dotic=0
                print('%s - 3quarter' % current_T)
                last_check = now
        else:
            if okToTic==True and delta_t_tic_sec>1:
                play_obj=twobj.play()
                play_obj.wait_done()
                last_tic_check = now

    sleep(smallTIME)
