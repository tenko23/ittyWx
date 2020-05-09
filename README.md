# ittyWx
Internet Weather for Teletype


This readme will help you get started with the ittyWx - Internet Weather for Teletype!  ittyWx will allow you to get near real time weather alerts & bulletins from the National Weather Service API server, printed straight onto your Teletype!

These python scripts have been written to run on a Raspberry Pi - connected to a Volpe USB-Teletype (v2) board, with or without a 5v power relay.  This script may also run on other CPUs with Python... v2.7.16 and above.  Please keep all files in one folder, in order for everything to work properly.

What you will need to do first, in order to use the ittyWx script:


1 - You will need a National Weather Service API key.  not having a key will cause IP blocks - and signing up is free!  You can register for your key here:

https://api.data.gov/signup/

...and please do not share your key with anyone - it is only for you.  With this key, you can make up to 1,000 data requests per hour with the Weather Service, without restrictions nor daily limits.  Once you have your key, please enter it in the requests.auth script - line 6, between the second set of quotation marks.


2 - Find the location that you want to receive alerts from... it can either be a county or a state.

*For counties, it will be in the form of a code - three numbers and three letters.  To find the code, please look here:

https://alerts.weather.gov/

...scroll down, find the state you want, click on the "counties" link to the right and that will lead you to the counties page for that state.  Next, find the county / county code, copy/paste the code in the following two locations:

A - In ittyWx.py , paste it at the end of the link on line 40 (replacing the code that's already there), before the end of the first set of quotation marks.

B - In requests.auth , paste it at the end of the link on line 3 (replacing the code that's already there), before the end of the quotation marks.

Last, make sure line 41 in the ittyWx.py script is commented out.  To comment out a line (in other words, make it inactive), add a pound sign ( # ) at the beginning of the line.

*For statewide alerts, it's a simple as putting in the two-letter state abbreviation for that state (instead of the county code) - and the following below:

i - Follow most of step A (above), except the line you will use will be 41 in the ittyWx.py script (uncommenting, if needed - removing the # at the beginning of the line, along with adding the proper two-letter state abbreviation at the end of the link).  Also, comment out line 40.

ii - Copy the entire link between the first set of quotation marks on line 41, in the ittyWx.py script and paste it - replacing the entire link between the quotation marks on line 3, in the requests.auth script.


3 - Please make sure your Volpe board serial address is correct.

To check, open Terminal and type:

dmesg | grep tty

...you should see something similar to: "ttyACM0: USB ACM device" within the outputted text.  ttyACM0 or ttyACM1, etc. - whatever it may be, is the correct address.  Please verify that the address on line 3 of the TT_port.py script (entered right after /dev/ ) matches.  The default address ttyACM0 .


4 - These scripts are made to work with a single 5v power relay board.  To make things work, please make sure you follow the directions for your setup below:

If you have a relay - Please make sure the GPIO pin number is correct on line 6 in the RelayOn.py script and on line 8 in the RelayOff.py script.

If you do not have a relay - Please comment out lines 7, 8, 106, 107, 114, 115, 116, 117 and 118 in the ittyWx.py script.  You will have to have your Teletype on, in order to receive bulletins as they come along.


With this, you should be all ready to go!

*The README.md and _config.yml files - after download, may be deleted... these are extra github files that are unnecessary.

*if you downloaded the script(s) prior to May 5th, 2020, you will need to download the itty.py script again.  A critical fix has been made.



Fun facts/ more info:

*ittyWx.py is the main script to run, to get weather bulletins... the other files are support files.

*With a web scrape at every 3.7 seconds, it will keep you below the 1,000/hour threshold with the NWS (as long as you have an API key registered with them).  To decrease the frequency of scrapes, increase the number in parentheses on line 120 - in the ittyWx.py script, to anything above 3.7 (in minutes).

*This script will automatically back off of the frequency of requests - for a time, if a variety of network error codes are received.

*The script has a coded-in garbage collector.  With constant running, the small RAM space on some Raspberry Pis can get bogged down pretty fast - thus, the garbage collector freeing up a bit of space every 45 minutes.  If your Raspberry Pi begins to become unresponsive after running this script for a time - or if you get an error that the script was expecting something but instead got something else (numbers), it might be worth increasing the frequency of collection.  This will be a lower number (in minutes) on line 24, in the ittyWx.py script (current default is 30 minutes).

*The alert bell system:  10 bells for a Warning; 5 for a Watch; and 4 for an Advisory, statement or anything else.

*The format of the bulletins have been coded to look almost exactly how they originally appeared on the old Weather Service wire back in the day!

*The script will only print each new alert received only once.

*With a 5v power relay tied in with your Teletype setup (and depending on the setup), this script will automatically turn on your Teletype before and off after a weather alert/bulletin is received/printed.

*Do not change the requests.auth script anymore than what is described above.  This API key script is very picky and may not work / may cause IP blocks, if changed in any other way.

*This software is free to use... but please do consider a donation for the development of this software (and for any potential future software development geared towards Teletype).  Also, if any bugs are found, please contact me.

*A special thank you to Faizan Mustafa for patiently working with me on the whole bit and getting these scripts exactly right, without even having a Teletype to test them on (Faizan)!


ittyWx (Internet Weather for Teletype)
-tenko23
GNU GPLv3
