def find_top_topics(student_topic_scores):
    num_students = len(student_topic_scores)
    passing_threshold = int(num_students * 0.8)
    top_topics = set()
    for topic in student_topic_scores:
        # print(sum([student_topic_scores[topic][score] for score in student_topic_scores[topic] if student_topic_scores[topic][score] >= 80]))     #Debugging Statement
        num_passing_students = sum([1 for score in student_topic_scores[topic] if student_topic_scores[topic][score] >= 80])
        if num_passing_students >= passing_threshold:
            top_topics.add(topic)
    return top_topics

if __name__ == '__main__':
    student_topic_scores = {
        "student1": {
            "topic1": 90,
            "topic2": 70,
            "topic3": 80,
            "topic4": 90,
            "topic5": 80,
        },
        "student2": {
            "topic1": 80,
            "topic2": 60,
            "topic3": 90,
            "topic4": 70,
            "topic5": 90,
        },
        "student3": {
            "topic1": 90,
            "topic2": 80,
            "topic3": 90,
            "topic4": 60,
            "topic5": 90,
        },
        "student4": {
            "topic1": 70,
            "topic2": 90,
            "topic3": 80,
            "topic4": 90,
            "topic5": 80,
        },
        "student5": {
            "topic1": 80,
            "topic2": 70,
            "topic3": 90,
            "topic4": 90,
            "topic5": 90,
        },
    }
    top_topics = find_top_topics(student_topic_scores)
    print(top_topics)
