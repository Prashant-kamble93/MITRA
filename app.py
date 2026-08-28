import streamlit as st
from workflow import run_mitra

st.set_page_config(
    page_title="MITRA",
    page_icon="🤖"
)

st.title("🤖 MITRA")
st.caption("Meaningful Intelligent Trusted Responsive Assistant")

user_input = st.text_area(
    "What can I help you with?",
    placeholder="Ask MITRA anything..."
)

if st.button("Ask MITRA"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("MITRA is thinking..."):
            result = run_mitra(user_input)

        if not result["success"]:
            st.error(result["answer"])
        else:
            st.subheader("MITRA's Response")
            st.write(result["answer"])

            with st.expander("View MITRA's workflow"):
                st.write("**Intent:**")
                st.write(result["intent"])

                st.write("**Plan:**")
                st.write(result["plan"])

                st.write("**Review:**")
                st.write(result["review"])