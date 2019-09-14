#!python
# cython: embedsignature=True, binding=True

cdef class Test1:
    cdef int a
    #Init cannot have arguments apparently so
    #creating an instance of this type of actor will fail.
    def __cinit__(self, a):
        self.a = a
    def never_here(self):
        self.a += 1
        return self.a

cdef class Test2:
    cdef int a
    #Init cannot have arguments apparently so
    #creating an instance of this type will succeed.
    def __cinit__(self):
        pass
    def initialize(self,  a):
        self.a = a
        return self.a+1

cdef class Test3:
    cdef int a
    cdef int b
  
    def __cinit__(self):
        pass
    def method1(self, a, *args):
        #Ray allows *args
        self.a = a
        return self.a+1
    def method2(self, a, *args, b=2):
        #Ray checks for *args  and **kwargs in method as its not supported
        #But this slips by and breaks when workers try to run.
        self.a = a
        self.b = b
        return self.a+self.b
    def method3(self, a, *args, b=2, **kwargs):
        #Ray checks for *kwargs of a method as its not supported
        #But this slips by and breaks when workers try to run.
        self.a = a
        self.b = b
        return self.a+self.b

cdef class Test4:
    cdef int a
    cdef int b
  
    def __cinit__(self):
        pass
    def method1(self, a=1, b=2):
        #Ray does not support default arguments for keyword type
        #variables so running this method with no arguments will fail.
        self.a = a
        self.b = b
        return self.a+self.b
