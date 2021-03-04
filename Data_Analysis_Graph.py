import matplotlib.pyplot as plt

f = open("/Users/saimonish/IntelliJ_workspace/ACSEF2021/waiting_times.txt", "r")

waittimes = []
array = [0]*400
for j in array:
    x = f.readline()
    if x != "==== \n":
        waittimes.append(int(x))

# frequencies


# setting the ranges and no. of intervals
range = (0, 10)
bins = 10

# plotting a histogram
plt.hist(waittimes, bins, range, color = 'green',
         histtype = 'bar', rwidth = 0.8)

# x-axis label
plt.xlabel('No. of Units Waited')
# frequency label
plt.ylabel('No. of cars')
# plot title
plt.title('Wait Time of Each Car')

# function to show the plot
plt.show()

plt.savefig("/Users/saimonish/IntelliJ_workspace/ACSEF2021/Data_Analysys_Graph.png")