# Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing

## Project Overview

The Real-Time Parallel Log Aggregation Engine is a Python-based application designed to collect, process, and organize log data from multiple servers in real time. The system uses socket communication to receive logs from different locations and automatically stores them into separate binary files based on their log level.

The project demonstrates real-time log monitoring, binary file handling, socket programming, and log classification.

---

## Features

- Real-time log collection using sockets
- Parallel log aggregation
- Custom socket-based communication
- Binary log storage (.bin files)
- Automatic log classification
- Multiple city log simulation
- Binary log reader
- Easy to extend for enterprise monitoring

---

## Technologies Used

- Python 3.x
- Socket Programming
- Binary File Handling
- VS Code
- Struct Library

---

## Project Structure

```
RealTimeLogEngine/

│
├── read_binary.py
├── log_server_simulator.py
├── log_harvester_daemon.py
│
├── mumbai_WARNING.bin
├── mumbai_ERROR.bin
├── mumbai_INFO.bin
├── mumbai_DEBUG.bin
│
├── chennai_WARNING.bin
├── chennai_ERROR.bin
├── chennai_INFO.bin
├── chennai_DEBUG.bin
│
├── bangalore_WARNING.bin
├── bangalore_ERROR.bin
├── bangalore_INFO.bin
├── bangalore_DEBUG.bin
│
└── README.md
```

---

## Log Levels

### INFO

Stores normal system activities.

Examples

- Server Started
- User Login
- Backup Completed

---

### WARNING

Stores warning messages.

Examples

- High CPU Usage
- Memory Usage High
- Disk Space Low

---

### ERROR

Stores critical errors.

Examples

- Database Connection Failed
- Authentication Failed
- Socket Timeout

---

### DEBUG

Stores debugging information.

Examples

- Variable Initialized
- Thread Started
- Cache Loaded

---

## Cities Included

- Mumbai
- Chennai
- Bangalore

Each city contains four binary log files:

- WARNING
- ERROR
- INFO
- DEBUG

---

## Working Process

1. Start the Log Harvester Server.
2. Run the Log Server Simulator.
3. The simulator sends logs through sockets.
4. The harvester receives logs.
5. Logs are categorized by level.
6. Logs are stored inside binary files.
7. The Binary Reader displays stored logs.

---

## How to Run

### Step 1

Open the project folder in VS Code.

### Step 2

Run the Log Harvester.

```
python log_harvester_daemon.py
```

### Step 3

Open a new terminal.

Run

```
python log_server_simulator.py
```

### Step 4

Open another terminal.

Run

```
python read_binary.py
```

---

## Expected Output

```
Waiting for Logs...

Connected Successfully

2026-07-09 10:00:05 | Mumbai | INFO | Server Started

2026-07-09 10:00:10 | Chennai | WARNING | CPU Usage High

2026-07-09 10:00:15 | Bangalore | ERROR | Database Connection Failed
```

---

## Advantages

- Real-time monitoring
- Easy log management
- Fast log processing
- Organized binary storage
- Simple architecture
- Easy maintenance

---

## Future Enhancements

- Multi-threaded processing
- Dashboard using Flask
- Database Integration
- Email Alerts
- Cloud Log Storage
- AI-based Log Analysis
- Automatic Error Detection

---

# project output:

<img width="1186" height="709" alt="Screenshot 2026-07-10 133538" src="https://github.com/user-attachments/assets/b7826b02-fb26-48a8-a788-e08d09155030" />




## Conclusion

This project provides a simple and efficient solution for collecting and managing logs from multiple servers in real time. By using socket communication and binary file storage, the system improves log organization, enables quick monitoring, and serves as a foundation for advanced enterprise log management solutions.

---

## Author

**vijaya lakshmi K**

Bachelor of Computer Application (BCA)

Project: Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing
