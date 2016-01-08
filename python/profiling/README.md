Basic examples for two possible profiling tools.

###cProfile
Simply run a python script via a command like
```
python -m cProfile -s cumtime script.py
```

(example: script1.py and profile\_script1\_via\_cProfile.sh)

###kernprof
First, install line\_profiler (long story: https://github.com/rkern/line_profiler, short story: `pip install line_profiler`, if you use pip). Then change your script by adding a `@profile` decorator in the line before the `def` of each function that you need to profile. Finally, use a command like
```
kernprof.py -l -v script.py
```

(example: script2.py and profile\_script2\_via_kernprof.sh)
