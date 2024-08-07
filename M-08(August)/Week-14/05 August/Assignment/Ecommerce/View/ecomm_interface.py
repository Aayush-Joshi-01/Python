from Routes.ecomm_urls import route

def menu():
    pass

def get_choice():
    url_choice = input("Enter the url you want to go to including /: ")
    if url_choice.strip().lower() in ['exit', 'n', 'no']:
        print("Exiting...")
        return False
    else:
        route(url_choice)
        return True


def main():
    flag = True
    menu()
    while flag:
        flag = get_choice()
        