import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 재현성을 위해 시드 설정
np.random.seed(0)

# 정규 분포를 따르는 (평균=0, 표준편차=1) 무작위 데이터 생성 (형태: (100, 2))
data = np.random.randn(100, 2)

# 2x2 그리드와 지정된 피규어 크기로 서브플롯 생성
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 데이터에서 변수 추출
a = data[:, 0]
b = data[:, 1]

# 서브플롯 1: 변수 a와 b의 평균 및 중앙값에 대한 막대 그래프
axes[0, 0].bar(['평균', '중앙값'], [np.mean(a), np.median(a)], color='blue', alpha=0.7, label='변수 a')
axes[0, 0].bar(['평균', '중앙값'], [np.mean(b), np.median(b)], color='green', alpha=0.7, label='변수 b')
axes[0, 0].legend()
axes[0, 0].set_title('기술 통계: 평균 및 중앙값')

# 서브플롯 2: 두 변수 간의 상관 행렬에 대한 히트맵
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('상관 분석')

# 서브플롯 3: 변수 a와 b의 히스토그램
axes[1, 0].hist(a, bins=15, color='blue', alpha=0.7, label='변수 a')
axes[1, 0].hist(b, bins=15, color='green', alpha=0.7, label='변수 b')
axes[1, 0].legend()
axes[1, 0].set_title('변수의 히스토그램')

# 서브플롯 4: 변수 a 대 변수 b의 산점도
axes[1, 1].scatter(a, b, alpha=0.7)
axes[1, 1].set_xlabel('변수 1')
axes[1, 1].set_ylabel('변수 2')
axes[1, 1].set_title('변수 1 대 변수 2의 산점도')

# 더 나은 외관을 위해 레이아웃 조정
plt.tight_layout()

# 플롯 표시
plt.show()

