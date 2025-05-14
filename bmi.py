def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("bmi = " + str(bmi))
    if bmi < 18.5:
        print("You are underweighttttt")
    if bmi > 18.5 and bmi < 25:
        print("You are normalll YAAHH")
    if bmi > 25:
        print("You are overweightttt NOOOO")
calculate_bmi(weight=57, height=1.73)