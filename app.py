import streamlit as st

st.title("🎬 AttentionX Lite")

uploaded_file = st.file_uploader("Upload a video", type=["mp4"])

if uploaded_file:
    st.success("Video uploaded successfully!")

    if st.button("Generate Highlights"):
        st.write("✨ Generating highlights...")
        st.success("✅ Highlight clip created (demo)")
