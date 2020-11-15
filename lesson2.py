# 增加单个元素
# list1=[1,2,3]
# list1.append(4)
# print(list1)

# 指定位置添加
# list1=[1,2,3]
# list1.insert(3,4)
# print(list1)

# 列表一次性添加多个元素
# list1 = [1,2,3,4]
# list1.extend([5,6,7,8,9,10])
# print(list1)

#取值
# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(list1[0:4])

# 修改
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list1[-1]=11
# print(list1)

# 默认删除最后一个元素
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list1.pop()
# print(list1)

# 删除整个列表，清空
# list1 = [1,2,3,4,5,6,7,8,9,10]
# del list1

# 创建空列表
# list2=[]
# print(list2,type(list2))

# 字典
# dict1 = {"name":"lemon"}
# print(dict1,type(dict1))

# 取值
# dict1 = {"name":"lemon"}
# # print(dict1['name'])
# print(dict1.get('name'))

# 更新修改字典
# dict1 = {"name":"lemon","age":18}
# dict1["age"]=19
# print(dict1)

# 字典增加多个元素：update({字典})
# dict1 = {"name":"lemon","age":18}
# dict1.update({"工作年限：":2,"sex":"男"})
# print(dict1)

# 字典增加一个元素
# dict1 = {"name":"lemon","age":18}
# dict1["adress"]="江苏"
# dict1["工作年限"]=2
# print(dict1)

# 创建只有一个元素的元祖
# tup3=(4,)
# print(tup3)

# 元祖中的元素不能修改
# tup1=(1,2,3,4,5)
# tup1[0]=0
# print("修改后的元组：",tup1)

# 元祖和列表转换，然后修改元素
# tup1=(1,2,3,4,5)
# list1=list(tup1)
# # print(list1,type(list1))
# list1[0]=0
# # print(list1)
# tup2=tuple(list1)
# print(tup2)

# 元祖转换为列表取值
# tup1=(1,2,3,4,5)
# list1=list(tup1)
# print(list1[0])

# 集合去重复
# set1=set({1,2,3,4,5,1,2,3})
# print (set1)

# 两种方式定义集合
# 方法一：{}
# set1={1,2,3,4,5}
# print (set1)
# 方法二：set() 函数
# set1=set({1,2,3,4,5})
# print (set1)

# if判断语句
# 根据你输入的工资，去判断你当前的岗位级别，初级：小于15k；中级：15-25k；高级：25-50k
# xinzi=int(input('请输入月薪：'))
# if xinzi < 15:
#     print('初级')
# elif xinzi >= 15 and xinzi < 25:
#     print('中级')
# else:
#     print('高级')

# for循环语句
# sum=0
# for nuber in [1,2,3,4,5,6,7,8,9,10]:
#    print(nuber)
#    sum=sum+nuber
# print('1+2+3+4+5+6+7+8+9+10=',sum)

# 求1+2+3+4+....+100=？range() 函数
# sum=0
# for nuber in range(1,101):
#    sum+=nuber
# print('1+2+3+4+....+100=',sum)

# 求2+4+6+...+100=？---->求偶数值
# 方法一
# sum=0
# for nuber in range(2,101,2):
#    sum += nuber
# print('2+4+6+...+100=',sum)
# 方法二：内嵌 if 语句
# sum=0
# for nuber in range(1,101):
#     if nuber%2==0:
#        print(nuber)
#        sum+=nuber
#     else:
#          continue
# print('2+4+6+...+100=',sum)
# 方法三：while 语句
# sum=0
# nuber=2
# while nuber<=100:
#       sum+=nuber
#       nuber+=2
# print('2+4+6+...+100=',sum)

# 定义无参数函数
# def sum():
#     sum = 0
#     for nuber in range(1, 11):
#         print(nuber)
#         sum = sum + nuber
#     print('1+2+3+...+10=', sum)
# sum()

# 求1+2+...+n=?
# def sum(n):
#     sum = 0
#     for nuber in range(1, n + 1):
#         print(nuber)
#         sum = sum + nuber
#     print(f'1+2+...+{n}=', sum)
# sum(10)

# 必备参数
# def user_info(name,age,adress):
#     # name = "张三"
#     # age = 18
#     # adress = "江苏"
#     print(f"hello{name},age{age},来自：{adress}")
# user_info("张三",18,"江苏")

# 关键字参数
# def user_info(name, age, adress, nianxian, sex):
#     print(f"hello{name},age{age},来自：{adress},工作年限：{nianxian},性别：{sex}")
# # user_info(name="张三", age=18, adress="江苏", nianxian=2, sex="男")
# user_info(age=18,adress="江苏",nianxian=2,name="张三",sex="男")

