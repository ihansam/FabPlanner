import pandas as pd
import plotly.colors as pc
import plotly.graph_objects as go
import streamlit as st

from front.dao import get_all_fab_step, get_all_schedule


# Project 선택
_schedules = get_all_schedule()
_steps = get_all_fab_step()
_project = st.selectbox("Select a project: ", _schedules['project'].unique())
schedules = _schedules[_schedules['project'] == _project]
steps = _steps[_steps['project'] == _project]


# Milestone 취합
MAIN_EVENTS = ['kickOff', 'fabIn', 'fabOut', 'approved']
TIMELINE = 'timeline'
STONE_NAME = 'name'
STONE_DATE = 'date'

milestones = pd.DataFrame(columns=[TIMELINE, STONE_NAME, STONE_DATE])

for _, schedule in schedules.iterrows():  # schedule에 속한 메인 이벤트 취합
    for event in MAIN_EVENTS:
        _milestone = {TIMELINE: schedule['type'],
                      STONE_NAME: [event],
                      STONE_DATE: schedule[event]}
        milestones = pd.concat([milestones, pd.DataFrame.from_dict(_milestone)],
                               ignore_index=True)
for _, row in steps.iterrows():  # fab step에 속한 이벤트 취합
    _milestone = {TIMELINE: row['fabname'],
                  STONE_NAME: row['stepname'],
                  STONE_DATE: [row['eta']]}
    milestones = pd.concat([milestones,
                            pd.DataFrame.from_dict(_milestone)],
                           ignore_index=True)

print(milestones)


# 로드맵 그래프 생성
_color_map = {evt: idx for idx, evt in enumerate(MAIN_EVENTS, 1)}

fig = go.Figure()

for _, row in milestones.iterrows():  # 각 milestone add_trace
    fig.add_trace(go.Scatter(
        x=[row[STONE_DATE]],
        y=[row[TIMELINE]],
        mode='markers',
        marker=dict(size=36,
                    symbol='circle',
                    sizemode='diameter',
                    color=pc.DEFAULT_PLOTLY_COLORS[_color_map.get(row['name'], 0)]
                    ),
        hoverinfo='text',
        name=f"{row[TIMELINE]}-{row[STONE_NAME]}",
        hovertext=row[STONE_NAME],
    ))

labels = []
for _, row in milestones.iterrows():  # 각 마일스톤에 이름 및 날짜 라벨 추가
    labels.append(dict(
        x=row[STONE_DATE],
        y=row[TIMELINE],
        text=str(f"{row[STONE_DATE].split('-')[-2]}/{row[STONE_DATE].split('-')[-1]}"),
        showarrow=False,
        font=dict(size=12, color='white')
    ))
    labels.append(dict(
        x=row[STONE_DATE],
        y=row[TIMELINE],
        yshift=24,
        text=row[STONE_NAME],
        showarrow=False,
        font=dict(size=12, color='black')
    ))

fig.update_yaxes(autorange='reversed')

fig.update_layout(
    xaxis=dict(type='date', tickmode='linear', dtick='M1'),
    annotations=labels,
    title='Roadmap',
    xaxis_title='Date',
    yaxis_title='Timelines',
    showlegend=False
)

st.plotly_chart(fig)
