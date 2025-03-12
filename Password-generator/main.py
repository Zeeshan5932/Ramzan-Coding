import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def password_strength(password):
    strength = 0
    if len(password) >= 12:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1
    return strength

st.title("🔐 Password Generator")

# Layout
col1, col2 = st.columns(2)

with col1:
    length = st.slider("Length of password", min_value=4, max_value=30, value=12)
    use_digits = st.checkbox("Include digits", value=True)
    use_special = st.checkbox("Include special characters", value=True)

with col2:
    st.write("### Password Strength Tips")
    st.write("- Use at least 12 characters.")
    st.write("- Include numbers and special characters.")
    st.write("- Avoid common words or patterns.")

if st.button("Generate New Password"):
    password = generate_password(length, use_digits, use_special)
    st.write("### Generated Password:")
    
    # Use st.code with the `copy` option to allow users to copy the password
    st.code(password, language="plaintext")
    
    # Password strength indicator
    strength = password_strength(password)
    st.write("### Password Strength:")
    if strength == 3:
        st.success("Strong")
    elif strength == 2:
        st.warning("Moderate")
    else:
        st.error("Weak")

    st.write("-----------------------------------------------")
    st.write("Password generated successfully!")