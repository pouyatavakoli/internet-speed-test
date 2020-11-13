# internet-speed-test
this is a simple code for testing your download and upload speed and it can also check your ping

python has lots of libraries for different purposes One library is speedtest-cli. This library is a command-line interface for testing internet bandwidth using speedtest.net

**here we have 2 ways wich you can check your internet speed with them . for using the script you should install the package using this toturial:**

**Installation :**

This module does not come built-in with Python. To install it type the below command in the terminal.

pip install speedtest-cli

After installing the above package one can check if the package is installed correctly or not by doing the version check. The version of the package can be checked using the following command

speedtest-cli --version

**Speedtest-cli Package :**

Speedtest-cli is a module that is used in the command-line interface for testing internet bandwidth using speedtest.net. To get the speed in the megabits type the below command in the terminal.

speedtest-cli

The above command gives the speed test result is in Megabits. To get the result in Bytes we can use the following command.

speedtest-cli --bytes

The pictorial version of your speed test result can also be retrieved using this module. To do the same type the below command in the terminal.

speedtest-cli --share

It returns a link on which we can visit on our browser and see the graphical representation of various kinds of our internet speed.

To print a simpler version of the speed test result containing only Ping, Download & Upload results instead of detailed output.

speedtest-cli --simple
