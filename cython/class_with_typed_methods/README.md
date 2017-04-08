In both cases, the file `lib_class_1.pyx` contains the definition of MyClass1:
```python
cdef class MyClass1:
    def __init__(self):
        pass

    def method_def(self, double x, double y, double z):
        return x + y + z

    cpdef double method_cpdef(self, double x, double y, double z):
        return x + y + z

    cdef double method_cdef(self, double x, double y, double z):
        return x + y + z
```

An instace C1 of MyClass1 will be used somewhere else (in cython code), and I want to make sure that I can access all the methods. Obviously my goal is to use the cdef method, as it should have the smallest overhead for calling.


## Case 1 (call from same file)
If the cython code where I want to access MyClass1 methods is in the same file where MyClass1 is defined, I can already use it as a type.
See for instance the following definition of MyClass2:
```python
cdef class MyClass2:
    def __init__(self, MyClass1 C):
        # Do other things here...

```
This
Inside MyClass2, I can call all the three methods of MyClass1, and this is an example of the time
```
method_def:   3.542060e-08 s/call
method_cpdef: 2.311900e-09 s/call
method_cdef:  2.034700e-09 s/call
```
I see that cpdef and cdef are both significantly faster than def (with a speedup larger than x10, in this case).


## Case 2 (call from another file)
In this case, I want to call the methods of MyClass1 from another (cython) file, and make sure that also method_cdef is accessible.
One way to do this is to use a pxd file, which is some sort of header file 

Quoting from [http://cython.readthedocs.io/en/latest/src/tutorial/pxd_files.html](http://cython.readthedocs.io/en/latest/src/tutorial/pxd_files.html)):

    When accompanying an equally named pyx file, they provide a Cython
    interface to the Cython module so that other Cython modules can
    communicate with it using a more efficient protocol than the Python one.

Then I simply create the file `lib_class_1.pxd`, like this:
```python
cdef class MyClass1:
    cpdef double method_cpdef(self, double x, double y, double z)
    cdef double method_cdef(self, double x, double y, double z)
```
where I only include the methods with cpdef or cdef.

Now I can use MyClass1 as a type in a different cython file (after `cimport`-ing it), like in this `lib_class_2.pyx`:
```python
import cython
from lib_class_1 cimport MyClass1

cdef class MyClass2:
    cdef MyClass1 C
    def __init__(self, MyClass1 C):
        self.C = C
        # Do things with self.C...
```

An example of the timing is:
```
method_def:   5.494130e-08 s/call
method_cpdef: 2.038100e-09 s/call
method_cdef:  2.016000e-09 s/call
```

I suspect (but I'm not sure) that this second method is also giving a small improvement on the cpdef calls, as compared to case1.
