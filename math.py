import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")

arr = list(df["math score"])

mean = statistics.mean(arr)
median = statistics.median(arr)
mode = statistics.mode(arr)
sd = statistics.stdev(arr)

firstSDStart, firstSDEnd = mean-sd, mean+sd
listOfDataWithinFirstSD = [result for result in arr if result>firstSDStart and result < firstSDEnd]

secondSDStart, secondSDEnd = mean-(sd*2), mean+(sd*2)
listOfDataWithinSecondSD = [result for result in arr if result > secondSDStart and result < secondSDEnd]

thirdSDStart, thirdSDEnd = mean-(sd*3), mean+(sd*3)
listOfDataWithinThirdSD = [result for result in arr if result > thirdSDStart and result < thirdSDEnd]

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)

print("{}% of data lies within 1 standard deviation".format(len(listOfDataWithinFirstSD)*100.0/len(arr)))
print("{}% of data lies within 2 standard deviation".format(len(listOfDataWithinSecondSD)*100.0/len(arr)))
print("{}% of data lies within 3 standard deviation".format(len(listOfDataWithinThirdSD)*100.0/len(arr)))

fig = ff.create_distplot([arr], ["height"], show_hist=False)
fig.show()