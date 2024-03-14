import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests

st.title("Pokemon Explorer!")

st.text('''
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|

''')

### display image of pokemon
### make it look better
## add the audio of the latest battle cry
### 
##



def get_details(poke_number):   
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
        response = requests.get(url)
        pokemon = response.json()
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), pokemon['sprites']['front_default'], [pokemon['cries']['latest']]
    except:
        return 'Error', np.NAN, np.NAN, np.NAN, 'default_image_url', 

    
def display_image(image_url):
    if image_url:
        st.image(image_url, caption='Pokemon Image', use_column_width=True)
        


pokemon_number = st.slider("Pick a pokemon",
                           min_value = 1,
                           max_value = 150
                           )

name, height, weight, moves, image_url, audio_url = get_details(pokemon_number)
height = height * 10


height_data = pd.DataFrame({'Pokemon': ['Weedle', name.title(), 'lapras'],
               'Heights': [30, height, 250]})


colors = ['purple', 'red', 'orange']

graph = sns.barplot(data = height_data,
                    x = 'Pokemon',
                    y = 'Heights',
                    palette = colors)


st.write('Image:')
display_image(image_url)
st.write(f'Name: {name.title()}')
st.write(f'Height: {height}')
st.write(f'Weight: {weight}')
st.write(f'Move Count: {moves}')



st.pyplot(graph.figure)
