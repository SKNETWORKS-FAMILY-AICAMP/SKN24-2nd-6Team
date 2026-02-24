# Data Dictionary — Cell2Cell Telecom Churn (58 columns)
  
> Target(타깃): **Churn** / ID: **CustomerID**

| No. | Column | Description (KR) | Role |
|---:|---|---|---|
| 1 | CustomerID | 고객 식별 번호 | ID |
| 2 | Churn | 고객 이탈 여부 | Target |
| 3 | MonthlyRevenue | 월평균 수익 | Feature |
| 4 | MonthlyMinutes | 월평균 사용 시간(분) | Feature |
| 5 | TotalRecurringCharge | 평균 총 정기 요금 | Feature |
| 6 | DirectorAssistedCalls | 상담원(관리자) 지원 통화 평균 횟수 | Feature |
| 7 | OverageMinutes | 요금제 외 평균 초과 사용 시간(분) | Feature |
| 8 | RoamingCalls | 로밍 통화 평균 횟수 | Feature |
| 9 | PercChangeMinutes | 전월과 전전월 사이의 사용 시간 변화율(%) | Feature |
| 10 | PercChangeRevenues | 전월과 전전월 사이의 수익 변화율(%) | Feature |
| 11 | DroppedCalls | 통화 끊김 평균 횟수 | Feature |
| 12 | BlockedCalls | 수신 차단 통화 평균 횟수 | Feature |
| 13 | UnansweredCalls | 미응답 통화 평균 횟수 | Feature |
| 14 | CustomerCareCalls | 고객 고객 센터 통화 평균 횟수 | Feature |
| 15 | ThreewayCalls | 3자 통화 평균 횟수 | Feature |
| 16 | ReceivedCalls | 수신 통화 평균 횟수 | Feature |
| 17 | OutboundCalls | 발신 통화 평균 횟수 | Feature |
| 18 | InboundCalls | 착신 통화 평균 횟수 | Feature |
| 19 | PeakCallsInOut | 피크 시간대 평균 발신 및 착신 통화 횟수 | Feature |
| 20 | OffPeakCallsInOut | 비피크 시간대 평균 발신 및 착신 통화 횟수 | Feature |
| 21 | DroppedBlockedCalls | 통화 끊김 평균 횟수 | Feature |
| 22 | CallForwardingCalls | 착신 전환 통화 평균 횟수 | Feature |
| 23 | CallWaitingCalls | 통화 중 대기 평균 횟수 | Feature |
| 24 | MonthsInService | 서비스 이용 기간(개월) | Feature |
| 25 | UniqueSubs | 고유 가입자 수 | Feature |
| 26 | ActiveSubs | 현재 활성 가입자 수 | Feature |
| 27 | ServiceArea | 통신 서비스 지역 | Feature |
| 28 | Handsets | 지급된 단말기 | Feature |
| 29 | HandsetModels | 지급된 단말기 모델 | Feature |
| 30 | CurrentEquipmentDays | 현재 기기 사용 일수 | Feature |
| 31 | AgeHH1 | 첫 번째 가구원의 연령 | Feature |
| 32 | AgeHH2 | 두 번째 가구원의 연령 | Feature |
| 33 | ChildrenInHH | 가구 내 자녀 유무 | Feature |
| 34 | HandsetRefurbished | 단말기 재생(리퍼비시) 여부 | Feature |
| 35 | HandsetWebCapable | 단말기 웹 접속 가능 여부 | Feature |
| 36 | TruckOwner | 트럭 소유 여부 | Feature |
| 37 | RVOwner | 레저용 차량(RV) 소유 여부 | Feature |
| 38 | Homeownership | 주택 소유 여부 확인 가능 여부 | Feature |
| 39 | BuysViaMailOrder | 우편 주문 이용 여부 | Feature |
| 40 | RespondsToMailOffers | 우편 제안 응답 여부 | Feature |
| 41 | OptOutMailings | 우편 수신 거부 여부(우편 응답 여부 관련) | Feature |
| 42 | NonUSTravel | 해외(미국 외) 여행 여부 | Feature |
| 43 | OwnsComputer | 컴퓨터 소유 여부 | Feature |
| 44 | HasCreditCard | 신용카드 소유 여부 | Feature |
| 45 | RetentionCalls | 고객 유지팀에 의한 통화 횟수 | Feature |
| 46 | RetentionOffersAccepted | 이전에 수락한 고객 유지 제안 횟수 | Feature |
| 47 | NewCellphoneUser | 신규 휴대폰 사용자 여부 | Feature |
| 48 | NotNewCellphoneUser | 기존 휴대폰 사용자 여부 | Feature |
| 49 | ReferralsMadeBySubscriber | 가입자에 의한 추천 횟수 | Feature |
| 50 | IncomeGroup | 소득 그룹 | Feature |
| 51 | OwnsMotorcycle | 오토바이 소유 여부 | Feature |
| 52 | AdjustmentsToCreditRating | 신용 등급 조정 횟수 | Feature |
| 53 | HandsetPrice | 단말기 가격 | Feature |
| 54 | MadeCallToRetentionTeam | 고객 유지팀 문의 여부 | Feature |
| 55 | CreditRating | 고객 신용 등급 | Feature |
| 56 | PrizmCode | 고객 Prizm 코드(라이프스타일 분류 코드) | Feature |
| 57 | Occupation | 고객 직업 | Feature |
| 58 | MaritalStatus | 고객 결혼 여부 | Feature |
