#!/bin/bash


convert -density 100 \
        \( fig_1.pdf fig_2.pdf +append \) \
        -bordercolor white -border 50 \
        fig_combined_horizontal.pdf
