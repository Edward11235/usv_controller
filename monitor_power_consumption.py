import glob

def find_hwmon_path(base_path="/sys/bus/i2c/drivers/ina3221/1-0040"):
    # Dynamically find the hwmon path for the INA3221 device
    hwmon_paths = glob.glob(f"{base_path}/hwmon/hwmon*")
    if hwmon_paths:
        return hwmon_paths[0]  # Assuming only one match is found
    else:
        return None

def read_ina3221_channel(channel_name):
    hwmon_path = find_hwmon_path()
    if hwmon_path is None:
        print("INA3221 device not found.")
        return
    
    try:
        # Construct file paths
        voltage_path = f"{hwmon_path}/in{channel_name}_input"
        current_path = f"{hwmon_path}/curr{channel_name}_input"
        
        # Read voltage and current
        with open(voltage_path, 'r') as file:
            voltage = int(file.read().strip()) / 1000.0  # Convert millivolts to volts
        
        with open(current_path, 'r') as file:
            current = int(file.read().strip()) / 1000.0  # Convert milliamps to amps
        
        print(f"Channel {channel_name} Voltage: {voltage}V, Current: {current}A")
    
    except FileNotFoundError:
        print(f"Files for channel {channel_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage for each channel
for channel in range(1, 4):  # Channels 1 to 3
    read_ina3221_channel(channel)
