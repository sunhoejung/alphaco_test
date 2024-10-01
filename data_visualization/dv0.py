'''

matplotlib : 파이썬 내 시각화 도구 중 최대 / 데이터만 있으면 모든 그림 다 그릴 수 있음
기본값 : list
matplotlib 시각화 문법 어려움
그래서 seaborn 통해 pandas 데이터 프레임에서 쉽게 시각화 구현 가능하게 함

seaborn 단점: 기본 제공 그림이 안 이쁨, 그래서 세부 옵션 수정하려면 어차피 matplotlib 알아야 함
결국 matplotlib + seaborn 한 세트로 생각하기

matplotlib이 어려운 이유
-Gap이 존재함
-예제는 거의 리스트 형태로 구성
하지만 우리가 다루는 데이터는 series, pandas

즉, series와 pandas 형태를 리스트로 형변환 해야 한다

'''