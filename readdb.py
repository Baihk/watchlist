import sqlite3

# 连接到数据库文件
conn = sqlite3.connect('data.db')

# 创建游标对象
cursor = conn.cursor()

# 执行查询语句
cursor.execute('SELECT * FROM User')

# 获取查询结果
results = cursor.fetchall()

# 遍历结果并打印
for row in results:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()