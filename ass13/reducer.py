import sys

temperature_sum = 0
temperature_count = 0
dewpoint_sum = 0
dewpoint_count = 0
windspeed_sum = 0
windspeed_count = 0

for line in sys.stdin:
    line = line.strip() # to remove trailing whitespace
    
    key, value = line.split('\t', 1)  # key-value split
    
    # updates sum and count based on the key
    if key == 'temperature':
        temperature_sum += float(value)
        temperature_count += 1
    elif key == 'dewpoint':
        dewpoint_sum += float(value)
        dewpoint_count += 1
    elif key == 'windspeed':
        windspeed_sum += float(value)
        windspeed_count += 1

average_temperature = temperature_sum / temperature_count if temperature_count > 0 else 0
average_dewpoint = dewpoint_sum / dewpoint_count if dewpoint_count > 0 else 0
average_windspeed = windspeed_sum / windspeed_count if windspeed_count > 0 else 0

print('Average Temperature:', average_temperature)
print('Average Dew Point:', average_dewpoint)
print('Average Wind Speed:', average_windspeed)
