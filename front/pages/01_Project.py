import streamlit as st

from front.dao import get_all_project

_projects = get_all_project()

_filter = st.multiselect("Select projects: ", _projects['name'].unique())
filtered = _projects[_projects['name'].isin(_filter)][['name', 'core']]

st.dataframe(filtered.T)
