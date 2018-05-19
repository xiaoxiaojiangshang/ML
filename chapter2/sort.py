#
# student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
# sorted(student_tuples, key = lambda student: student[0]) # 对姓名排序
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# sorted(student_tuples, key = lambda student: student[2])  # 年龄排序
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# sorted(student_tuples, key = itemgetter(2))  # 根据年龄排序
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# sorted(student_tuples, key = itemgetter(1, 2))  # 根据成绩和年龄排序
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
# sorted(student_tuples, key = itemgetter(1, 2), reverse=True) # 反转排序结果
# [('jane', 'B', 12), ('dave', 'B', 10), ('john', 'A', 15)]