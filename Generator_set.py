import random
import string


class total_length:  # 密码长度定义器

    @staticmethod
    def total_length_random():  # 随机密码总长度(8-16位)
        return random.randint(8, 16)

    @classmethod
    def total_length_userlen(a, b):  # 自定义密码总长度
        return random.randint(a, b)


symbol_stock = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                '-', '+', '=', '[', ']', '{', '}', '|', ';', ':', '"', '\'', ',', '<', '>',
                '.', '/', '?']


class generator:  # char type chooser and generator
    @staticmethod
    def method_choice():  # choose a type for next char in the password
        return random.randint(1, 4)

    @staticmethod
    def generator_randsym():
        return random.choice(symbol_stock)

    @staticmethod
    def generator_randint():
        sto = random.randint(0, 9)
        return sto

    @staticmethod
    def generator_randlow():
        return random.choice(string.ascii_lowercase)

    @staticmethod
    def generator_randup():
        return random.choice(string.ascii_uppercase)


ktype = []  # 已经生成的密码字符类型列表,每生成一个字符，都把字符类型存入。


class gener:

    @staticmethod
    def generator1():
        tl1: int = total_length.total_length_random()  # 程序已经generate出最终是几位数的密码
        i: int = 0
        tojoin = []  # 准备列表，每个生成字符作为独立元素加入列表。注意千万不能放在while loop里，否则每次循环都会创建一个列表
        while i < tl1:  # 当密码位数没到设计位数时的loop
            k = generator.method_choice()  # 决定下一个Char的类型

            if k == 1:
                ktype.append(k)
                char = generator.generator_randsym()
                tojoin.append(char)
                i += 1

            elif k == 2:
                ktype.append(k)
                char1 = generator.generator_randint()
                tojoin.append(str(char1))
                i += 1

            elif k == 3:
                ktype.append(k)
                char2 = generator.generator_randlow()
                tojoin.append(char2)
                i += 1

            else:
                ktype.append(k)
                char3 = generator.generator_randup()
                tojoin.append(char3)
                i += 1

        # 循环结束，产生了一个每个字符是独立元素的列表，要把列表里的每个元素利用迭代器凑成一个整字符串输出
        # print(ktype)  # 可以检测生成字符类型
        while ktype is not None:  # 自检生成的密码是否含有所有类型的字符
            if 1 not in ktype:
                gener.generator1()
                break
            elif 2 not in ktype:
                gener.generator1()
                break
            elif 3 not in ktype:
                gener.generator1()
                break
            elif 4 not in ktype:
                gener.generator1()
                break
            else:
                break

        if 1 & 2 & 3 & 4 not in ktype:
            gener.generator1()

        password1 = ''.join(tojoin)  # 利用迭代器把列表里的字符拼成一个完整的str输出
        return password1

    def generator2(len0):

        i: int = 0
        tojoin = []  # 千万不能放在while loop里，否则每次循环都会创建一个列表
        h = len0
        while i < h:  # 当密码位数没到设计位数时的loop
            k = generator.method_choice()  # 决定下一个Char的类型

            if k == 1:
                ktype.append(k)
                char = generator.generator_randsym()
                tojoin.append(char)
                i += 1

            elif k == 2:
                ktype.append(k)
                char1 = generator.generator_randint()
                tojoin.append(str(char1))
                i += 1

            elif k == 3:
                ktype.append(k)
                char2 = generator.generator_randlow()
                tojoin.append(char2)
                i += 1

            else:
                ktype.append(k)
                char3 = generator.generator_randup()
                tojoin.append(char3)
                i += 1
        password2 = ''.join(tojoin)
        return password2

    def generator3(self):
       pass


def len_selector(i2):
    try:
        return gener.generator2(i2)

    except ValueError:
        print('enter an integer please!')


while True:
    pree = input('Digit of Password or press enter to randomly generate: ')

    if pree == '':
        print(gener.generator1())
    else:
        try:
            i1 = int(pree)
            print(len_selector(i1))
        except ValueError:
            print('Please enter an integer')
