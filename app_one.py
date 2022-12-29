import streamlit as st
if "photo" not in st.session_state:
    st.session_state["photo"]="not done"
col1,col2,col3=st.columns([1,2,1])
col1.markdown("welcome to my app")

def changed_photo_state():
    st.session_state["photo"]="done"
uploaded_photo=col2.file_uploader("upload a photo")
camera_photo=col2.camera_input("Take a photo")

if st.session_state["photo"]=="done":
    progress_bar=col2.progress(0)
    for perc_completed in range(100):
        time.sleep(5)
        progress_bar.progress(perc_completed+1)
    col2.success("Photo uploaded")
    col3.metric(label="Temp",value="60",delta="3")

    with st.expander("click to read"):
        st.write('Hello there')
        if uploaded_photo is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photo)