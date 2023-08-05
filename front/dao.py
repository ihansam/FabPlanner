import os
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
ROOT = os.environ.get('PROJECT_ROOT')


# 일단 Temporary DB 폴더의 csv file을 읽어 READ
@st.cache_data
def get_all_project():
    path = Path(ROOT).joinpath("front/tmp_db/project.csv")
    return pd.read_csv(path)


@st.cache_data
def get_all_schedule():
    path = Path(ROOT).joinpath("front/tmp_db/schedule.csv")
    return pd.read_csv(path)


@st.cache_data
def get_all_fab():
    path = Path(ROOT).joinpath("front/tmp_db/fabrication.csv")
    return pd.read_csv(path)


@st.cache_data
def get_all_fab_step():
    path = Path(ROOT).joinpath("front/tmp_db/fab_step.csv")
    return pd.read_csv(path)
