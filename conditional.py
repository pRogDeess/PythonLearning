def whatIsTheWeather(weather, rating):
    if weather == "snowing":
        print("Snowing")
        if rating > 2:
            print("happy")
        else:
            print("sad")
    elif weather == "sunny" and rating > 2:
        print("Sunny")
    elif weather == "sunny" or rating == 1:
        print("sunny but sad")
    else:
        print("Else case")

# whatIsTheWeather("sunny")
# whatIsTheWeather("snowing")
weather = input("What is the weather today?")
rating = int (input("How is your day from 1-5"))
print(type(rating))
whatIsTheWeather(weather, rating)