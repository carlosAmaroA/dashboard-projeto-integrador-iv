import dash_bootstrap_components as dbc 
from dash import html

dropdown = dbc.Card([
        dbc.CardBody([
            html.H6("Ano",className='card-title'),
            dbc.Select(
                id="overview-select-year",
                options=[{"label": str(y), "value": y} for y in range(2017, 2025)],
                value=2017
            )
        ])
], className="mb-3 h-80")