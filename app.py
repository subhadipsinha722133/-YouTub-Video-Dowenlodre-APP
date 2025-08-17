import os
import yt_dlp
import streamlit as st

# Streamlit app title
st.title("🤩 YouTube Video Downloader WEB_APP✨")

# Input field for YouTube URL
url = st.text_input("Enter YouTube Video URL :")

# Create a folder named "video" if it doesn't exist
os.makedirs("video", exist_ok=True)

if st.button("Download Video"):
    if url.strip():
        try:
            st.write("📥  (❁´◡`❁)  Downloading video...")
            
            # yt-dlp options
            ydl_opts = {
                'format': 'best',  # Best quality
                'outtmpl': os.path.join("video", "%(title)s.%(ext)s"),  # Save to 'video' folder
            }

            # Download video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            st.success("✅ Download completed! Video saved in the 'video' folder.")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠ Please enter a valid YouTube URL.")
else:
    st.warning(" This web app is made by SUBHADIP 😎 ")