import streamlit as st

col1, col2 = st.columns(2)
#layout wide means fit to size of window
st.set_page_config(layout="wide")
with col1:
    st.image("photo.jpg")

with col2:
    st.title("Kaamil Rifaq")
    content = """Kaamil Rifaq is a final-year Mechanical Engineering student at NUST with strong leadership, technical, and industrial experience. He has led award-winning engineering projects, interned at Atlas Honda, and co-founded a sustainability-focused startup. Kaamil aims to drive innovation in renewable energy and engineering through global exposure and advanced education."""
    st.write(content)

st.write("This is the First initialization of the app sdfsadfsafsfasdfsfasdf f asf asdfs fd fsd fasf f sdf afasfa sf sd sd")