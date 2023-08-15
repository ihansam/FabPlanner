import pandas as pd
import streamlit as st
from streamlit import session_state as ss

from front.api_call import get_all_schedule, get_all_project

STATE_SCHEDULE_SUBMITTED = "STATE_SCHEDULE_SUBMITTED"
SUBMITTED_SCHEDULE_DATA = "SUBMITTED_SCHEDULE_DATA"
_projects = get_all_project()['codeName']


def set_submitting_state(state: bool):
    ss[STATE_SCHEDULE_SUBMITTED] = state


def show_add_form():
    with st.form("add_schedule_form"):
        st.write("Add New Schedules.")
        _config = {
            'project': st.column_config.SelectboxColumn("Project",
                                                        help="select a project",
                                                        required=True,
                                                        options=_projects),
            'type': st.column_config가.TextColumn("Type", required=True),
            'kickOff': st.column_config.DateColumn("Kick Off"),
            'fabIn': st.column_config.DateColumn("Fab In"),
            'fabOut': st.column_config.DateColumn("Fab Out"),
            'approved': st.column_config.DateColumn("Approved"),
        }
        _new = pd.DataFrame(columns=list(_config.keys()))
        st.data_editor(_new, column_config=_config, num_rows='dynamic',
                       key=SUBMITTED_SCHEDULE_DATA, use_container_width=True)
        st.form_submit_button(on_click=set_submitting_state, args=(True, ))


def submit_new_schedule():
    print("POST /schedule")  # TODO
    new_schedules = ss.get(SUBMITTED_SCHEDULE_DATA)
    st.write(new_schedules)
    print(new_schedules)
    set_submitting_state(False)


if __name__ == '__main__':
    print("run schedule page")

    st.markdown("# Project Schedules  ")

    _schedules = get_all_schedule()

    _filter = st.multiselect("Select projects: ", options=_schedules['project'].unique(), placeholder="")
    filtered = _schedules[_schedules['project'].isin(_filter)] if _filter else _schedules

    st.data_editor(filtered, key="schedules", disabled=('project', '_index'), hide_index=True, use_container_width=True)
    # st.write(st.session_state.get("schedules"))  # 변경 사항 추적

    btns = st.columns(2)

    if btns[0].button("New", on_click=set_submitting_state, args=(False, )):
        show_add_form()

    if STATE_SCHEDULE_SUBMITTED in ss and ss.get(STATE_SCHEDULE_SUBMITTED):
        submit_new_schedule()

    if btns[1].button("Save"):
        print("UPDATE /schedule")  # TODO
        st.write("saved!")
