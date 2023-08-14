import streamlit as st

from front.api_call import get_all_project

print("run project page")
st.markdown("# Projects  ")

_projects = get_all_project()
print(_projects)

_filter = st.text_input("Find project by codename", "")
projects = _projects[_projects['codeName'].str.contains(_filter, case=False)]

st.dataframe(projects, hide_index=True)
