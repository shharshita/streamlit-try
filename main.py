import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
from annotated_text import annotated_text

colours = {
	'normal': '#A8A77A',
	'fire': '#EE8130',
	'water': '#6390F0',
	'electric': '#F7D02C',
	'grass': '#7AC74C',
	'ice': '#96D9D6',
	'fighting': '#C22E28',
	'poison': '#A33EA1',
	'ground': '#E2BF65',
	'flying': '#A98FF3',
	'psychic': '#F95587',
	'bug': '#A6B91A',
	'rock': '#B6A136',
	'ghost': '#735797',
	'dragon': '#6F35FC',
	'dark': '#705746',
	'steel': '#B7B7CE',
	'fairy': '#D685AD',
}

st.title('Pokemon Data Visualization Tool')
st.divider()

#Get a random pokedex number
random_number = str(np.random.randint(1, 1000))
random_number_2 = str(np.random.randint(1, 1000))

#Fetch the name of that pokemon 
def get_random_pokemon(number:int) -> str:
    try: 
        url = 'https://pokeapi.co/api/v2/pokemon/'+number
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data.get('name')


poke_name = get_random_pokemon(random_number)
poke_name_2 = get_random_pokemon(random_number_2)

def get_pokemon_data(pokemon_name) -> dict:
    try: 
        url = 'https://pokeapi.co/api/v2/pokemon/'+pokemon_name
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data

pokemon_data = get_pokemon_data(poke_name)
pokemon_data_2 = get_pokemon_data(poke_name_2)

if pokemon_data and pokemon_data_2:
    col1, col2 = st.columns(2)

    with col1:
        st.header(pokemon_data.get('name').capitalize())
        st.image(pokemon_data.get('sprites').get('front_default'))
        st.write('Pokemon Weight',pokemon_data.get('weight'))
        poke_type = pokemon_data.get('types')[0].get('type').get('name') 
        annotated_text(
            (poke_type,"", colours[poke_type]),
        )
    with col2:
        st.header(pokemon_data_2.get('name').capitalize())
        st.image(pokemon_data_2.get('sprites').get('front_default'))
        st.write('Pokemon Weight',pokemon_data.get('weight'))
        poke_type = pokemon_data_2.get('types')[0].get('type').get('name') 
        annotated_text(
            (poke_type,"", colours[poke_type]),
        )    
    

    stats_data = {stat.get('stat').get('name'): stat.get('base_stat') for stat in pokemon_data.get('stats')}
    stats_data_2 = {stat.get('stat').get('name'): stat.get('base_stat') for stat in pokemon_data_2.get('stats')}
    stats_df = pd.DataFrame([stats_data,stats_data_2])

    st.bar_chart(stats_df)
       

# Load the data
# def load_data():
#    data = pd.read_csv('pokemon.csv')
#   return data

#data = load_data()

# create a dataframe with the pokemon data
#df = pd.DataFrame(data)

# Display the data
#st.dataframe(df)