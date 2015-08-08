#!/usr/bin/env bash

###############################################################################
# Weather forecast script                                                     #
# 2013-10-22, tc                                                              #
#                                                                             #
# The script makes use of                                                     #
#     - gnuplot (see http://www.gnuplot.info)                                 #
#     - jq (see http://stedolan.github.io/jq)                                 #
# before use, the variables GNUPLOT and JQ should be set to their paths.      #
#                                                                             #
# Rights for the original version:                                            #
#     AnsiWeather 1.00 (c) by Frederic Cambus 2013                            #
#     https://github.com/fcambus/ansiweather                                  #
#     AnsiWeather is released under the BSD 3-Clause license.                 #
#     (see https://github.com/fcambus/ansiweather/blob/master/LICENSE)        #
###############################################################################

# (0) program paths
GNUPLOT=''
JQ=''

# (1) set parameters
if [ $# -eq 1 ] && [[ $1 =~ ^-?[0-9]+$ ]]; then ndays=$1; else ndays=3; fi;
if (("$ndays>5")); then echo "ERROR: weather is a chaotic system, long-term predictions are impossible."; exit 1; fi
location="Paris,FR";

# (2) fetch data
forecast=$(curl -s http://api.openweathermap.org/data/2.5/forecast?q=$location\&units='metric');

# (3) parse data
DATAFILE='/tmp/weather_forecast.dat'; rm $DATAFILE; touch $DATAFILE;
for ((step=0;step<8*$ndays;step++)); do
    list=$(echo $forecast | $JQ -r  ".list[$step]");
    t=$(echo $list | $JQ -r ".dt_txt")
    temp=$(echo $list | $JQ -r ".main.temp")
    rain=$(echo $(echo $list | $JQ -r ".rain") | cut -d ' ' -f 3)
    day_new=$(echo $t |cut -d '-' -f 3|cut -d ' ' -f 1)
    if [ "$day_new" != "$day_old" ] && (("$step">0));then echo -e "\n" >>$DATAFILE; fi
    tlabel=$(echo $t|cut -d ' ' -f 2| cut -d ':' -f 1)'h'
    echo "$tlabel $step $temp $rain" >> $DATAFILE
    day_old=$(echo $t |cut -d '-' -f 3|cut -d ' ' -f 1)
done

# (4) plot parsed data
PLOTFILE='/tmp/plot-weather.sh'; rm $PLOTFILE; touch $PLOTFILE
echo -e "#!$GNUPLOT --persist
set term wxt size 1000,500 font 'Arial, 14' dashed;
set title 'Weather forecast, next $ndays days'
set grid; set k below;
set xtics nomirror rotate by -35; set ytics nomirror; set y2tics;
set ylabel 'temp (°C)' font ',16'; set y2label 'rain (mm/3h)' font ',16';
plot '$DATAFILE' using 2:3:xticlabel(1) w lp tit 'temp' lw 2.5 lc 1 lt 2,'$DATAFILE' using 2:4 axis x1y2 w lp tit 'rain 3h' lw 2.5 lc 3 lt 1;
replot;" >> $PLOTFILE
chmod +x $PLOTFILE
$PLOTFILE
