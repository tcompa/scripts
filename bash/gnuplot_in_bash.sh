#!/bin/bash

for FUNCTION in sin cos; do
    gnuplot <<- EOF
        set term wxt persist
        f(x)=${FUNCTION}(x)
        set xrange [0:2.0*pi]
        set grid
        set title "${FUNCTION}(x)"
        plot f(x)
EOF
done

# If you plot data from a file, and want to process
# the columns, you need to escape the "$" as \$:
#     plot 'data.dat' u 1:(\$2 * 7) 
