import streamlit as st
import pandas as pd
import pickle
import requests
movies_list=pickle.load(open('movie_dict.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))
df=pd.DataFrame(movies_list)
st.title("Movie Recommender System")
movie=st.selectbox(
    'Select Your Movie',
    (df['title'].values)
)

def fetch_poster(movie_id):
  response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=94e093ef0851a594fdb5852f470ce81d'.format(movie_id))
  data=response.json();
  print(data['poster_path'])
  return "https://image.tmdb.org/t/p/original/"+data['poster_path'];
def recommend (movie):
  themovie=df[df['title']==movie].index[0]
  distances=similarity[themovie]
  movieslist=(sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6])
  l=[]
  posters=[];
  for i in movieslist:
    l.append(df.iloc[i[0]]['title'])
    posters.append(fetch_poster(df.iloc[i[0]]['id']));
  return l,posters;

if st.button('Recommend'):
  name,posters=recommend(movie);

  tab1,tab2,tab3,tab4,tab5 = st.tabs([name[0],name[1],name[2],name[3],name[4]])
  with tab1:
    st.header(name[0])
    st.image(posters[0],width=200)
  with tab2:
    st.header(name[1])
    st.image(posters[1],width=200)
  with tab3:
    st.header(name[2])
    st.image(posters[2],width=200)
  with tab4:
      st.header(name[3])
      st.image(posters[3],width=200)
  with tab5:
      st.header(name[4])
      st.image(posters[4],width=200)