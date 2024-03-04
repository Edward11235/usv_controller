import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust as necessary
time.sleep(2)  # Allow time for serial connection to establish

try:
    while True:
        nums = []
        for i in range(4):  # Collect four integers
            while True:
                try:
                    num = int(input(f"Enter integer {i+1} (between 1000 and 2000): "))
                    if 1000 <= num <= 2000:
                        nums.append(num)
                        break
                    else:
                        print("Number must be between 1000 and 2000.")
                except ValueError:
                    print("Please enter a valid integer.")
        
        # Format message with the protocol
        message = "<[" + "][".join(map(str, nums)) + "]>"
        ser.write(message.encode())  # Send the message
        
        # Wait for and print the response from Arduino
        print("Waiting for response...")
        while ser.in_waiting == 0:
            pass
        response = ser.readline().decode().strip()
        print("Received back:", response)

except KeyboardInterrupt:
    ser.close()
