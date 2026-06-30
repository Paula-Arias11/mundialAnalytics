import streamlit as st
from statsbombpy import sb

# CONFIGURACIÓN DE LA PESTAÑA DEL NAVEGADOR
st.set_page_config(page_title='Spain Tactic Analyzer', layout='wide')

# TITULO PRINCIPAL EN LA PANTALLA
st.title('Spain historical tactical analyzer')
st.write('Analiza los partidos históricos de España con datos reales')

#BARRA LATERAL

st.sidebar.header('Filtros de la selección')

#COMPETICIONES

competiciones = sb.competitions()

#FILTRAR PARA QUEDARNOS CON LA COPA DEL MUNDO (en statsbomb es el 43)

mundiales = competiciones[competiciones['competition_id'] == 43]

#DESPLEZAR LAS EDICIONES DEL MUNDIAL DISPONIBLE

temporada_seleccionada = st.sidebar.selectbox('Selecciona la edición del mundial:', mundiales['season_name'].unique())

#OBTENER ID DE LA TEMPORADA/AÑO
id_temporada = mundiales[mundiales['season_name'] == temporada_seleccionada]['season_id'].values[0]

#TRAER PARTIDOS
partidos = sb.matches(competition_id=43, season_id=id_temporada)

#FILTRAR SOLO LOS DE ESPAÑA

partidos_espana= partidos[(partidos['home_team'] == 'Spain') | (partidos['away_team'] == 'Spain')]

#CREAR TEXTO PARA DESPLEGABLE

partidos_espana['match_label'] = partidos_espana['home_team'] + 'vs' + partidos_espana['away_team']

#DESPLEGABLE PARA ELEGIR PARTIDO

partido_seleccionaado = st.sidebar.selectbox('Selecciona el partido de España:', partidos_espana['match_label'].unique())
