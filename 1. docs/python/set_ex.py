s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합과 합집합
print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s2 - s1)

# s3 = set()
# print(type(s3))
#
# s4 = {}
# print(type(s4))