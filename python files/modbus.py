import larsson
import pymodbus3
import serial
from pymodbus3.pdu import ModbusRequest
from pymodbus3.client.sync import ModbusSerialClient as ModbusClient
#initialize a serial RTU client instance
from pymodbus3.transaction import ModbusRtuFramer
larsson.gogo(10,'Larsson')
