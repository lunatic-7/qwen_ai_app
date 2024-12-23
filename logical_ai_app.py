import streamlit as st
from langchain_openai import ChatOpenAI

# Page configuration
st.set_page_config(
    page_title="AI Math & Logic Solver",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stTextArea>div>div>textarea {
        background-color: #555555;
        border-radius: 5px;
        padding: 10px;
    }
    .success-box {
        background-color: #f0f7f4;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 10px 0;
    }
    .sidebar-content {
        padding: 20px;
    }
    h1 {
        color: #1e3d59;
        margin-bottom: 2rem;
    }
    h3 {
        color: #1e3d59;
    }
    </style>
    """, unsafe_allow_html=True)

# Main title with emoji and subtitle
st.title("🧮 AI Math & Logic Solver")
st.markdown("""
    <p style='font-size: 1.2em; color: #666; margin-bottom: 2rem;'>
    Your intelligent companion for solving complex mathematical problems, logical puzzles, 
    and reasoning challenges with ease and precision.
    </p>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    st.image("https://api.dicebear.com/7.x/shapes/svg?seed=math", width=100)  # Placeholder icon
    st.header("⚙️ Configuration")
    
    api_key = st.text_input(
        "OpenRouter API Key:",
        type="password",
        help="Enter your OpenRouter API key to access the AI model"
    )
    
    st.markdown("---")
    st.markdown("""
        ### 📚 Tips for best results:
        - Be specific in your questions
        - Include all relevant information
        - Format mathematical expressions clearly
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Main app logic
if not api_key:
    st.warning("🔑 Please enter your OpenRouter API Key in the sidebar to begin.")
else:
    try:
        # Initialize AI client
        client = ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            model="qwen/qwq-32b-preview",
        )

        # Create two columns for better layout
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.header("🤔 Ask Your Question")
            user_query = st.text_area(
                "Enter your problem here:",
                height=150,
                placeholder="Example: Solve the quadratic equation x² + 5x + 6 = 0"
            )

        with col2:
            st.markdown("""
                ### 💡 Example queries:
                - Solve algebraic equations
                - Analyze logical statements
                - Solve geometry problems
                - Evaluate probability scenarios
            """)

        if st.button("🚀 Solve Problem", key="solve_button"):
            if user_query.strip():
                with st.spinner('Thinking...'):
                    try:
                        response = client.invoke(user_query)
                        st.markdown("<div class='success-box'>", unsafe_allow_html=True)
                        st.markdown("### 💫 Solution:")
                        st.write(response.content)
                        st.markdown("</div>", unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"🔴 Error processing your request: {str(e)}")
            else:
                st.warning("⚠️ Please enter a question or problem to solve.")

        # Footer with additional information
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 🎯 Features")
            st.markdown("- Advanced problem-solving\n- Step-by-step explanations\n- Multiple domains support")
        
        with col2:
            st.markdown("### 🛠️ Powered By")
            st.markdown("- Qwen 32B Model\n- OpenRouter API\n- Streamlit")
        
        with col3:
            st.markdown("### 📊 Capabilities")
            st.markdown("- Mathematics\n- Logic\n- Reasoning\n- Problem-solving")

    except Exception as e:
        st.sidebar.error(f"🔴 Error initializing AI client: {str(e)}")