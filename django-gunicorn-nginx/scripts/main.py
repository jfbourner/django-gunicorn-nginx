import math
import mimetypes

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

def print_hi(name):
    if True:
       print("Its true")
    a = 10
    if a > 10:
        print("Greater than 10")
    elif a == 10:
        print("Exactly equal")
    d = ["apple",
         "orange",
         "pear"]
    e = { "Name" : "Jack",
          "Age": 1}
    print(e)
    cities = ["London", "Paris", "Tokyo", "Berlin"]
    for city in cities:
        print(city)


    # Use a
    # breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    POD_IP = os.environ.get('PYTHON_APP_V1_SERVICE_HOST','')
    ALLOWED_HOSTS = [".jackbourner.co.uk", ".localhost", ".0.0.0.0", ".127.0.0.1", "192.168.50.10",
                     ".python-app-v1", POD_IP]
    print_hi('PyCharm')
    print(ALLOWED_HOSTS)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
