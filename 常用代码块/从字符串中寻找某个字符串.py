import re
string = 'SSS41faert5.88he哈llo哈world@￥…￥english我的小15可爱love89吗!@沙雕$'
result = re.search(r'[A-Za-z]+[0-9]+[.][0-9]+', string)
print(result)
print(type(result))
print(result.group())