import pymodbus
import datetime
import pyodbc
import serial
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient #initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer
#more import dependencies
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.compat import iteritems
import logging
import sys
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
 
driver= '{SQL Server Native Client 11.0}'




try:
    deviceId=int(input("ENTER THE DEVICE ID "))
    registerStart=int(input("ENTER THE START REGISTER "))
    registerReading=int(input("ENTER THE NO OF REGISTERS TO READ "))

    client= ModbusClient(method = "rtu", port="COM8",stopbits = 1, bytesize = 8, parity = 'N', baudrate= 19200)
    

    dbRegister=registerStart
    if deviceId>1:
        registerStart=registerStart-1
    result= client.read_holding_registers(registerStart,1,unit= deviceId)
    print(result)
    vals=str(result)   
   
    count=0
    while (count < registerReading):
        
        result= client.read_holding_registers(registerStart,1,unit= deviceId)
        print(result)
        vals=str(result)   
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=CZROZWHP6063581\SQLEXPRESS;DATABASE=Register;UID=larsson;PWD=S@ftware123456')     
        cursor = conn.cursor()
        values=[deviceId,'03',dbRegister, datetime.datetime.now()]
        sqlcmd=('''
                INSERT INTO Register.dbo.LoggerTable (Device, FunctionCode, RegisterReq, LoggedTime)
                VALUES
                (?,?,?,?)
                ''')
        cursor.execute(sqlcmd,values)
        conn.commit()
        conn.close() 
        count = count + 1
        dbRegister=dbRegister+1
        registerStart=registerStart+1
       

    client.close()
except:
    print("INPUT VARIABLES ERROR")
