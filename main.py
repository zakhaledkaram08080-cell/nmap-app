import nmap

target = input("Enter IP: ")
nm = nmap.PortScanner()
nm.scan(target, '1-1000')
for host in nm.all_hosts():
    print("Host:", host, nm[host].state())
    for proto in nm[host].all_protocols():
        ports = nm[host][proto].keys()
        for port in ports:
            print(f"Port {port}: {nm[host][proto][port]['state']}")
