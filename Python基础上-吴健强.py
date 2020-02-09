print('='*15,'输出九九乘法表','='*15)
print('='*10,'用for语句实现','='*10)
print('第一种九九乘法表的输出')
print('')
for j in range(1,10):
    for i in range(1,j+1):
        if i*j<10:
            print("{}*{}={:<5}".format(i,j,i*j),end='  ')
        else:
                print("{}*{}={:<4}".format(i,j,i*j),end='  ')
        '''
        每行每一个的公式所要输入的内容
        {}：占位作用；
        {:<4}：占位，且输出的数据从左到右占位；
        {:<4}、 {:<5}：对齐
        format:对格式进行统一；
        end='  '： 输出结尾不换行，只占用空格
        '''
    print('')
    #换行
print('='*60)
#分隔符分隔开
print('第二种九九乘法表的输出')
print('')
for j in range(9,0,-1):
    for i in range(1,j+1):
        if i*j<10:
            print("{}*{}={:<5}".format(i,j,i*j),end='  ')
        else:
                print("{}*{}={:<4}".format(i,j,i*j),end='  ')
    print('')
print('='*60)
print('第三种九九乘法表的输出')
print('')
for j in range(1,10):
    for k in range(1,10-j):
        print(end=" "*16)
        #空格个数
    for i in range(j,0,-1):
        if i*j<10:
            print("{}*{}={:<5}".format(i,j,i*j),end='  ')
        else:
                print("{}*{}={:<4}".format(i,j,i*j),end='  ')
    print('')
print('='*60)
print('第四种九九乘法表的输出')
print('')
for j in range(9,0,-1):
    for k in range(1,10-j):
        print(end=" "*16)
    for i in range(j,0,-1):
        if i*j<10:
            print("{}*{}={:<5}".format(i,j,i*j),end='  ')
        else:
                print("{}*{}={:<4}".format(i,j,i*j),end='  ')
    
    print('')
print('='*60)
print('='*10,'用while语句实现','='*10)
print('第一种九九乘法表的输出')
print('')
j=1
while j<=9 :
    i=1
    while i<=j:
        if i*j<10:
            print("{}*{}={:<5}".format(i,j,i*j),end='  ')
        else:
            print("{}*{}={:<4}".format(i,j,i*j),end='  ')
        i+=1
    j+=1
    print('')
print('='*60)
print('第二种九九乘法表的输出')
print('')
j=9
while j>0:
    i=1
    while i<=j:
        if i*j<10:
            print('{}*{}={:<5}'.format(i,j,i*j),end='  ')
        else:
            print("{}*{}={:<4}".format(i,j,i*j),end='  ')
        i+=1
    j-=1
    print('')
print('='*60)
print('第三种九九乘法表的输出')
print('')
j=1
while j<10:
    k=(9-j)
    while k>0:
        print(end=" "*16)
        k-=1
    i=j
    while i>0:
        if i*j<10:
            print("{}*{}={:<5}".format(i,j,i*j),end='  ')
        else:
            print("{}*{}={:<4}".format(i,j,i*j),end='  ')
        i-=1
    j+=1
    print('')
print('='*60)
print('第四种九九乘法表的输出')
print('')
j=9
while j>0:
    k=(9-j)
    while k>0:
        print(end=" "*16)
        k-=1
    i=j
    while i>0:
          if i*j<10:
              print("{}*{}={:<5}".format(i,j,i*j),end='  ')
          else:
              print("{}*{}={:<4}".format(i,j,i*j),end='  ')
          i-=1
    j-=1
    print('')
print('='*60)



