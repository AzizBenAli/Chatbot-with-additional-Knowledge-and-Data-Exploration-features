import streamlit as st

def show_home_page():
    
    st.markdown(
        """
        <style>
        /* Global Styles */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            color: #333333;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }

        /* Title Styles */
        .header {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 10px 20px; /* Reduced padding */
            background-color: #0E1117;
            color: #FFD700;
            margin-bottom: 30px;
            border-radius: 10px;
            font-size: 44px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            animation: fadeInTitle 1s ease-in-out; /* Apply fade-in animation to the title */
        }

        /* Info Section Styles */
        .info-section {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 30px;
            background-color: #0E1117;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            margin-bottom: 40px;
            animation: slideInInfo 1s ease-in-out; /* Apply slide-in animation to the info section */
        }

        .info-section img {
            max-width: 300px;
            border-radius: 10px;
            margin-right: 30px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .info-text {
            font-size: 30px; /* Increased paragraph font size */
            color: #ffffff;
            line-height: 1.6;
            font-family: ADLaM Display; /* Changed font style */
            font-style: italic; /* Added italic style */
        }

        /* Animation Keyframes */
        @keyframes fadeInTitle {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @keyframes slideInInfo {
            from {
                transform: translateX(-20px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main title with emoji
    st.markdown("<h1 class='header'>Hi, I am Ted!<br> Your AI Assistant </h1>", unsafe_allow_html=True)

    # Performance Metrics section with images and text
    st.markdown(
        """
        <div class="info-section">
            <img src="https://images.unsplash.com/photo-1589254066213-a0c9dc853511?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHJvYm90fGVufDB8fDB8fHww" alt="Performance Metrics" />
            <div class="info-text">
                <h2>I'm a versatile chatbot equipped to assist with a wide range of queries and facilitate data exploration using a diverse set of tools programmed into my system.</h2>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    show_home_page()
