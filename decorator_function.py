import time


#decorator function
def start_calculation(function) :
    def wrapper_function() :
        start_time=time.time()
        function()
        end_time=time.time()
        print(f"function {function.__name__} : run_time={end_time - start_time}")
    return wrapper_function
    

@start_calculation
def iteration_function() :
    for i in range(100000): 
        i=i

iteration_function()
