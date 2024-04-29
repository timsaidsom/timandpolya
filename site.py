from datetime import datetime
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
from tqdm import tqdm, tqdm_notebook
import time

st.set_page_config(page_title='My Webpage', page_icon=':💗:', layout='wide')

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["ABOUT US", "MEETING!", "NOTE"],
        icons=["flower3", "calendar2-check", "envelope"],
        default_index=0,
        orientation='horizontal',
        styles={
            'container': {'padding': '0!important', 'background-color': '#df4320'},
            'icon': {'color': 'black', 'font-size': '25px'},
            'nav-link': {
                'font-size': '25px',
                'text-align': 'left',
                'margin': '0px',
                '--hover-color': '#eee'
            },
            'nav-link-link-selected': {'background-color': '#0a473a'},
        })


#------------------------ 1 VKLADKA--------------------------------


if selected == "ABOUT US":
    def load_lottieur1(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # load assets
    lottie_coding = load_lottieur1('https://lottie.host/0c9c6b64-7f94-4700-91fa-931ee133da67/4sCBk3c5Pb.json')
    lottie_coding1 = load_lottieur1('https://lottie.host/614419a1-c03a-4b1f-a1da-d0a5ee1f821b/MvlYUnx9Oi.json')

    # ----Header section----
    with st.container():
        st.subheader('Tim and Polya lifeboard👑')
        st.title('Our information')

    # ---- WHAT I DO
    with st.container():
        st.write('---')
        left_column, right_column = st.columns(2)
        with left_column:
            st.header('Who we are?')
            st.write('##')
            st.write(
                "- Tim and Polya is a sweet couple, that live in Siberia. They're have a huge plans for their own future."
                "\n- So I'm Tim), creator of this site, just trying to keep our relationships in tonus and health."
                "\n- I love Polya, and this is my try to simplify all our schedule issues, make a place where we can read about us easy.")
            st.write('Links: ')
        with right_column:
            st_lottie(lottie_coding, height=300, key='coding')
        with left_column:
            st_lottie(lottie_coding1, height=100, key='coding1')


#-----------------2 VKLADKA---------------------------------


if selected == "MEETING!":
    with st.container():
        st.header('Meeting')
        st.write('---')
        st.write('##')
        image_column, text_column = st.columns((1, 2))
        img1 = Image.open('venv/images/first.png')
        st.write('---')
        img2 = Image.open('venv/images/second.png')
        img3 = Image.open('venv/images/third.png')
        img4 = Image.open('venv/images/fourth.png')
        with image_column:
            st.image(img4)
        with image_column:
            st.image(img2)
        with image_column:
            st.image(img1)

            with image_column:
                st.image(img4)
            with text_column:
                st.subheader('DAYS!!!')
                first_day = datetime(2023, 7, 8)
                today = datetime.now()
                deadline = datetime(2024, 7, 8)
                total_days = (deadline - first_day).days
                howmany0 = (today - first_day).days  # сколько прошло
                howmany1 = (deadline - today).days  # сколько осталось
                progress = howmany0 / total_days * 100

                def styled_text(text, font_size, color):
                    return '<span style="font-size:{}; color:{};">{}</span>'.format(font_size, color, text)

                # Цвета текста в формате HEX
                color_passed = "#82217A"
                color_left = "#F33D6E"

                # Вывод текста с помощью HTML тегов для установки размера шрифта и цвета
                st.write(styled_text("Прошло {} дней".format(howmany0), "38px", color_passed), unsafe_allow_html=True)
                st.write(styled_text("Осталось {} дней".format(howmany1), "38px", color_left), unsafe_allow_html=True)
                # Ждем 1 секунду перед обновлением
                time.sleep(1)

#--------------------- 3 VKLADKA----------------------------------


if selected == "NOTE":
    def tab3_content():
        st.header("Содержимое третьей вкладки")
        st.write("Это содержимое третьей вкладки.")

    # ----projects

































# Создание боковой панели с вкладками

