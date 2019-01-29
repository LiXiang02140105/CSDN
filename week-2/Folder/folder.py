#!/usr/bin/python3
#coding = utf-8
''' 
    2019/1/23
    LI Xiang
    lx02140105@163.com
    递归显示一个文件夹的内容：文件夹、空文件夹、文件  
'''
import os 

def search(path):
    folder_size = 0 #记录当前文件夹size
    files = os.listdir(path)   #查找路径下的所有的文件夹及文件
    current = os.path.split(path)[1]

    for filee in files:
        f_path = os.path.join(path, filee) #使用绝对路径
        if os.path.isfile(f_path):  #判断是文件夹还是文件
            #文件计算文件大小
            folder_size = folder_size + os.path.getsize(f_path)

        elif os.listdir(f_path) != []:  #判断文件夹是否为空
            folder_size = folder_size + search(f_path)
            #递归显示文件夹中的文件夹的内容
    return folder_size

if __name__ =='__main__':
    path = input('Input path:')  #input 函数数从命令输入
    while not os.path.exists(path):
        path = input('Please input correct path:')  #判断文件路径是否合法
    if os.path.isfile(path):
        #如果是文件，则直接输出文件size
        print("File {0} size:{2} M, {1} 字节".format(os.path.basename(path),folder_size,int(folder_size/(1024*1024))))

    elif os.listdir(path) != []:
        #如果是文件夹，则递归输出文件夹大小
        folder_size = search(path)
        print("Folder {0} size:{2} M, {1} 字节".format(os.path.basename(path),folder_size,int(folder_size/(1024*1024))))
    
#D:\source\CSDN\week-1
#‪D:\source\CSDN  