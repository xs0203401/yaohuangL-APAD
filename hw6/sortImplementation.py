# abstract template class
class QSTemplate:
    ls = []

    def __cpr__(self, x, y):
        pass

    def __init__(self):
        pass

    def sort_fun(self, l):
        if len(l) <= 1:
            return l

        # pick the pivot index p and swap the pivot num to the [0]
        p = self.__pivot__(l)
        l[p], l[0] = l[0], l[p]

        l1, l2 = self.__partition__(l)
        l1 = self.sort_fun(l1)
        l2 = self.sort_fun(l2)

        return [*l1, l[0], *l2]

    def __partition__(self, l):
        l1 = []
        l2 = []
        for i in l[1:]:
            if self.__cpr__(i, l[0]):
                l1.append(i)
            else:
                l2.append(i)
        return l1, l2

    def __pivot__(self):
        return 0


class QSPivotFirst(QSTemplate):

    def __init__(self, strategy):
        QSTemplate.__init__(self)
        self.__cpr__ = {"ASC": (lambda x, y: True if (x < y) else False),
                    "DESC": (lambda x, y: True if (y < x) else False)
                    }[strategy]

    def __pivot__(self, l):
        # pivot first implement
        pivot = 0
        return pivot


class QSPivotLast(QSTemplate):

    def __init__(self, strategy):
        QSTemplate.__init__(self)
        self.__cpr__ = {"ASC": (lambda x, y: True if (x < y) else False),
                    "DESC": (lambda x, y: True if (y < x) else False)
                    }[strategy]

    def __pivot__(self, l):
        # pivot last implement
        pivot = len(l)-1
        return pivot


class QSPivotMid(QSTemplate):

    def __init__(self, strategy):
        QSTemplate.__init__(self)
        self.__cpr__ = {"ASC": (lambda x, y: True if (x < y) else False),
                    "DESC": (lambda x, y: True if (y < x) else False)
                    }[strategy]

    def __pivot__(self, l):
        # pivot middle implement
        pivot = (len(l)-1)//2
        return pivot


def main():
    print("test input list")
    test_list_2 = []
    test_list_1 = [1, 3, 5, 2, 2, 4, 7, 8, 9, 6]
    test_list_3 = [1, 1, 3, 3, 5]
    print(test_list_3)

    # ASC=non-decreasing DESC=non-increasing
    # Pivot First:
    dr = "ASC"
    print("direction: " + dr)
    qs1 = QSPivotFirst(dr)
    print(qs1.sort_fun(test_list_3))
    dr = "DESC"
    print("direction: " + dr)
    qs2 = QSPivotFirst(dr)
    print(qs2.sort_fun(test_list_3))

    # Pivot Last
    dr = "ASC"
    print("direction: " + dr)
    qs3 = QSPivotLast(dr)
    print(qs3.sort_fun(test_list_3))
    dr = "DESC"
    print("direction: " + dr)
    qs4 = QSPivotLast(dr)
    print(qs4.sort_fun(test_list_3))

    # Pivot Mid
    dr = "ASC"
    print("direction: " + dr)
    qs5 = QSPivotMid(dr)
    print(qs5.sort_fun(test_list_3))
    dr = "DESC"
    print("direction: " + dr)
    qs6 = QSPivotMid(dr)
    print(qs6.sort_fun(test_list_3))


if __name__ == "__main__":
    main()