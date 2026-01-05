import streamlit as st
import random

# 页面基础配置（设置标题、图标，适配手机）
st.set_page_config(page_title="猜数字小游戏", page_icon="🎮", layout="centered")

# 核心：仅隐藏个人信息/页脚，保留分享按钮、菜单等功能
hide_style = """
<style>
/* 隐藏页脚（包含作者/仓库等个人信息） */
footer {visibility: hidden;}
/* 保留右上角菜单（含分享按钮）、页面头部，不做隐藏 */
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 游戏核心逻辑
st.title("🎮 猜数字小游戏")
st.subheader("猜猜我心里的数字（1-100）")

# 初始化游戏数据（刷新页面不重置）
if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 100)  # 随机生成目标数字
    st.session_state.count = 0  # 统计猜测次数
    st.session_state.tips = "开始你的猜测吧！"  # 提示语

# 数字输入框（适配手机，限制1-100）
guess_num = st.number_input("请输入你猜的数字：", min_value=1, max_value=100, step=1)

# 提交按钮（占满宽度，手机更友好）
if st.button("提交答案 🚀", use_container_width=True):
    st.session_state.count += 1
    # 猜数字逻辑判断
    if guess_num > st.session_state.num:
        st.session_state.tips = f"❌ 猜大啦！你已经猜了{st.session_state.count}次"
    elif guess_num < st.session_state.num:
        st.session_state.tips = f"❌ 猜小啦！你已经猜了{st.session_state.count}次"
    else:
        st.session_state.tips = f"🎉 恭喜猜对啦！总共猜了{st.session_state.count}次，正确数字是{st.session_state.num}"
        # 猜对后重置游戏按钮
        if st.button("再来一局 🔄", use_container_width=True):
            st.session_state.num = random.randint(1, 100)
            st.session_state.count = 0
            st.session_state.tips = "开始你的猜测吧！"

# 显示提示语
st.info(st.session_state.tips)
