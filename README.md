# LiveKit Assistant

First, create a virtual environment, update pip, and install the required packages:

```
$ python -m venv .venv
$ .venv\Scripts\activate
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```
### Required API Keys

Before running this project, you need to sign up and obtain API keys from the following services:

- **LiveKit**:  
  Sign up or log in at [https://livekit.io/](https://livekit.io/) and retrieve your LiveKit credentials.

- **Groq**:  
  Visit [https://console.groq.com/keys](https://console.groq.com/keys), sign up or log in, and generate your API key.

- **Gemini (Google AI Studio)**:  
  Go to [https://aistudio.google.com/app/](https://aistudio.google.com/app/), log in or sign up, and obtain a free API key.

> ⚠️ Note: These services offer free access with limited capabilities. Ensure you stay within their usage limits.

You need to set up the following environment variables, you can refer envexamples.txt and save it as ".env.local" :

```
LIVEKIT_URL=...
LIVEKIT_API_KEY=...
LIVEKIT_API_SECRET=...
GROQ_API_KEY=...
GOOGLE_API_KEY=...
```

Then, run the voice-assistant-arabic:

```
$ python voice-assistant-arabic.py download-files
$ python voice-assistant-arabic.py start
```

Finally, you can load the [hosted playground](https://agents-playground.livekit.io/) and connect it.
