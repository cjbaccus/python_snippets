import psutil


def list_network_interfaces():
    interfaces = psutil.net_if_addrs()
    statuses = psutil.net_if_stats()

    for interface, addr_list in interfaces.items():
        print(f"Interface: {interface}")
        for addr in addr_list:
            print(f"  Address: {addr.address} ({addr.family.name})")

        status = statuses.get(interface)
        if status:
            print(f"  Status: {'Up' if status.isup else 'Down'}")
            print(f"  Speed: {status.speed} Mbps\n")


# Example usage
list_network_interfaces()
