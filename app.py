import streamlit as st
import time

# Set the page title and layout
st.set_page_config(page_title="Eid ul Fitr Wishes", page_icon="🌙", layout="centered")

# Display a title and subtitle
st.title("Eid ul Fitr Wishes 🌙")
st.subheader("Click the button below to receive a special message and see floating flowers! 🌸")

# HTML and JavaScript code for the floating flower animation
flower_animation_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eid ul Fitr Flowers</title>
    <style>
        @keyframes floatFlower {
            0% { transform: translateY(100vh); }
            100% { transform: translateY(-100vh); }
        }
        .flower {
            position: absolute;
            bottom: -50px;
            animation: floatFlower 7s ease-in-out infinite;
            width: 50px;
            height: 50px;
            background-image: url('https://img.icons8.com/emoji/452/flower-emoji.png');
            background-size: cover;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }
        .flower:nth-child(1) { background-color: #FF4500; }
        .flower:nth-child(2) { background-color: #FFD700; }
        .flower:nth-child(3) { background-color: #32CD32; }
        .flower:nth-child(4) { background-color: #1E90FF; }
        .flower:nth-child(5) { background-color: #FF69B4; }
        .flower:nth-child(6) { background-color: #8A2BE2; }
        .flower:nth-child(7) { background-color: #FF6347; }
        .flower:nth-child(8) { background-color: #00FA9A; }
        .flower:nth-child(9) { background-color: #00BFFF; }
        .flower:nth-child(10) { background-color: #FF1493; }
    </style>
</head>
<body>
    <div id="flowers"></div>
    <script>
        function createFlower() {
            const flower = document.createElement("div");
            flower.classList.add("flower");
            document.getElementById("flowers").appendChild(flower);

            // Randomize the position and animation duration
            flower.style.left = Math.random() * window.innerWidth + "px";
            flower.style.animationDuration = (Math.random() * 5 + 5) + "s";  // Randomize speed
            flower.style.animationTimingFunction = Math.random() > 0.5 ? "ease-in" : "ease-out"; // Randomize speed curve
        }

        // Create flowers every 0.3 seconds
        setInterval(createFlower, 300);
    </script>
</body>
</html>
"""

# Add the button that will trigger the message and flower animation
if st.button("Click for Best Wishes"):
    # Simulate a loading animation effect
    with st.spinner("Sending best wishes... Please wait."):
        time.sleep(2)  # Simulate some delay
    st.success("✨🌙 **Best Wishes for Eid ul Fitr!** 🌙✨")
    st.markdown("""
        🎉 May this Eid bring peace, prosperity, and happiness to you and your family! 
        🌙 **Nabila Bannay Khan** wishes you a blessed and joyous Eid filled with love, laughter, and countless blessings. 🙏💖
        
        🌟 May your prayers be answered, your fasts accepted, and your heart filled with joy! 🌟
        💫 Eid Mubarak! 💫
    """)

    # Display the flower animation HTML using Streamlit's html() function
    st.components.v1.html(flower_animation_html, height=600)

# Customizing the page further (optional)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #008CBA;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px;
        width: 250px;
    }
    .stButton>button:hover {
        background-color: #005F73;
    }
    </style>
""", unsafe_allow_html=True)
