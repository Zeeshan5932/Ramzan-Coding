import streamlit as st
import random
import time
import requests
from PIL import Image

# ✅ Page configuration
st.set_page_config(page_title="💰 Money Making Machine", page_icon="💸", layout="wide")

# ✅ Subtitle for enjoyment (not real)
st.markdown("""
    <h4 style="text-align: center; color: gray;">
        🎭 Just for Fun – Not Real Money Making 🎭
    </h4>
    """, unsafe_allow_html=True)



# ✅ Custom Styling with full-page background
st.markdown("""
    <style>
    body { 
        background: linear-gradient(to right, #141e30, #243b55);  /* Full page gradient */
        color: white;
    }
    .main { 
        background: transparent !important;  /* Make main container transparent */
        padding: 0px !important;  /* Remove default padding */
    }
    .big-font { font-size:35px !important; font-weight: bold; color: #FFD700; }
    .money-text { font-size:28px !important; color: #00FF7F; }
    .stButton>button { background-color: #FFD700 !important; color: black !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ✅ Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Premium", "Partner Offers"])

# ✅ Header with Logo
col1, col2 = st.columns([1, 3])
with col1:
    try:
        img = Image.open("E:\\Ramzan coding practice\\Making-Money-Machine\\images\\money.jpg")
        st.image(img, width=100)
    except:
        st.warning("⚠️ Logo not found. Please upload 'money.jpg'.")

with col2:
    st.markdown('<p class="big-font">💰 Money Master Pro</p>', unsafe_allow_html=True)
    st.caption("Created by Zeeshan | Make Money Online")

# ✅ Home Page
if page == "Home":
    st.markdown("---")
    st.markdown('<p class="money-text">💸 Instant Cash Generator</p>', unsafe_allow_html=True)

    with st.expander("Generate Money Now!", expanded=True):
        if st.button("🚀 Generate Magic Money", use_container_width=True):
            with st.spinner("Hacking the Federal Reserve..."):
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.05)
                    progress_bar.progress(percent_complete + 1)
                amount = random.randint(500, 5000)
                st.balloons()
                st.success(f"🎉 Congratulations! You've generated **${amount:,}** (Simulated Money)")

    st.markdown("---")
    st.markdown('<p class="money-text">📝 Wealth Wisdom</p>', unsafe_allow_html=True)

    if st.button("🌟 Get Millionaire Quote", use_container_width=True):
        with st.spinner("Connecting with billionaires..."):
            try:
                response = requests.get("https://api.adviceslip.com/advice", timeout=5)
                response.raise_for_status()
                data = response.json()
                quote = data["slip"]["advice"] if "slip" in data else "No advice available now."
            except requests.exceptions.RequestException as e:
                quote = f"Error fetching quote: {e}"
            st.success(f'💬 *"{quote}"*')

# ✅ Premium Features
elif page == "Premium":
    st.markdown('<p class="money-text">💎 Premium Features</p>', unsafe_allow_html=True)
    st.write("""
    - Exclusive money-making strategies 🚀
    - Personal wealth coach 📈
    - AI-powered investment insights 🤖
    """)
    
    if st.button("💰 Upgrade to Pro ($99/month)", use_container_width=True):
        st.markdown("""
        <a href="https://buy.stripe.com/test_4gw3fy1Bv1RqcFqfZ1" target="_blank">
            <button style="background-color:#FF4B4B; color:white; padding:10px; border:none; border-radius:5px; cursor:pointer;">
                Proceed to Payment
            </button>
        </a>
        """, unsafe_allow_html=True)

# ✅ Partner Offers
elif page == "Partner Offers":
    st.markdown('<p class="money-text">🤝 Partner Offers</p>', unsafe_allow_html=True)
    st.write("""
    - **High-Yield Investments (20% ROI)**
    - **Crypto Masterclass**
    - **Affiliate Program (50% Commission)**
    """)
    


    if st.button("🤑 Claim Offers Now", use_container_width=True):
        st.success("Its For Fun No Real Offers Available")

# ✅ Footer
st.markdown("---")
st.markdown("### 🔥 Hot Offers")
st.markdown("""
<marquee behavior="scroll" direction="left" scrollamount="10">
🚨 EARN $5000 DAILY | 💵 GUARANTEED RETURNS | 🤑 RISK-FREE INVESTMENTS | 💰 INSTANT PAYOUTS
</marquee>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("💵 Money Tools")
    st.markdown("""
    - [💰 Best Investment App](https://www.etoro.com/)
    - [📈 Stock Market Course](https://www.udemy.com/course/stock-trading/)
    - [💻 Freelancing Mastery](https://www.freelancer.com/)
    """)
    st.markdown("---")
    st.markdown("**Enhanced by Zeeshan** | *Version 2.0*")
