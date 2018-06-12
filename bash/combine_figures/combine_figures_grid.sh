#!/bin/bash


convert -density 100 \
        \( fig_1.pdf fig_2.pdf +append \) \
        \( fig_3.pdf fig_4.pdf +append \) \
        -append \
        -bordercolor white -border 50 \
        fig_combined_grid.pdf
