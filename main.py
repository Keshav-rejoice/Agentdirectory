import streamlit as st
import pandas as pd


agents = [
    {"name": "Capital firm Bot","Built by":"Keshav Sharma", "description": "Handles financial news related to stock market to make faster  decisions", "url": "https://capital-firm-bot-hqsf58hbezwpunw9wg7sfb.streamlit.app/"},
    {"name": "Live Loan Approval Agent","Built by":"Keshav Sharma" ,"description": "Built credit scoring and loan underwriting engines to offer instant loan approvals, reducing delays and improving the customer experience.", "url": "https://loan-approval-system-g8t2yfmaccdzdwqragxzxy.streamlit.app/"},
    {"name": "Voucher chatbot", "Built by":"Utsav davda","description": """Answers user queries on various types of vouchers and their usage details (conditions for use, discount amount, purchase amount,etc).
It also answers tokens purchased by the user and give personalized response based on it.
Contains a dataset of 3 tables: users, vouchers and tables.
Each user have a set of tokens. Each token has a token id and the token id maps to a voucher type.
The voucher table contains all kinds of vouchers available and details on each of them(ID,Type,ConditionsStatus,Amount,MinPurchaseAmount)""", "url": "https://voucheragentpy-utsavsd.streamlit.app/"},
{"name": "Market Sentiment Chatbot","Built by":"Utsav davda","description":"""The news collected through APIs is marked with metadata for each article: EG: People, companies, stock, sentiment, sector, etc.
The user can ask any question related to the news articles, they will be filtered based on the query and the meta-data attached to them. The filtered articles will be used as context to answer the user's query.""","url" :"https://retreiverpy-utsavsd.streamlit.app/"},
{"name":"Crypto Chatbot","Built by":"Keshav Sharma","description": "Real-time price alerts, volume changes, or movement tracking to help retail traders make informed decisions.","url": "https://crypto-bot-qeac8utvilgpr4swftd7nk.streamlit.app/"},
{"name":"Policy Summarizer Agent","Built by":"Keshav Sharma","description":"provide clear, simplified explanations of complex policy terms, answering specific client questions about their coverage.","url":"https://policyexplainer-bot-mlkwaqzxdw2aquvzuw59jy.streamlit.app/"},



]

st.title("Agent Directory")

st.subheader("Agent Table")
agent_df = pd.DataFrame(agents)  # Convert to a DataFrame for tabular display
st.table(agent_df)

st.subheader("Agent Cards")
for agent in agents:
    with st.expander(agent["name"]):  # Expander for each agent as a card
        st.write(agent["description"])
        if "url" in agent:
            st.markdown(f"[Visit {agent['name']}]({agent['url']})")

