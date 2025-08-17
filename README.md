# YouTube Video Downloader App

A simple YouTube Video Downloader web app built with [Streamlit](https://streamlit.io/) and [yt-dlp](https://github.com/yt-dlp/yt-dlp). Download videos or audio from YouTube by just pasting the URL!

## Features

- Download YouTube videos in various formats (MP4, WebM, etc.)
- Download only audio (MP3/M4A/Opus)
- Simple, clean, and interactive Streamlit web interface
- No need to install browser extensions or visit ad-heavy websites

## Technologies Used

- **Python 3.7+**
- **Streamlit** for UI
- **yt-dlp** for downloading
- **os** for file management

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/YouTub-Video-Dowenlodre-APP.git
    cd YouTub-Video-Dowenlodre-APP
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

    Or install manually:
    ```bash
    pip install streamlit yt-dlp
    ```

## Usage

1. **Run the Streamlit app**
    ```bash
    streamlit run app.py
    ```

2. **Open your browser** (Streamlit will show the link, usually http://localhost:8501)
3. **Paste YouTube video URL**
4. **Select format (video/audio)**
5. **Download!**

## Example

![Screenshot](screenshot.png)

## Project Structure

```
YouTub-Video-Dowenlodre-APP/
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── downloads/            # Downloaded files (created automatically)
```

## Sample `app.py`

```python
import streamlit as st
import yt_dlp
import os

st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube Video URL")
download_type = st.radio("Download", ("Video", "Audio"))

if st.button("Download"):
    if url:
        if not os.path.exists("downloads"):
            os.makedirs("downloads")
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best' if download_type == "Video" else 'bestaudio',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            st.success(f"Download complete: {info_dict['title']}")
    else:
        st.error("Please enter a valid URL.")
```

## License

[MIT](LICENSE)

---

**Note**: This app is for educational purposes. Please respect YouTube's Terms of Service and copyright laws.
