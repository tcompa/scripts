#!/bin/bash

user_jobs=`qstat -r | grep $USER | wc -l`
tot_jobs=`qstat -Bf|grep nodect|cut -d' ' -f 7`
others_jobs=$(($tot_jobs - $user_jobs))

echo "User's running jobs: $user_jobs ($USER)"
echo "Total running jobs:  $tot_jobs"
echo "Oters' running jobs: $others_jobs"
