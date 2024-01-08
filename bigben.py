#!/usr/bin/python
# Will play grandfather clcok sounds
# Version 1.4
# Daniel Goldenholz

# Library calls
from datetime import datetime
from time import sleep
import simpleaudio as sa

# MAIN CODE
mydir = '/home/pi/bigben/'
# constants
# smallTIME is how many secs to wait
smallTIME = 1
last_check = datetime.now()

# Initialize sound
clocklist = ['01','02','03','04','05','06','07','08','09','10','11','12']
quarterlist = ['quarter','half','3quarter']
ticname = 'tic2.wav'
wobj=[]
print('loading hours...')
for counter in range(12):
    fn = mydir + clocklist[counter] + '.wav'
    print(f'{counter+1} : {fn}')
    wobj.append(sa.WaveObject.from_wave_file(fn))

# load the quarter hours
qwobj=[]
print('loading quarters...')
for counter in range(3):
    print(counter+1)
    qwobj.append(sa.WaveObject.from_wave_file(mydir + quarterlist[counter] + '.wav'))

print('loading tic.')
twobj=sa.WaveObject.from_wave_file(mydir + ticname)

print('Loaded.')

dotic = 0
keepGoing=1
while keepGoing==1:
    keepGoing=0
    now = datetime.now()
    delta_t = now - last_check
    delta_t_sec = delta_t.total_seconds()
    current_HR = now.strftime("%H")
    current_T = now.strftime("%H%M")

    oktoplay = (now.hour>=8) and (now.hour<23)
    #if delta_t_sec > 900 and oktoplay==1:
    if oktoplay==1:
        print(f'Minutes: {now.minute}')
        #play_obj =twobj.play()
        #play_obj.wait_done()
        print(f'abs(now-0): {abs(now.minute-0)}')
        if abs(now.minute-0)<8 or abs(0-now.minute) < 8:
            H = now.hour % 12
            if H==0:
                H=12
            play_obj = wobj[H-1].play()
            play_obj.wait_done()
            dotic=0
            print('%s - %d' % (current_T,H))
            last_check = now

        if abs(now.minute-15)<8:
            play_obj = qwobj[0].play()
            play_obj.wait_done()
            dotic=0
            print('%s - quarter' % current_T)
            last_check = now

        if abs(now.minute-30)<8:
            play_obj = qwobj[1].play()
            play_obj.wait_done()
            dotic=0
            print('%s - half' % current_T)
            last_check = now

        if abs(now.minute-45)<8:
            play_obj = qwobj[2].play()
            play_obj.wait_done()
            dotic=0
            print('%s - 3quarter' % current_T)
            last_check = now

    sleep(smallTIME)
