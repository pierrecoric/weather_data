import csv
import matplotlib.pyplot

sumPrecipitation = 0.0
allTimePrecipitation = 0.0
year = '1959'
day = '01'
counterYears = 0
newYear = []
dailySums = []
allTimesum = []

csvFile = 'marrakesh_1959_2021.csv'

with open(f'data/{csvFile}', newline='') as csvfile:
    rainReader = csv.reader(csvfile)
    for row in rainReader:
        workingYear = year
        year = row[0][0:4]
        #trigger actions when new year:
        if year > workingYear:
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

def yearlySum():
    for i in range(len(dailySums)):
        sumYear = dailySums[i][len(dailySums[i])-1]
        print(f'{i+1959} - {sumYear}')
        matplotlib.pyplot.plot(dailySums[i], label=1959 + i)
    matplotlib.pyplot.show()

def allTimeSum():
    matplotlib.pyplot.plot(allTimesum)
    matplotlib.pyplot.show()



allTimeSum()
        
