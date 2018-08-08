# abstract template class
class QSTemplate:
    ls = []

    def __cpr__(self, x, y):
        pass

    def __init__(self):
        pass

    def sort_fun(self, l):
        p = self.__pivot__(l)
        del l[p]
        l1, l2 = self.__partition__(l, l[p])
        if len(l1) > 1:
            l1 = self.sort_fun(l1)
        if len(l2) > 1:
            l2 = self.sort_fun(l2)
        return [*l1, l[p], *l2]

    def __partition__(self, l, pivot):
        l1 = []
        l2 = []
        for i in l:
            if self.__cpr__(i, pivot):
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
                    "DESC": (lambda x, y: True if (x < y) else False)
                    }[strategy]

    def __pivot__(self, l):
        # pivot first implement
        pivot = 0
        return pivot


class QSPivotLast(QSTemplate):

    def __init__(self, strategy):
        QSTemplate.__init__(self)
        self.__cpr__ = {"ASC": (lambda x, y: True if (x < y) else False),
                    "DESC": (lambda x, y: True if (x < y) else False)
                    }[strategy]

    def __pivot__(self, l):
        # pivot last implement
        pivot = len(l)
        return pivot


class QSPivotMid(QSTemplate):

    def __init__(self, strategy):
        QSTemplate.__init__(self)
        self.__cpr__ = {"ASC": (lambda x, y: True if (x < y) else False),
                    "DESC": (lambda x, y: True if (x < y) else False)
                    }[strategy]

    def __pivot__(self, l):
        # pivot middle implement
        pivot = len(l)//2
        return pivot


def main():
    test_list = [1, 3, 5, 2, 2, 4, 7, 8, 9, 6]
    # ASC=non-decreasing DESC=non-increasing
    qs = QSPivotFirst("ASC")
    print(qs.sort_fun(test_list))



if __name__ == "__main__":
    main()