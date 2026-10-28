중간고사 미션 - Streamlit 앱에 iframe 게임 메뉴 2개 추가

학번: D20250166
이름: Abdurashid Doniyorov

GitHub 저장소 URL: https://github.com/adoniyorov/openbook
Streamlit 앱 URL:  https://openbook.streamlit.app


[추가한 메뉴]
1. 블록리게임
   - 사이드바에서 "블록리게임"을 선택하면 메인 화면에 제목과 함께
     Blockly Games(https://blockly.games/?lang=ko)가 iframe으로 표시됩니다.
   - 블록을 조립하며 프로그래밍 개념을 배우는 교육용 게임입니다.

2. 테트리스게임
   - 사이드바에서 "테트리스게임"을 선택하면 메인 화면에 제목과 함께
     Tetris(https://play.tetris.com/)가 iframe으로 표시됩니다.
   - 떨어지는 블록을 맞춰 줄을 지우는 고전 퍼즐 게임입니다.

[구현 방식]
- streamlit.components.v1.iframe(url, height=900, scrolling=True) 사용
- st.set_page_config(layout="wide")로 넓은 화면 레이아웃 적용
- 각 iframe 아래에 "새 탭에서 열기" 버튼(st.link_button)을 대체 링크로 제공

[iframe 임베딩 확인]
- 두 사이트 모두 X-Frame-Options 및 CSP frame-ancestors 헤더가 없어
  iframe 임베딩이 정상적으로 동작합니다.
- 테트리스 사이트는 처음 로딩 시 약 30초간 광고가 표시된 후 게임 화면이 나타납니다.

[파일 구성]
- app.py                 : Streamlit 앱 메인 파일
- requirements.txt       : 필요 패키지 목록
- screenshot_blockly.png : 블록리게임 메뉴 실행 화면
- screenshot_tetris.png  : 테트리스게임 메뉴 실행 화면
- readme.txt             : 본 설명 파일
