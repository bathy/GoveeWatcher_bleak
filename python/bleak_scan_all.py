import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover(timeout=10, return_adv=True)
    for key in devices:
        print(key, devices[key])
      
asyncio.run(main())
