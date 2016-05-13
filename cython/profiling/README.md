Basic line-by-line profiling of a cython function. This is essentially the same as http://nbviewer.jupyter.org/gist/tillahoffmann/296501acea231cbdf5e7, but without a notebook.  

Intructions:
 + Install [line_profiler](https://pypi.python.org/pypi/line_profiler/) (short story: `conda install line_profiler`, or `pip install line_profiler`).
 + Write your cython function in a .pyx file (see [my_function.pyx](my_function.pyx)).
 + Compile it, by running `python setup_cython.py build_ext --inplace`. Note that [the setup script provided](setup_cython.py) includes some compiler directives necessary for the line-by-line profiling (`linetrace` and `binding`).
 + In [profile_cython_function.py](profile_cython_function.py), choose the arguments for which the functions has to be profiled (list variable `arguments`).
 + Run [profile_cython_function.py](profile_cython_function.py).
