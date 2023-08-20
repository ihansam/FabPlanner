from typing import Optional

import pandas as pd
from plotly import graph_objects as go, colors as pc

from front.api_call import get_all_schedule, get_all_fab_step


MAIN_EVENTS = ['kickOff', 'fabIn', 'fabOut', 'approved']
TIMELINE = 'timeline'
STONE_NAME = 'name'
STONE_DATE = 'date'


def gather_milestones(project, gather_schedule: bool = True, gather_fab_step: bool = True):
    _all_schedules = get_all_schedule()
    _all_steps = get_all_fab_step()
    schedules = _all_schedules[_all_schedules['project'] == project]
    steps = _all_steps[_all_steps['project'] == project]

    _milestones = pd.DataFrame(columns=[TIMELINE, STONE_NAME, STONE_DATE])

    if gather_schedule:
        for _, schedule in schedules.iterrows():  # schedule에 속한 메인 이벤트 취합
            for event in MAIN_EVENTS:
                _milestone = {TIMELINE: schedule['type'],
                              STONE_NAME: [event],
                              STONE_DATE: schedule[event]}
                _milestones = pd.concat([_milestones, pd.DataFrame.from_dict(_milestone)],
                                        ignore_index=True)
    if gather_fab_step:
        for _, row in steps.iterrows():  # fab step에 속한 이벤트 취합
            _milestone = {TIMELINE: row['fabname'],
                          STONE_NAME: row['stepname'],
                          STONE_DATE: [row['eta']]}
            _milestones = pd.concat([_milestones,
                                     pd.DataFrame.from_dict(_milestone)],
                                    ignore_index=True)
    print(_milestones)
    return _milestones


def generate_roadmap(milestones, project_name: Optional[str] = None):
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
        title=f'{project_name or ""} Roadmap',
        xaxis_title='Date',
        yaxis_title='Timelines',
        showlegend=False
    )
    return fig
