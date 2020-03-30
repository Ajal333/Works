import json, requests, sys , webbrowser

if len(sys.argv) < 2  :
    print("Usage: python learn1.py <cityname>")
    sys.exit()

location = ''.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=a1595a21bdd184196d3b23e71546a6be'%(location)
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)

w = weatherData['weather']
w1 = weatherData['main']
w_wind = weatherData['wind']
print('Current weather in %s:' % (location))
print("{0} - {1}.".format(w[0]['main'], w[0]['description']))
print("Temperature - {0} Centigrede.\nHumidity - {1}%.".format((w1['temp']-273.15), w1['humidity']))
print("Wind speed - {0} m/sec.".format(w_wind['speed']))

print('Do you want to open the browser to show weather details? (Ctrl-c To exit) ')
choice = raw_input()

webbrowser.open('https://www.google.com/search?safe=off&sxsrf=ALeKk013Uywv2GcTNiMhhs5RkTyyyBwtZw%3A1585554787221&ei=Y6WBXvuGDdSCyAPDm5TABg&q=weather+{}'.format(location))
