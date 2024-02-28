# 0x07. Networking basics #0

## The OSI model

The OSI model is conceptual model that provides common basis for the coordination of standards development for the purpose of system interconnection.

The communication between systems is divided into seven different abstraction layers:

    1. Physical layer
    2. Data Link layer
    3. Network layer
    4. Transport layer
    5. Session layer
    6. Presentation layer
    7. Application layer

It is organized from the highest to the lowest level.

## LAN

The Local Area Network (LAN) is a network that connects computers within a limited area.

The following are some of the uses of LAN:

    - File sharing
    - Printer sharing
    - Internet access sharing
    - Email and messaging
    - Network gaming

## WAN

This is a computer network that covers a broad area, typically spanning to multiple geographic locations.

The following are some of its uses:

    - Interconnecting branch offices
    - remote access
    - internet connectivity 
    - wide area file sharing
    - unifies comminication
    - disaster recovery and data replication
  
## IP Address

A unique number that identifies each device connected to a computer network that uses the Internet Protocol for communication.

### Types of IP Addresses

There are two most well-known types of IP address:

    1. IPV4
        This type of addresses consist of four sets of numbers separated by periods, for example, 192.168.1.1.
        Each set can range from 0 to 255.

    2. IPV6
        This type of addresses are much longer than IPv4 addresses and are represented as eight groups of hexadecimal numbers separated by colons, for example, 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
        IPv6 addresses were introduced to address the limitations of IPv4, particularly the exhaustion of available IPv4 addresses. 

## Localhost

This is a loopback network that typically points back to itself.

## Subnet

This is a division of IP addresses into smaller, more manageable parts.

## Data Transfer Protocols

There are two common data transfer protocols used in the Internet Protocol:

    1. Transmission Control Protocol
 
       This is connection control protocol that ensures data packets are transfered in sequence and lost/corrupted packets are retransmitted.
 
    2. User Datagram Protocol
 
       This is a connection-less protocol that transfers packets from one device to the other.

## Ports

This is a virtual communication endpoint that allows application/services to communicate with each other in a network.

### Common ports

- HTTP (web traffic) - port 80
- HTTPS (secure web traffic) - port 443
- Secure Shell - port 22

## Internet Control Message Protocol

This is a protocol used to send error, control and information messages between network devices.
