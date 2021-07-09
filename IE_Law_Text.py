#!/usr/bin/python3
#法律文书的要素抽取（正则匹配）
__author__ = 'Liuyichuan'

import re

pat_name = "被告人）*[^，]*"#被告人名字
pat_birthdate = "\d{4}年\d{1,2}月\d{1,2}日出生"#出生日期
pat_birthplace = "出生于[^，]*" # 两个..表示一个中文字
pat_nation = "，(..){1,4}族"#最长的民族名称有4个字
pat_knowledge = "，(..){1,2}文化"#文化程度
pat_home = "住[^，]*"#居住地
pat_detendate = "于\d{4}年\d{1,2}月\d{1,2}日被"#被拘留日期

with open("test.txt", "r",encoding="utf-8") as f:
    msg = f.read() 

res_name = re.search(pat_name.encode('gbk'), msg.encode('gbk')) # 抽取名字
if res_name is not None:
    print(res_name.group().decode('gbk')[4:])#去掉“被告人”三个字

res_birthdate = re.search(pat_birthdate.encode('gbk'), msg.encode('gbk')) #抽取出生日期，统一转化为gbk编码再匹配
if res_birthdate is not None:
    print(res_birthdate.group().decode('gbk')[0:-2])#去掉“出生”两个字
    
res_birthplace = re.search(pat_birthplace.encode('gbk'), msg.encode('gbk')) # 抽取出生地
if res_birthplace is not None:
    print(res_birthplace.group().decode('gbk')[3:])#去掉“出生于”三个字
 
res_nation = re.search(pat_nation.encode('gbk'), msg.encode('gbk')) # 抽取民族
if res_nation is not None:
        print(res_nation.group().decode('gbk')[1:])#去掉开头的逗号
        
res_knowledge = re.search(pat_knowledge.encode('gbk'), msg.encode('gbk'))# 抽取文化程度
if res_knowledge is not None:
    print(res_knowledge.group().decode('gbk')[1:])#去掉开头的逗号
 
res_home = re.search(pat_home.encode('gbk'), msg.encode('gbk'))# 抽取居住地
if res_home is not None:
    print(res_home.group().decode('gbk')[1:])#去掉开头的“住”字
 
res_detendate = re.search(pat_detendate.encode('gbk'), msg.encode('gbk'))# 抽取拘留日期
if res_home is not None:
    print(res_detendate.group().decode('gbk')[1:-1])#去掉开头的“于”字和结尾的“被”字


