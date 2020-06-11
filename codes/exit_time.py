## @package exit_time
# This function will keep a track of time and breaks the process if the it exceeds the predefined time limit.

def exit_after(s):
    """
    Args : 
        s : Maximum amount of time in seconds that a process can run
    
    Return:
        breaks the statement when the running time exceeds the specified time
    """
    def quit_function(fn_name):
        return(None)

    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer