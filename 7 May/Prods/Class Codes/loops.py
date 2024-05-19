class loops_demo:
    emp_list = [1, 2, 3, 4, 5]
    def for_loop(self):
        for num in range(1, 10):
            print(num, end=' ')

    def for_loop_in_list(self):
        for num in self.emp_list:
            print(num, end=' ')

    def while_loop(self):
        num = 1
        while num < 10:
            print(num, end=' ')
            num += 1

    def task_1(self):
        for num in range(15, 0, -2):
            print(num, end=', ')

    def task_2(self):
        temp = 1
        while temp <= 7:
            if temp > 5:
                break
            print('Hey ', temp)
            temp += 1

    def task_3(self):
        temp = 1
        while temp <= 5:
            print('loop is working')
            if temp > 3:
                temp += 1
                continue
            print('Hey ', temp)
            temp += 1
    def insurance(self):
        cart = (10, 20 , 30, 800, 500, 700, 900)
        for item in cart:
            if item > 500:
                print(f"You are eligible for insurance for {item}")
                continue
            print(f"Processing item without insurance: {item}")


if __name__ == '__main__':
    object = loops_demo()
    # object.for_loop()
    # print()
    # object.for_loop_in_list()
    # print()
    # object.while_loop()
    # print()
    # object.task_1()
    # print()
    # object.task_2()
    # print()
    # object.task_3()
    object.insurance()

