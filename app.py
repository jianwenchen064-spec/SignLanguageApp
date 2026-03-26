import streamlit as st
import os

# 网页标题设置
st.set_page_config(page_title="手语翻译原型", page_icon="👋")

st.title("🤖 手语数字人翻译系统 (GIF版)")
st.markdown("---")

# 侧边栏
st.sidebar.header("系统状态")
st.sidebar.success("本地库已就绪")

# 输入框
word = st.text_input("请输入想要翻译的词汇：", placeholder="例如：你好")

# 按钮点击逻辑
if st.button("开始翻译"):
    if word:
        # 统一格式，匹配你仓库里的文件名
        gif_path = f"./{word}.gif"
        
        if os.path.exists(gif_path):
            st.subheader(f"正在展示：{word}")
            # 显示你仓库里的 GIF
            st.image(gif_path, use_column_width=True)
            st.balloons() # 成功的小彩蛋
        else:
            st.error(f"抱歉，词库暂未收录 '{word}'。目前支持：你好、谢谢、再见")
    else:
        st.warning("请输入文字后再点击翻译。")

st.info("提示：本项目直接调用仓库内的 GIF 素材进行演示。")
