
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Dance Coach AI",
    page_icon="🩰"
)

st.title("🩰 Dance Coach AI")
st.write("Your personal AI dance instructor")

st.sidebar.header("AI & Role Settings")

api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key",
    type="password"
)

role = st.sidebar.selectbox(
    "Choose a creative role",
    [
        "Dance Instructor",
        "Choreographer",
        "Performance Critic",
        "Acting Coach",
        "Fashion Stylist"
    ]
)

prompts = {
    "Dance Instructor":
        "You are a professional dance instructor. "
        "Give clear, practical advice about technique, "
        "movement, rhythm, and expression.",

    "Choreographer":
        "You are a professional choreographer. "
        "Suggest creative movements and choreography ideas.",

    "Performance Critic":
        "You are a performing arts critic. "
        "Analyze performances constructively.",

    "Acting Coach":
        "You are a professional acting coach. "
        "Help performers express emotions naturally.",

    "Fashion Stylist":
        "You are a professional fashion stylist. "
        "Recommend outfits, colors, and stage costumes."
}

st.info(prompts[role])

question = st.text_area(
    "Ask your creative coach a question",
    placeholder="How can I express sadness through dance?"
)

if st.button("Generate Response"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": prompts[role]
                        },
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                )

            st.success("AI Response")
            st.write(
                response.choices[0].message.content
            )

        except Exception as e:
            st.error(
                "Unable to generate a response. "
                "Please check your API key and API credits."
            )

st.caption("Powered by OpenAI API & Streamlit")
