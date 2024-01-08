# bigben

There are several old bash script version that are called clock2.sh, clock3.sh clock4.sh and clock5.sh. There is also bigben_v2.py and bigben_old.py.

The current version is bigben.py.

It is assumed you will run this on linux. If not, feel free to modify.
The sound files are assumed to be .wav files, which must be converted from the .m4a files. This is becuase on some linux systems it is hard to get a good codec for those. Just find a free converter and convert *.m4a to *.wav.

In linux you will want this bigben.py to run every quarter hour. The following way is good in case your linux system ever shuts down, it will keep working next startup:

how to add to startup
crontab -e
*/15 * * * * XDG_RUNTIME_DIR=/run/user/$(id -u) python ~/bigben/bigben.py
