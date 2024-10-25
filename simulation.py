import numpy as np

n = 1000000
trials = 12

solves = np.random.normal(loc=17.35, scale=1.61, size=n) # I used my own stats from my best ao200 

# Create 2 arrays that have the stackmatted-2-decimals times, and one with millisecond precision (could be stackmatted or cstimer timer, doesn't matter)
solves_2dec = np.trunc(solves*100)/100

solves_3dec = np.trunc(solves*1000)/1000

print(f'worst single: {np.max(solves_2dec)}, best single: {np.min(solves_2dec)}')  #just out of curiosity lol, apparently with a million solves, my best is 8.7 -9.8

mode = ['round', 'truncate']
time_format = [5,12,100]

