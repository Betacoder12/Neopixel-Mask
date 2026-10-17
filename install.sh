#!/usr/bin/env bash
# Sets up the LED mask project on a Raspberry Pi.
# Run it from the project folder:  bash install.sh
set -e

echo "Installing system packages..."
sudo apt update
sudo apt install -y git python3-venv python3-pip build-essential python3-dev swig liblgpio-dev

echo "Creating virtual environment in ./venv ..."
python3 -m venv venv

echo "Installing Python libraries..."
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt
./venv/bin/python -m pip install --force-reinstall adafruit-blinka

echo
echo "Done. NeoPixel code needs root, so run scripts with sudo and the venv's Python:"
echo "  sudo ./venv/bin/python led_test.py"
echo
echo "If the strip misbehaves on GPIO18, turn off onboard audio:"
echo "  set dtparam=audio=off in /boot/firmware/config.txt, then reboot."
