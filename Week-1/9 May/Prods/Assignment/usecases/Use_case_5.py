# You're developing a customer queue management system for a service center.
# How would you use a list in Python to manage the queue and serve customers?

def add_customer(queue, customer):
    queue.append(customer)

def remove_customer(queue):
    if len(queue) > 0:
        return queue.pop(0)
    else:
        return None

def serve_customer(queue):
    customer = remove_customer(queue)
    if customer is not None:
        print(f"Now serving {customer}.")

if __name__ == '__main__':
    queue = []

    while True:
        user_input = input("Enter 'add', 'serve', or 'quit': ")
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'add':
            new_customer = input("Enter new customer: ")
            add_customer(queue, new_customer)
        elif user_input.lower() == 'serve':
            serve_customer(queue)
        else:
            print("Invalid command.")
        print(f"Queue: {queue}")
