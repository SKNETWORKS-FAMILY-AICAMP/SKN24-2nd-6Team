import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
import os

ROOT_DIR = './../'

def print_header(title):
    print("\n" + "=" * 60)
    print(f"  {title}".center(60))
    print("=" * 60 + "\n")

def get_float_input(prompt, default_val):
    while True:
        user_input = input(f"🔹 {prompt} (기본값: {default_val}): ").strip()
        if not user_input:
            return default_val
        try:
            val = float(user_input)
            if 0 <= val <= 1:
                return val
            else:
                print("   [오류] 확률은 0.0과 1.0 사이의 값이어야 합니다.")
        except ValueError:
            print("   [오류] 올바른 숫자(소수) 형식을 입력해주세요.")

def get_int_input(prompt, default_val):
    while True:
        user_input = input(f"🔹 {prompt} (기본값: {default_val}): ").strip()
        if not user_input:
            return default_val
        try:
            val = int(user_input)
            if val >= 0:
                return val
            else:
                print("   [오류] 0 이상의 정수를 입력해야 합니다.")
        except ValueError:
            print("   [오류] 올바른 숫자(정수) 형식을 입력해주세요.")

def main():
    print_header("📡 통신사 기기변경 지원금 대상자 추출 시스템 📡")

    # 경로 설정
    model_path = ROOT_DIR + 'saved_models/catboost.cbm'
    test_data_path = ROOT_DIR + 'data/preprocessed/cell2cell_unscaled_test.csv'
    output_path = ROOT_DIR + 'data/preprocessed/subsidy_targets.csv'
    
    print(f"▶ [1/4] 모델 로드 중... ({model_path})")
    if not os.path.exists(model_path):
        print(f"\n❌ [오류] 모델 파일을 찾을 수 없습니다: {model_path}")
        return

    model = CatBoostClassifier()
    model.load_model(model_path)
    
    print(f"▶ [2/4] 데이터 로드 중... ({test_data_path})")
    try:
        df = pd.read_csv(test_data_path)
    except FileNotFoundError:
        print(f"\n❌ [오류] 데이터 파일을 찾을 수 없습니다: {test_data_path}")
        return

    original_df = df.copy()

    # 전처리 (temp.py 로직 반영)
    cat_features = [
        'ChildrenInHH', 'HandsetRefurbished', 'HandsetWebCapable', 'TruckOwner', 
        'RVOwner', 'BuysViaMailOrder', 'RespondsToMailOffers', 'OptOutMailings', 
        'NonUSTravel', 'OwnsComputer', 'HasCreditCard', 'RetentionCalls', 
        'RetentionOffersAccepted', 'NewCellphoneUser', 'NotNewCellphoneUser', 
        'ReferralsMadeBySubscriber', 'IncomeGroup', 'OwnsMotorcycle', 
        'AdjustmentsToCreditRating', 'HandsetPrice', 'MadeCallToRetentionTeam', 
        'CreditRating', 'Prizm_Other', 'Prizm_Rural', 'Prizm_Suburban', 'Prizm_Town', 
        'Occ_Clerical', 'Occ_Crafts', 'Occ_Homemaker', 'Occ_Other', 'Occ_Professional', 
        'Occ_Retired', 'Occ_Self', 'Occ_Student', 'Marital_No', 'Marital_Yes',
        'UniqueSubs', 'ActiveSubs', 'Handsets', 'HandsetModels'
    ]

    for col in cat_features:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)

    model_features = model.feature_names_
    
    for col in model_features:
        if col not in df.columns:
            df[col] = 0
            
    X_test = df[model_features]

    print("▶ [3/4] 고객별 이탈 확률 예측 중...\n")
    probabilities = model.predict_proba(X_test)[:, 1]
    original_df['ChurnProbability'] = probabilities

    print_header("⚙️ 대상자 선정 기준 설정 ⚙️")
    print("엔터(Enter) 키를 누르시면 괄호 안의 '기본값'이 적용됩니다.\n")
    
    churn_threshold = get_float_input("최소 이탈 확률 (0.0 ~ 1.0)", 0.6)
    equipment_days_threshold = get_int_input("최소 단말기 사용 일수 (일)", 365)

    print("\n▶ [4/4] 조건에 맞는 대상자 추출 중...")
    
    targets = original_df[
        (original_df['ChurnProbability'] >= churn_threshold) & 
        (original_df['CurrentEquipmentDays'] >= equipment_days_threshold)
    ].copy()

    targets = targets.sort_values(by='ChurnProbability', ascending=False)

    selected_columns = ['CustomerID', 'ChurnProbability', 'CurrentEquipmentDays', 'MonthsInService']
    result_list = targets[selected_columns]
    
    print_header("📊 최종 대상자 추출 결과 📊")
    
    print(f"  ▪ 전체 분석 대상 고객 : {len(original_df):,} 명")
    print(f"  ▪ 기준 충족 대상 고객 : {len(result_list):,} 명")
    print("-" * 60)
    
    if len(result_list) > 0:
        print("\n🏆 [위험도 최상위 10명 미리보기]")
        print(result_list.head(10).to_string(index=False))
        
        result_list.to_csv(output_path, index=False)
        print("\n" + "=" * 60)
        print(f"✅ 대상자 명단이 성공적으로 저장되었습니다.")
        print(f"📂 저장 위치: {os.path.abspath(output_path)}")
        print("=" * 60 + "\n")
    else:
        print("\n⚠️ 현재 설정한 기준에 부합하는 고객이 없습니다.")
        print("   기준을 조금 낮추어 다시 시도해 보세요.\n")

if __name__ == "__main__":
    main()
