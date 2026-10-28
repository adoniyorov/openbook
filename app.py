import streamlit as st
import streamlit.components.v1 as components

# Must be the first Streamlit call.
st.set_page_config(page_title="오픈북 미니게임", page_icon="🎮", layout="wide")

IFRAME_HEIGHT = 900

GAMES = {
    "블록리게임": {
        "title": "🧩 블록리 게임 (Blockly Games)",
        "url": "https://blockly.games/?lang=ko",
        "desc": "블록을 조립하며 프로그래밍 개념을 배우는 교육용 게임입니다.",
    },
    "테트리스게임": {
        "title": "🟦 테트리스 게임 (Tetris)",
        "url": "https://play.tetris.com/",
        "desc": "떨어지는 블록을 맞춰 줄을 지우는 고전 퍼즐 게임입니다.",
    },
}


def show_home():
    st.title("🏠 홈")
    st.write("왼쪽 메뉴에서 게임을 선택하세요.")
    for name, game in GAMES.items():
        st.markdown(f"- **{name}** — {game['desc']}")


def show_game(name):
    game = GAMES[name]
    st.title(game["title"])
    st.write(game["desc"])
    components.iframe(game["url"], height=IFRAME_HEIGHT, scrolling=True)
    st.caption("게임이 보이지 않으면 아래 버튼으로 새 탭에서 여세요.")
    st.link_button(f"{name} 새 탭에서 열기 ↗", game["url"])


menu = st.sidebar.radio("메뉴", ["홈", *GAMES.keys()])

if menu == "홈":
    show_home()
else:
    show_game(menu)
