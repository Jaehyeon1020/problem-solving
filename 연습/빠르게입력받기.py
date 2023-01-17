'''
sys 라이브러리의 readline() 함수를 이용하면 입력 데이터의 개수가 많은 문제에서 입력 시간을 줄일 수 있음
input() 함수 대신 사용
'''

import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 출력
print(input_data)