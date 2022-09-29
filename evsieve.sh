#!/usr/bin/env bash

# Run as root

set -x

event=$(grep -A2 rc0 /proc/bus/input/devices |tail -n1|sed -r 's/.*(event[0-9]+).*$/\1/')
inputdevice="/dev/input/$event"

evsieve --input "$inputdevice" --map key:%352 key:%28  --output
