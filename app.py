import streamlit as st
from home_page import show_home_page
from AI_Assistant import show_chatbot_page

PAGES = {
    "Home": show_home_page,
    "AI Assistant 🤖": show_chatbot_page,
}

def main():
    st.markdown(
        """
        <style>
        .sidebar-content {
            background-color: #1E1E1E; /* Sidebar background color */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sidebar shadow */
            animation: fadeInLeft 0.5s ease-out; /* Fade-in animation */
        }
        .sidebar-title {
            font-size: 24px;
            font-weight: bold;
            color: #FFD700; /* Sidebar title color */
            margin-bottom: 20px;
            animation: fadeInDown 0.8s ease-in-out; /* Fade-in animation */
        }
        .sidebar-title span {
          color: #ffd700; /* Yellow color */
        }
        .sidebar-option {
            color: #E8DAD7; /* Sidebar option color */
            margin-bottom: 10px;
            transition: color 0.3s ease-in-out; /* Smooth color transition */
        }
        .sidebar-option:hover {
            color: #FFD700; /* Hover color for sidebar options */
        }
        .sidebar-footer {
          text-align: center;
          color: #ccc;
          font-size: 14px;
          margin-top: 20px;
}
        
        @keyframes fadeInLeft {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("<div class='sidebar-title'>Navigation</div>", unsafe_allow_html=True)

    selection = st.sidebar.radio("", list(PAGES.keys()), key="sidebar_radio")
    
    page = PAGES[selection]
    page()

    st.sidebar.markdown("---")
    st.sidebar.markdown("<div class='sidebar-footer'>🌟 **Enjoy your experience!** 🌟 <br>| <a href='#' target='_blank'>Your App</a></div>", unsafe_allow_html=True)
    st.sidebar.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
