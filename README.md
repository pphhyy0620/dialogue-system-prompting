# Care Assistant System with LLM's prompting

- 이 프로젝트에서는 LLM의 prompt를 이용해 assistant라는 role을 부여해줌으로써 assistant의 역할이 가능해지도록 하였습니다.
- **설정한 Role Prompt** :
    ```노인을 돌보며 위험상황을 볼 수 있고 사람처럼 대화할 수 있는 로봇이야. 당신은 마치 방금 일을 본 것처럼 관찰 대상자에게 직접 대화를 걸어주는 것이에요. 따뜻한 모습을 보여주는 사람 스타일로 대화하고 대답은 간결하게 해주세요. 이 말투로 모든 답변을 해주고 계속 유지해줄게요. 그럼 대화하는데 도움이 될 거예요. ```
- 현재 추가적으로 해야할 연구 부분은 visual description을 prompt로 이용하여 사람의 이상행동을 반영하여는 assistant를 만드는 것입니다.

<img src="https://github.com/pphhyy0620/dialogue-system-prompting/assets/122515100/ecc5059f-174b-4494-a56e-891b669cbefe" width="600" height="600"/>

## Environment Setup

필요한 라이브러리들을 설치한 후에,
 ```
pip install -r requirements.txt
```

app 파일을 구동시키면 웹페이지가 만들어지게 됩니다.
 ```
streamlit run app.py
```
