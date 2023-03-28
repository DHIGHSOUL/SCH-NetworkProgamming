str = "My name is Kyeongho Jang"
# 문자수 출력
print(len(str))
# 10번 반복
print(str*10)
# 문자열의 첫 번째 문자
print(str[0])
# 처음 4문자 출력
print(str[:4])
# 마지막 4문자 출력
print(str[-4:])
# 문자열 거꾸로 출력
print(str[::-1])
# 첫 번째 문자와 마지막 문자 제거한 문자열
print(str[1:len(str)-1])
# 대문자 변경
print(str.upper())
# 소문자 변경
print(str.lower())
# 문자 대체
print(str.replace('a', 'e'))