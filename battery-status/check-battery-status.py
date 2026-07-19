# -----------------------------------------------------------
# demonstrates how to read the battery status using the psutil library
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

import psutil

# retrieve battery status
battery = psutil.sensors_battery()

if battery is not None:
    print(f"Battery percentage: {battery.percent:.2f} %")
    print(f"Power plugged in: {battery.power_plugged}")

    secondsLeft = battery.secsleft
    seconds = secondsLeft // 3600
    minutes = secondsLeft // 60
    hours = minutes // 60
    minutes = minutes - hours * 60
    print(f"Time left: {hours:}:{minutes:02d}:{seconds:02d}")
else:
    print("No battery information available")