#第二题
print('='*15,'计算目标文件夹的大小','='*15)
import os
#将os模块导入
def folder_size(x):
    size=0    
    #定义文件夹大小变量，并赋予初值 0
    if os.path.isfile(x):
        ##判断所输入的路径中的内容是否为文件
        size+=os.path.getsize(x)
        #获取文件的大小，并将结果与size变量进行相加，然后从新赋值给变量size
    if os.path.isdir(x):
         #判断所输入的路径中的内容是否为目录
        a=os.listdir(x)
        #获取目标文件夹中的所有文件和文件夹组成的列表
        for f in a:
            #遍历a的内容（即：遍历a这个由目标文件夹内容所组成的列表）
            #a：目标文件夹中的所有文件和文件夹组成的列表，
            file=os.path.join(x,f)
            #路径拼装,将x的路径拼装到f上去，从而补全所输入的文件夹中各文件或子文件夹的路径
            #x:所输入的文件夹路径
            if os.path.isdir(file):
                #判断是否是目录
                size+=folder_size(file)
                #递归调用自己，来实现该目录的文件大小计算
            if os.path.isfile(file):
                #判断是否为文件
                size+=os.path.getsize(file)
                
    return size
    #将所计算出的文件夹大小值返回给size

y=input('请输入文件夹路径：')
#获取所输入的路径
folder_size(y)
#调用该函数进行文件夹的大小的计算
print('该文件夹的大小为：{}字节'.format(folder_size(y)),end=' ')
#输出文件夹大小的数值
print('')
#换行



#第三题
#自动取款机系统
#定义一个用于存放卡信息的列表变量
card=[
    {'account':'101','code':'111','name':'wujianqiang','balabce':'100.25'},
    {'account':'102','code':'222','name':'hejingfeng','balabce':'200.2'},
    {'account':'103','code':'333','name':'chenshunchao','balabce':'300.67'}]
#定义一个检测银行卡账号和密码是否正确的函数
def card_info(): 
    global money
    #声明金额这个变量为全局变量
    global tf
    #声明tf为全局变量
    for i in card:
        if int(zhanghao)==int(i['account']):
            #判断账号是否存在
            #cishu=0
            if int(mima)==int(i['code']):
                #判断密码是否正确
                print('尊敬的',i['name'],'用户，本行自助式ATM机很高兴为您服务！')          
                money=round((float(i["balabce"])),2)
                tf=True
'''
下面的这段不知道怎么加进去。。。。。。
            else:
                print('密码错误！请重新输入')
                tf=False
                cishu+=1
                if cishu==3:
                    print('密码校验次数超限，已锁定！！！')
                    tf=False
        else:
            print('无此账号信息！')
            tf=False     
'''

#定义一个查询账户余额的函数
def balabce_info():
    print('余额：',money)

#定义一个存钱的函数
def savemoney():
    global money
    balabce_info()
    save=float(input('请输入存入金额：'))
    #确保含小数点的数值可以输入
    money=round((money+save),2)
    #保留小数点后两位
    balabce_info()
    #再次调用显示余额

#定义一个取钱的函数
def getmoney():
    global money
    balabce_info()
    get=float(input('请输入取款金额：'))
    #确保含小数点的数值可以输入
    money=round((money-get),2)
    #保留小数点后两位
    if money>=0:
        print('操作成功！')    
    else:
        print('所取金额额度超出！请重新输入！')
        money=round((money+get),2)
        #把之前的金额数重新返回去
        
    balabce_info()
    #重新显示一次金额数目

#定义一个按键操作的函数
def keyscan():
    global tf
    #声明tf是全局变量
    card_info()
    #调用判断所输入的账号和密码是否正确的函数
    while tf:
        print('{0:1}{1:10}{2:8}{3:6}'.format('','2.查询余额','3.存钱','4.取钱'))
        print('{0:1}{1:20}'.format('','5.退出'))
        key=input('请输入对应选项：')
        if key=='2':
            balabce_info()
            input('继续操作请敲回车键！')
        elif key=='3':
            savemoney()
            input('继续操作请敲回车键！')
        elif key=='4':
            getmoney()
            input('继续操作请敲回车键！')
        elif key=='5':
            tf=False
            #input('继续操作请敲回车键！')
            print('退出系统')
            break
        else:
            print('=========无效操作==========')
            input('继续操作请敲回车键！')
   

#主函数
tf = False
print('='*15,'自动取款机系统','='*15)
print('='*40)
while True:
    zhanghao=input('请输入银行卡卡号：')
    mima=input('请输入密码：')
    keyscan()



            

