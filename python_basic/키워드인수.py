def student_report(name, *scores, **details):
    print(f"학생 이름: {name}")

    # 점수가 입력된 경우에만 평균을 계산
    if scores:
        average_score = sum(scores) / len(scores)
        print(f"평균 점수: {average_score:.2f}")
    else:
        print("점수를 입력하지 않았습니다.")

    # 키워드 인수로 전달된 추가 정보를 출력
    for key, value in details.items():
        print(f"{key}: {value}")

# 함수 호출 예제
student_report("Alice", 88, 92, 85, grade="2학년", school="Seoul High School")
print("\n")
student_report("Bob", 75, 80, 78, 90, grade="3학년", school="Busan High School", hobby="축구")
print("\n")
student_report("Charlie", grade="1학년")