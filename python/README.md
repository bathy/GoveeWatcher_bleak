# Govee Watcher with Bleak (Python)

The original code by [Thrilleratplay](https://github.com/Thrilleratplay/GoveeWatcher) used [Bleson](https://github.com/TheCellule/python-bleson), which doesn't work well for me, so I changed it to [Bleak](https://bleak.readthedocs.io/en/latest/)

Also added support for Govee H5104, so it works with both Govee H5075 and H5104

*NOTE*: Tested on Linux and Windows 11

## Requirements
  * Python 3.7+
  * sudo privileges
  * Bleak library


## Install
Clone or download this repo.
```shell
  sudo pip3 install bleak
```
or on win 11 terminal
```shell
  python -m pip install bleak
```

## Usage
In a terminal:
```shell
  sudo python bleak_scan_all.py
```
or on win 11 terminal

```shell
  python bleak_scan_all.py
```

This will list all your device, find yours and add them to watcher_with_bleak.py

```shell
  sudo python watcher_with_bleak.py
```
or on win 11 terminal

```shell
  python watcher_with_bleak.py
```
