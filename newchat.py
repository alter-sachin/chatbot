import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html
from chatbot import main_chain





# with st.spinner("Indexing document... This may take a while⏳"):
#     folder_index = embed_files(
#         files=[chunked_file],
#         embedding=EMBEDDING if model != "debug" else "debug",
#         vector_store=VECTOR_STORE if model != "debug" else "debug",
#         openai_api_key=openai_api_key,
#     )

with st.form(key="qa_form"):
    st.header("Hero Homes Ask Us Anything")
    query = st.text_area("Ask a question about our project in Mohali")
    submit = st.form_submit_button("Ask")





if submit:
    # if not is_query_valid(query):
    #     st.stop()
    #on_open()
    # Output Columns
    #answer_col = st.columns(1)

    #llm = get_llm(model=model, openai_api_key=openai_api_key, temperature=0)
    with st.spinner("Indexing document... This may take a while⏳"):
        result = main_chain(query)

        st.text_area(result)

    # with sources_col:
    #     st.markdown("#### Sources")
    #     for source in result.sources:
    #         st.markdown(source.page_content)
    #         st.markdown(source.metadata["source"])
    #         st.markdown("---")