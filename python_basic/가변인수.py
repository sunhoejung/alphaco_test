def calculate_average(name, *scores):
    if scores:  # 가변 인수가 비어있지 않은지 확인
        average_score = sum(scores) / len(scores)
        print(f"{name}의 평균 점수는 {average_score:.2f}점입니다.")
    else:
        print(f"{name}의 점수를 입력하지 않았습니다.")


calculate_average('j',19,20,31)
#scores의 타입은 tuple