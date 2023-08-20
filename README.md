# Fabrication Schedule Planner
- Easily view your product development roadmap


### How to Demonstrate
- Create `.env` file refer to `env.example`
- Run streamlit server
```commandline
streamlit run front/0_🏠home.py
```

### ERD Diagram
- 프로젝트는 여러 개의 일정을 갖고 진행됨
- 일정의 종류: Engineering Sample, Customer Sample, Mass Production
- 일정의 주요 마일스톤: 킥오프, 제조 시작, 제조 종료, 승인
- 일정은 여러 개의 제조 공정에 투입해 진행
- 제조 공정은 여러 개의 step으로 구성
```mermaid
erDiagram
    PROJECT{
        int pjId PK
        str codeName
    }
    SCHEDULE{
        int sdId PK
        int pjId FK
        str type "ES, CS, MP"
        date kickOff "in design"
        date fabIn "in fabrication"
        date fabOut "in testing"
        date approved
    }
    FABRICATION{
        int fbId PK
        int sdId FK
        str fabName
        str objective
        int quantity
    }
    FAB_STEP{
        int stId PK
        int fbId FK
        str stepName
        date ETA
    }
    PROJECT ||--o{ SCHEDULE: logically_proceed_by
    SCHEDULE ||--o{ FABRICATION: physically_proceed_by
    FABRICATION ||--o{ FAB_STEP: has
```
