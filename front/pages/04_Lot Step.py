import streamlit as st

from front.dao import get_all_lot_steps

_steps = get_all_lot_steps()

_filter = st.multiselect("Select projects: ", _steps['project'].unique())
filtered = _steps[_steps['project'].isin(_filter)]

st.dataframe(filtered)
