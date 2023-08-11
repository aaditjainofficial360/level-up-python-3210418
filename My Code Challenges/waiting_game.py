import time
def waiting_game():
    print('Welcome to Game!')
    target_time=int(input('Enter your target time(in seconds):'))
    print(f'Your target time is {target_time} seconds.')
    print('---Press Enter to begin---')
    input()
    start_time=time.time()
    print(f'...Press Enter gain after {target_time} seconds...')
    input()
    end_time=time.time()
    time_elapsed=end_time-start_time
    if time_elapsed>target_time:
        print(f'Elapsed time: {(time_elapsed)} seconds ({(time_elapsed-target_time)} seconds too slow)')
    else:
        print(f'Elapsed time: {abs(time_elapsed)} seconds ({abs(time_elapsed - target_time)} seconds too fast)')
    return ''

waiting_game()


