import streamlit as st

from front.api_call import get_all_fab_step

print("run step page")
st.markdown("# Fabrication Steps  ")

_steps = get_all_fab_step()

_filter = st.multiselect("Select projects: ", _steps['project'].unique())
filtered = _steps[_steps['project'].isin(_filter)] if _filter else _steps

st.dataframe(filtered)
