'''
LI Xiang
2019/1/21
    四种方式输出九九乘法表
'''

'''
    使用for的方式输出九九乘法表
'''
class for_ninenine():
    #从左上角开始，从小到大
    def left_from_1(self):
        print("= "*20,"从左上角开始，从小到大 ","= "*21)
        for i in range(1,10):
            for j in range(1,i+1):
                print("{0} * {1} = {2:2}".format(j,i,i*j),end='  ')
            if i < 9:
                print("\n")
        print("\n","= "*53)  
    #从左上角开始，从大到小
    def left_from_9(self):
        print("\n","= "*20,"从左上角开始，从大到小 ","= "*21)
        for i in range(1,10):
            for j in range(1,10-i+1):
                print("{0} * {1} = {2:2}".format(j,(10-i), (10-i)*j), end = '  ')  
            if i < 9:
                print("\n")
        print("\n","= "*53)
    
    #从右上角开始，从小到大
    def right_from_1(self):
        print("\n","= "*20,"从右上角开始，从小到大 ","= "*21)
        for i in range(1,10,1):
            for j in range(9,0,-1):
                if j <= i:
                    print("{0} * {1} = {2:2}".format(j, i, i * j), end = '  ')
                else:
                    print(" "*11,end = " ")
            if i < 9: 
                print("\n")
        print("\n","= "*53)
    
    #从右上角开始,从大到小
    def right_from_9(self):
        print("\n","= "*20,"从右上角开始,从大到小 ","= "*21)
        for i in range(9,0,-1):
            for j in range(9,0,-1):
                if j > i:
                    print(" "*11,end = " ")
                else:
                    print("{0} * {1} = {2:2}".format(j, i, i*j), end = '  ')
            if i > 1:
                print("\n")
        print("\n","= "*53)

if __name__ == "__main__":
    for_99 = for_ninenine()
    print("= "*25," For ","= "*25)
    for_99.left_from_1()
    for_99.left_from_9()
    for_99.right_from_1()
    for_99.right_from_9()