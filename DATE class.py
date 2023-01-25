class Date:
    def __init__(self, day, month, year):
        self.d = day
        self.m = month
        self.y = year
        print("tha date is:", self.d, "/", self.m, "/", self.y)


    def __str__(self):
        return str(self.d) + "/" + str(self.m) + "/" + str(self.y)


    def order(self):
        o = self.d
        dpm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days per month
        if self.y % 4 == 0:
            dpm[1] = 29
        for i in range(self.m-1):
            o += dpm[i]
        return o


    def __sub__(self, other):
        nd1 = self.y*365 + self.d            # number of days before date1
        dpm1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days per month
        if self.y % 4 == 0:
            nd1 += 1
            dpm1[1] = 29
        for i in range(self.m-1):
            nd1 += dpm1[i]

        nd2 = other.y * 365 + other.d       # number of days before date2
        dpm2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days per month
        if other.y % 4 == 0:
            nd2 += 1
            dpm2[1] = 29
        for k in range(other.m - 1):
            nd2 += dpm2[k]
        if nd1 > nd2:
            number_of_days = nd1 - nd2
        else:
            number_of_days = nd2 - nd1

        return number_of_days


    def __add__(self, other):
        o = self.order()
        if self.y % 4 == 0:
            remdays = 366 - o
        else:
            remdays = 365 - o

        if other <= remdays:
            y2 = self.y
            o2 = o + other
        else:
            other -= remdays
            y2 = self.y + 1
            if y2 % 4 == 0:
                y2days = 366
            else:
                y2days = 365

            while other >= y2days:
                other -= y2days
                y2 += 1
                if y2 % 4 == 0:
                    y2days = 366
                else:
                    y2days = 365

            o2 = other

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y2 % 4 == 0:
            month[1] = 29
        for index in range(12):
            if o2 <= month[index]:
                break
            o2 = o2 - month[index]

        d2 = o2
        m2 = index+1
        date2 = str(d2)+"/"+str(m2)+"/"+str(y2)
        return date2


    def __lt__(self, other):
        nd1 = self.y * 365 + self.d  # number of days before date1
        dpm1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days per month
        if self.y % 4 == 0:
            nd1 += 1
            dpm1[1] = 29
        for i in range(self.m - 1):
            nd1 += dpm1[i]

        nd2 = other.y * 365 + other.d  # number of days before date2
        dpm2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days per month
        if other.y % 4 == 0:
            nd2 += 1
            dpm2[1] = 29
        for k in range(other.m - 1):
            nd2 += dpm2[k]
        if nd1 < nd2:
            return "Right"
        else:
            return "Wrong"


d1 = Date(1, 11, 2013)
d2 = Date(1, 1, 2014)
print("number of days between two dates:", d2 - d1)
print(d1 + 100, "is the date 100 days after", d1)
print(d1 < d2)
print(d1.order())
