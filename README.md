# QR Code Attendance System

## Overview

The QR Code Attendance System is a Python-based project designed to streamline attendance tracking using QR codes. This system automates the attendance process by generating and scanning QR codes, offering an efficient solution for various educational or organizational settings.

## Features

- **QR Code Generation**: Creates unique QR codes for individual attendees or participants.
- **QR Code Scanning**: Scans and records attendance by decoding QR codes using a webcam or mobile device.
- **Attendance Log**: Maintains a digital log of attendees, providing a convenient and accurate attendance record.

## Setup

Setup the development environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```
Install zbar shared library

```bash
sudo apt update
sudo apt install libzbar0
```

Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Usage

### **Generate QR Codes**

Generate unique QR codes for attendees or participants.

Create a text file named `data/attendees.txt` listing the attendees. Each line of the file represents one attendee, 
it should contain any text that uniquely identifies the person.

For example `<ID> <FULL NAME>`:

```
13983390 PEREZ GALINDO JUAN
48277105 MARTINEZ LOPEZ ANA
90541237 GOMEZ RODRIGUEZ CARLOS
31764982 HERNANDEZ CRUZ MARIA
76820541 TORRES VARGAS LUIS 
```

Use the `generate.py` script to generate an individual QR code for each attendee.

```bash
python3 ./generate.py
```

The resulting codes are stored in `data/qr`.  
Distribute the codes among the attendees.

### **Attendance Recording**

Use a webcam or mobile device to scan the QR codes and automatically record attendance.

```bash
python3 ./attend.py
```

When finished taking attendance press `s` to save the attendance data and close the camera capture window.

You can find the attendance list as a `csv` file in `data/attendance`.

## Contributions

Contributions to enhance this project are welcome! Fork this repository, propose improvements, or add new features to optimize the attendance system.

## Acknowledgments

- **Open-Source Community**: Grateful for the collaborative spirit and resources available in the open-source community.
- **Educational Institutions/Workplaces**: Acknowledgment for inspiring the development of solutions catering to attendance management needs.

## License

This project is licensed under the [MIT License]

---
