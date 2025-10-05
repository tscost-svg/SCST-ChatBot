import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Telangana SC/ST DSS Data Assistant",
    page_icon="🗺️",
    layout="centered",
)

st.title("🗺️ Telangana SC/ST DSS Data Assistant")
st.caption("Ask questions about datasets, analytics, and indicators from the Decision Support System (DSS) Hub.")

# Use secret key if available, else placeholder
api_key = st.secrets.get("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

context = """
You are an intelligent data assistant for the Telangana SC/ST Decision Support System (DSS).
This Hub integrates data across five major thematic areas:
1. Education – literacy rates, school enrolment, dropout rates, higher education access.
2. Livelihood – employment generation, agricultural activities, SHG (Self Help Group) participation.
3. Skill Development – vocational training, youth skill programs, employment linkages.
4. Health – healthcare access, maternal and child health, public health programs.
5. Financial Inclusion – access to banking, SHG credit, financial literacy programs.

Data is collected through ArcGIS Survey123 and stored in related tables.
The base survey (CESS_SURVEY_0) contains household-level data with GlobalID.
All other thematic datasets (Education, Health, Livelihood, Skill Development, Financial Inclusion)
are linked using the ParentGlobalID field.

You are embedded inside an ArcGIS Hub site and must answer in a friendly, concise, and data-aware way.
If the user asks for specific numbers or insights, guide them to relevant dashboards or datasets on the Hub.

Example sources (replace with actual Hub URLs):
- Education Dashboard: https://hub.telanganadss.in/education
- Livelihood Dashboard: https://hub.telanganadss.in/livelihood
- Health Dashboard: https://hub.telanganadss.in/health
- Skill Development Dashboard: https://hub.telanganadss.in/skill
- Financial Inclusion Dashboard: https://hub.telanganadss.in/finance

When unsure, respond: “Please refer to the relevant dashboard or dataset on the DSS Hub for verified data.”
"""

st.markdown("### 💬 Chat with the Data Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello 👋! I’m your Telangana DSS Data Assistant. How can I help you today?"}
    ]

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

user_input = st.chat_input("Ask a question about Telangana SC/ST DSS data...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    with st.spinner("Analyzing DSS data..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": context},
                *st.session_state.messages,
            ],
            temperature=0.4,
        )
        answer = response.choices[0].message.content.strip()

    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

st.divider()
st.caption("© 2025 Telangana SC/ST DSS | Powered by OpenAI GPT and ArcGIS Hub")
