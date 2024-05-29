def find_unique_sensor_types(sensor_data):
    unique_sensor_types = set()
    for data in sensor_data:
        unique_sensor_types.add(data["sensor_type"])
    return unique_sensor_types


if __name__ == '__main__':
    sensor_data = [
        {"device_id": "1", "sensor_type": "temperature", "value": 23.5},
        {"device_id": "2", "sensor_type": "humidity", "value": 45.6},
        {"device_id": "3", "sensor_type": "pressure", "value": 1234.5},
        {"device_id": "4", "sensor_type": "temperature", "value": 25.3},
        {"device_id": "5", "sensor_type": "humidity", "value": 48.2},
        {"device_id": "6", "sensor_type": "pressure", "value": 1200.0},
        {"device_id": "7", "sensor_type": "temperature", "value": 27.1},
        {"device_id": "8", "sensor_type": "humidity", "value": 50.1},
        {"device_id": "9", "sensor_type": "pressure", "value": 1250.5},
    ]
    unique_sensor_types = find_unique_sensor_types(sensor_data)
    print(unique_sensor_types)
