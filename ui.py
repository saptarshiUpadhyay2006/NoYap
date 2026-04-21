import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="NoYap | YouTube Video Summarizer",
    page_icon="🤫",
    layout="centered",
)

st.markdown("""
<style>

/* Improve default text contrast */
body, p, span, div {
    color: #E5E7EB !important;   /* light gray instead of dull gray */
}

/* Headings */
h1, h2, h3 {
    color: #FFFFFF !important;
}

/* Highlight keywords like Agno, Groq */
.highlight {
    color: #FFFFFF;
    font-weight: 600;
    background: linear-gradient(90deg, #6366F1, #8B5CF6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Code-style highlight (alternative) */
.code-highlight {
    background-color: #1F2937;
    padding: 3px 6px;
    border-radius: 5px;
    font-size: 14px;
    color: #F9FAFB;
    font-family: monospace;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1><span class='highlight'>NoYap</span> 🤫</h1>", unsafe_allow_html=True)
st.caption("Skip the 10-minute intro. Get straight to the lore, summaries, and key takeaways.")

st.markdown(
    'Built using <span class="highlight">Agno</span> and <span class="highlight">Groq</span>',
    unsafe_allow_html=True
)

st.divider()

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

st.markdown("### Drop your link below: ")
video_url = st.text_input(
    "YouTube URL", 
    label_visibility="collapsed",
    placeholder="e.g., https://www.youtube.com/watch?v=..."
)

analyze_button = st.button("Analyze Video", type="primary", use_container_width=True)

if analyze_button:
    if not video_url:
        st.warning("⚠️ Please enter a YouTube URL first!")
    else:
        with st.spinner("AI is cutting the yap... This might take a moment."):
            try:
                response = agent.run(f"Analyse this video: {video_url}")
                
                st.success("Yap successfully cut!")
                st.subheader("📝 Analysis Report")
                
                with st.container(border=True):
                    st.markdown(response.content)
                    
            except Exception as e:
                st.error(f"Something went wrong during analysis: {e}")