import streamlit as st

from front.dao import get_all_schedules

print("run2")

_schedules = get_all_schedules()

_filter = st.multiselect("Select projects: ", _schedules['project'].unique())
filtered = _schedules[_schedules['project'].isin(_filter)]

st.dataframe(filtered)
