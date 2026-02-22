# Git 협업 전략 문서

---

## 브랜치 전략

### 브랜치 구조

(각자 필요한 브랜치 규칙에 맞게 생성 및 삭제)

- `main`: 프로덕션 배포 브랜치 (직접 수정 금지)
- `dev`: 개발 통합 브랜치 (모든 PR의 타겟)
- `feat`:
    - feat/ML
        - feat/ML/train
        - feat/ML/eval
        - feat/ML/…
    - feat/EDA
    - feat/…
- `docs` :
    - docs/readme
    - docs/…

### 브랜치 명명 규칙

```
{ prefix }/{ detail }/...
```

- 소문자로 작성
- prefix (예: feat, docs, …)
- detail (예: ML, EDA, …)
- 그 외, 때에 따라 필요한 브랜치 생성
- 예: prefix/feat/ML/train/…

---

## 커밋 컨벤션

### 커밋 타입

```
feat: 새로운 기능 추가
fix: 버그 수정
chore: 빌드, 패키지 매니저 설정 등 (코드 외의 업데이트 사항(폴더구조변경, requirements 등))
docs: 문서 생성 및 수정
refactor: 코드 리팩토링 (내부 구조 개선, 코드 가독성 향상 등 | 기능 변경 없는 코드 수정)
others: 위에 해당하지 않는 기타 등등
```

### 커밋 메시지 작성 예시

```
feat: 사용자 로그인 API 구현
fix: 회원가입 유효성 검증 오류 수정
chore: requirements.txt 수정(pandas 추가)
docs: README에 설치 가이드 추가
```

---

## Pull Request 프로세스

### PR 생성 규칙

1. **타겟 브랜치**: 모든 PR은 `dev` 브랜치로 생성
2. **제목 형식**: 커밋 컨벤션과 동일 (`feat:`, `fix:` 등)
3. **Reviewers**: 팀원 최소 1명 이상 태그 필수

### PR 템플릿

```markdown
## 🔧 주요 변경사항

<!-- 구체적인 변경 내용을 나열해 주세요 -->
<!-- 체크표시를 위해 [ ]안에 X 표시 넣어서 [X] 형태로 만들어주시면 됩니다.-->

- [ ] 새로운 기능 추가
- [ ] 기존 기능 개선
- [ ] 버그 수정
- [ ] 리팩토링
- [ ] 문서 업데이트
- [ ] 설정 변경

## ✅ 체크리스트

<!-- PR 제출 전 확인사항들을 체크해 주세요 -->

- [ ] 커밋 및 PR 제목이 팀 규칙을 따릅니다
- [ ] 코드가 프로젝트의 코딩 스타일을 따릅니다
- [ ] 자체 검토를 완료했습니다
- [ ] 문서를 업데이트했습니다 (해당하는 경우)

## 📝 추가 노트

<!-- 리뷰어에게 전달하고 싶은 추가 정보가 있다면 작성해 주세요 -->
```

### Merge 규칙

- **승인 조건**: 최소 1명 이상의 Approve 필요

---

## 추가 권장 사항

### 1. 커밋 작성 세부 규칙

- 커밋 메시지는 말머리 제외 한글로
- 제목은 50자 이내로 간결하게

### 2. 금지 사항

```markdown
❌ main 브랜치에 직접 push
❌ dev 브랜치에 직접 push (PR 필수)
❌ force push (git push -f) 사용
❌ 대용량 파일 커밋 (100MB 이상)
```

이 문서는 팀 상황에 맞춰 지속적으로 업데이트 됩니다.

---

## Git 명령어 요약

```python
# 모든 수정 및 업데이트는 자신이 현재 어떤 브랜치 사용중인지 반드시 확인할 것!
# 현재 자신의 브랜치는 git bash의 괄호 안에서 확인 가능
## 브랜치 생성 명령어
git checkout -b (브랜치명)
## 브랜치 이동 명령어
git checkout (브랜치명)
## 브랜치 삭제 명령어
git checkout -D (브랜치명)
## 브랜치 내에서 변경사항 확인
## 항상 반드시 모든 일 시작전 git status를 해보고 읽어보는 습관을 가지자!!
## 충돌 예방에 도움이 된다!
git stauts

# 수정 완료 후 github에 올릴때 (순서)
git 폴더에서 git bash 열기         # 꼭 본인이 클론해온 폴더에서 해야함
git checkout (commit할 브랜치명)   # 
git add .                          
git commit -m "변경사항"           # 커밋 컨벤션 지킬 것
git push
github 사이트에서 변경사항 확인                      
pull request                       # 위 프로세스를 따라 dev를 대상으로 PR 생성

# 자신의 로컬 dev와 브랜치들의 최신화를 하고 싶을때
git fetch                          # 로 이상 없는지 확인
git checkout dev                   # dev 브랜치로 변경
git pull origin dev                # 메인 브랜치를 업데이트
git checkout  (본인 브랜치명)
git pull origin dev                # 자신의 브랜치를 메인브랜치와 최신화
```