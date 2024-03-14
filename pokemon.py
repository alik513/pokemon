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
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), pokemon['sprites']['front_default'], pokemon['cries']['latest']
    except:
        return 'Error', np.NAN, np.NAN, np.NAN, np.Nan 


        


pokemon_number = st.slider("Pick a pokemon",
                           min_value = 1,
                           max_value = 1025
                           )

name, height, weight, moves, image_url, audio_url = get_details(pokemon_number)
height = height * 10
weight = weight / 10


height_data = pd.DataFrame({'Pokemon': ['Sobble', name.title(), 'Celesteela'],
               'Heights': [30, height, 920]})


colors = ['blue', 'indigo', 'purple']

graph = sns.barplot(data = height_data,
                    x = 'Pokemon',
                    y = 'Heights',
                    palette = colors)

col1, col2, col3, = st.columns(3)

with col1:
	st.image(image_url, caption= name.title() , use_column_width=True)

with col2:
      st.header(name.title())
      st.divider()
      st.subheader(f'Height: {height} cm') 
      st.subheader(f'Weight: {weight} kg')
      st.subheader(f'Move Count: {moves}')
with col3:
      st.header('Battle Cry: ')
      st.divider()
      st.audio(audio_url, format = 'audio/ogg')
      
	  


st.divider()
st.pyplot(graph.figure)
