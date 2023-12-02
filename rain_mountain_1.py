import csv
import matplotlib.pyplot
import math
import collections

sumPrecipitation = 0.0
allTimePrecipitation = 0.0
year = '1959'
day = '01'
counterYears = 0

newYear = []
dailySums = []
allTimesum = []
yearlySums = []

#dictionary with all the yearly sums
trackingYears = {}
trackingYearsDaily = {}


csvFile = 'marrakesh_1959_2021.csv'

with open(f'data/{csvFile}', newline='') as csvfile:
    rainReader = csv.reader(csvfile)
    for row in rainReader:
        workingYear = year
        year = row[0][0:4]
        #trigger actions when new year:
        if year > workingYear:
            trackingYearsDaily[int(workingYear)] = newYear
            dailySums.append(newYear)
            newYear = []
            sumPrecipitation = 0
        #trigger action for each line:
        hourlyPrecipitaion = row[1]
        if hourlyPrecipitaion == 'NaN':
            hourlyPrecipitaion = 0
        hourlyPrecipitaion = float(hourlyPrecipitaion)
        sumPrecipitation += hourlyPrecipitaion
        allTimePrecipitation += hourlyPrecipitaion
        workingDay = day
        day = (row[0][8:10])
        #append sum for each new day:
        if day != workingDay:
            newYear.append(sumPrecipitation)
            allTimesum.append(allTimePrecipitation)

#dictionary with rain sum for each year
for i in range (len(dailySums)):
    thisYearSum = (dailySums[i][len(dailySums[i])-1])
    thisYear = 1959 + i
    trackingYears[thisYear] = math.floor(thisYearSum)
#sorted dictionary from the driest to the most rainy year
trackingYearsSorted = sorted(trackingYears.items(), key=lambda kv: kv[1])

#show one line for each individual year. put in a starting year and an end year
def yearlySum(start, end):
    end = end + 1
    for i in range(end - start):     
        matplotlib.pyplot.plot(trackingYearsDaily[start+i], label = start + i)
    matplotlib.pyplot.show()

#show the sum year by year, all time
def allTimeSum():
    matplotlib.pyplot.plot(allTimesum)
    matplotlib.pyplot.show()

#show the sum for each year individualy
def individualYearSums(start, end):
    end = end + 1
    totalYear = []
    years = []
    for i in range(end - start):
        totalYear.append(trackingYears[start+i])
        years.append(start+i)
    default_x_ticks = range(len(totalYear))
    matplotlib.pyplot.plot(default_x_ticks, totalYear)
    matplotlib.pyplot.xticks(default_x_ticks, years)
    matplotlib.pyplot.show()
        



#allTimeSum()
individualYearSums(1959, 2021)






