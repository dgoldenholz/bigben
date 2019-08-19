#!/bin/bash
# Triggered through Crontab every 30 minutes
export DISPLAY=:0

volumeX=0.2
onpi=0

if [[ $onpi == 1 ]]
then
  thishome=/home/pi/bigben
  cmd="cvlc --play-and-exit --alsa-audio-device snd_rpi_googlevoicehat_soundcard"
else
  thishome=~/Documents/GitHub/bigben
#  cmd="/Applications/VLC.app/Contents/MacOS/VLC -I rc --play-and-exit --demux=avformat"
  cmd="$thishome/sox-14.4.2/play --volume $volumeX"
fi

outfile=$thishome/log.txt

minute=$(date +"%M")
echo  $miniute >> $outfile

if [[ $minute == 15 ]]
then
  eval $cmd "$thishome/quarter.wav" >> $outfile 2>&1
  echo 15 >> $outfile
elif [[ $minute == 30 ]]
then
  eval $cmd "$thishome/half.wav" >> $outfile 2>&1
  echo 30 >> $outfile
elif [[ $minute == 45 ]]
then
  eval $cmd "$thishome/3quarter.wav" >> $outfile 2>&1
  echo 45 >> $outfile
elif [[ $minute == 00 ]]
then
  hour=$(date +"%I")
  theHour="$thishome/${hour}.wav"
  eval $cmd $theHour >> $outfile 2>&1

  echo "$hour" >> $outfile
else
  echo "waiting...." >> $outfile
fi

