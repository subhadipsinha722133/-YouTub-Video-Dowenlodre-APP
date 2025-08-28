# YouTube Video Downloader App

A simple YouTube Video Downloader web app built with [Streamlit](https://streamlit.io/) and [yt-dlp](https://github.com/yt-dlp/yt-dlp). Download videos or audio from YouTube by just pasting the URL!

## Features

- Download YouTube videos in various formats (MP4, WebM, etc.)
- Simple, clean, and interactive Streamlit web interface
- No need to install browser extensions or visit ad-heavy websites

## Technologies Used

- **Python 3.11.9**
- **Streamlit** for UI
- **yt-dlp** for downloading
- **os** for file management

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/subhadipsinha722133/-YouTub-Video-Dowenlodre-APP.git
    cd YouTub-Video-Dowenlodre-APP
    ```
![Accuracy](https://github.com/subhadipsinha722133/-YouTub-Video-Dowenlodre-APP/blob/main/webpage_photo)
![Accuracy](https://github.com/subhadipsinha722133/-YouTub-Video-Dowenlodre-APP/blob/main/webpage_photo2)


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


## Project Structure

```
YouTub-Video-Dowenlodre-APP/
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── downloads/            # Downloaded files (created automatically)
```

**Note**: This app is for educational purposes. Please respect YouTube's Terms of Service and copyright laws.
