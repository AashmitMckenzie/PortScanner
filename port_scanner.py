import socket

# Function to scan a specific port
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    s.close()
    return result == 0

# List of commonly used ports
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}

# Get user input
ip = input("Enter target IP address: ")

print(f"\nScanning common ports on {ip}...\n")

# Scan only relevant ports
for port, service in common_ports.items():
    if scan_port(ip, port):
        print(f"Port {port} ({service}): OPEN")
    else:
        print(f"Port {port} ({service}): CLOSED")
