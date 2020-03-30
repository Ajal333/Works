import Tkinter, json, requests, sys , webbrowser
from functools import partial

def browser(location) :
    webbrowser.open('https://www.google.com/search?safe=off&sxsrf=ALeKk013Uywv2GcTNiMhhs5RkTyyyBwtZw%3A1585554787221&ei=Y6WBXvuGDdSCyAPDm5TABg&q=weather+{}'.format(location))

def weather(label_result,inputValue) :

    location = (inputValue.get())
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=a1595a21bdd184196d3b23e71546a6be'%(location)
    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)

    w = weatherData['weather']
    w1 = weatherData['main']
    w_wind = weatherData['wind']
    #print('Current weather in %s:' % (location))
    #print("{0} - {1}.".format(w[0]['main'], w[0]['description']))
    #print("Temperature - {0} Centigrede.\nHumidity - {1}%.".format((w1['temp']-273.15), w1['humidity']))
    #print("Wind speed - {0} m/sec.".format(w_wind['speed']))

    str1 = 'Current weather in %s:' % (location)
    str2 = "{0} - {1}.".format(w[0]['main'], w[0]['description'])
    str3 = "Temperature - {0} Centigrede.\nHumidity - {1}%.".format((w1['temp']-273.15), w1['humidity'])
    str4 = "Wind speed - {0} m/sec.".format(w_wind['speed'])

    quote = '{0}\n{1}\n{2}\n{3}.'.format(str1,str2,str3,str4)
    label_result.config(text = quote)

    browser_open = partial(browser,location)
    submit = Tkinter.Button(root, text = "Open in Browser",activebackground="blue", command = browser_open)
    submit.grid(row = 3, column = 1)


root = Tkinter.Tk()
root.title('Weather App')
inputValue = Tkinter.StringVar()
location = Tkinter.Label(root, text = 'Location: ').grid(row = 0)

location_entry = Tkinter.Entry(root, bd = 5, textvariable = inputValue)
location_entry.grid(row = 0, column = 1)

labelResult = Tkinter.Label(root)  
  
labelResult.grid(row=4, column=1)  

weather = partial(weather,labelResult, inputValue)
submit = Tkinter.Button(root, text = "Show weather",activebackground="blue", command = weather)
submit.grid(row = 3, column = 1)

root.mainloop()