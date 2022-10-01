import time


def countdown(decor):
    def three_second():
        for i in range(1, 4):
            print(i)
            time.sleep(1)
        print(decor())

        return decor()
    return three_second

@countdown
def main():
    current_time = time.strftime('%H:%M')
    return current_time

main()


