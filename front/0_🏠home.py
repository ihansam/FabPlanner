import os
import sys

import streamlit as st
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.environ.get('PROJECT_ROOT'))

st.set_page_config(
    page_title="FabScheduler",
    page_icon="📅",
)
st.sidebar.success("Select a menu above.")

st.write("# Welcome to Fab Scheduler! 👋")
st.markdown(
    """
    Fab Scheduler를 통해 제품 개발 일정을 쉽게 관리하고 로드맵을 확인할 수 있습니다.  
    **👈 sidebar에서 원하는 메뉴를 선택하세요**
    """
)
