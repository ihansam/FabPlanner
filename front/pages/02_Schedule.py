import pandas as pd
import streamlit as st
from streamlit import session_state as ss

from front.api_call import get_all_schedule, get_all_project
from front.roadmap import gather_milestones, generate_roadmap

SHOWING_NEW_SCHEDULE_FORM = "SHOWING_NEW_SCHEDULE_FORM"
PROCESSING_SUBMITTED_SCHEDULE = "PROCESSING_SUBMITTED_SCHEDULE"
SUBMITTED_SCHEDULE_DATA = "SUBMITTED_SCHEDULE_DATA"
_projects = get_all_project()['codeName']


def set_submit_state(show: bool = None, submit: bool = None):
    if show is not None:
        ss[SHOWING_NEW_SCHEDULE_FORM] = show
    if submit is not None:
        ss[PROCESSING_SUBMITTED_SCHEDULE] = submit


def show_add_form():
    with st.form("add_schedule_form"):
        st.write("Add New Schedules.")
        _config = {
            'project': st.column_config.SelectboxColumn("Project",
                                                        help="select a project",
                                                        required=True,
                                                        options=_projects),
            'type': st.column_config.TextColumn("Type", required=True),
            'kickOff': st.column_config.DateColumn("Kick Off"),
            'fabIn': st.column_config.DateColumn("Fab In"),
            'fabOut': st.column_config.DateColumn("Fab Out"),
            'approved': st.column_config.DateColumn("Approved"),
        }
        _new = pd.DataFrame(columns=list(_config.keys()))
        st.data_editor(_new, column_config=_config, num_rows='dynamic',
                       key=SUBMITTED_SCHEDULE_DATA, use_container_width=True)
        st.form_submit_button(on_click=set_submit_state, kwargs={'show': False, 'submit': True})


def submit_new_schedule():
    print("POST /schedule")  # TODO
    new_schedules = ss.get(SUBMITTED_SCHEDULE_DATA)
    st.write(new_schedules)
    print(new_schedules)
    set_submit_state(submit=False)


if __name__ == '__main__':
    print("run schedule page")

    st.markdown("# Project Schedules  ")

    _schedules = get_all_schedule()

    _filter = st.multiselect("Select projects: ", options=_schedules['project'].unique(), placeholder="")
    filtered = _schedules[_schedules['project'].isin(_filter)] if _filter else _schedules

    st.data_editor(filtered, key="schedules", disabled=('project', '_index'), hide_index=True, use_container_width=True)
    # st.write(st.session_state.get("schedules"))  # 변경 사항 추적

    _, col_new, col_save = st.columns([8, 1, 1])

    if col_new.button("New"):
        set_submit_state(show=True, submit=False)

    if SHOWING_NEW_SCHEDULE_FORM in ss and ss.get(SHOWING_NEW_SCHEDULE_FORM):
        show_add_form()

    if PROCESSING_SUBMITTED_SCHEDULE in ss and ss.get(PROCESSING_SUBMITTED_SCHEDULE):
        submit_new_schedule()

    if col_save.button("Save"):
        print("UPDATE /schedule")  # TODO
        st.write("saved!")

    with st.expander("Roadmap", expanded=True):
        for _prj in _filter:
            _stones = gather_milestones(_prj, gather_schedule=True, gather_fab_step=False)
            _fig = generate_roadmap(_stones, project_name=_prj)
            st.plotly_chart(_fig, use_container_width=True)
