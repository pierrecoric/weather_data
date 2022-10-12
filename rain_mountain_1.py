import csv
import matplotlib.pyplot

sumPrecipitation = 0.0
year = '1959'
day = '01'
counterYears = 0
newYear = []
dailySums = []

with open('liege_1959_2021.csv', newline='') as csvfile:
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
        workingDay = day
        day = (row[0][8:10])
        #append sum for each new day:
        if day != workingDay:
            newYear.append(sumPrecipitation)

print(len(dailySums))

for i in range(len(dailySums)):
    sumYear = dailySums[i][len(dailySums[i])-1]
    print(f'{i+1959} - {sumYear}')
    matplotlib.pyplot.plot(dailySums[i], label=1959 + i)
        
#matplotlib.pyplot.legend()
#petite modification
matplotlib.pyplot.show()
        
