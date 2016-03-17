Basic examples for python profiling tools.

###cProfile
Simply run a python script via a command like
```
python -m cProfile -s cumtime script.py
```

(example: run `./profile_script1_via_cProfile.sh` to profile script1.py)

###cProfile+runsnake
Run a python script via a command like
```
python -m cProfile -o output_file script.py
```
and read its output file via
```
runsnake output_file
```

(example: run `./profile_script2_via_cProfile_and_runsnake.sh` to profile script2.py)

###cProfile+runsnake


###kernprof
First, install line\_profiler (short story: `pip install line_profiler`, if you use pip | long story: https://github.com/rkern/line_profiler | fun story: http://xkcd.com/1654). Then change your script by adding a `@profile` decorator in the line before the `def` of each function that you need to profile. Finally, use a command like
```
kernprof.py -l -v script.py
```

(example: run `./profile_script3_via_kernprof.sh` to profile script3.py)
