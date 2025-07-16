import streamlit as st
from pandas import read_csv
col1, col2 = st.columns(2) 

#layout wide means fit to size of window
st.set_page_config(layout="wide")

with col1:
    st.image("photo.jpg")

with col2:
    st.title("Kaamil Rifaq")
    content = """Kaamil Rifaq is a final-year Mechanical Engineering student at NUST with strong leadership, technical, and industrial experience. He has led award-winning engineering projects, interned at Atlas Honda, and co-founded a sustainability-focused startup. Kaamil aims to drive innovation in renewable energy and engineering through global exposure and advanced education."""
    st.write(content)

st.write("This is the first initialization")

col3, gap, col4 = st.columns([3,1,3])

df = read_csv("data.csv",sep = ";")      #converts the code into classes with each class being a row
print(df)

with col3:
    for index,classes in df.iterrows():
        if index % 2 == 0:
            st.title(classes["title"])
            st.text(classes["description"])
            st.image(f"pictures/{classes["image"]}")
            st.write(f"[Source Code]({classes["url"]})")

with col4:
    for index,classes in df.iterrows():          # Very Important iterrows
        if index % 2 != 0:
            st.title(classes["title"])
            st.text(classes["description"])
            st.image(f"pictures/{classes["image"]}")
            st.write(f"[Source Code]({classes["url"]})")
        

#with col4