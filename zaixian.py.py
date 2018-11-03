# 学员信息在线管理
import pymysql

class studb:
	def __init__(self):
		'''构造方法，打开SQL数据库'''
		self.db = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
		self.cursor=self.db.cursor()
		try:
			#检查是否已有同名数据库
			self.cursor.execute('show databases;')
			for i in self.cursor.fetchall():
				if i==('stu',):
					if input('已有数据库stu，是否删除并重新创建？（yes/no）\n')=='yes':
						self.cursor.execute('drop database stu;')
			self.cursor.execute('create database stu;')
			self.cursor.execute('use stu')
			#检查是否有同名表
			self.cursor.execute("show tables like'stume';")
			if self.cursor.rowcount == 0:
				self.cursor.execute('create table stume(id int unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT,name varchar(20) NOT NULL,age tinyint unsigned NOT NULL,classid VARCHAR(20) NOT NULL);')
				self.cursor.execute("insert into stume VALUES (NULL,'zhangsan',20,'python02'),(NULL,'lisi',22,'python03'),(NULL,'wangwu',25,'python04');")
			self.db.commit()
			'''事务提交'''
		#处理异常,用超级对象接收异常信息
		except Exception as err:
			self.db.rollback()
			'''事务回滚'''
			print('操作失败！,原因是：', err)

	def findall(self):
		'''信息查询函数'''
		try:
			self.cursor.execute('select * from stume;')
			'''检测条数'''
			if self.cursor.rowcount==0:
				print("========== 没有学员信息可以输出！=============")
			else:
				print("|{0:<5}| {1:<10}| {2:<5}| {3:<10}|".format("sid", "name", "age", "classid"))
				print("-" * 66)
				for i in self.cursor.fetchall():
					print("|{0:<5}| {1:<10}| {2:<5}| {3:<10}|".format(i[0], i[1], i[2],i[3]))
		except Exception as err:
			self.db.rollback()
			print('查询失败！,原因是：', err)

	def insert(self,stu):
		'''信息插入函数'''
		try:
			self.cursor.execute('insert into stume values(null,"{}","{}","{}");'.format(stu["name"],stu["age"],stu["classid"]))
			print("-" * 33,'添加成功！！！',"-" * 66)
		except Exception as err:
			self.db.rollback()
			print('查询失败！,原因是：', err)

	def delete(self,sid):
		'''信息删除函数'''
		try:
			self.cursor.execute('delete from stume where id={};'.format(sid))
			print("-" * 33,'删除成功！！！',"-" * 66)
		except Exception as err:
			self.db.rollback()
			print('删除失败！,原因是：', err)

	def __del__(self):
		'''析构方法，关闭数据库'''
		self.cursor.close()
		self.db.close()


#建立操作类对象
studb=studb()
#程序主循环
while True:
	# 输出初始界面
	print("="*20,"学员管理系统","="*20)
	print("{0:1} {1:13} {2:15}".format(" ","1. 查看学员信息","2. 添加学员信息"))
	print("{0:1} {1:13} {2:15}".format(" ","3. 删除学员信息","4. 退出系统"))
	print("="*40)
	key = int(input("请输入对应的选择："))
	# 根据键盘值，判断并执行对应的操作
	if key == 1:
		print("="*12,"学员信息浏览","="*14)
		studb.findall()
		input("按回车键继续：")
	elif key == 2:
		print("="*12,"学员信息添加","="*14)
		stu={}
		stu['name']=input("请输入要添加的姓名：")
		stu['age']=int(input("请输入要添加的年龄："))
		stu['classid']=input("请输入要添加的班级号：")
		studb.insert(stu)
		studb.findall()
		input("按回车键继续：")
	elif key == 3:
		print("="*12,"学员信息删除","="*14)
		studb.findall()
		sid = input("请输入你要删除的信息id号：")
		studb.delete(sid)
		studb.findall()
		input("按回车键继续：")
	elif key == 4:
		print("="*33,"bye","="*33)
		break
	else:
		print("======== 无效的键盘输入！ ==========")
	
