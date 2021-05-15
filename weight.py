import csv
from collections import Counter

with open("heightWeight.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)
    weight_data = []
    sum_of_weight = 0
    mode_of_weight = 0

    #weight
    for i in range(len(file_data)):
        weight = file_data[i][2]
        weight_data.append(float(weight))

    #Mean
    for w in weight_data:
        sum_of_weight += w

    length_of_weight = len(weight_data)
    mean_of_weight = sum_of_weight/length_of_weight
    #print("Mean(Average) is -> " + str(mean_of_weight))

    #Median
    weight_data.sort()

    if(length_of_weight %2 == 0):
        middle_1 = weight_data[int(length_of_weight/2)]
        middle_2 = weight_data[int(length_of_weight/2 - 1)]

        median = (middle_1 + middle_2)/2
        #print("Median is -> " + str(median))
    else:
        median = weight_data[int(length_of_weight/2)]
        #print("Median is -> " + str(median))

    #Mode
    dictionary = Counter(weight_data).items()
    mode_data = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0
    }
    for weight, occurence in dictionary:
        if(75 < float(weight) < 85):
            mode_data["75-85"] += occurence
        elif(85 <= float(weight) < 95):
            mode_data["85-95"] += occurence
        elif(95 <= float(weight) < 105):
            mode_data["95-105"] += occurence
        elif(105 <= float(weight) < 115):
            mode_data["105-115"] += occurence
        elif(115 <= float(weight) < 125):
            mode_data["115-125"] += occurence
        elif(125 <= float(weight) < 135):
            mode_data["125-135"] += occurence
        elif(135 <= float(weight) < 145):
            mode_data["135-145"] += occurence
        elif(145 <= float(weight) < 155):
            mode_data["145-155"] += occurence
        elif(155 <= float(weight) < 165):
            mode_data["155-165"] += occurence
        elif(165 <= float(weight) < 175):
            mode_data["165-175"] += occurence
    mode_range = 0
    mode_occurence = 0
    
    for weight_range, occurence in mode_data.items():
        if(occurence > mode_occurence):
            mode_range = [
                int(weight_range.split("-")[0]),
                int(weight_range.split("-")[1]),
                
            ]
            mode_of_weight = (mode_range[0] + mode_range[1])/2
    print(mode_of_weight)  