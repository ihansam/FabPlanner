import streamlit as st

from front.dao import get_all_project

print("run project page")
st.markdown("# Projects  ")

_projects = get_all_project()
st.dataframe(_projects)
