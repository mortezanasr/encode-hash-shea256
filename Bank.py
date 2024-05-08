from turtle import goto

import self

import random
a = []
b = {}
class Bank_Account:
    def __init__(self,name,family):
        id = random.randint(10, 100)
        if id in a :
            self.id = random.randint(100,1000)
            a.append(id)
        else:
            self.id = id
            a.append(id)
        self.name = name
        b[self.name] = self.id
        self.family = family
        self.total = 0
    def variz(self):
        amount = int(input("مبلغ مورد انتقال را وارد کنید: "))
        self.total += amount

    def bardasht(self):
        amount = int(input("مبلغ برداشتی را وارد کنید: "))
        if amount < self.total:
            self.total -= amount

        else:
            print(f"{self.name} {self.family} مبلغ برداشتی بیشتر از باقیمانده شما است ")
            print(20 * "-")
    def display_total(self):
        return print(f"شماره حساب شما {self.id} \nخوش آمدید {self.name} {self.family}\nدر حال حاضر حساب شما {self.total}Rial می باشد")


    def display_totall(self):
        return print( f"باقیمانده حساب شما {self.total}Rial می باشد")

    def display_totalll(self):
        return print(f"باقیمانده حساب شما {self.total}Rial می باشد")


def modir():
    return print(b)


def main():
   sec = int(input(f"برای مدیریت شماره ۱""\n""برای افتتاح حساب شماره 2""\n""خروج شماره ۳""\n"))
   while True:
       if sec == 2:
           print(20 * "-")
           acc = input("نام خود را وارد کنید:  ")
           fcc = input("نام خانوادگی خو را وارد کنید: ")
           print(20 * "+")
           acc = Bank_Account(acc, fcc)
           acc.display_total()
           print(20 * "-")

           while True:
               i = int(input("برداشت از حساب : 1""\n""واریز به حساب: 2""\n""خروج : 3""\n"))
               print(20 * "-")

               if i == 1:
                   acc.bardasht()
                   acc.display_totall()
                   print(20 * "-")
               elif i == 2:
                   acc.variz()
                   acc.display_totall()
                   print(20 * "-")
               else :
                   main()
       elif sec == 1:
           print(20 * "-")
           modir()
           print(20 * "-")
           main()



       elif sec == 3 :
           break



if __name__ == "__main__":
    main()









