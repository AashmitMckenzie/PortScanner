# Port Scanner

A lightweight Python-based network port scanner for identifying open ports on target hosts.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Project Folder Structure](#project-folder-structure)
- [Installation Guide](#installation-guide)
- [How to Run the Application](#how-to-run-the-application)
- [Usage Guide](#usage-guide)
- [Configuration](#configuration)
- [Security Considerations](#security-considerations)
- [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
- [Future Improvements / TODOs](#future-improvements--todos)
- [License](#license)

## Overview

### What the application is

Port Scanner is a command-line network reconnaissance tool that scans a predefined set of commonly used ports on a target IP address to determine which ports are open and accessible.

### What problem it solves

- **Network Security Assessment**: Helps identify open ports that may pose security risks
- **Service Discovery**: Detects running services on target hosts
- **Network Troubleshooting**: Assists in diagnosing connectivity issues
- **Educational Tool**: Provides a simple introduction to network scanning concepts

### High-level architecture

The application uses a straightforward sequential scanning approach:
1. Accepts target IP address as user input
2. Iterates through a predefined list of common ports
3. Attempts TCP connection to each port with a timeout
4. Reports port status (OPEN/CLOSED) with service identification

### Who the project is for

- **Cybersecurity Students**: Learning network scanning fundamentals
- **Network Administrators**: Quick port availability checks
- **Security Researchers**: Basic reconnaissance tasks
- **Developers**: Understanding network connectivity and port status

## Key Features

- ✅ Scans 13 commonly used ports (FTP, SSH, Telnet, SMTP, DNS, HTTP, POP3, IMAP, HTTPS, MySQL, RDP, HTTP-Alt)
- ✅ Service name identification for each port
- ✅ Fast scanning with 0.5-second timeout per port
- ✅ Simple command-line interface
- ✅ No external dependencies (uses Python standard library)
- ✅ Clear OPEN/CLOSED status reporting

## Tech Stack

- **Language**: Python 3.x
- **Core Library**: `socket` (Python Standard Library)
- **Protocol**: TCP/IP
- **Platform**: Cross-platform (Windows, Linux, macOS)

## System Architecture

```
┌─────────────────┐
│   User Input    │
│  (Target IP)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Port Scanner   │
│   Main Loop     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────┐
│  Common Ports   │─────▶│  scan_port() │
│     Dictionary  │      │   Function   │
└─────────────────┘      └──────┬───────┘
                                 │
                                 ▼
                          ┌──────────────┐
                          │ Socket API   │
                          │ (TCP Connect)│
                          └──────┬───────┘
                                 │
                                 ▼
                          ┌──────────────┐
                          │  Results     │
                          │  Display     │
                          └──────────────┘
```

**Workflow**:
1. User provides target IP address
2. Application iterates through predefined common ports
3. For each port, `scan_port()` function creates a TCP socket
4. Attempts connection with 0.5-second timeout
5. Returns connection status (success = OPEN, failure = CLOSED)
6. Results displayed with port number and service name

## Project Folder Structure

```
Port Scanner/
│
└── port_scanner.py    # Main application file
```

## Installation Guide

### Prerequisites

- Python 3.6 or higher
- No additional packages required (uses standard library only)

### Installation Steps

1. **Clone or download the project**:
   ```bash
   # If using git
   git clone <repository-url>
   cd "Port Scanner"
   
   # Or simply download port_scanner.py
   ```

2. **Verify Python installation**:
   ```bash
   python --version
   # Should show Python 3.6 or higher
   ```

3. **No additional setup required** - the application is ready to use!

## How to Run the Application

### Basic Usage

```bash
python port_scanner.py
```

### Execution Flow

1. Run the script using Python
2. Enter the target IP address when prompted
3. Wait for scan to complete (approximately 6-7 seconds for all ports)
4. Review the results showing OPEN/CLOSED status for each port

### Example Output

```
Enter target IP address: 192.168.1.1

Scanning common ports on 192.168.1.1...

Port 21 (FTP): CLOSED
Port 22 (SSH): OPEN
Port 23 (Telnet): CLOSED
Port 25 (SMTP): CLOSED
Port 53 (DNS): OPEN
Port 80 (HTTP): OPEN
Port 110 (POP3): CLOSED
Port 143 (IMAP): CLOSED
Port 443 (HTTPS): OPEN
Port 3306 (MySQL): CLOSED
Port 3389 (RDP): CLOSED
Port 8080 (HTTP-Alt): CLOSED
```

## Usage Guide

### Scanning Localhost

```bash
python port_scanner.py
# Enter: 127.0.0.1
```

### Scanning Remote Hosts

```bash
python port_scanner.py
# Enter: <target-ip-address>
```

### Scanning Your Own Network

```bash
python port_scanner.py
# Enter: 192.168.1.x (your network range)
```

### Important Notes

- **Legal Use Only**: Only scan systems you own or have explicit permission to scan
- **Network Access**: Ensure you have network connectivity to the target
- **Firewall**: Results may be affected by firewall rules on target or your machine
- **Scanning Speed**: Sequential scanning means total time = number of ports × timeout (0.5s)

## Configuration

### Port List Customization

To modify the ports being scanned, edit the `common_ports` dictionary in `port_scanner.py`:

```python
common_ports = {
    21: "FTP",
    22: "SSH",
    # Add or remove ports as needed
    8080: "HTTP-Alt",
    9000: "Custom-Service"  # Example addition
}
```

### Timeout Adjustment

Modify the timeout value in the `scan_port()` function:

```python
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Change this value (in seconds)
    # ...
```

**Recommended timeout values**:
- `0.5` - Fast scanning (default)
- `1.0` - Balanced speed/accuracy
- `2.0` - More reliable for slow networks

### No External Configuration Files

The application uses hardcoded values and does not require:
- `.env` files
- Configuration files
- External dependencies

## Security Considerations

### ⚠️ Legal and Ethical Warnings

1. **Authorization Required**: Only scan systems you own or have written permission to scan
2. **Legal Implications**: Unauthorized port scanning may be illegal in many jurisdictions
3. **Ethical Use**: Use responsibly for legitimate security testing and network administration

### Security Features

- **No Data Collection**: Application does not store or transmit scan results
- **No Persistent Connections**: Each connection is immediately closed after testing
- **Minimal Network Footprint**: Only attempts TCP handshake, no data exchange

### Best Practices

- Use on isolated test networks when learning
- Obtain proper authorization before scanning production systems
- Be aware of your organization's security policies
- Consider rate limiting for large-scale scans

### Limitations

- **No Stealth Mode**: Scans are detectable by intrusion detection systems
- **Sequential Scanning**: Not optimized for speed (can be slow for many ports)
- **Basic Detection**: Only identifies open/closed status, no service version detection

## Screenshot or GIF placeholders

```
[SCREENSHOT: Terminal showing port scanner execution]
[SCREENSHOT: Example scan results with multiple open ports]
[GIF: Animated demonstration of scanning process]
```

## Common Issues and Troubleshooting

### Issue: "Connection refused" or all ports show CLOSED

**Possible Causes**:
- Target host is down or unreachable
- Firewall blocking connections
- Network connectivity issues

**Solutions**:
- Verify target IP is correct and reachable (try `ping`)
- Check firewall settings on target and local machine
- Ensure you have network access to the target

### Issue: Script hangs or takes too long

**Possible Causes**:
- Network latency
- Firewall dropping packets silently
- Target not responding

**Solutions**:
- Reduce timeout value (may miss slow-responding ports)
- Check network connectivity
- Verify target is online

### Issue: "Name or service not known" error

**Possible Causes**:
- Invalid IP address format
- DNS resolution failure (if using hostname)

**Solutions**:
- Use IP address instead of hostname
- Verify IP address format (e.g., 192.168.1.1)
- Check DNS settings if using hostnames

### Issue: Permission denied errors

**Possible Causes**:
- Insufficient permissions on some systems
- Security software blocking socket creation

**Solutions**:
- Run with appropriate permissions (usually not required)
- Check antivirus/firewall settings
- Run from command line with proper user privileges

### Issue: Python not found

**Solutions**:
- Install Python 3.6+ from python.org
- Use `python3` instead of `python` on Linux/Mac
- Verify Python is in system PATH


## License

This project is provided as-is for educational and legitimate security testing purposes. Please ensure you have proper authorization before using this tool on any network or system.

**Disclaimer**: The authors and contributors are not responsible for any misuse of this software. Users are solely responsible for ensuring their use complies with applicable laws and regulations.

---

**Version**: 1.0  
**Last Updated**: 2024  
**Maintainer**: [Your Name/Organization]

