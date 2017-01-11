# TideTimes
Simple Python script to get tide times for any UK location and report the next high tide and low tide on demand.

Install dependancies:

```pip install requests```

```pip install bs4```
    
To configure:

```cp config.py.example config.py```

```nano config.py```

Edit the *URL* and *LOCATION* variables. *URL* should point to the [Met Office tide times page](http://www.metoffice.gov.uk/public/weather/tide-times) for your location and *LOCATION* should point to your local installation directory.

In this example the *URL* is set to Sandown Beach on the Isle of Wight and *LOCATION* is `/home/hass/TideTimes` (so the script may intergrate with [Home Assistant](https://home-assistant.io/)).

To get started:

Set up a cronjob `crontab -e` at 06:00 (as Met Office does not update website at exactly midnight) to grab new tide times for the day ahead:

```0 6 * * * /usr/bin/python /home/hass/TideTimes/tides.py```

Test it! Run `python tideupdate.py` and check for an output like this:

```
Tide Times Location: Sandown (Beach)
Next High Tide: 22:34
Next High Tide Height: 4.1
Next Low Tide: 04:11
Next Low Tide Height: 0.8
```

## Intergration with Home Assistant

Home Assistant is an amazing, open source, home automation platform. If you're into home automation and own a few devices you should think about linking them together inside [Home Assistant](https://home-assistant.io/)!

Here's how TideTimes looks inside Home Assistant:

<img src="https://raw.githubusercontent.com/imikerussell/TideTimes/master/tidetimes.png" width="441" alt="TideTimes works with Home Assistant">

Example sensor setup (using the [Command Line sensor](https://home-assistant.io/components/sensor.command_line/) from Home Assistant):

```
- platform: command_line
  name: Tide Times Location
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Tide Times Location:' | sed 's/^.*: //'"

- platform: command_line
  name: High Tide Time
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Next High Tide:' | sed 's/^.*: //'"

- platform: command_line
  name: High Tide Height
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Next High Tide Height:' | sed 's/^.*: //'"
  unit_of_measurement: "m"

- platform: command_line
  name: Low Tide Time
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Next Low Tide:' | sed 's/^.*: //'"

- platform: command_line
  name: Low Tide Height
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Next Low Tide Height:' | sed 's/^.*: //'"
  unit_of_measurement: "m"
```

Example group (to get the sensors in a box of their own):

```
Tide Times:
  - sensor.tide_times_loaction
  - sensor.high_tide_time
  - sensor.high_tide_height
  - sensor.low_tide_time
  - sensor.low_tide_height
```

Example customize (for cool icons):

```
sensor.tide_times_loaction:
  icon: mdi:fish

sensor.high_tide_time:
  icon: mdi:flag-variant

sensor.high_tide_height:
  icon: mdi:elevation-rise

sensor.low_tide_time:
  icon: mdi:flag-outline-variant

sensor.low_tide_height:
  icon: mdi:elevation-decline
```
