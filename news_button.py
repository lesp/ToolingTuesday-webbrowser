from gpiozero import Button
from signal import pause
import webbrowser

def news():
    webbrowser.open_new_tab("http://news.bbc.co.uk")

button = Button(17)

button.when_pressed = news

pause()
