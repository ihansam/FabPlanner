import streamlit as st

from front.api_call import get_all_fab

print("run fab page")
st.markdown("# Project Fabrications  ")

_fabs = get_all_fab()

_filter = st.multiselect("Select projects: ", _fabs['project'].unique())
filtered = _fabs[_fabs['project'].isin(_filter)] if _filter else _fabs

st.dataframe(filtered)
