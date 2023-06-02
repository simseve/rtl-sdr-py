from rtlsdr import RtlSdr

# Get a list of detected device serial numbers (str)
serial_numbers = RtlSdr.get_device_serial_addresses()


print(serial_numbers)
# # Find the device index for a given serial number
device_index = RtlSdr.get_device_index_by_serial('00000001')

sdr = RtlSdr(device_index)


# # Or pass the serial number directly:
# sdr = RtlSdr(serial_number='00000001')