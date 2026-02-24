# 데이터 분석과 머신러닝, 딥러닝

# 📊 가입 고객 이탈 예측

---

# 📅 프로젝트 기간

- 2026.02.18(수)~2026.02.24(수)

# 1. 팀 소개

## 1-1. 팀명 : 비상

非常과 飛上을 뜻하는 중의적인 표현

1-2. 팀원 구성 및 GitHub

| 이름 | 역할 | GitHub |
| --- | --- | --- |
| 김은우 |  | https://github.com/edu-ai-jiwon |
| 김현수 |  |  |
| 문성준 |  |  |
| 박세현 |  |  |
| 이동민 |  |  |

---

# 2. 프로젝트 개요

## 2-1. 프로젝트명

통신 고객 이탈(Churn) 예측 및 프로모션 타겟팅

---

## 2-2. 배경

통신 서비스 시장은 신규 고객 유치 비용이 높아 기존 고객 유지가 핵심 과제가 됩니다.

고객 이탈은 매출 감소로 직결되기 때문에, 이탈 가능성이 높은 고객을 조기에 식별해 적절한 혜택/프로모션을 제공하는 전략이 필요합니다.

본 프로젝트는 고객의 이용 패턴 데이터를 활용해 이탈 가능성을 사전에 예측하고, 예측 결과를 기반으로 실행 가능한 프로모션 타겟 선정까지 연결하는 것을 목표로 합니다.

---

## 2-3. 프로젝트 소개 및 목표

본 프로젝트는 통신 고객 데이터를 기반으로 이탈 여부를 예측하는 분류 모델을 구축하고, 모델 성능 비교를 통해 최적 모델을 선정한 뒤, 예측 결과를 활용한  프로모션 전략을 제안 합니다

1. **동일한 데이터 기준으로 다양한 분류 모델을 비교하고 최적 모델을 선정**
- XGBoost, LightGBM, Gradient Boosting, Random Forest, Decision Tree, CatBoost 등 여러 모델을 학습·평가하여 성능을 비교합니다.
1. **불균형 데이터 특성을 고려한 성능 평가 지표 적용**
- 이탈 데이터는 소수 클래스(이탈) 비율이 낮아 Accuracy만으로는 성능이 과대평가될 수 있습니다.
- 따라서 F1, ROC-AUC 등 지표를 함께 확인하여 이탈 고객 탐지 성능을 평가합니다.
1. **ROC-AUC를  기준으로 최종 모델 선정**
- 임계값(Threshold)에 덜 의존하는 전반적인 구분력(ROC-AUC)을 중심으로 최종 모델을 선정합니다.
- 혜택/프로모션을  제공하는 전략이기에 이탈 예측
1. **예측 결과 기반 프로모션 타겟팅 전략 제안**
- 이탈 확률이 높은 고객군을 선별하고, 혜택 제공 등 프로모션 전략을 통해 이탈 감소에 활용할 수 있는 방향을 제시합니다.

---

# 3. 기술 스택

