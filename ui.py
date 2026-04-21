import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="NoYap | YouTube Video Summarizer",
    page_icon="🤫",
    layout="centered",
)

st.markdown("""
<style>
.highlight {
    font-weight: 800;
    background: linear-gradient(90deg, #FF4B4B, #FF904F);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

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
    '<span style="font-size:0.9em; color:#9CA3AF;">Built using <span class="highlight">Agno</span> & <span class="highlight">Groq</span> ⚡</span>',
    unsafe_allow_html=True
)

st.divider()

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

st.markdown("### 🔗 Drop the link, cut the yap:")
video_url = st.text_input(
    "YouTube URL", 
    label_visibility="collapsed",
    placeholder="e.g., https://www.youtube.com/watch?v=..."
)

analyze_button = st.button("Cut The Yap", type="primary", use_container_width=True)

if analyze_button:
    if not video_url:
        st.warning("⚠️ Please enter a YouTube URL first!")
    else:
        with st.spinner("🤫 AI is cutting the yap... This might take a moment."):
            try:
                response = agent.run(f"Analyse this video: {video_url}")
                
                st.success("Yap successfully cut!")
                st.subheader("📝 The Bottom Line")
                
                with st.container(border=True):
                    st.markdown(response.content)
                    
            except Exception as e:
                st.error(f"Something went wrong: {e}")