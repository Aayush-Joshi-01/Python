def find_pages_with_long_visit_duration(traffic_data):
    visit_duration_threshold = 5 * 60  # 5 minutes in seconds
    long_visits = [visit for visit in traffic_data if visit['duration'] > visit_duration_threshold]
    unique_pages = {visit['page'] for visit in long_visits}
    return unique_pages


if __name__ == '__main__':
    traffic_data = [
        {'user': 'user1', 'page': 'page1', 'duration': 300},
        {'user': 'user2', 'page': 'page2', 'duration': 420},
        {'user': 'user3', 'page': 'page1', 'duration': 360},
        {'user': 'user4', 'page': 'page3', 'duration': 180},
        {'user': 'user5', 'page': 'page2', 'duration': 480},
    ]
    unique_pages = find_pages_with_long_visit_duration(traffic_data)
    print(unique_pages)
