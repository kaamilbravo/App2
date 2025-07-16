import streamlit as st
from pandas import read_csv
col1, col2 = st.columns(2)
#layout wide means fit to size of window
st.set_page_config(layout="wide")
with col1:
    st.image("MainProj/photo.jpg")

with col2:
    st.title("Kaamil Rifaq")
    content = """Kaamil Rifaq is a final-year Mechanical Engineering student at NUST with strong leadership, technical, and industrial experience. He has led award-winning engineering projects, interned at Atlas Honda, and co-founded a sustainability-focused startup. Kaamil aims to drive innovation in renewable energy and engineering through global exposure and advanced education."""
    st.write(content)

st.write("sdfsdfsf This is the First initialization of the app sdfsadfsafsfasdfsfasdf f asf asdfs fd fsd fasf f sdf afasfa sf sd sd")

col3,col4 = st.columns(2)

df = read_csv("MainProj/data.csv",sep = ";")
print(df)
with col3:
    for index,classes in df.iterrows():
        if index % 2 == 0:
            st.title(classes["title"])
            st.text(classes["description"])
            st.image(f"MainProj/pictures/{index+1}.png")
with col4:
    for index,classes in df.iterrows():
        if index % 2 != 0:
            st.title(classes["title"])
            st.text(classes["description"])
            st.image(f"MainProj/pictures/{index+1}.png")
        

#with col4