def display_vehicles(vehicles):
    for vehicle in vehicles:
        print(f"Type: {vehicle['type']}, Model: {vehicle['model']}, Status: {vehicle['status']}")


def update_vehicle_status(vehicles, vehicle_id, new_status):
    for vehicle in vehicles:
        if vehicle['model'] == vehicle_id:
            vehicle['status'] = new_status
            break


def remove_vehicle(vehicles, vehicle_id):
    for i, vehicle in enumerate(vehicles):
        if vehicle['model'] == vehicle_id:
            del vehicles[i]
            break


if __name__ == '__main__':
    vehicles = [
        {'type': 'Car', 'model': 'Tesla Model S', 'status': 'Available'},
        {'type': 'Van', 'model': 'Ford Transit', 'status': 'On Delivery'},
        {'type': 'Truck', 'model': 'Volvo FH16', 'status': 'Under Maintenance'},
        {'type': 'Car', 'model': 'BMW i3', 'status': 'Available'},
    ]
    display_vehicles(vehicles)
    update_vehicle_status(vehicles, 'Volvo FH16', 'Available')
    remove_vehicle(vehicles, 'Tesla Model S')
    print("Updated fleet:")
    display_vehicles(vehicles)