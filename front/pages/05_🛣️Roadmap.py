import pandas as pd
import plotly.colors as pc
import plotly.graph_objects as go
import streamlit as st

from front.dao import get_all_lot_steps, get_all_schedules

# milestone DataFrame 생성
_schedules = get_all_schedules()
_steps = get_all_lot_steps()

_filter = st.selectbox("Select projects: ", _steps['project'].unique())
schedules = _schedules[_schedules['project'] == _filter]
steps = _steps[_steps['project'] == _filter]

milestones = pd.DataFrame(columns=['timeline', 'name', 'date'])
for _, row in schedules.iterrows():
    for col in ('kick off', 'fab in', 'fab out'):
        _milestone = {'timeline': row['type'],
                      'name': [col],
                      'date': row[col]}
        milestones = pd.concat([milestones,
                                pd.DataFrame.from_dict(_milestone)],
                               ignore_index=True)
for _, row in steps.iterrows():
    _milestone = {'timeline': row['lot_name'],
                  'name': row['name'],
                  'date': [row['eta']]}
    milestones = pd.concat([milestones,
                            pd.DataFrame.from_dict(_milestone)],
                           ignore_index=True)

print(milestones)

# 로드맵 그래프 생성
_color_map = {'kick off': 1,
              'fab in': 2,
              'fab out': 3}

fig = go.Figure()

for _, row in milestones.iterrows():
    fig.add_trace(go.Scatter(
        x=[row['date']],
        y=[row['timeline']],
        mode='markers',
        marker=dict(size=36,
                    symbol='circle',
                    sizemode='diameter',
                    color=pc.DEFAULT_PLOTLY_COLORS[_color_map.get(row['name'], 0)]
                    ),
        hoverinfo='text',
        name=f"{row['timeline']}-{row['name']}",
        hovertext=row['name'],
    ))

annotations = []
for _, row in milestones.iterrows():
    annotations.append(dict(
        x=row['date'],
        y=row['timeline'],
        text=str(f"{row['date'].split('-')[-2]}/{row['date'].split('-')[-1]}"),
        showarrow=False,
        font=dict(size=12, color='white')
    ))
    annotations.append(dict(
        x=row['date'],
        y=row['timeline'],
        yshift=24,
        text=row['name'],
        showarrow=False,
        font=dict(size=12, color='black')
    ))

fig.update_yaxes(autorange='reversed')

fig.update_layout(
    xaxis=dict(type='date', tickmode='linear', dtick='M1'),
    annotations=annotations,
    title='Roadmap',
    xaxis_title='Date',
    yaxis_title='Timelines',
    showlegend=False
)

st.plotly_chart(fig)
