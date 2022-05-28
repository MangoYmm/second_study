import pymysql
db=pymysql.connect(
	host='192.168.5.130',
	user='root',
	password='123456',
	db='mysql',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
)
def test_conn():
	with db.cursor() as cursor:
		sql='show tables;'
		cursor.execute(sql)
		print(sql)
		#print(cursor.fetchall())
		print(cursor.fetchone())
def test_insert():
	with db.cursor() as cursor:
		sql = "INSERT INTO `person` (`name`, `age`) VALUES (%s, %s)"
		cursor.execute(sql, ('amanda', '20'))
		print(cursor.fetchone())
		db.commit()
	with db.cursor() as cursor:
		sql = "select *  from `person`  where `name`=%s;"
		cursor.execute(sql, ('ada'))
		print(cursor.fetchone())