# 默认参数
# def user_info(name, age, adress, nianxian, sex='男'):
#     print(f"hello{name},age{age},来自：{adress},工作年限：{nianxian},性别：{sex}")
#
# user_info(name="张三", age=18, adress="江苏", nianxian=2)
# user_info(name="李四", age=18, adress="江苏", nianxian=2,sex='女')

# 题目：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面
# 方法一
# a=[1,2,'6','summer']
# print('i'in a)
# 方法二
# a=[1,2,'6','summer']
# print('i'not in a)

# 题目：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5 注：num表示课堂人数。如果大于5，输出人数
# dict_1={"class_id":45,'num':20}
# if dict_1['num'] > 5:
#    print(dict_1['num'])

# list3 = ['飞羽', '路飞', '凉公子', '社会杨', '小书生', '凉夏'] 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形
# 式表达。并且把字典都存在新的 list中，最后打印最终的列表
# 方法1： 手动扩充--字典--存放在列表里面；{} --简单
# list3=['飞羽','路飞', '凉公子', '社会杨', '小书生', '凉夏']
# dict1={"姓名":"飞羽","性别":'男',"年龄":"20","城市":"上海"}
# dict2={"姓名":"路飞","性别":'男',"年龄":"21","城市":"江苏"}
# dict3={"姓名":"凉公子","性别":'男',"年龄":"22","城市":"重庆"}
# dict4={"姓名":"社会杨","性别":'男',"年龄":"23","城市":"陕西"}
# dict5={"姓名":"小书生","性别":'男',"年龄":"24","城市":"浙江"}
# dict6={"姓名":"凉夏","性别":'男',"年龄":"25","城市":"上海"}
# list1=[dict1,dict2,dict3,dict4,dict5,dict6]
# # for list2 in list1:  -----> 这句不用写，写了打印出来的只是每个字典，而不是一个列表，题目时打印出列表
# print(list1)

# 方法1.1：
# list3=['飞羽','路飞', '凉公子', '社会杨', '小书生', '凉夏']
# list1=[]
# dict1={"姓名":'飞羽',"性别":'男',"年龄":"20","城市":"上海"}
# dict2={"姓名":"路飞","性别":'男',"年龄":"21","城市":"江苏"}
# dict3={"姓名":"凉公子","性别":'男',"年龄":"22","城市":"重庆"}
# dict4={"姓名":"社会杨","性别":'男',"年龄":"23","城市":"陕西"}
# dict5={"姓名":"小书生","性别":'男',"年龄":"24","城市":"浙江"}
# dict6={"姓名":"凉夏","性别":'男',"年龄":"25","城市":"上海"}
# list1.append(dict1)
# list1.append(dict2)
# list1.append(dict3)
# list1.append(dict4)
# list1.append(dict5)
# list1.append(dict6)
# # for list2 in list1:
# print(list2)

# 方法2：自动--dict（）--不强制 list.append()
# list3=['飞羽','路飞', '凉公子', '社会杨', '小书生', '凉夏']
# list1=[]
# for x in list3:
#  dict1 = { "性别": '男', "年龄": "20", "城市": "上海"}
#  print(x)
#  dict1['姓名']=x
#  list1.append(dict1)
# print(list1)

# 遍历列表
# list1 = ['name', 'age', 'sex']
# for list2 in list1:
#  print(list2)

# 遍历字典，items()返回一个键 — 值对列表， for 循环依次将每个键 — 值对存储到指定的两个变量（key,value）中
# dict1 = {'name':"张三", 'age':"20", 'sex':"男"}
# for key,value in dict1.items():
#  print(key+"："+value)

# 遍历集合
# set1={1,2,3,4,5}
# for set2 in set1:
#  print(set2)

# 遍历元祖
# tup1=(1,2,3,4,5)
# for tup2 in tup1:
#  print(tup2)

# 题目：把字符串转成列表
# title=('hello','lemon',2)
# list1=list(title)
# print(list1,type(list1))

# 题目：任意整数序列相加
# def sum(n):
#   sum=0
#   for x in range(1,n+1):
#    print(x)
#    sum+=x
#   print(f'1+2+...+{n}=',sum)
#
# sum(10)

# 题目：定义函数，判断一个对象（列表、字典、字符串）的长度是否大于5
# def a(x):
#  if len(x) > 5:
#   print(len(x) > 5)
#  else:
#   print(len(x) <= 5)
#
# a({'namezhangsan'})


# 不定长参数
# def sum2(**b):
#  print(b)
#  sum=0
#  for x in b:
#    sum += b[x]
#  print(sum)
#  return sum
#
# print(sum2(one=1,two=2,three=3),type(sum2(one=1,two=2,three=3)))
# print(all,type(all))

# 计算字符串中 a 的数量
# x="python hello aaa 123123aabb"
# print('a的次数：',x.count('a'))