- Python
    
    [](https://img.shields.io/badge/python-blue?style=for-the-badge&logo=python&logoColor=white)
    
- selenium
    
    [](https://img.shields.io/badge/selenium-green?style=for-the-badge&logo=selenium&logoColor=white)
    
- pandas
    
    [](https://img.shields.io/badge/pandas-yellow?style=for-the-badge&logo=pandas&logoColor=white)
    
- numpy
    
    [](https://img.shields.io/badge/numpy-lightblue?style=for-the-badge&logo=numpy&logoColor=white)
    
- matplotlib
    
    [](https://img.shields.io/badge/matplotlib-black?style=for-the-badge&logo=matplotlib&logoColor=white)
    
- seaborn
    
    [](https://img.shields.io/badge/seaborn-darkblue?style=for-the-badge&logo=seaborn&logoColor=white)
    
- folium
    
    [](https://img.shields.io/badge/folium-white?style=for-the-badge&logo=folium&logoColor=black)
    

| Language | Python |
| --- | --- |
| Web Crawling | selenium |
| Data Processing | pandas, numpy |
| Data Visualization | matplotlib, seaborn, folium |

---

# 4. WBS 및 폴더 구조
<img width="514" height="497" alt="SKN24_2nd_6team_WBS" src="https://github.com/user-attachments/assets/b1a9fc66-c547-4a39-bb77-ca2557dfcf51" />

```markdown
burger-crime-eda/
├── features/
│   ├── burger/
│   │   ├── lotteria/
│   │   │   ├── crawl_lotteria.py
│   │   │   ├── transform_lotteria.py
│   │   │   └── lotteria.json
│   │   │
│   │   ├── burgerking/
│   │   │   ├── crawl_burgerking.py
│   │   │   ├── transform_burgerking.py
│   │   │   └── burgerking.json
│   │   │
│   │   ├── mcdonalds/
│   │   │   ├── crawl_mcdonalds.py
│   │   │   ├── transform_mcdonalds.py
│   │   │   └── mcdonalds.json
│   │   │
│   │   └── kfc/
│   │       ├── crawl_kfc.py
│   │       ├── transform_kfc.py
│   │       └── kfc.json
│   │
│   ├── population/
│   │   ├── crawl_population.py
│   │   │── transform_population.py
│   │   └── population.json
│   │
│   └── crime/
│       ├── crawl_crime.py
│       │── transform_crime.py
│       └── crime.json
│
├── docs/
│   └── git_strategy.md
├── main.py
├── data.json                    # 최종 통합 파일
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 5. 데이터 수집

### 데이터 출처

- Kaggle: Cell2Cell Telecom Churn Dataset
    - https://www.kaggle.com/datasets/jpacse/datasets-for-churn-telecom
- 참고 문헌: The Impact of Various Combinations of Preprocessing Steps (THESAI)
    - https://thesai.org/Downloads/Volume16No3/Paper_64-The_Impact_of_Various_Combinations_of_Preprocessing_Steps.pdf

### 데이터 규모

- 전체: **71,047 rows × 58 columns**
- Train: **51,047 rows × 58 columns**
- Holdout: **20,000 rows × 58 columns**

### 데이터 구성(수집 항목 요약)

- 고객/계정 정보
- 요금·청구 정보
- 사용량(통화/이용) 지표
- 통화 패턴(유형/시간대 등) 특성
- 서비스/상호작용 관련 지표
- **타깃 변수: Churn(이탈 여부)**
    
    전체 컬럼(58개) 상세 목록과 변수 설명은 `data_dictionary.md`에 정리
    
    GitHub: `[Data Dictionary](docs/data_dictionary.md)` 
    

---

# 7. 데이터 전처리

## 범주형 데이터 Unique값 확인

<img width="1067" height="766" alt="image (1)" src="https://github.com/user-attachments/assets/cdae0af9-9787-4cf8-9032-4160eba5560e" />

- Service Area(통신 서비스 지역)
    - unique 값이 지나치게 많아 학습에 영향이 갈 수 있음
    - 비슷한 내용을 담은 PrizmCode가 존재하므로 제거
- Homeownership(주택 소유 여부 확인 가능 여부)
    - 값이 ‘Known/Unknown’ → 있는지 없는지를 알아야하는데 단순히 알고 모르고는 도움이 안됨
    - 방해 요소로 판단하고 제거
- HandsetPrice(단말기 가격)
    - 수치형 데이터에 가끔 'Unknown'이 끼어 있어 범주형으로 계산됨
    - ‘Unknown’ 값을 결측치로 간주할지 고려
    - ‘Unknown’ 비율 56.8%
    - 너무 많아서 중앙값으로 대체(이상치에 강함)
- MaritalStatus(고객 결혼 여부)
    - 'No', 'Yes'에 'Unknown'이 끼어 있음
    - ‘Unknown’ 값을 결측치로 간주할지 고려
    - ‘Unknown’ 비율 37.4%
    - 너무 많아서 원핫 인코딩 진행
- 그 외 범주형에는 필요에 맞는 인코딩 진행

## 결측치 확인

<img width="588" height="567" alt="image (2)" src="https://github.com/user-attachments/assets/a90c7d61-1c65-47d4-81f6-35de0a0f4fab" />

**결측치 비율: 2.49%**

<img width="557" height="219" alt="image (3)" src="https://github.com/user-attachments/assets/cd66a9b7-666a-4b08-8016-74e14c75db6e" />

- **Handsets, HandsetModels, CurrentEquipmentDays 처리 (결측치 1개)**
    - ***Handsets, HandsetModels, CurrentEquipmentDays는 전부 같은 행에서 결측치를 가짐***
    - ***다른 값으로 대체하기 어려움, 1개 뿐이므로 제거***
    
- ***PercChangeRevenues, PercChangeMinutes 전부 같은 행에서 결측치를 가짐***
    - ***각각 수익변화율, 사용시간변화율 → 혹시 신규 고객인지 확인***
    - ***평균 이용기간 26.6개월로, 신규고객으로 보기 어려움***
        
        <img width="972" height="471" alt="image (4)" src="https://github.com/user-attachments/assets/f3b86785-a98e-439c-95c8-41cd83d01c54" />


    - ***대체값을 찾기 어려워 제거***
    - 
- **DirectorAssistedCalls, TotalRecurringCharge. RoamingCalls, OverageMinutes, MonthlyRevenue, MonthlyMinutes 처리 결측치 (156개)**
    - ***PercChangeRevenues를 제거하면서 함께 제거됨***
    - ***즉, 이 열에서 결측치를 가지고 있던 행들은 너무 많은 결측치(col2 + col3)를 가지고 있어서 제거될만 했음***
    
- **AgeHH1, AgeHH2 처리 (결측치 909개)**
    - ***혹시 1인 가구일 가능성을 고려***
    
    <img width="971" height="206" alt="image (5)" src="https://github.com/user-attachments/assets/c0b1b8fe-0d38-4e43-a7cd-0f427b745cec" />

    - ***MaritalStatus(결혼 여부)가 Unknown인 값이 너무 많아 판단 어려움. No 비율이 더 높긴 하지만, Unknown 자체가 많아서 제거***
    

- **결과**
- 
<img width="769" height="356" alt="image (6)" src="https://github.com/user-attachments/assets/fca8086e-0d25-459d-be3c-5fec27da5e3a" />

- 결과적으로 결측치가 존재하는 행은 전부 삭제하였으나, 전체(51048행) 중 약 2.54%(약 1300행) 밖에 해당하지 않아 무리가 없을 것으로 판단

58Cols → 66Cols

이후 L1 Norm을 진행하며 중요도가 낮은 feature가 0으로 죽는 것을 확인할 예정

성능에 영향을 끼친다면 필요 없어 보이는 열 제거 + feature engineering 진행

---

# 8. 인공지능 학습 결과서

### DT

- 최적화 전후 분류표 레포트
<img width="600" height="300" alt="image (7)" src="https://github.com/user-attachments/assets/146a0a5e-1890-46db-b9d0-32d4b79323cf" />

<img width="600" height="300" alt="image (8)" src="https://github.com/user-attachments/assets/c4290520-67ea-4309-bdac-46962dd032e7" />

- 최적화 전후 Confusion Matrix

<img width="600" height="300" alt="image (9)" src="https://github.com/user-attachments/assets/587a0b76-0140-4334-9fb9-91c74cedea1f" />

<img width="600" height="300" alt="image (10)" src="https://github.com/user-attachments/assets/b0b2352a-6e30-4e23-9653-fbf07414a87c" />

- 최적화 전후 ROC curve

<img width="913" height="785" alt="image (11)" src="https://github.com/user-attachments/assets/965baa5d-b822-4517-9b52-ebb03cec8f5e" />

<img width="912" height="775" alt="image (12)" src="https://github.com/user-attachments/assets/deaf7b5c-b306-4d53-89c8-1a206d76465a" />

- 결정트리 시각화

<img width="1465" height="687" alt="image (13)" src="https://github.com/user-attachments/assets/6e1fe8fb-286c-46a7-ade1-a07d18631099" />


최적화 전에는 전체적인 정확도가 `0.62`로 비교적 낮았습니다.
최적화 후에는 Optuna가 정확도를 높이는 방향으로 매개변수를 탐색하다 보니까 비율이 높은 Class 0을 더 많이 맞히는 쪽으로 최적화가 일어났습니다.
그 결과 Class 0의 Recall이 `0.72`에서 `0.96`까지 올랐지만 Class 1의 Recall은 `0.38` 에서 `0.10`으로 떨어졌습니다.
확실한 상황이 아니면 Class 1로 분류하지 않게 되었음을 의미합니다.
재현율과 정밀도를 함께 높이지 못하는 Precision-Recall Trade-off현상을 확인할 수 있었습니다.

### RF

---

- 최적화 전후 분류 레포트
<p align="center">
<img width="500" height="auto" alt="image (14)" src="https://github.com/user-attachments/assets/ef1ec4a7-449e-4ac0-b41a-fb545128140a" />
<img width="500" height="auto" alt="image (15)" src="https://github.com/user-attachments/assets/3081e87b-e99c-4ee5-a6d3-1aed41d0ab46" />
</p>
- 최적화 전후 ROC curve
<p align="center">
<img width="300" height="auto" alt="image (16)" src="https://github.com/user-attachments/assets/699f72f3-8d22-47f2-84a9-d70b36f09815" />

<img width="300" height="auto" alt="image (17)" src="https://github.com/user-attachments/assets/bee9b4f5-b85c-46ad-a0fd-86b6396db4f9" /> 다시 최적화 수행 (recall 을 높이도록)
</p>
최적화 후 Class 1의 정밀도가 `0.52`에서 `0.62`로 올랐습니다.
반면 재현율은 `0.10`에서 `0.05`로 떨어졌습니다.
Precision-Recall Trade-off 현상을 확인할 수 있었습니다.
재현율이 지나치게 낮아 모델을 학습시키는 의미가 없다고 판단했습니다.
따라서 recall을 높이는 쪽으로 다시 한 번 최적화를 시도해봤습니다.
class1에 가중치를 높이고 목적함수를 f1-score로 설정했습니다.

<img width="705" height="287" alt="image (19)" src="https://github.com/user-attachments/assets/dde15d84-eaa0-44ba-955f-148371859101" />

<img width="716" height="312" alt="image (18)" src="https://github.com/user-attachments/assets/0a86d731-0aca-48c4-9ec5-ce32da4f7883" />

가장 큰 성과는 Class 1의 Recall을 `0.05`에서 `0.64`까지 끌어올렸다는 점입니다.
하지만 나머지 지표들이 대부분 하락하여 여전히 모델은 무의미했습니다.
Class 0의 recall(`0.99` -> `0.61`), f1-score(`0.83` -> `0.69`)이 하락하였고
Class 1의 precision(`0.62` -> `0.39`)도 하락했습니다.
accuracy도 `0.72` 에서 `0.61` 로 하락해 모델은 여전히 낮은 성능을 보였습니다.

# XGBoost

### 각 하이퍼 파라미터 설정값
<table style="width: 100%;">
  <tr>
    <td align="center"><b>일반 학습 파라미터</b></td>
    <td align="center"><b>L1 규제 파라미터</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/579d7ea6-72e9-4a83-a39e-2b28079cc646" width="100%"></td>
    <td><img src="https://github.com/user-attachments/assets/9898f484-98d1-4872-ba29-7d978d4dcc3b" width="100%"></td>
  </tr>
  <tr>
    <td align="center"><b>Elastic Net 파라미터</b></td>
    <td align="center"><b>Optuna 최적화 파라미터</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/abbe4f98-b4c7-4dd8-bdaf-383f42b0dbe8" width="100%"></td>
    <td><img src="https://github.com/user-attachments/assets/33cd5ea5-9db6-4348-ade4-f5ebf2e43420" width="100%"></td>
  </tr>
</table>


 XGBoost  모델의 하이퍼 파라미터 튜닝 과정입니다. 초기 베이스라인 모델 설정 후, 특성이 65개로 많은 점을 고려해 모델의 복잡도를 제어하고 일반화 성능을 확보하기 위해 L1 규제(`reg_alpha`)와 L2 규제(`reg_lambda`)를 병행하는 Elastic Net 방식을 적용하여 과적합을 방지하였습니다. 이후 Optuna를 활용하여 194개의 에스티메이터(`n_estimators`)와 학습률(`learning_rate`), 트리 깊이(`max_depth`) 등의 핵심 하이퍼파라미터를 ROC-AUC 지표 기준으로 최적화하였습니다. 그 결과, 전체 데이터에 대해 72%의 정확도를 달성하였으며, 가장 높은 값의 ROC-AUC 지표를 뽑아낼 수 있었습니다.

### 정확도

일반 진행 / L1규제 (reg_alpha=10)

![image.png](attachment:ba58027a-cd38-4728-8284-8a44f4aa9ed4:image.png)

![image.png](attachment:244b3ef6-4d39-4d36-87af-c4691c5f7984:image.png)

Elastic Net 규제 / Optuna 최적화

![image.png](attachment:afaa9faa-f11b-4695-940d-f85517aefccd:image.png)

![image.png](attachment:27a317cd-d1e7-40f2-a532-eb6d0161b600:image.png)

본 실험에서는 XGBoost 모델을 기반으로 일반 학습부터 L1 규제, Elastic Net, 그리고 Optuna를 이용한 베이지안 최적화까지 단계별 고도화를 수행하였습니다. 분석 결과, **Optuna 최적화 모델이 훈련 정확도(Train Accuracy) 0.742를 기록**하며 가장 높은 학습 효율을 보였는데, 이는 최적화 과정에서 도출된 하이퍼파라미터 조합이 데이터 내의 복잡한 비선형 관계를 효과적으로 포착했음을 의미합니다. 특히 2만 개 이상의 고차원 피처셋임에도 불구하고 강한 L1 규제(`reg_alpha: 10`)보다 Optuna의 미세 조정 조합이 선택된 것은, 변수를 강제로 제거하여 정보 손실을 초래하기보다는 트리 깊이(`max_depth: 4`)와 분할 조건(`min_child_weight: 6`)을 통해 모델 복잡도를 간접적으로 제어하는 방식이 본 데이터셋의 일반화 성능 확보에 더 적합했기 때문으로 분석됩니다. 최종 테스트 정확도가 0.719 수준에서 안정화되고 후에 나올 Recall이 1.5배 증가한것은 모델이 과적합(Overfitting)을 성공적으로 억제하면서도 예측의 견고함(Robustness)을 확보했음을 입증하는 결과입니다.

### 특성 중요도

![image.png](attachment:c788ce37-7f5c-4ab9-96f7-7979f5bf3eb9:image.png)

![image.png](attachment:960be8f7-24ce-4827-942d-345ca0be0b02:image.png)

![image.png](attachment:d2c770ea-19c6-490b-91e2-9eab9053061a:image.png)

전체 특성 중요도를 뽑아보면 확실히 L1 규제를 가했을때 중요도가 떨어지는 특성들이 가중치가 0이 되는 모습을 확인할 수 있습니다. 

아래는 특성이 많아 상위 7개 특성만 뽑아 분석하였습니다.

![XGBoost_Optuna_feature_importance.png](attachment:4e3b7145-78ac-4e7c-92ce-49a5e5e2e3b9:XGBoost_Optuna_feature_importance.png)

![image.png](attachment:076b56ab-5f05-4fa9-acf1-9e27752ab603:image.png)

![XGBoost_L1_top7_importance.png](attachment:e0edf7fb-3b0d-436a-b55c-cdcfbe94364a:XGBoost_L1_top7_importance.png)

![XGBoost_Elastic_top7_importance.png](attachment:8069b34c-4a19-43ae-bab5-f880484c52c4:XGBoost_Elastic_top7_importance.png)

![XGBoost_Optuna_top7_importance.png](attachment:e65f726a-1b66-4f0b-80d7-c1ee5eb54d26:XGBoost_Optuna_top7_importance.png)

모든 모델 아키텍처에서 **'CurrentEquipmentDays(장비 사용 기간)'**와 **'MonthsInService(서비스 유지 기간)'**가 압도적인 중요도를 기록하며 고객 이탈을 결정짓는 핵심 지표임을 재확인하였습니다. 특히 일반 학습 모델에 비해 **L1 규제와 Elastic Net 모델**에서는 'CurrentEquipmentDays'의 중요도 수치가 약 0.13까지 증가하였는데, 이는 규제 적용 과정에서 변별력이 낮은 피처들이 정제되면서 실제 이탈과 직결된 주요 변수들의 영향력이 더 선명하게 드러난 결과로 해석됩니다. 반면 **Optuna 최적화 모델**의 경우, 특정 변수에만 가중치가 쏠리지 않도록 파라미터가 조정되면서 'CreditRating(신용 등급)'과 같은 새로운 변수가 상위권에 진입하는 등 데이터의 다양한 측면을 고르게 반영하여 예측의 견고함을 높였습니다. 결론적으로 본 모델들은 사용 기간과 장비 노후화라는  특성을 중심으로 이탈 징후를 포착하고 있으며, 하이퍼파라미터 최적화를 통해 단순 성능 수치를 넘어 변수 간의 균형 잡힌 해석력을 확보한 것으로 평가됩니다.

### Confusion Matrix

![image.png](attachment:98088664-08d3-4450-8bf5-54da0caef21d:image.png)

일반 학습

![image.png](attachment:c29bcaa8-25cc-4ee3-a10c-a8ba13bed6b2:image.png)

Elastic Net

![image.png](attachment:4e4c3ebf-d47c-4b41-9d1d-b0c83c5e1382:image.png)

L1 규제

![image.png](attachment:1ea365f6-b6c2-4338-b2ab-228a34bc6373:image.png)

Optuna 파라미터 적용 후

![XGBoost_1_confusion_matrix.png](attachment:4b190280-eead-4773-b345-07f02399e8bb:XGBoost_1_confusion_matrix.png)

![XGBoost_L1_confusion_matrix.png](attachment:73a21b8d-bc87-4b99-a49a-ce39010cfed3:XGBoost_L1_confusion_matrix.png)

![XGBoost_Elastic_confusion_matrix.png](attachment:b0b69289-91af-4149-b45b-12869bbfa943:XGBoost_Elastic_confusion_matrix.png)

![XGBoost_Optuna_confusion_matrix.png](attachment:747c9233-8193-4e9b-812f-7fbad99ea36a:XGBoost_Optuna_confusion_matrix.png)

각 모델의 혼동 행렬을 분석한 결과, **Optuna 최적화 모델**이 실제 이탈자(Class 1)를 찾아내는 능력이 가장 우수한 것으로 나타났습니다.

- **이탈자 포착 능력 향상**: 일반 학습 및 규제 모델들은 실제 이탈자 2,844명 중 약 170~200명(약 6~7%)만을 정답으로 맞혔으나, **Optuna 모델은 306명을 적중**시키며 탐지 능력을 약 **1.5배 이상 끌어올렸습니다.**
- **오분류 특성**: 모든 모델이 '유지 고객(Class 0)'에 대해서는 98% 이상의 압도적인 정답률을 보이지만, '이탈 고객'에 대해서는 보수적으로 예측하는 경향이 있습니다.
- **최적화의 의의**: 정확도(Accuracy) 수치는 비슷해 보일지라도, Optuna를 통해 하이퍼파라미터를 미세 조정함으로써 **불균형 데이터 환경에서 이탈 고객에 대한 민감도(Recall)를 개선**했다는 점이 이번 분석의 핵심 성과입니다.

### ROC /AUC

![XGBoost_1_ROC_curve.png](attachment:1e65255a-e369-48d1-b889-7dddf6e7901b:XGBoost_1_ROC_curve.png)

일반학습 AUC : 0.66569

![XGBoost_L1_ROC_curve.png](attachment:cfcd7178-c43b-4aaf-89d3-d6dd752a2555:XGBoost_L1_ROC_curve.png)

L1규제 AUC : 0.66565

![XGBoost_Elastic_ROC_curve.png](attachment:ab186e90-faf5-4a7c-9fed-167a66de28ab:XGBoost_Elastic_ROC_curve.png)

![XGBoost_Optuna_ROC_curve.png](attachment:c2d2c352-9b9d-491d-8c54-d2657225f9eb:XGBoost_Optuna_ROC_curve.png)

Elastic Net AUC : 0.66649                                             Optuna AUC : 0.67120

전체 모델의 ROC 커브를 분석한 결과, 일반 학습과 규제 모델(L1, Elastic Net)은 모두 **0.66 수준의 AUC**를 기록하며 정체된 성능을 보였으나, **Optuna 최적화 모델은 0.6712**로 가장 높은 수치를 달성하며 모델의 전반적인 판별 성능을 유의미하게 개선했습니다. 특히 L1 규제와 Elastic Net 모델은 일반 모델 대비 AUC 수치가 거의 동일하거나 미세하게 낮은 양상을 보이는데, 이는 규제 적용이 단순히 과적합을 억제할 뿐 클래스 간의 이진 분류 성능(Separability) 자체를 끌어올리지는 못했음을 시사합니다. 일반 학습과 규제 모델들은 AUC 0.66 수준에서 정체되어 분류 임계값 변화에 따른 변별력을 충분히 확보하지 못했으나, **Optuna 최적화 모델은 소폭 상승한 0.6712**를 기록하며 상대적으로 가장 진전된 판별 성능을 보여주었습니다. 이는 규제 적용만으로는 한계가 있었던 클래스 분리 능력을 베이지안 최적화 기반의 파라미터 미세 조정을 통해 미미하게나마 개선할 수 있었음을 보여줬습니다. 비록 비즈니스에 즉시 투입하기엔 변별력이 다소 부족한 수치이지만, Optuna를 통한 튜닝 과정이 모델을 무작위 추측 단계에서 벗어나 유의미한 예측 방향성을 갖게 하는 최적의 지점을 도출했음을 보여줍니다.

# 추가) DeepLearning (MLP)

가볍게 배운 DeepLearning MLP 구조로 학습을 진행해봤습니다. 배치 사이즈 , learning rate, dropout_rate, hidden_dim 을 조절해가며 진행하다 roc_auc를 평가지표로 optuna를 진행하였습니다.

### Optuna가 찾은 최적의 하이퍼 파라미터

![image.png](attachment:5fbc79f9-09fd-4b44-98f8-f2a7e3a63708:image.png)

딥러닝 기반의 MLP 모델을 구축하며 Optuna를 통해 구조적 최적화를 수행한 결과, 위와 같은 하이퍼 파라미터들이 도출되었습니다. 먼저 학습률(`lr`)이 **0.0015** 수준으로 낮게 설정된 것은 손실 함수(Loss Function)의 국소해(Local Minimum)에 빠지지 않고 안정적으로 수렴하기 위한 선택으로 풀이되며, 배치 사이즈 또한 비교적 크고, 은닉층의 크기(`hidden_dim`)를 **142**로 구성하여 데이터의 비선형적 특징을 충분히 학습할 수 있는 용량을 확보하였습니다. 또한, **30.2% 수준의 드롭아웃(`dropout_rate`)**을 적용함으로써 고차원 데이터에서 발생하기 쉬운 노드 간의 과도한 상호의존성을 차단하고 일반화 성능을 높였습니다. 결과적으로 이러한 하이퍼파라미터 구성은 단순 수치 최적화를 넘어, 신경망이 통신사 이탈 데이터의 불규칙한 패턴을 편향 없이 학습할 수 있는 최적의 아키텍처를 형성하고 있음을 보여줍니다.

### 정확도

![image.png](attachment:00ed4b09-4f99-4307-9c68-c48180279c67:image.png)

딥러닝 기반의 MLP 모델을 구축하여 최적화를 진행한 결과, **훈련 정확도 0.7303, 테스트 정확도 0.7161**을 기록하며 머신러닝 모델(XGBoost Optuna: 0.719) 대비 소폭 낮은 정확도를 보였습니다. 이는 정형 데이터 분석에 특화된 트리 기반 앙상블 모델에 비해, 신경망 구조가 고차원 피처(2만 개 이상) 간의 상관관계를 해석하는 데 있어 상대적으로 더 많은 학습 데이터나 정교한 아키텍처 설계를 필요로 하기 때문으로 분석됩니다. 하지만 **Optuna**를 통해 도출된 **142차원의 은닉층(Hidden Layer)**과 **0.302의 드롭아웃(Dropout)** 적용은 모델이 단순 암기(Overfitting)를 지양하고 일반화된 패턴을 학습하도록 유도하였으며, 훈련과 테스트 점수 간의 격차를 최소화함으로써 딥러닝 모델 특유의 안정적인 예측 변별력을 확보했다는 점에 의의가 있습니다.

### 특성 중요도 (Permutaion Method 방식으로)

![image.png](attachment:e5c2e364-f3a4-4fd3-bdba-df1651db4e3b:image.png)

- **통화량 변화 민감도**: 트리 모델과 달리 **'PercChangeMinutes(통화량 변화율)'**와 **'MonthlyMinutes(월 사용 분수)'**가 압도적인 1, 2위를 기록하며 이탈 예측의 핵심 지표로 나타났습니다.
- **신경망 특유의 해석**: 장비 사용 기간에 집중하던 머신러닝 모델과 달리, MLP는 실질적인 **통화 패턴의 변화와 품질(DroppedCalls)** 등 비선형적 요소를 더 민감하게 포착하여 분석했습니다.
- **서비스 지속성**: **'MonthsInService'**와 **'RetentionCalls'** 역시 상위권에 위치하여, 고객의 서비스 유지 기간과 고객 센터 접촉 이력이 이탈 판단에 중요한 근거가 됨을 확인했습니다.
- **결론**: MLP는 수치형 데이터의 미세한 변동을 학습하여 머신러닝 모델이 놓칠 수 있는 행동 패턴 기반의 이탈 징후를 보완적으로 제시해주고 있습니다.

![image.png](attachment:a29d4248-088a-4927-9773-dc6eb19ff5b6:image.png)

딥러닝(MLP) 모델의 **Confusion Matrix** 분석 결과입니다.

- **이탈자 탐지 성능**: 실제 이탈자 2,844명 중 **268명을 정확히 예측**해냈으며, 이는 일반 XGBoost 모델(199명)보다 우수하고 Optuna 최적화 모델(306명)에 근접한 수치입니다.
- **예측 성향**: 유지 고객(Class 0)에 대해서는 **6,861명을 정답**으로 맞히며 매우 높은 정확도를 유지하지만, 이탈 고객에 대해서는 다소 보수적으로 판단하는 경향이 관찰됩니다.
- **오분류 특성**: 이탈하지 않은 고객을 이탈로 잘못 판단한 오답(False Positive)은 **251건**으로, 전반적인 모델 안정성을 저해하지 않는 수준에서 관리되고 있습니다.
- **종합 평가**: 머신러닝 모델과 비교했을 때, 딥러닝 특유의 비선형 학습을 통해 **이탈 징후가 뚜렷한 소수 고객층을 효과적으로 선별**해내고 있음을 보여줍니다.

### ROC AUC

![image.png](attachment:dde844ab-9e0c-44cc-8b02-eb354017572c:image.png)

DeepLearning MLP : 0.65012

**판별 능력 (AUC 0.65)**: MLP 모델은 **AUC 0.65**를 기록하며 XGBoost(0.67) 대비 다소 낮은 판별력을 보였습니다. 이는 정형 데이터의 복잡한 규칙을 파악하는 데 있어 트리 기반 앙상블 모델이 소폭 유리함을 시사하지만, 신경망 또한 비슷한 성능을 유지하고 있습니다.

# SVM

### 기초 LinearSVC

![image.png](attachment:df60c819-af6f-49e4-afed-e376a61bdd95:image.png)

![image.png](attachment:4f0839a9-ad6e-425c-bf0e-21d180e14b57:image.png)

Train Accuracy: 0.712

Test Accuracy: 0.715

![image.png](attachment:c548eaf7-58b8-472d-b6b9-34c1b29b60f6:image.png)

![unbalanced_cfMatrix.png](attachment:05c576b1-8ff6-4f6b-b2ff-3f17eade4885:unbalanced_cfMatrix.png)

- ROC-AUC Score: 0.6157365356934609

![unbalanced_AUC.png](attachment:f12bf2b3-b632-44f9-b64e-f0d4ae8c0166:unbalanced_AUC.png)

- random_state를 제외한 나머지 하이퍼 파라미터를 기본값으로 학습
- **Accuracy:** Train set과 Test set 모두 0.71의 값을 보여주는 준수한 모습
- **Recall:** 실제 이탈자(Class 1)에서 0.02의 무의미한 값을 보여줌
    
    → 모델이 실제로 ‘학습’을 진행하지 않은 것으로 판단, 하이퍼 파라미터를 이용하여 어느정도 조정을 진행함
    

### Balanced SVM

![image.png](attachment:f81f89ba-2a91-444c-b4ad-96b7cac3e9c5:image.png)

![image.png](attachment:0eff9338-d4a2-4f5e-80dc-6255cf4b789a:image.png)

Train Accuarcy : 0.588
Test Accuarcy : 0.590

![image.png](attachment:7c061c28-f3fe-4355-b5ec-37c4b39ea7b8:image.png)

![balanced_cfMatrix.png](attachment:19c5da99-1367-41f1-9a0b-c55188a3f8d4:balanced_cfMatrix.png)

ROC-AUC Score: 0.615243366474203

→ 오히려 0.0005 떨여졌다

![balanced_AUC.png](attachment:96ec4ce8-b832-4dcc-abf8-1a19487ef91a:balanced_AUC.png)

- class_weight를 ‘balanced’로 두어 모델이 편향
    - class_weight: 소수 클래스 데이터의 무게를 무겁게 설정하여 균형있게 학습을 가능하게 해준다
- **Accuracy**: 0.71 → 0.58~0.59로 크게 줄어들었다
- **Recall:** 0.58로, 이전 사실상 이탈자를 잡지 못하던 것에 비해 크게 값이 커짐
    - Accuracy와 AUC도 중요하지만 recall이 더 중요하다고 판단, 이후 과정에서도 전부 class_weight=’balanced’로 진행

### Lasso 규제

![image.png](attachment:295e84dc-e033-4ed7-896d-1bee74d7b983:image.png)

![image.png](attachment:24ba5039-c3f3-44f9-bade-77844aa1de26:image.png)

L1 Train Accuarcy : 0.588
L1 Test Accuarcy : 0.590

![image.png](attachment:4e503372-4a7a-4ad0-9f12-07aa050c980f:image.png)

![L1_cfMatrix.png](attachment:8ab0de80-9fbb-42af-9edd-72b420471e93:L1_cfMatrix.png)

![L1_AUC.png](attachment:b1ce815e-e2e4-4240-b6fe-010c912bdb84:L1_AUC.png)

![image.png](attachment:50033b97-9a18-4f69-9602-aebceb0f8806:image.png)

ROC-AUC Score: 0.6156943259385665

→ 현재까지 중 가장 높은 수치 (기본 SVM보다 0.0002 높음)

- penaly를 ‘l1’으로 두고서 Lasso 규제를 진행하였고, 결과적으로 19개의 feature가 제외되었다.
    - feature를 제외함으로써 AUC와 accuracy가 소폭 상승하였음
- **Accuracy:** 0.0007 가량 높아졌으나 눈에 띄는 향상은 없었다.
- **Recall:** 0.58로, 마찬가지로 큰 변화는 없었다.
- Confusion matrix의 값이 미세하게 변하였으나 사실 상 그 외 precision과 accuracy는 변화가 없었다

### 특성 중요도

L1으로 feature를 제외 전/후 비교

![balanced_FeatureImportance.png](attachment:463d66e4-8e3f-4c4a-ac49-f7c0d35f2c51:balanced_FeatureImportance.png)

![L1_FeatureImportance.png](attachment:51fe56dd-b1f7-407d-a3b1-7868e355247a:L1_FeatureImportance.png)

고찰 

- MadeCallToRetentionTeam: 압도적 1위 였으나, 규제를 통해 사라짐

→ retention team에 연락하는 것은 이미 이탈을 결정하고, 연락하는 것으로 볼 수도 있지 않을까?

→ 열 자체가 이탈 징후/원인 보다는 결과에 가까운 값으로 보임

- CurrentEquipmentDays: 계속해서 최상위권에 존재함

→ 단말기를 바꿀 때가 된 사람이 기기 변경을 하며 타 통신사로 이동하는 경향이 높다고 볼 수 있음

- PercChangeMinutes: 상위 5개에 포함되지 않던 값이 상위권에 들어옴

→ 모델이 고객의 ‘추세’에 집중하게 된 것으로 보임

### Optuna

LinearSVC 모델에서는 조절 가능한 하이퍼파라미터 수가 적었음

- penalty: 규제의 종류(Lasso/Ridge)
- C: 규제 강도
- loss: 손실함수
- class_weight: 클래스별 가중치 조절

이 중 recall의 값 유지를 위한 class_weight는 고정, 기준이 될 손실함수는 roc_auc로 고정해두었다.

즉, 규제와 규제 강도만을 optuna를 통해 튜닝 하였다.

![image.png](attachment:53e103e6-b583-48aa-87ae-b934417dc685:image.png)

**결과**

best params: {'C': 0.0003895631989094481, 'penalty': 'l2'}

best AUC: 0.6148503968659134

![image.png](attachment:1552e121-ee15-4f79-8864-ba20e117aab5:image.png)

![image.png](attachment:b58f6144-7ebe-4c4b-92ac-ed2833e2620b:image.png)

Optuna Train Accuarcy: 0.587833494053359
Optuna Test Accuarcy: 0.5908068145290903

![image.png](attachment:0213ff21-42a9-4e64-a2d3-8db6c436904e:image.png)

![optuna_cfMatrix.png](attachment:b7959e7a-76f4-4654-96ce-128dd61f46b2:optuna_cfMatrix.png)

![optuna_AUC.png](attachment:cacdf11a-b899-455d-84c1-64ec60a88b36:optuna_AUC.png)

ROC-AUC Score: 0.6159611553023353
→ 하이퍼 파라미터 튜닝을 진행한 만큼 가장 높은 AUC 값을 가진다.

→ 최소값 보다 0.0007 증가

- penaly가 ‘l2’, optuna를 진행하여 모든 feature를 다 사용하였을 때 더 높은 성능을 보여주는 것을 확인하였다
- accuracy, confusion matrix, precisioni, recall 모두 소폭의 변화만 있었을 뿐, 유의미한 성능 향상을 보여주지 않는 것으로 판단하였다

# CatBoost

### 범주형 변수 데이터 타입 변환

![image.png](attachment:99e774fc-6178-461c-a441-311aa2ed48f7:image.png)

![image.png](attachment:7636e0e2-d6a4-4459-b459-80d78b457198:image.png)

CatBoost 모델 특징에 맞춰 범주형 변수의 데이터 타입을 정수형으로 변환

### CatBoost 1차 모델 학습

 

![image.png](attachment:9bf02bc5-eb63-4a1e-99f1-2f5072ab68df:image.png)

![image.png](attachment:a36e9237-55ee-4734-af93-1f4bd90cf59e:image.png)

![image.png](attachment:6597f456-b0f1-44a3-8433-ee58a3dacbae:image.png)

test: 훈련용 데이터셋에 대한 AUC

test1: 테스트 데이터셋에 대한 AUC

### CatBoost 1차 모델 평가

**ROC-AUC 커브**

![image.png](attachment:fdd4e608-7700-45c2-8950-3d5d9770bdd0:image.png)

**Confusion Matrix**

![image.png](attachment:57cb2730-c102-464f-8789-e8501b337916:image.png)

![image.png](attachment:fe6b7cc8-5274-4478-9a88-d904ad872823:image.png)

**정확도**

- 하이퍼파라미터 튜닝을 진행하지 않은 기본 모델임에도 불구하고, 훈련 정확도(Train Accuracy) 0.743, 테스트 정확도(Test Accuracy) 0.727 수준을 기록하며 과적합 없이 안정적인 학습 능력을 보여주었습니다.

**Confusion Matrix 분석**

- **유지 고객(Class 0) 과적합성 예측:** 모델이 유지 고객에 대해서는 97%의 압도적인 재현율을 보이며, 대부분의 고객을 '이탈하지 않을 것'으로 방어적이고 보수적으로 예측하는 경향이 뚜렷했습니다.
- **치명적으로 낮은 이탈자 재현율(Recall):** 전체 테스트 데이터 중 실제 이탈자(Class 1) 4,277명에 대해 모델이 정답을 맞힌 비율(Recall)은 **약 12% 수준**에 불과했습니다.
- **결론 및 Next Step:** 이탈 예측 모델의 핵심 목적은 **실제 이탈할 고객을 최대한 많이 찾아내어 사전에 방어 조치를 취하는 것**입니다. 현재의 베이스라인 모델은 전반적인 성능 수치는 높을지언정, 정작 가장 중요한 '이탈자'를 88%나 놓치고 있어 실질적인 비즈니스 활용이 불가능하다고 판단했습니다.

**특성 중요도 분석**

![image.png](attachment:191bb0c2-4055-4719-ba0b-7a45ad98fe8e:image.png)

**핵심 지표 및 행동 패턴 포착:** 타 모델들과 마찬가지로 **MonthsInService(서비스 유지 기간)**와 **CurrentEquipmentDays(장비 사용 기간)***를 가장 강력한 이탈 요인으로 꼽았습니다. 더불어 PercChangeMinutes(통화량 변화율)와 MonthlyMinutes(월 사용 분수) 역시 높은 중요도를 기록했는데, 이는 장비의 노후화뿐만 아니라 고객의 '실제 통화 패턴 변화'라는 행동적 특성까지 기본 모델에서부터 균형 있게 학습하고 있음을 보여줍니다.

### **L1 규제 대안 평가 및 전체 특성 유지(Feature Retention) 전략**

**1. Feature Selection 실험 배경**

- 앞선 XGBoost 모델에서는 66개 고차원 특성으로 인한 과적합을 제어하고자 L1 규제(reg_alpha)를 적용해 가중치를 강제로 압축했습니다.
- 본 CatBoost 모델에서는 L1 규제와 같이 수학적인 페널티를 주는 대신, 실제 타겟 변수와 연관성이 낮아 노이즈로 작용할 수 있는 하위 특성들을 단계적으로 제거(Feature Elimination)하며 모델이 어떻게 반응하는지 실험을 진행했습니다.

**2. 실험 결과 및 성능 검증**

![image.png](attachment:1d3326dc-c9c9-4aa6-ae4b-e5c6f5d6643c:image.png)

bestTest = 0.6830251824

![image.png](attachment:7f97dcfa-a69b-4c18-8709-03c2aebf8859:image.png)

bestTest = 0.6834692785

![image.png](attachment:26df029c-16cb-4d1c-85a0-804f65d70009:image.png)

bestTest = 0.6827287087

- 자체적인 Feature Selection 기법을 적용하여 특성을 대폭 축소해 보았으나, 전체 데이터를 모두 사용했을 때와 비교하여 **정확도(Accuracy) 및 ROC-AUC 성능 지표에 유의미한 차이나 성능 향상이 발생하지 않았습니다.**

**3. 최종 인사이트**
본 분석에서는 실험 결과를 바탕으로 피처를 인위적으로 제거하지 않고 **65개의 전체 피처를 그대로 유지하여 학습을 진행**하는 전략적 결정을 내렸습니다. 그 이유는 다음과 같습니다.

- **미세한 고객 행동 패턴의 유실 방지:** 전체 데이터 관점에서는 중요도가 낮은 특성(예: 특정 직업군, 자녀 유무 등)일지라도, 특정 소수 고객 그룹에게는 이탈을 암시하는 핵심적인  정보일 수 있습니다.
- **비즈니스 목적에 부합:** 특성 축소로 인한 성능 이득이 없는 상황에서 변수를 강제로 제거하는 것은, 자칫 모델이 다양한 고객의 행동 맥락을 학습할 기회를 박탈하는 정보의 손실로 이어질 위험이 크다고 판단했습니다.

## CatBoost 하이퍼파라미터 튜닝 및 최종 모델 최적화 결과

**1. 최적화 배경 및 튜닝 전략**
앞선 베이스라인 모델은 전반적인 정확도와 AUC는 우수했으나, 데이터 불균형으로 인해 실제 이탈자의 탐지 비율(Recall)이 현저히 낮다는 치명적인 한계가 있었습니다. 이에 따라 본 튜닝 단계에서는 **'실제 이탈할 고객을 최대한 많이, 정확하게 찾아내는 것'**을 최우선 비즈니스 목표로 설정하고 다음 두 가지 전략을 실행했습니다.

- **불균형 데이터 제어:** CatBoost 모델 내부에 'auto_class_weights': 'Balanced' 옵션을 적용하여 이탈 고객(Class 1)에 대한 모델의 민감도를 강제로 높였습니다.
- **구조적 파라미터 최적화:** Optuna를 활용해 트리의 깊이(depth), 학습률(learning_rate), L2 정규화(l2_leaf_reg) 등의 파라미터를 1,000번 반복(Iterations)하며 베이지안 최적화 탐색을 진행했습니다.

**2. 도출된 최적 파라미터**

![image.png](attachment:3b75b155-b2e9-4561-b0a3-588a76273b06:image.png)

Best AUC: 0.6857904757843397
Best params: {

'depth': 6, 

'learning_rate': 0.028124781194669244, 

'l2_leaf_reg': 5.691073892881603, 'random_strength': 0.20531112463660664, 

'bagging_temperature': 0.81735113850536, 

'rsm': 0.6236002964928216, 

'min_data_in_leaf': 68

}

- 30번의 Optuna 탐색 결과, **`[depth: 6, learning_rate: 0.028, l2_leaf_reg: 5.69]`** 수준에서 최적의 파라미터 조합이 도출되었습니다.

 **3. 최종 모델 평가**

**ROC-AUC Curve**

![image.png](attachment:4ae7129e-e3d7-4f13-a389-ca564f66b1b0:image.png)

- 최적화 후 검증 데이터 기준 ROC-AUC 지표는 기존 0.683에서 **0.6858**로 소폭 상승했습니다.

**Confusion Matrix**

![image.png](attachment:ba1b3deb-0ea8-4720-b0ad-fec37740a438:image.png)

![image.png](attachment:6703c8b9-ab28-4469-8a40-dc01e700aaa7:image.png)

- 훈련 정확도 0.690, 테스트 정확도 0.632를 기록하며 기존 베이스라인(0.727) 대비 전체 정확도는 다소 하락했습니다.
- **이탈자 탐지 능력(Recall)의 향상:** 베이스라인에서 극히 저조했던 이탈자 재현율이 튜닝 후 **65%**로 대폭 상승했습니다. 실제 이탈자 2,852명 중 약 1,854명가량을 정확히 예측해 낸 결과입니다.

# LightGBM

**LightGBM은 데이터에서 성능과 학습 속도가 안정적인 부스팅 모델이라, 최종 후보로 두고 베이스라인→규제→Optuna 순으로 개선했습니다.**

또한 이탈 데이터는 불균형이라 Accuracy만 보면 착시가 생길 수 있어, ROC-AUC와 Confusion Matrix(이탈 탐지 성능)를 같이 확인했습니다.

### 1) Baseline (class_weight=balanced, early stopping)

- **ROC-AUC: 0.6832 / Accuracy: 0.62**
- 이탈(Class 1) 기준 **Recall : 0.66 / F1 : 0.50**
    
    ![스크린샷 2026-02-24 023621.png](attachment:3f5b9034-82cd-417e-963a-30b0162ee6a4:스크린샷_2026-02-24_023621.png)
    
    ![image.png](attachment:978e8c1c-d419-455f-99b9-e62518471662:image.png)
    

→ 기본 설정의 경우 Recall(이탈 탐지율)은 0.66로 확보됐지만, Precision(타겟 적중률)이 0.40으로 오탐이 상대적으로 많은 것으로 확인

![LGBM_confusin_matrix.png](attachment:a670ad3a-27e2-4693-afe9-d5d79228fe7b:LGBM_confusin_matrix.png)

![LGBM_ROC_Curve.png](attachment:aeb0f7ed-ad14-4ddc-890f-266e87b9d152:LGBM_ROC_Curve.png)

### 2) 규제 적용(L1 / Elastic)

- **L1 ROC-AUC: 0.6833 / Accuracy: 0.63 / Recall: 0.63 / F1: 0.49**
- **Elastic ROC-AUC: 0.6830 / Accuracy: 0.62 / Recall: 0.64 / F1: 0.49**
    
    ![image.png](attachment:d4e103f5-b317-4b14-a75e-210b5342d85e:image.png)
    
    ![스크린샷 2026-02-24 024215.png](attachment:48af0b2e-5fc0-4d80-afb2-6f173e99ea13:스크린샷_2026-02-24_024215.png)
    
    ![스크린샷 2026-02-24 024756.png](attachment:6c4a2aa4-30e7-480d-b268-f1c9b7e501ab:스크린샷_2026-02-24_024756.png)
    
    ![스크린샷 2026-02-24 024823.png](attachment:22589d5c-d4a2-428a-8e7a-48bd6a850644:스크린샷_2026-02-24_024823.png)
    
    → 규제 적용만으로는 **AUC가 거의 비슷한 수준**이라 성능 개선 폭이 크지 않았고, 대신 예측 안정성 확인 정도로 사용 후 다음 단계로 넘어감
    
    ![LGBM_L1_confusin_matrix.png](attachment:779cbf34-8bd3-4710-be38-bd566a999292:LGBM_L1_confusin_matrix.png)
    
    ![LGBM_Elastic_confusin_matrix.png](attachment:a70892ba-cac7-40a1-8ad9-5182e5bfd1d6:LGBM_Elastic_confusin_matrix.png)
    
    ![LGBM_L1__ROC_Curve.png](attachment:2e3f5ef4-3848-4623-8182-0c07a2530daa:LGBM_L1__ROC_Curve.png)
    
    ![LGBM_Elastic_Curve_optuna.png](attachment:be47e8c5-3502-4743-be41-cd2757ea7272:LGBM_Elastic_Curve_optuna.png)
    

### 3) Optuna 최적화(최종 후보)

- **ROC-AUC: 0.6874 / Accuracy: 0.64**
- **Recall 0.63 /  F1 0.50**
    
    ![스크린샷 2026-02-24 024913.png](attachment:2bb66d4d-124e-4f82-9aa3-98362a5f1e0a:스크린샷_2026-02-24_024913.png)
    
    ![image.png](attachment:6233f483-d614-4b75-8aa8-6b5a2d4cc34d:image.png)
    
    → AUC 개선 폭은 크지 않지만(0.683→0.687), 다른 설정(L1/Elastic)에서는 AUC가 정체되거나 소폭 하락한 것에 비해 좀 더 크게 상승된 것이 확인. 이탈 탐지 성능도 유지되어 최종 모델 후보로 선정
    
    ![LGBM(optuna)_top10_importance_optuna.png](attachment:ec3ad721-1279-4a7a-ab9a-c6b82161ee15:LGBM(optuna)_top10_importance_optuna.png)
    
    ![LGBM_Optuna_confusin_matrix_optuna.png](attachment:6605538e-c145-41c0-b45b-6c33223b86dc:LGBM_Optuna_confusin_matrix_optuna.png)
    
    ![LGBM_Optuna_ROC_Curve.png](attachment:8622c82d-e018-4b20-9c02-dff2507f7618:LGBM_Optuna_ROC_Curve.png)
    

![image.png](attachment:e17b9e65-9160-443a-a1ff-e84a76e3af2b:image.png)

1) CurrentEquipmentDays (기기 사용일수)

현재 단말을 얼마나 오래 썼는지를 나타내는 변수  = 
여러 트리 모델에서 1~2순위로 반복된 건, 기기 교체 주기/약정 갱신 시점이 churn을 강하게 가르는 신호일 수 있다고 예상

2) MonthsInService (가입 기간)

서비스 가입 후 경과 기간  = 가입 초기에는 이탈 위험이 상대적으로 높고, 어느 기간 이상 유지되면 안정화되는 경향이 있어 중요하게 나타나는 것으로 예상

3) PercChangeMinutes (사용량 변화율)

최근 통화 사용량이 전월 대비 변화 = 절대적인 사용량보다 갑작스러운 감소/변동이 이탈 직전에 나타나는 전조일 수 있기에 여러 모델에서 상위로 나타나는 것으로 예상

![image.png](attachment:616dd9d9-c9e6-4c81-9184-374175da1f03:image.png)

### 한계점

예측하기 어렵다. 다소 어려운 부분이 있다. 억지로 결론을 내지 말자

참고 정도는 가능한

특성 중요도 

장비 사용기간 < - 기기 변경 때 프로모션을  

# 9. 회고

- 김은우

두 번의 미니 프로젝트를 거치며 머신러닝의 고도화 기법과 딥러닝 MLP의 기초를 실무 통신사 데이터에 적용해 보았습니다. 특히 성능 지표를 단순 정확도로만 보는 것이 아니라, **Confusion Matrix와 ROC-AUC 곡선**을 통해 모델이 소수 클래스(이탈자)를 얼마나 정밀하게 판별하는지 심층적으로 이해할 수 있었습니다.

기술적으로는 **XGBoost 기반의 규제 모델(L1, Elastic Net)**과 **Optuna 하이퍼파라미터 최적화**를 비교하며, 모델의 복잡도와 일반화 성능 사이의 트레이드오프를 직접 체감했습니다. 또한, 트리 기반 머신러닝 모델은 '장비 사용 기간'과 같은 정적인 지표에 집중하는 반면, **MLP 딥러닝 모델은 '통화량 변화율' 등 비선형적 패턴**을 핵심 변수로 포착한다는 점을 확인하며 데이터 특성에 따른 모델 선택의 중요성을 배웠습니다.

협업 측면에서는 Git의 **Feature-Branch 전략**과 엄격한 **PR 규칙**을 준수하며 코드의 일관성을 유지했고, 모든 의사결정 과정을 **노션에 중앙화**하여 소통 비용을 획기적으로 줄였습니다. 단순한 구현을 넘어, 팀원들과 논리적인 근거를 바탕으로 최적의 모델을 합의해 나가는 과정이 가장 유익한 경험이었습니다.

---

# 참고

![image.png](attachment:5e71844d-1da1-4ea8-932b-b20083264c11:image.png)

![image.png](attachment:00a0c5cf-83f0-4925-9fb5-be69b431bfd9:image.png)

![XGBoost_Optuna_feature_importance.png](attachment:2b83d0ba-d8fe-4f19-9594-4fb3dea4b54f:XGBoost_Optuna_feature_importance.png)

