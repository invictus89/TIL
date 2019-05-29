# # 1
# lunch = {
#     'chinese' : '02'
# }
# 2
lunch = dict(chinese='02')
lunch['junk'] = '031'
# print(lunch)

idol = {
    'bts': {
        'jimin' : 25,
        'rm': 24
    }
}
# print(idol['bts']['rm'])

# for key in lunch:
#     print(key)
#     print(lunch[key])

for key, value in lunch.items():
    print(key, value)
for value in lunch.values():
    print(value)
for key in lunch.keys():
    print(key)