import streamlit as st
import asyncio
from deriv_api import DerivAPI

# UI Configuration
st.set_page_config(page_title="Deriv Trading Bot", layout="centered")
st.title("📊 Deriv Trading Bot")

# Input field for API token
token = st.text_input("🔑 Enter API Token", type="password")

# Initialize the API
api = DerivAPI(app_id=1089)  # You can use your own app_id here

# Async helpers
async def authorize(token):
    return await api.authorize({'authorize': token})

async def get_balance():
    res = await api.balance()
    return res['balance']['balance']

# Run when button is clicked
if token and st.button("Authorize"):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(authorize(token))
        st.success("✅ Authorized Successfully")

        balance = loop.run_until_complete(get_balance())
        st.info(f"💰 Current Balance: ${balance:.2f}")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

