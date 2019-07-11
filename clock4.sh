#!/bin/bash
# Triggered through Crontab every 30 minutes
export DISPLAY=:0

onpi=1

if [[ $onpi == 1 ]]
then
  outfile=/home/pi/bigben/log.txt
else
  outfile=~/Documents/GitHub/bigben/log.txt
fi

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
  hour=$(date +"%I")
  theHour="/home/pi/bigben/${hour}.m4a"
  cvlc --play-and-exit --alsa-audio-device snd_rpi_googlevoicehat_soundcard $theHour >> $outfile 2>&1

  echo "$hour" >> $outfile
else
  echo "waiting...." >> $outfile
fi

