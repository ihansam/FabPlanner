import os
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
ROOT = os.environ.get('PROJECT_ROOT')


@st.cache_data
def get_all_project():
    path = Path(ROOT).joinpath("front/tmp_db/project.csv")
    return pd.read_csv(path)


@st.cache_data
def get_all_schedules():
    path = Path(ROOT).joinpath("front/tmp_db/schedule.csv")
    return pd.read_csv(path)


@st.cache_data
def get_all_lots():
    path = Path(ROOT).joinpath("front/tmp_db/lot.csv")
    return pd.read_csv(path)


@st.cache_data
def get_all_schedules():
    path = Path(ROOT).joinpath("front/tmp_db/schedule.csv")
    return pd.read_csv(path)


@st.cache_data
def get_all_lot_steps():
    path = Path(ROOT).joinpath("front/tmp_db/lot_step.csv")
    return pd.read_csv(path)
