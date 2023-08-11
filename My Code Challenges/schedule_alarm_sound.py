import time

def schedule_function(event_time,function,message):
    start_time=time.time()
    while start_time<=event_time:
        function(message)
        start_time+=1

    return 'Done'

# Event_time(in seconds) : 500 seconds
schedule_function(time.time()+20,print,'Hey Brother!')