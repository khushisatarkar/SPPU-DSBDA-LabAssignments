import sys

temperature_sum = 0
temperature_count = 0
dewpoint_sum = 0
dewpoint_count = 0
windspeed_sum = 0
windspeed_count = 0

for line in sys.stdin:
    line = line.strip()  # removes trailing whitespace
    
    # skips empty lines
    if not line:
        continue
    
    # splits the line into temperature, dew point, wind speed
    values = line.split(',')
    
    if len(values) != 3:
        continue
    
    try:
        temperature, dewpoint, windspeed = map(float, values)
        
        print('temperature\t{}'.format(temperature))
        print('dewpoint\t{}'.format(dewpoint))
        print('windspeed\t{}'.format(windspeed))
    except ValueError:
        continue
