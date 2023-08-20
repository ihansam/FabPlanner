import streamlit as st

from front.api_call import get_all_schedule
from front.roadmap import gather_milestones, generate_roadmap


all_project = get_all_schedule()['project'].unique()
selected_project = st.selectbox("Select a project: ", all_project)
milestones = gather_milestones(selected_project)
figure = generate_roadmap(milestones)
st.plotly_chart(figure)
