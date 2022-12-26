# OBS Timer Synchronization
 Allows you to read timer values from chronograph io sources into a timefile, which can be used as an OBS-Text input to syncronize and allow multiple actors to interact with the timer on your stream.
 
# Requirements:
-Python 3.10.x ; x >= 4<br>
-Python Selenium Package

# Installation:
Configure the Python Interpreter Path in OBS ("Tools" Drop-down menu, and then "Scripts" -> "Python Settings"). Load the script into OBS and create a timer.txt file. After loading the script, link the timer.txt file from your drive via the script description ("Scripts" Window, right hand side after selecting the timeSynchro script.) Generate the "view" page of your chronograph io site and paste the "view" code into the script description text box, make sure you have the timefile loaded into OBS as a Text(GDI+) source, then toggle time synchronization with the "Toggle" button. The Script will always track the first timer on the view page.
