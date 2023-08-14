import os
from pathlib import Path

import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
ROOT = os.environ.get('PROJECT_ROOT')
URL = os.environ.get('API_URL')


def get_all_project():
    try:
        response = requests.get(f"{URL}/projects")
    except requests.exceptions.RequestException:
        return get_all_project_dummy()
    ret = pd.DataFrame(response.json())
    ret.set_index('pjId', inplace=True)
    return ret


@st.cache_data
def get_all_project_dummy():
    path = Path(ROOT).joinpath("front/dummy_data/project.csv")
    return pd.read_csv(path)


def get_all_schedule():
    try:
        response = requests.get(f"{URL}/schedules")
    except requests.exceptions.RequestException:
        return get_all_schedule_dummy()
    ret = response.json()
    for sch in ret:
        sch['project'] = sch['project']['codeName']
    ret = pd.DataFrame(ret)
    ret.set_index('project', inplace=True)  # project 컬럼 맨 왼쪽 으로
    ret.reset_index(level='project', inplace=True)
    ret.set_index('sdId', inplace=True)
    return ret


@st.cache_data
def get_all_schedule_dummy():
    path = Path(ROOT).joinpath("front/dummy_data/schedule.csv")
    return pd.read_csv(path)


@st.cache_data
def get_all_fab():
    path = Path(ROOT).joinpath("front/dummy_data/fabrication.csv")
    return pd.read_csv(path)


@st.cache_data
def get_all_fab_step():
    path = Path(ROOT).joinpath("front/dummy_data/fab_step.csv")
    return pd.read_csv(path)
