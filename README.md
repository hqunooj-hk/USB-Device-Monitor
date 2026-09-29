# USB Device Monitor

## Project Overview

This project is a Python-based USB Device Monitor that detects USB device connection and disconnection events.

The monitor continuously checks connected USB devices and displays their Vendor ID and Product ID when a device is connected or disconnected.

## Features

* Detects USB device connections
* Detects USB device disconnections
* Displays Vendor ID and Product ID
* Continuously monitors USB devices
* Saves monitoring output to a log file
* Provides test evidence of detected USB events

## Technologies Used

* Python 3.11.1
* PyUSB
* libusb

## Project Structure

```text
USB-Device-Monitor/
├── README.md
├── src/
│   └── usb_monitor.py
├── screenshots/
├── logs/
│   └── output.log
└── evidence/
    └── sample_data.txt
```

## How to Run

Open Command Prompt in the project directory:

```cmd
cd C:\Users\Lenovo\Desktop\USB-Device-Monitor
```

Run the monitor:

```cmd
python src\usb_monitor.py
```

The program will start monitoring USB devices.

To stop the monitor:

```text
Ctrl + C
```

## Logging

To save the monitoring output into a log file:

```cmd
python -u src\usb_monitor.py > logs\output.log
```

## Sample Output

```text
USB Device Monitor Started...
Monitoring USB devices...
Press Ctrl+C to stop.

[CONNECTED] Vendor ID: 22d9, Product ID: 2764
[DISCONNECTED] Vendor ID: 22d9, Product ID: 2764
[CONNECTED] Vendor ID: 22d9, Product ID: 2764
```

## Test Result

The USB Device Monitor successfully detected USB device connection and disconnection events during testing.

The test device was identified using:

* Vendor ID: `22d9`
* Product ID: `2764`

## Evidence

Test evidence is available in:

```text
evidence/sample_data.txt
```

Monitoring logs are available in:

```text
logs/output.log
```

Screenshots demonstrating the project setup and working output are stored in:

```text
screenshots/
```

## Note

This implementation was tested on Windows using PyUSB with the libusb backend.
