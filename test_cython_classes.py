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
        
        if True:
            #Method 1 has *args after positional arg
            #Neither **kwargs nor **args with **kwargs supported
            #by remote functions according to signature.py docstring
            #Initialization of the actor succeeds and succeeds in
            #execution
            res = ray.get(a.method1.remote(1))
            print("Res is: ", res)
        if False:
            #Method 2 has *args after positional arg
            #and a default keyword argument, b, after *args
            #Neither **kwargs nor **args with **kwargs supported
            #by remote functions according to signature.py docstring
            #But the initialization of the actor succeeds and then fails in
            #execution
            #Fails with:
            #Exception: The name 'b' is not a valid keyword argument 
            #for the function 'method2'
            res = ray.get(a.method2.remote(1,b=2))
            print("Res is: ", res)
        if False:
            #Method 3 has *args after positional arg
            #and a keyword argument after *args, followed by **kwargs
            #Neither **kwargs nor **args with **kwargs supported
            #by remote functions according to signature.py docstring
            #But the initialization of the actor succeeds and then fails in
            #execution.
            #Fails with:
            #Exception: The name 'b' is not a valid keyword argument 
            #for the function 'method3'
            res = ray.get(a.method3.remote(1,b=2))
            print("Res is: ", res)

    if classut == "Test4":
        T = ray.remote(Test4)
        a = T.remote()
        #Method 1 has no positional args but default keyword values
        #--not supported
        res = ray.get(a.method1.remote())
        print("Res is: ", res)
        
