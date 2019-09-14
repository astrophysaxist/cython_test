import sys
sys.path.append('.')
from cython_test import Test1, Test2, Test3, Test4
import ray


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Incorrect number of args. Provide number of class to test.")
        sys.exit(1)

    classut = "Test"+sys.argv[1]

    ray.init()
    
    if classut == "Test1":
        T = ray.remote(Test1)
        #Initializing an actor with an argument in its __init__ fails
        a = T.remote(1)
        res = ray.get(a.never_here.remote())
        print("Res is: ", res)

    if classut == "Test2":
        T = ray.remote(Test2)
        #Creating separate function to initialize class variables with
        #no arguments to class __init__ succeeds
        a = T.remote()
        res = ray.get(a.initialize.remote(1))
        print("Res is: ", res)

    if classut == "Test3":
        T = ray.remote(Test3)
        a = T.remote()
        #Method 1 has *args after positional arg--not supported
        res = ray.get(a.method1.remote(1))
        print("Res is: ", res)
        #Method 2 has *args after positional arg--not supported
        #and a keyword argument after *args
        res = ray.get(a.method2.remote(1))
        print("Res is: ", res)
        #Method 3 has *args after positional arg--not supported
        #and a keyword argument after *args, followed by **kwargs
        res = ray.get(a.method3.remote(1))
        print("Res is: ", res)

    if classut == "Test4":
        T = ray.remote(Test4)
        a = T.remote()
        #Method 1 has no positional args but default keyword values
        #--not supported
        res = ray.get(a.method1.remote())
        print("Res is: ", res)
        
