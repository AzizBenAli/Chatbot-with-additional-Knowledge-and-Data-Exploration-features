import streamlit as st

def show_home_page():
    st.markdown(
        """
        <style>
        body {
            background-color: #1E1E1E; /* Background color */
            color: #E8DAD7; /* Text color */
        }
        .header-text {
            font-size: 36px;
            font-weight: bold;
            color: #FFD700; /* Header text color */
            margin-bottom: 20px;
            animation: fadeInUp 1s ease-in-out; /* Fade-in animation */
        }
        .info-section {
            padding: 20px;
            background-color: #333; /* Info section background color */
            border-radius: 10px;
            margin-bottom: 20px;
            animation: slideInLeft 1s ease-in-out; /* Slide-in animation */
        }
        .info-section p {
            margin-bottom: 15px;
            font-size: 18px;
        }
        .info-section ul {
            margin-bottom: 15px;
        }
        .info-section li {
            margin-bottom: 10px;
            font-size: 16px;
        }
        .contact-section {
            padding: 20px;
            background-color: #444; /* Contact section background color */
            border-radius: 10px;
            margin-bottom: 20px;
            animation: fadeInRight 1s ease-in-out; /* Fade-in animation */
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes fadeInRight {
            from {
                opacity: 0;
                transform: translateX(20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main title with emoji
    st.title("🤖 Welcome to Our ChatBot App 🚀")
    # Header for Performance Metrics section with emoji
    st.markdown('<p class="header-text">📊 Performance And Use</p>', unsafe_allow_html=True)
    
    # Performance Metrics section with emojis
    st.markdown(
    """
    <div class="info-section">
        <p>Our AI assistant is currently undergoing development and continuously improving its capabilities. 
        It's designed to handle a variety of tasks, including <span style='color:#FF6347'>knowledge-based queries</span>, 
        <span style='color:#FF6347'>mathematical problem-solving</span>, <span style='color:#FF6347'>uploading CSV files</span>, 
        and even <span style='color:#FF6347'>uploading PDF files</span> for engaging in conversations with your PDF content.</p>
    </div>
    """,unsafe_allow_html=True
    )


    st.markdown('<p class="header-text">📧 Contact Us</p>', unsafe_allow_html=True)
    
    # Contact Us section with emoji
    st.markdown(
        """
        <div class="contact-section">
            <p>For feedback or inquiries, please contact us at:</p>
            <p><a href="mailto:benaliaziz@gmail.com">📩 benaliaziz@gmail.com</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    show_home_page()
