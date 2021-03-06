Adafruit Python DHT Sensor Library
==================================

Python library to read the DHT series of humidity and temperature sensors on a 
Raspberry Pi or Beaglebone Black.

Designed specifically to work with the Adafruit DHT series sensors ---->
https://www.adafruit.com/products/385

Currently the library is tested with Python 2.6, 2.7, 3.3 and 3.4. It should
work with Python greater than 3.4, too.


Installing
----------

### Dependencies

For all platforms (Raspberry Pi and Beaglebone Black) make sure your system is
able to compile and download Python extensions with **pip**:

On Raspbian or Beaglebone Black's Debian/Ubuntu image you can ensure your
system is ready by running one or two of the following sets of commands:

Python 2:

````sh
sudo apt-get update
sudo apt-get install python-pip
sudo python -m pip install --upgrade pip setuptools wheel
````

Python 3:

````sh
sudo apt-get update
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
````

### Install with pip

Use `pip` to install from PyPI.

Python 2:

```sh
sudo pip install Adafruit_DHT
```

Python 3:

```sh
sudo pip3 install Adafruit_DHT
```

### Compile and install from the repository

First download the library source code from the [GitHub releases
page](https://github.com/adafruit/Adafruit_Python_DHT/releases), unzipping the
archive, and execute:

Python 2:

```sh
cd Adafruit_Python_DHT
sudo python setup.py install
```

Python 3:

```sh
cd Adafruit_Python_DHT
sudo python3 setup.py install
```

You may also git clone the repository if you want to test an unreleased
version:

```sh
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
```

Usage
-----

See example of usage in the examples folder.

Author
------

Adafruit invests time and resources providing this open source code, please
support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries.

MIT license, all text above must be included in any redistribution

Install alert and CanvasJS Dashboard
------------------------------------

Files for alert and dashboard is in "Add_mrigonnaux" folder. 

The file CanvasJS_Dashboard/index.html must be installed at the root of the web server.

The file Python/DHT22.py must be cron on your server (every hour) :
```
0 * * * * python /path_to_the_script/DHT22.py temperature >> /var/www/html/temperature.csv
0 * * * * python /path_to_the_script/DHT22.py humidity >> /var/www/html/humidity.csv
0 * * * * python /path_to_the_script/DHT22.py alert
```
You must then modify the python script to enter your sending and receiving email addresses and password. 

For more information : https://net-security.fr/non-classe/raspberry-thermometre-connecte-avec-une-sonde-dht22/
