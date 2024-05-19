def collect_survey_responses():
    responses = []

    while True:
        user_input = input("Please enter your response (or 'quit' to finish): ")
        if user_input.lower() == 'quit':
            break
        response_data = {
            'response_text': user_input,
            'response_number': len(responses) + 1
        }
        responses.append(response_data)

    return responses

def print_survey_responses(responses):
    print("Survey responses:")
    for response in responses:
        print(f"Response {response['response_number']}: {response['response_text']}")

if __name__ == '__main__':
    responses = collect_survey_responses()
    print_survey_responses(responses)
