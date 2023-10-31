import asyncio
import os
from bleak import BleakScanner


'''
There is a slight difference in GVH5104 and GVH5075 device, with a 2 byte offset

My 5075 devices all start with A4:C1, 5104 devices all starts with mac C6:35

Bleak (https://bleak.readthedocs.io/en/latest/) works a little better for me then the bleson used in the original implementation
'''

# find all your govee device mac address and put them here
govee_dict = {'C6:35:34:35:99:66': 1,
              'C6:35:34:35:99:77': 2,
              'C6:35:34:35:99:88': 3,
              'A4:C1:38:44:99:66': 4,
              'A4:C1:38:60:99:77': 5,
              'A4:C1:38:49:99:88': 6}

name_dict = {1: 'living room',
             2: 'attic',
             3: 'bedroom',
             4: 'kitchen',
             5: 'garage',
             6: 'office'}

info_dict = {}


def decode_info(mac, bdata):
    if mac.startswith('A4:C1:'):
        # GVH5075
        start_byte, end_byte = 2, 8
    else:
        # GVH5104
        start_byte, end_byte = 4, 10
    return ("%s--%s\tTemperature: %s°C\tHumidity: %s%%\tBattery: %s%%" %
            (govee_dict[mac], name_dict[govee_dict[mac]].ljust(15),
            format((int(bdata.hex()[start_byte:end_byte], 16) / 10000), '.2f'),
            format(((int(bdata.hex()[start_byte:end_byte], 16) % 1000) / 10), '.2f'),
            str(int(bdata.hex()[end_byte:end_byte + 2], 16))))


async def main():
    devices = await BleakScanner.discover(timeout=10, return_adv=True)
    for key in devices:
        if devices[key][0].name != None:
            if devices[key][0].name.startswith('GVH'):
                bdata = devices[key][1].manufacturer_data[60552] if key.startswith('A4:C1') else \
                    devices[key][1].manufacturer_data[1]
                info_dict[govee_dict[key]] = '\t'.join([decode_info(key, bdata), 'Signal: %sdb\n' % devices[key][1].rssi])

while True:
    asyncio.run(main())
    os.system("cls")
    for each in sorted(info_dict.items()):
        print(each[1])

