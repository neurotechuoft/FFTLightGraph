import serial
import time

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0')  # open serial port
    ser.dsrdtr = False
    ser.setDTR(level=False)
    print(ser.name)         # check which port was really used
    # ser.write(b'Hello')
    while True:
        print("Sent")
        ser.write('1000')     # write a string
        time.sleep(5)

    ser.close()             # close port
    print("This is bad")
