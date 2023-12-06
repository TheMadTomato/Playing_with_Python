"""
 PDU at Layer 2 are called frames. the Datalink have 2 sublayers: LLC and MAC
 LLC: Logical Link Control which involves the logical part of the link such as flow control, error checking,
      and frame synchronization.
 MAC: Media Access Control which involves the physical part of the link such as the topology,
      the transmission technique, and the physical addressing.

 The DataFrame is a class that emulate the DataFrame of the Datalink Layer
"""
import random
import binascii
class DataFrame:
    def __init__(self, source, destination, data):
        self.source = source.zfill(6) # ensure that the source is 6 bytes long
        self.destination = destination.zfill(6) # ensure that the destination is 6 bytes long
        self.data = data

    def size_check(self):
        # check if the size of a frame is greater than 1500 return it's a giant
        # if it's less than 64 return it's a runt
        if len(self.data) > 1500:
            return "Giant"
        elif len(self.data) < 64:
            return "Runt"
        else:
            return "Normal"
    def make_header(self):
        # The header is the source and destination & is the first 2 bytes of the frame
        return f"{self.source} -> {self.destination}"
    def type_and_lenght(self):
        # The type and lenght is the type of the frame and the lenght of the data
        return f"Type: {type(self.data)} Lenght: {len(self.data)}"

    def fcs(self):
        # The FCS is the Frame Check Sequence, it is a CRC-32 checksum
        data_bytes = self.data.encode('utf-8')
        checksum = binascii.crc32(data_bytes)
        return checksum

    def check_fcs(self, fcs):
        # Decrypt the FCS
        data_bytes = self.data.encode('utf-8')
        checksum = binascii.crc32(data_bytes)
        if checksum == fcs:
            return True
        else:
            return False


def random_mac():
    # Random mac address generator
    return ":".join("{:02x}".format(random.randint(0, 255)) for _ in range(6))
def main():
    mac1, mac2 = random_mac(), random_mac()
    # Create a frame
    frame = DataFrame(mac1, mac2, "Hello World")
    # Print the size
    print("Size: ")
    print(frame.size_check())
    # Print the header
    print("Header: ")
    print(frame.make_header())
    # Print the type and lenght
    print("Type and lenght: ")
    print(frame.type_and_lenght())
    # Print the data
    print("Payload: ")
    print(frame.data)
    # Print the FCS
    print("Trailer: ")
    print(frame.fcs())
    # Decrypt the FCS
    print("FCS Check: ")
    print(frame.check_fcs(frame.fcs()))
# test
main()