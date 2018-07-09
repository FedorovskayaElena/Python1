import random
import string
import jsonpickle
import os.path
import getopt
import sys

# чтобы при вызове из командной строки было видно модуль model.contact
model_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(model_dir)
from model.group import Group


def random_string(postfix, maxlen):
    s = "".join([random.choice(string.ascii_letters + string.digits + " "*6) for i in range(random.randrange(maxlen))])
    return s + postfix


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# вначале первый реальный контакт со всеми заполненными полями, похожими на реальные данные
# затем комбинации пустых/заполненых полей (по всем полям, представленным на главное странице)
# затем несколько контактов со случайно сгенеренными данными
if n == 0:
    test_data = []
else:
    test_data = [Group(name="Группа в полосатых купальниках", header="Хедер группы в полосатых купальниках",
                       footer="Футер группы в полосатых купальниках")] + \
                [Group(name=random_string("name", 20), header=random_string("header", 20),
                       footer=random_string("footer", 20))
                 for i in range(0, n-1)]

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file_name, "w") as file:
    jsonpickle.set_encoder_options("json", indent=2, ensure_ascii=False)
    file.write(jsonpickle.encode(test_data))




