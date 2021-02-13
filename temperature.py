#funtion that takes a temperature as an argument and then decides if it is warm or not. 

def myTemp (temp):
    if temp < 0:
        print("It a frrezing cold", temp)
    elif 1 <= temp <= 10:
        print("It is a chilly", temp)
    elif 11 <= temp <= 18 :
        print("It is a warm", temp)
    elif temp >= 19 :
        print("It is a hot", temp)
