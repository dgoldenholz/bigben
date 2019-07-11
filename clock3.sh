#!/bin/bash
# Triggered through Crontab every 30 minutes
export DISPLAY=:0
outfile=/home/pi/bigben/log.txt
minute=$(date +"%M")
echo  $miniute >> $outfile

if [[ $minute == 15 ]]
then
  cvlc --play-and-exit --alsa-audio-device snd_rpi_googlevoicehat_soundcard "/home/pi/bigben/quarter.m4a" >> $outfile 2>&1
  echo 15 >> $outfile
elif [[ $minute == 30 ]]
then
  cvlc --play-and-exit --alsa-audio-device snd_rpi_googlevoicehat_soundcard "/home/pi/bigben/half.m4a" >> $outfile 2>&1
  echo 30 >> $outfile
elif [[ $minute == 45 ]]
then
  cvlc --play-and-exit --alsa-audio-device snd_rpi_googlevoicehat_soundcard "/home/pi/bigben/3quarter.m4a" >> $outfile 2>&1
  echo 45 >> $outfile
elif [[ $minute == 00 ]]
then
  cvlc --play-and-exit --alsa-audio-device snd_rpi_googlevoicehat_soundcard "/home/pi/bigben/hour.m4a" >> $outfile 2>&1
  hour=$(date +"%I")
  h2=$(expr $hour - 1)
  x=0
  while [ $x -lt $h2 ]
  do
    cvlc --play-and-exit --alsa-audio-device snd_rpi_googlevoicehat_soundcard "/home/pi/bigben/strike.m4a" >> $outfile 2>&1
    let x=x+1
  done
  cvlc --play-and-exit --alsa-audio-device snd_rpi_googlevoicehat_soundcard "/home/pi/bigben/laststrike.m4a" >> $outfile 2>&1

  echo "$hour" >> $outfile
else
  echo "waiting...." >> $outfile
fi

