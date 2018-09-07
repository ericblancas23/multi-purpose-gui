from rapidconnect import RapidConnect
import sys

def weather(city):
    rapid = RapidConnect("default-application_59bbda2be4b0b0cacf7c7995",
                     "db4efe57-20a5-4f2d-966c-b292a14a8695")

    result = rapid.call('YahooWeatherAPI', 'getWeatherForecast', {'location': city})


    desc = result["query"]["results"]["channel"]["item"]["condition"]["temp"]
    temp = result["query"]["results"]["channel"]["item"]["condition"]["temp"]

    print "I'ts" + desc + "in {}, with a temperature of {} Farenheit".format(city.capitalize(), temp)
    sys.stdout.flush()