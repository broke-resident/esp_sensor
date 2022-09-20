***ESP8266 Temperature and Humidity Sensor***

An inital esp8266 sensor with a ssd1306 (0.91") OLED screen attached with some initial recommendations based on the interpreted temperature. Currently in Farenheight only. Based on Micropython.

***Libraries***

Need the ssd1306 module, simply copy and paste into a new file in your working directory and save to your device.

***Functions***

Push the button, get a reading. The DHT11 libraries can be finicky and not get a reading, if that's the case the script will keep attempting every two seconds while displaying a "working" message on screen. Push the button again to "turn off" (make blank) the screen.