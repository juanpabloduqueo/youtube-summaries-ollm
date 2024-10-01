import streamlit as st
import lchelper as lch

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.text_area("What is the YouTube video URL?", max_chars=200)
        query = st.text_area("Ask me about the video?", max_chars=500, key="query")
        language_options = {
            "English": "en",
            "Spanish": "es",
            "German": "de"
        }
        language_name = st.selectbox("Select the language of the video and the response:", list(language_options.keys()))
        language_code = language_options[language_name]
        submit_button = st.form_submit_button(label='Submit')       

if submit_button and query and youtube_url:
    with st.spinner('Processing...'):
        try:
            db = lch.create_vector_from_youtube_url(youtube_url, language_code)
            response, docs = lch.get_response_from_query(db, query, language_code)
            st.subheader("Answer:")
            st.markdown(response, unsafe_allow_html=False)
        except ValueError as e:
            st.error(f"An error occurred: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

