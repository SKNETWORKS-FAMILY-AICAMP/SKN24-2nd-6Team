import streamlit as st
import pandas as pd
import numpy as np
import time
from catboost import CatBoostClassifier
import os

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="통신사 기기변경 지원금 대상자 추출",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed" # 사이드바를 기본적으로 접어둠
)

# -----------------------------------------------------------------------------
# 2. 전역 상수 설정
# -----------------------------------------------------------------------------
ROOT_DIR = './../' if os.path.basename(os.getcwd()) == 'src' else './'
MODEL_PATH = os.path.join(ROOT_DIR, 'saved_models', 'catboost.cbm')
TEST_DATA_PATH = os.path.join(ROOT_DIR, 'data', 'preprocessed', 'cell2cell_unscaled_test.csv')
SMS_COST_PER_MSG = 20  # SMS 1건당 발송 비용 (원)

# -----------------------------------------------------------------------------
# 3. 데이터 및 모델 로드 (캐싱)
# -----------------------------------------------------------------------------
@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    model = CatBoostClassifier()
    model.load_model(MODEL_PATH)
    return model

@st.cache_data
def load_data():
    if not os.path.exists(TEST_DATA_PATH):
        return None
    return pd.read_csv(TEST_DATA_PATH)

@st.cache_data
def preprocess_and_predict(_df, _model):
    original_df = _df.copy()
    working_df = _df.copy()
    
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
        if col in working_df.columns:
            working_df[col] = working_df[col].fillna(0).astype(int)
            if col == 'OptOutMailings':
                original_df['OptOutMailings_Int'] = working_df[col]

    model_features = _model.feature_names_
    for col in model_features:
        if col not in working_df.columns:
            working_df[col] = 0
            
    X_test = working_df[model_features]
    probabilities = _model.predict_proba(X_test)[:, 1]
    original_df['ChurnProbability'] = probabilities
    
    return original_df

