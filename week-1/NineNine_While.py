'''
LI Xiang
2019/1/21
    四种方式输出九九乘法表
'''

'''
    使用While的方式输出九九乘法表
'''
class While_ninenine():
    #从左上角开始，从小到大
    def left_from_1(self):
        print("= "*20,"从左上角开始，从小到大 ","= "*21)
        i = 1
        while i < 10:
            j = 1
            while j < i+1:
                print("{0} * {1} = {2:2}".format(j,i,i*j),end='  ')
                j += 1
            if i < 9:
                print("\n")
            i += 1
        print("\n","= "*53)  
    #从左上角开始，从大到小
    def left_from_9(self):
        print("\n","= "*20,"从左上角开始，从大到小 ","= "*21)
        i = 1
        while i < 10:
            j = 1
            while j < 10-i+1:
                print("{0} * {1} = {2:2}".format(j,(10-i), (10-i)*j), end = '  ')  
                j += 1
            if i < 9:
                print("\n")
            i += 1
        print("\n","= "*53)
    
    #从右上角开始，从小到大
    def right_from_1(self):
        print("\n","= "*20,"从右上角开始，从小到大 ","= "*21)
        i = 1
        while i < 10:
            j = 9
            while  j > 0:
                if j <= i:
                    print("{0} * {1} = {2:2}".format(j, i, i * j), end = '  ')
                else:
                    print(" "*11,end = " ")
                j -= 1
            if i < 9: 
                print("\n")
            i += 1
        print("\n","= "*53)
    
    #从右上角开始,从大到小
    def right_from_9(self):
        print("\n","= "*20,"从右上角开始,从大到小 ","= "*21)
        i = 9
        while i > 0:
            j = 9
            while j > 0:
                if j > i:
                    print(" "*11,end = " ")
                else:
                    print("{0} * {1} = {2:2}".format(j, i, i*j), end = '  ')
                j -= 1
            if i > 1:
                print("\n")
            i -= 1
        print("\n","= "*53)

if __name__ == "__main__":
    while_99 = While_ninenine()
    print("= "*25,"While","= "*25)
    while_99.left_from_1()
    while_99.left_from_9()
    while_99.right_from_1()
    while_99.right_from_9()