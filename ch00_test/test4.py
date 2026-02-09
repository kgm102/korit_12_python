# boss_num = int(input(f'후보자 수를 입력하시오 >>> '))
# votes = {}
# for i in range(boss_num):
#     dict_key = input(f'{i+1}번째 후보자의 이름을 입력하시오 >>> ')
#     votes[dict_key] = dict_key
#
# vote_counts = int(input(f'전체 투표 횟수를 입력하시오'))
# for i in range(vote_counts):
#   plus =   input(print(f'{i+1}번째 투표 (1: {list(votes.keys())[i]}, 2: {list(votes.keys())[1]}, 3:{list(votes.keys())[2]} >>>'))

# 여기 이상은 모르겠습니다.

# 1. 전체 후보자의 수를 입력받음
num_candidates = int(input("후보자 수를 입력하시오 >>> "))

# 2. 후보자 이름을 입력받아 리스트에 저장
candidates = []
for i in range(num_candidates):
    name = input(f"{i + 1}번째 후보자의 이름을 입력하시오 >>> ")
    candidates.append(name)

# 3. 투표 수를 저장할 딕셔너리 생성 (초깃값 0)
votes = {name: 0 for name in candidates}

# 4. 전체 투표 횟수를 입력받음
total_votes = int(input("전체 투표 횟수를 입력하시오 >>> "))

# 후보자 안내 문자열 생성 (예: "1: 김일, 2: 김이...")
candidate_info = ", ".join([f"{i + 1}: {name}" for i, name in enumerate(candidates)])

# 5 & 6. 투표 진행 및 결과 업데이트
for i in range(total_votes):
    vote_num = int(input(f"{i + 1}번째 투표 ({candidate_info}) >>> "))

    # 입력받은 번호(1부터 시작)를 인덱스(0부터 시작)로 변환하여 후보자 이름 찾기
    selected_name = candidates[vote_num - 1]

    # 해당 후보자의 득표수 1 증가
    votes[selected_name] += 1

# 7. 최종 결과 출력
print("\n--- 투표 결과 ---")
for name, count in votes.items():
    print(f"{name}: {count}표")

