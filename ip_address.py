import ipaddress
import random


class IPAddress:
    def __init__(self):
        # Generate a random IP address in the range 1.0.0.1 (?) to 223.255.254.254
        self.start = int(ipaddress.IPv4Address('10.0.0.1'))
        self.stop = int(ipaddress.IPv4Address('223.255.254.254'))
        self.random_ip = random.randrange(self.start, self.stop)

        # Subnet mask between 1 and 31
        self.mask = random.randint(9, 31)

        # Get an IPv4Address object from the random integer generated on line 4
        self.ip = ipaddress.IPv4Address(self.random_ip)

        # Format ip_address with a random mask from 1 - 31 generated on line 5
        self.formatted_ip_address = '{0}/{1}'.format(self.ip, self.mask)

        # Get the network address of formatted_ip_address
        # strict must be left at False
        # returns an IPv4 Network object
        self.ip_network = ipaddress.IPv4Network(self.formatted_ip_address, strict=False)

        # Broadcast address of ip_network
        self.broadcast = self.ip_network.broadcast_address

        # Subnets of ip_network with CIDR notation
        self.subnets = self.ip_network.subnets()
