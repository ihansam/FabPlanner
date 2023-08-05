import streamlit as st

from front.dao import get_all_schedule

print("run schedule page")
st.markdown("# Project Schedules  ")

_schedules = get_all_schedule()

_filter = st.multiselect("Select projects: ", _schedules['project'].unique())
filtered = _schedules[_schedules['project'].isin(_filter)] if _filter else _schedules

st.dataframe(filtered)
