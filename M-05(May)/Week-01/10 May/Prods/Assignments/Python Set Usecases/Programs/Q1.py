def get_unique_cities(cities: list) -> list:
    return list(set(cities))


if __name__ == '__main__':
    extracted_user_cities = ['delhi', 'mumbai', 'indore', 'ujjain', 'delhi', 'dehradun', 'mumbai', 'agra', 'indore']
    print(extracted_user_cities)
    print(get_unique_cities(extracted_user_cities))
