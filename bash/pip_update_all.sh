#!/bin/bash

# update all pip packages
# source: http://stackoverflow.com/a/3452888

pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo -H pip install -U
