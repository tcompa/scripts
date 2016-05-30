#!/bin/bash

echo "First way:"
for i in $(seq -f "%05.2f" 1 4); do
  echo $i
done

echo "Second way:"
for i in {1..4}; do
  printf "%05.2f\n" $i
done
