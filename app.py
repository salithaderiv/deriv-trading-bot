import streamlit as st
import asyncio
from deriv_api import DerivAPI

# Page setup
st.set_page_config(page_title="Deriv Trading Bot", layout="centered")
st.title("📊 Deriv Trading Bot")

# User input
token = st.text_input("🔑 Enter API Token", type="password")

# Only run API code when button is clicked
if token and st.button("Authorize"):
    try:
        # Set up a new asyncio loop (required by DerivAPI)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # Initialize API inside the event loop
        api = DerivAPI(app_id=1089)  # demo app_id

        # Async functions inside the event loop
        async def main():
            await api.authorize({'authorize': token})
            balance = await api.balance()
            return balance['balance']['balance']

        # Run the async tasks
        balance = loop.run_until_complete(main())
        st.success("✅ Authorized Successfully")
        st.info(f"💰 Balance: ${balance:.2f}")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
