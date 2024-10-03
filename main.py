import asyncio
from bleak import BleakClient
from crccheck.crc import Crc16Cms

address = "c5:cf:57:a0:f6:1f"

async def main(address):
	async with BleakClient(address) as client:
		a = bytes.fromhex('55aa01080604ed')
		crcinst = Crc16Cms()
		crcinst.process(a)
		model_number = await client.write_gatt_char("0000a040-0000-1000-8000-00805f9b34fb", a + crcinst.finalbytes())
	
asyncio.run(main(address))

# attr handle: 0x0001, end grp handle: 0x0003 uuid: 00001800-0000-1000-8000-00805f9b34fb
# attr handle: 0x0004, end grp handle: 0x0010 uuid: 0000a032-0000-1000-8000-00805f9b34fb
