import streamlit as st
import random

# 页面标题（手机端适配）
st.set_page_config(page_title="猜数字游戏", page_icon="🎮", layout="centered")
st.title("🎮 猜数字小游戏")
st.subheader("猜猜我心里的数字（1-100）")

# 初始化游戏数据（用session_state保存，刷新不重置）
if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 100)  # 目标数字
    st.session_state.count = 0  # 猜测次数
    st.session_state.tips = "开始你的猜测吧！"  # 提示语

# 输入框（手机端点击就能输入）
guess_num = st.number_input("请输入你猜的数字：", min_value=1, max_value=100, step=1)

# 提交按钮
if st.button("提交答案 🚀", use_container_width=True):
    st.session_state.count += 1
    # 判断逻辑
    if guess_num > st.session_state.num:
        st.session_state.tips = f"❌ 猜大啦！你已经猜了{st.session_state.count}次"
    elif guess_num < st.session_state.num:
        st.session_state.tips = f"❌ 猜小啦！你已经猜了{st.session_state.count}次"
    else:
        st.session_state.tips = f"🎉 恭喜猜对啦！总共猜了{st.session_state.count}次，正确数字是{st.session_state.num}"
        # 猜对后重置游戏
        if st.button("再来一局 🔄", use_container_width=True):
            st.session_state.num = random.randint(1, 100)
            st.session_state.count = 0
            st.session_state.tips = "开始你的猜测吧！"

# 显示提示语
st.info(st.session_state.tips)
