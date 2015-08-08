#!/bin/bash

INDMIN=20
INDMAX=79

for ((IND=$INDMIN;IND<=$INDMAX;IND++)); do
	number=`expr $IND - $INDMIN`
	INDone=`expr $IND + 1`
	VT=`head -n $INDone data-param.dat | tail -n 1`
	echo $number $IND $VT
	num_string=`printf "%03d\n" $number`
	gnuplot <<- EOF
		set grid
		set title 'N=75, N_{sites}=79, V_T/J=0.06'
		set xrange [-30:30]
		set yrange [0:2.5]
		set ytics 0.5
		set term pngcairo enhanced size 800,600
		set output "plot-nx-$num_string.png"
		set xlabel "x/a"
		set sample 1000
		trap(x)=$VT*x**2
		plot 'nx.dat' ind $IND w lp lw 1.5 title "n(x)", 'nx.dat' ind $IND u 1:3 w lp lw 1.5 title "n_0(x)",trap(x)
	EOF
done
