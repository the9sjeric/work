import random
rewardDict = {
    '一等奖': (0, 0.08),
    '二等奖': (0.08, 0.3),
    '三等奖': (0.3, 1.0)
}

aaa = rewardDict.get("一等奖", "没有一等奖")
bbb = rewardDict.get("www", "没有")
print(aaa, bbb)