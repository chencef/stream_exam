# coding = utf-8
import streamlit as st
import streamlit.components.v1 as components
st.video("https://youtu.be/yVV_t_Tewvs")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

path = 'C:\\Users\\111\\streamlit\\chromedriver'
driver = webdriver.Chrome(r'C:\\Users\\111\\streamlit\\chromedriver.exe')

#driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')

driver.get('http://www.youtube.com')
# 演示被其他st组件包围的html()效果，高度已设置
st.button('禁用', disabled=True)
st.button('正常')
components.html('''
<span>
我位于html()中
<video controls width="250" autoplay="true" muted="true" loop="true">
<source 
            src="https://www.youtube.com/watch?v=RH1xwRavPXw" 
            type="video/mp4" />
</video>
</span>
''', height=330)
st.button('正常2')



components.iframe(""" https://www.youtube.com/embed/zaoiriEbncc?rel=0&hd=1&vq=hd720""" , scrolling = True , height = 350)