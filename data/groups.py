from model.group import Group
import random
import string


def random_string(postfix, maxlen):
    s = "".join([random.choice(string.ascii_letters + string.digits + " "*6) for i in range(random.randrange(maxlen))])
    return s + postfix


testdata = [Group(name="Группа в полосатых купальниках", header="Хедер группы в полосатых купальниках",
                   footer="Футер группы в полосатых купальниках")] + \
            [Group(name=name, header=header, footer=footer)
             for name in ["", random_string("name", 20)]
             for header in ["", random_string("header", 20)]
             for footer in ["", random_string("footer", 20)]] + \
            [Group(name=random_string("name", 20), header=random_string("header", 20), footer=random_string("footer", 20))
             for i in range(0, 5)]


constant = [Group(name="Группа в полосатых купальниках", header="Хедер группы в полосатых купальниках",
                   footer="Футер группы в полосатых купальниках"),
            Group(name="Группа 1 в полосатых купальниках", header="Хедер группы 1",
                  footer="Футер группы 1"),
            Group(name="Группа 2 в полосатых купальниках", header="Хедер группы 2",
                  footer="Футер группы 2")
            ]
