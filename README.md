# LiveKit Assistant

First, create a virtual environment, update pip, and install the required packages:

```
$ python -m venv .venv
$ .venv\Scripts\activate
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```

You need to set up the following environment variables, you can refer envexamples.txt and save it as ".env.local" :
Login/Sign up in "https://livekit.io/" and fetch your credentials
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
