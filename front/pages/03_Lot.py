import streamlit as st

from front.dao import get_all_lots

_lots = get_all_lots()

_filter = st.multiselect("Select projects: ", _lots['project'].unique())
filtered = _lots[_lots['project'].isin(_filter)]

st.dataframe(filtered)
