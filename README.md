# TideTimes
Simple Python script to get tide times for any UK location and report the next high tide and low tide on demand.

Install dependancies:

```pip install bs4```
    
To configure:

```nano tides.py```

Edit the *URL* and *LOCATION* variables. *URL* should point to the [Met Office tide times page](http://www.metoffice.gov.uk/public/weather/tide-times) for your location and *LOCATION* should point to your local installation directory.

In this example the *URL* is set to Ventnor on the Isle of Wight and *LOCATION* is `/home/hass/TideTimes` (so the script may intergrate with [Home Assistant](https://home-assistant.io/)).

To get started:

Set up a cronjob `crontab -e` for a minute after midnight to grab new tide times for the day ahead:

```1 0 * * * * /usr/bin/python /home/hass/TideTimes/tides.py```

Test it! Run `python tideupdate.py` and check for an output like this:

```
Next High Tide: 03:18
Next High Tide Height: 3.7
Next Low Tide: 20:08
Next Low Tide Height: 1.2
```
