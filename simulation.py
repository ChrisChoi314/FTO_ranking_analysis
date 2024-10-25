import numpy as np

n = 200
trials = 12

 # I used my own stats from my best ao200 
solves = np.random.normal(loc=17.35, scale=1.61, size=n)

# Create 2 arrays that have the stackmatted-2-decimals times, and one with millisecond precision (could be stackmatted or cstimer timer, doesn't matter)
solves_2dec = np.trunc(solves*100)/100

solves_3dec = np.trunc(solves*1000)/1000

time_format = [5,12,100]
trim = [1,1,5]
averages_2dec = [[],[],[]]
averages_3dec = [[],[],[]]
averages_real = [[],[],[]]

# calculates ao5
def avg_of_x(arr, x):
    for i in range(x):
        arr = np.delete(arr,np.argmax(arr))
        arr = np.delete(arr,np.argmin(arr))
    return np.mean(arr)

arr = [1,2,3,4,5]
avg = avg_of_x(arr, 1)
print(avg, arr)

# compute the average arrays
for i in range(3):
    for j in range(n - time_format[i]):
        averages_2dec[i] = np.append(averages_2dec[i],avg_of_x(solves_2dec[j:j+time_format[i]], trim[i]))

        averages_3dec[i] = np.append(averages_3dec[i],avg_of_x(solves_3dec[j:j+time_format[i]], trim[i]))

        averages_real[i] = np.append(averages_real[i],avg_of_x(solves[j:j+time_format[i]], trim[i]))

# round the average arrays
round_2dec = averages_2dec