# -----------------------------------------------------------------------------
# 4. 메인 UI 구성
# -----------------------------------------------------------------------------
def main():
    st.title("📡 기기변경 대상자 추출 & 마케팅 자동화 시스템")
    st.markdown("""
    머신러닝(CatBoost) 예측을 기반으로 이탈 고위험군을 추출하고, 타겟 고객에게 맞춤형 프로모션 문자를 즉시 발송합니다.
    """)
    st.divider()

    with st.spinner("데이터 및 모델을 불러오는 중입니다..."):
        model = load_model()
        raw_df = load_data()

    if model is None or raw_df is None:
        st.error("❌ 데이터 또는 모델 파일을 찾을 수 없습니다.")
        st.stop()

    with st.spinner("머신러닝 모델이 이탈 확률을 예측하고 있습니다..."):
        processed_df = preprocess_and_predict(raw_df, model)

    # -------------------------------------------------------------------------
    # 컨트롤 패널 (메인 화면 상단으로 이동하여 넓게 배치)
    # -------------------------------------------------------------------------
    # 설정 영역을 카드 스타일처럼 보이게 컨테이너로 감쌈
    with st.container():
        col_settings, col_message = st.columns([1, 1], gap="large")
        
        with col_settings:
            st.subheader("⚙️ 1. 대상자 추출 기준 설정")
            st.markdown("지원금을 지급할 타겟 고객의 최소 조건을 설정하세요.")
            
            churn_threshold = st.slider("📈 최소 이탈 확률", min_value=0.0, max_value=1.0, value=0.60, step=0.01)
            equipment_days_threshold = st.number_input("📱 최소 단말기 사용 일수 (일)", min_value=0, value=365, step=30)
            st.info("💡 설정값을 변경하면 하단의 대상자 명단이 실시간으로 업데이트됩니다.")

        with col_message:
            st.subheader("✉️ 2. 마케팅 메시지 설정")
            st.markdown("추출된 대상자에게 발송할 안내 문자를 구성하세요.")
            
            template_choice = st.selectbox(
                "문자 템플릿 선택",
                options=["[감사 보상형] 장기 사용 혜택", "[기기 케어형] 노후 단말기 교체 지원", "[안심 보장형] 요금 인상 없는 교체"]
            )
            
            if "감사 보상형" in template_choice:
                default_msg = "[SKN통신 안내]\n고객님, 현재 사용 중이신 휴대폰을 오~래 아껴 써주셔서 감사합니다!\n그동안의 성원에 보답하고자 우수 사용 고객님을 위한 '최신폰 기기변경 특별 지원금'이 배정되었습니다.\n가까운 대리점에서 부담 없이 최신 기종으로 업그레이드 해보세요."
            elif "기기 케어형" in template_choice:
                default_msg = "[SKN통신 고객 케어]\n고객님, 현재 스마트폰을 사용하신 지 벌써 1년이 넘으셨네요!\n혹시 배터리가 빨리 닳거나 용량이 부족하지는 않으신가요?\n장기 사용 고객님들께만 드리는 '노후 단말기 교체 특별 지원금'으로 쾌적한 최신 스마트폰을 만나보세요."
            else:
                default_msg = "[SKN통신 혜택 안내]\n고객님, 현재 단말기를 오래 사용해주신 우수 고객님께 안내드립니다.\n기존에 쓰시던 요금제 수준을 유지하면서, '장기 사용 특별 지원금'을 통해 기기값 부담 없이 새 폰으로 교체하실 수 있는 기회가 열렸습니다.\n이번 달 한정 혜택을 놓치지 마세요!"
                
            custom_message = st.text_area("발송될 메시지 내용", value=default_msg, height=120)
            
    st.divider()

    # -------------------------------------------------------------------------
    # 데이터 필터링 로직
    # -------------------------------------------------------------------------
    targets = processed_df[
        (processed_df['ChurnProbability'] >= churn_threshold) & 
        (processed_df['CurrentEquipmentDays'] >= equipment_days_threshold)
    ].copy()

    # 수신거부 제외 (0인 사람만 대상)
    marketing_targets = targets[targets['OptOutMailings_Int'] == 0].copy()
    marketing_targets = marketing_targets.sort_values(by='ChurnProbability', ascending=False)
    
    selected_columns = ['CustomerID', 'ChurnProbability', 'CurrentEquipmentDays', 'OptOutMailings_Int']
    result_df = marketing_targets[selected_columns]

    # -------------------------------------------------------------------------
    # 결과 요약 (메트릭)
    # -------------------------------------------------------------------------
    st.subheader("📊 타겟팅 현황 및 비용 분석")
    
    # 메트릭 카드 시각화 개선
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="👥 전체 분석 대상", value=f"{len(processed_df):,} 명")
    with m_col2:
        st.metric(label="🎯 조건 충족 (전체)", value=f"{len(targets):,} 명")
    with m_col3:
        opt_out_count = len(targets) - len(result_df)
        st.metric(label="✅ 실제 발송 가능 인원", value=f"{len(result_df):,} 명", delta=f"-{opt_out_count}명 (수신거부)", delta_color="inverse")

    st.write("")

    # -------------------------------------------------------------------------
    # 최종 명단 및 액션 (다운로드 / 문자 발송)
    # -------------------------------------------------------------------------
    if len(result_df) > 0:
        st.subheader(f"🏆 최종 마케팅 대상자 명단 (미리보기)")
        
        display_df = result_df.copy()
        display_df['이탈확률 (%)'] = display_df['ChurnProbability'].apply(lambda x: f"{x * 100:.2f}%")
        display_df['단말기사용일수 (일)'] = display_df['CurrentEquipmentDays'].apply(lambda x: f"{int(x):,}")
        display_df['수신동의여부'] = display_df['OptOutMailings_Int'].apply(lambda x: "❌ 거부" if x == 1 else "✅ 동의")
        
        # UI 가독성을 위해 불필요한 원본 컬럼 숨김 (다운로드 시에는 원본 제공)
        display_df = display_df[['CustomerID', '이탈확률 (%)', '단말기사용일수 (일)', '수신동의여부']]
        
        st.dataframe(display_df, use_container_width=True, hide_index=True, height=250)
        
        st.write("")
        
        # 하단 액션 버튼 영역
        st.markdown("### 🚀 실행 액션")
        col_action1, col_action2, col_action3 = st.columns([1, 1, 2])
        
        with col_action1:
            csv_data = result_df.drop(columns=['OptOutMailings_Int']).to_csv(index=False).encode('utf-8-sig') 
            st.download_button(
                label="📥 결과 CSV 다운로드",
                data=csv_data,
                file_name='marketing_targets.csv',
                mime='text/csv',
                use_container_width=True
            )
            
        with col_action2:
            if st.button("✉️ 마케팅 문자 일괄 발송", type="primary", use_container_width=True):
                st.session_state['show_confirm'] = True
                
        # 발송 시뮬레이션
        if st.session_state.get('show_confirm', False):
            st.write("")
            st.error(f"⚠️ **{len(result_df):,}명**의 고객에게 마케팅 문자를 즉시 발송하시겠습니까?")
            
            c1, c2, c3 = st.columns([1, 1, 4])
            with c1:
                if st.button("✅ 네, 즉시 발송"):
                    st.session_state['show_confirm'] = False
                    
                    progress_text = "서버로 메시지 전송 중..."
                    my_bar = st.progress(0, text=progress_text)
                    for percent_complete in range(100):
                        time.sleep(0.01)
                        my_bar.progress(percent_complete + 1, text=progress_text)
                    
                    time.sleep(0.5)
                    my_bar.empty()
                    st.success(f"🎉 전송 완료! {len(result_df):,}명의 고객에게 성공적으로 문자가 발송되었습니다.")
                    st.balloons()
            with c2:
                if st.button("❌ 취소", type="secondary"):
                    st.session_state['show_confirm'] = False
                    st.rerun()

    else:
        st.warning("⚠️ 현재 기준에 부합하면서 수신 동의를 한 고객이 없습니다. 상단에서 기준을 완화해 보세요.")

if __name__ == "__main__":
    main()
