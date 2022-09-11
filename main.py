import requests
import csv
import json

with open("data.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(("Номер", "Оператор(Изначальный)", "Оператор(Из росреестра)","Совпадение данных"))

with open("Statistics.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(("СОВПАЛИ", "НЕ СОВПАЛИ", "НЕТ ДАННЫХ","ВСЕГО"))

Matched = 0
didNotMatch = 0
noDataMatch = 0
total = 0

with open("Num_operator.csv", newline='' , encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        num = row['num']
        operD = row['operator']
        url = ("http://rosreestr.subnets.ru/?get=num&format=json&num={}".format(num))
        link = url
        responce = requests.get(link).text
        responceJson = json.loads(responce)
        key = "error"
        if key in responceJson:
            operR = "Такого номера в росреестре нет"
            dataMatch = 2
            noDataMatch += 1
            with open("data.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow((num, operD, operR, dataMatch))
        else:
         operR = responceJson['0']['operator']
         if operR == operD:
           dataMatch = 1
           Matched += 1
           with open("data.csv", "a") as file:
             writer = csv.writer(file)
             writer.writerow((num,operD,operR,dataMatch))
         else:
          dataMatch = 0
          didNotMatch += 1
          with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow((num, operD, operR, dataMatch))
total = Matched + didNotMatch + noDataMatch
with open("Statistics.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow((Matched, didNotMatch, noDataMatch,total))

print("End")