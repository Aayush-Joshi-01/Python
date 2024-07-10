# You're developing a program to analyze website traffic.
# Write a Python function to Calculator the percentage of mobile users among all visitors given a list of user agents.

def percentage_of_mobile_users(user_agents):
    mobile_user_agents = [ua for ua in user_agents if "Mobile" in ua]
    total_user_agents = len(user_agents)
    mobile_user_agents_count = len(mobile_user_agents)
    percentage = (mobile_user_agents_count / total_user_agents) * 100
    return percentage


if __name__ == '__main__':
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.0.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    ]

    percentage = percentage_of_mobile_users(user_agents)

    print("Percentage of mobile users: ", percentage, "%")
