#Import libraries
from machine import Pin, I2C
import ssd1306
import dht
import time

#Set constants
SENSOR = dht.DHT11(Pin(12))
BUTTON = Pin(13, Pin.IN, Pin.PULL_UP)
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

def readings(sensor):
    #Function to get temperature and humidity readings
    #Will also convert Celcius to Farenheight
    sensor.measure()
    humidity = sensor.humidity()
    temperature = sensor.temperature()
    temp = round(temperature * 9/5 + 32)
    temperature = 'Temperature: ' + str(round(temperature * 9/5 + 32))
    humidity = 'Humidity: ' + str(humidity)
    return humidity, temperature, temp

def button_push():
    #Resetting the counter with button push
    global counter
    if counter == 0:
        counter = 1
    elif counter == 1 or counter == 2:
        counter =0
    #Sleep function helps reduce the button bouncing effect, more accurate reading per push
    time.sleep(.5)
    
def weather_advice(temp):
    saying = ''
    lines = 1
    if temp < 50:
        saying = 'I am dead'
    elif temp > 49 and temp < 66:
        saying = 'Turn on the heater!'
        lines = 2
    elif temp > 65 and temp <75:
        saying = 'Perfect Temp!'
    elif temp > 75 and temp < 85:
        saying = 'Time for AC'
    elif temp >= 85:
        saying = 'AC OR DEATH'
    return saying, lines

    
display.fill(0)
display.show()


counter = 0

while True:
    #Simple way to track which state the script is in. 
    # 0 == Off
    # 1 == button was just pressed and the reading will be generated
    # 2 == reading was generated and is displayed, currently waiting until next push to be done
    if BUTTON.value() == 0:
        button_push()
    if counter == 1:
        try:
            humidity, temperature, temp = readings(SENSOR)
            display.fill(0)
            display.show()
            #Minimal vertical spacing between lines with readability is 8 pixels
            display.text('Environment', 0, 0, 1)
            display.text(temperature, 0, 16, 1)
            display.text(humidity, 0, 24, 1)
            saying, lines = weather_advice(temp)
            if lines == 1:
                display.text(saying, 0, 32, 1)
            elif lines == 2:
                display.text(saying[:7], 0, 32, 1)
                display.text(saying[8:], 0, 40, 1)
            display.show()
            counter = 2

        except:
            display.text('Environment', 0, 0, 1)
            display.text('Getting info...', 0,16,1)
            display.show()
            time.sleep(2)

    elif counter == 0:
        display.fill(0)
        display.show()



