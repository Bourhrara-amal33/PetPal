import smbus
import time

# I2C address of the weight sensor
SENSOR_ADDRESS = 0x2A

# Create an I2C bus object
bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi Model B

try:
    while True:
        # Read data from the weight sensor
        data = bus.read_i2c_block_data(SENSOR_ADDRESS, 0, 4) 
        weight = (data[0] << 8) | data[1]

        print(f"Weight: {weight} grams")

        # Add a delay before reading again
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    # Clean up
    bus.close()
