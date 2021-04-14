import nmap

def default_scanner(target_ip, ports):
    nm = nmap.PortScanner()
    nm.scan(target_ip, ports)
    for host in nm.all_hosts():
        print(f'Host: {host, nm[host].hostname()}')
        print(f'State: {nm[host].state()}')
        for proto in nm[host].all_protocols():
            print('----')
            print(f'Protocol : {proto}')

            lport = nm[host][proto].keys()
            print(lport)
            for port in lport:
                print(f"port : {port} : state : {nm[host][proto][port]['state']}")

if __name__ == '__main__':
    default_scanner()