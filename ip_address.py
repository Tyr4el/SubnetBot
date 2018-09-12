import ipaddress
import random

# Generate a random IP address in the range 1.0.0.1 (?) to 223.255.254.254
random_ip = random.randrange(int(ipaddress.IPv4Address('223.255.254.254')))

# Subnet mask between 1 and 32 (31?)
mask = random.randint(0, 32)

# Get an IPv4Address object from the random integer generated on line 4
ip = ipaddress.IPv4Address(random_ip)

# Format ip_address with a random mask from 1 - 31 generated on line 5
formatted_ip_address = '{0}/{1}'.format(ip, mask)

# Get the network address of formatted_ip_address
# strict must be left at False
# returns an IPv4 Network object
ip_network = ipaddress.IPv4Network(formatted_ip_address, strict=False)

# Broadcast address of ip_network
broadcast = ip_network.broadcast_address

# Subnets of ip_network with CIDR notation
subnets = ip_network.subnets()
