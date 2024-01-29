cabinet = {3: "유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) # 오류 발생 5라는 키가 없기 때문, 프로그램이 끝난다.
print(cabinet.get(5)) # 5라는 키가 없어 None , 프로그램이 끝나지 않는다.
print(cabinet.get(5, "사용 가능"))


print(3 in cabinet) # key in value : 3이 있으면 True
print(5 in cabinet) # 5 가 있으면 True

cabinet = {"A-3": "유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
'''
유재석
김태호
유재석
None
사용 가능
True
False
유재석
김태호
{"A-3": "유재석", "B-100":"김태호"}
{"A-3": "김종국", "B-100":"김태호", "C-20":"조세호"}
{"B-100":"김태호", "C-20":"조세호"}
dict_keys(["B-100", "C-20"])
dict_values(["김태호", "조세호"])
dict_items([("B-100", "김태호"), ("C-20", "조세호")])
{}
'''