import numpy as np

n = 100000
trials = 12

 # I used my own stats from my best ao200 
solves = np.random.normal(loc=17.35, scale=1.61, size=n)

# Create 2 arrays that have the stackmatted-2-decimals times, and one with millisecond precision (could be stackmatted or cstimer timer, doesn't matter). we truncate here because it's how timers work in reality. 
solves_2dec = np.trunc(solves*100)/100
solves_3dec = np.trunc(solves*1000)/1000

time_format = [5,12,100]
trim = [1,1,5]
averages_2dec = [[],[],[]]
averages_3dec = [[],[],[]]
averages_real = [[],[],[]]

# calculates averages in the cubing way. note that x in the name isn't the same as the x in the parameters, the letter just tells you how much to trim from each side
def avg_of_x(arr, x):
    for i in range(x):
        arr = np.delete(arr,np.argmax(arr))
        arr = np.delete(arr,np.argmin(arr))
    return np.mean(arr)

# compute the average arrays
for i in range(3):
    for j in range(n - time_format[i]):
        averages_2dec[i] = np.append(averages_2dec[i],avg_of_x(solves_2dec[j:j+time_format[i]], trim[i]))

        averages_3dec[i] = np.append(averages_3dec[i],avg_of_x(solves_3dec[j:j+time_format[i]], trim[i]))

        averages_real[i] = np.append(averages_real[i],avg_of_x(solves[j:j+time_format[i]], trim[i]))

# round the average arrays
round_2dec = [[],[],[]]
for i in range(3):
    round_2dec[i] = np.round(averages_2dec[i]*100)/100
round_3dec = [[],[],[]]
for i in range(3):
    round_3dec[i] = np.round(averages_3dec[i]*100)/100

# trunc the average arrays
trunc_2dec = [[],[],[]]
for i in range(3):
    trunc_2dec[i] = np.trunc(averages_2dec[i]*100)/100
trunc_3dec = [[],[],[]]
for i in range(3):
    trunc_3dec[i] = np.trunc(averages_3dec[i]*100)/100

# compare the averages when rounding
print('Rounding\n')
for i in range(len(time_format)):
    same = 0
    greater = 0
    less = 0
    dev_2dec = 0
    dev_3dec = 0
    for j in range(len(round_2dec[i])):
        if round_2dec[i][j] - round_3dec[i][j] > 0.005:
            greater += 1
        elif round_2dec[i][j] - round_3dec[i][j] < -0.005:
            less += 1
        else:
            same += 1
        dev_2dec += np.abs(round_2dec[i][j] - averages_real[i][j])
        dev_3dec += np.abs(round_3dec[i][j] - averages_real[i][j])
    tot = same + greater + less
    print(f"     ao{time_format[i]} is same:          {np.round(same/tot*100)}%")
    #print(f"Percent that 2 decmial ao{time_format[i]} is greater than 3 decimal: {greater/tot*100}%")
    print(f"     2 decimal ao5 is less: {np.round(less/tot*100)}%")
    print(f"     avg deviation of 2 decimal from real: {dev_2dec/tot}")
    print(f"     avg deviation of 3 decimal from real: {dev_3dec/tot}\n")

# compare the averages when truncating
print('Truncating\n')
for i in range(len(time_format)):
    same = 0
    greater = 0
    less = 0
    dev_2dec = 0
    dev_3dec = 0
    for j in range(len(trunc_2dec[i])):
        if trunc_2dec[i][j] - trunc_3dec[i][j] > 0.005:
            greater += 1
        elif trunc_2dec[i][j] - trunc_3dec[i][j] < -0.005:
            less += 1
        else:
            same += 1
        dev_2dec += np.abs(trunc_2dec[i][j] - averages_real[i][j])
        dev_3dec += np.abs(trunc_3dec[i][j] - averages_real[i][j])
    tot = same + greater + less
    print(f"     ao{time_format[i]} is same:          {np.round(same/tot*100)}%")
    #print(f"Percent that 2 decmial ao{time_format[i]} is greater than 3 decimal: {greater/tot*100}%")
    print(f"     2 decimal ao5 is less: {np.round(less/tot*100)}%")
    print(f"     avg deviation of 2 decimal from real: {dev_2dec/tot}")
    print(f"     avg deviation of 3 decimal from real: {dev_3dec/tot}\n")

# just for fun, some stats 
