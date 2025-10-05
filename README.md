# Telangana DSS Data Chatbot

This Streamlit app provides a chatbot assistant for the Telangana SC/ST Decision Support System (DSS) Hub.
It can answer questions related to the datasets, indicators, and analytics published on your ArcGIS Hub site.

## 🚀 How to Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io and log in with GitHub.
2. Create a new repository and upload:
   - `streamlit_app.py`
   - `requirements.txt`
3. Click **New App** → Select your repo.
4. Set the main file path as `streamlit_app.py`.
5. Add your OpenAI API key under **App Settings → Secrets** as:
   ```ini
   OPENAI_API_KEY = "sk-..."
   ```
6. Click **Deploy**.

Once deployed, you’ll get a URL like:
`https://telangana-dss-chatbot.streamlit.app`

## 🧩 Embedding in ArcGIS Hub

Use this HTML snippet in your Hub **Embed Code Block**:

```html
<div id="chatbot-container" style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
  <button id="chatbot-toggle" style="background-color: #0c3c60; color: white; border: none; padding: 12px 16px; border-radius: 30px; font-size: 14px; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.3);">
    💬 DSS Data Chat
  </button>
  <div id="chatbot-box" style="display: none; width: 340px; height: 480px; background: white; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); margin-top: 10px; overflow: hidden;">
    <iframe src="https://telangana-dss-chatbot.streamlit.app" style="width: 100%; height: 100%; border: none;"></iframe>
  </div>
</div>

<script>
  const chatbotToggle = document.getElementById('chatbot-toggle');
  const chatbotBox = document.getElementById('chatbot-box');
  chatbotToggle.onclick = () => {
    chatbotBox.style.display = chatbotBox.style.display === 'none' ? 'block' : 'none';
  };
</script>
```
