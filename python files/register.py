import pymodbus
import serial
import mysql.connector
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient #initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
client= ModbusClient(method = "rtu", port="COM8",stopbits = 1, bytesize = 8, parity = 'N', baudrate= 19200)
connection = client.connect()
print (connection)
result= client.read_holding_registers(4112,1,unit= 1)
print(result)


client.close()