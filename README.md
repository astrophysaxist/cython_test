# Cython testing with ray

This is just a repo illustrating some features of [Ray](https://github.com/ray-project/ray), the framework for building and running distributed applications.

I've noticed some gotchas when trying to initialize and run Cython methods.

## Build Cython module of demo class

You can build the very simple Cython classes by executing:
```
python setup.py build_ext --inplace
```

## Running demos

You can run a demo of executing methods from the Cython demo classes by running test_classes.py with a commandline argument (number) of the test class to run.

```
python test_classes.py 1
```

*The above executes the testing of class Test1*

Explore comments in the test_classes.py and cython_test.pyx for more information.