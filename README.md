### Weather Application

A web app that I built with the aid of Pretty Printed's Youtube tutorial. I decided to use my own
CSS because I didn't want to just copy and paste code. This app was built using Flask, a Python
Framework, that connects to the OpenWeatherMap API. It has the basic function of most weather app's.


## Here's how it works

The user inputs the name of the city they wish to search. Upon clicking 'submit', the city is cross-referenced with the names of cities in the sqlite database. If the user has already successfully submitted that city, they receive a friendly pop-up notification. That notification comes from Bulma.io (a CSS framework I used to bring in for a better User Experience). 

If that city has not been added by the user yet, the app connects to the API to get the weather data. OpenWeatherMap.org has a lot of weather-based information, so I had to create a Python dictionary that would limit and hold only the information I wanted to collect. That data is then pulled and dropped into the web page and added to the user's database.