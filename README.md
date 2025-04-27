# Instagram Cat Art Generator 🐾🎨🚀

JamCatAI presents 🎶 the ultimate **Instagram Cat Art Generator**!  
**Upload 🖼️ your cat pics ➡️ transform them magically into stunning art** ✨ using **AI power** 🧠🎨 — and **post automatically** to Instagram 📷🔥.

---

## 🚀 Features

- 🎨 **AI Art Generation** — Pixar, Cyberpunk, Watercolor, Sketch styles
- 📸 **Instagram Auto-Posting** — One-click share magic ✨
- 🛡️ **Secure Credential Handling** — Environment variables 🔐
- 🔥 **Optimized for Speed** — GPU-backed inference ⚡
- 🐾 **Cat-Lovers Focused** — Because cats rule the internet 😻

---

## 🛠️ Tech Stack

| Layer             | Tech 📚          | Notes 🧠 |
|:------------------|:-----------------|:---------|
| AI Art Generation | HuggingFace API + Stable Diffusion 2 🌀 | Mind-blowing images 🎨 |
| Backend           | Python 🐍         | Fast and lightweight ⚡ |
| Instagram Upload  | Instagrapi 🛜      | Automates IG posting 📲 |
| Deployment        | CLI + VS Code 💻  | Smooth dev workflow 🚀 |

---

## 🎯 How It Works

1. 📥 Upload your cat photo into `/input_images/`
2. 🧠 AI transforms it into magical artwork
3. ✨ Save the generated art in `/generated_art/`
4. 📲 Automatically post to Instagram with a cute caption!

---

## 📋 Installation

```bash
git clone https://github.com/JamCatAI/Instagram-Cat-Art-Generator.git
cd Instagram-Cat-Art-Generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Usage

1. Add your API Keys 🔐 inside a `.env` file:

```
HUGGINGFACE_API_TOKEN=your_huggingface_token_here
IG_USERNAME=your_instagram_username_here
IG_PASSWORD=your_instagram_password_here
```

2. Run the script 🚀:

```bash
python main.py
```

3. Watch the AI Magic Unfold ✨🎶

---

## 📈 Project Status

🚀 **v1.0 Launched** — Core features complete  
🎯 **v2.0 Roadmap**:
- ✅ Batch art generation
- ✅ Multi-style prompts
- 🚀 Scheduled IG posting
- 🎨 User Style Profiles
- 🐱 Meme Cat Mode (!!!)

---

## 🧠 Fun Fact & Trivia ✨

- **Instagram** name comes from combining **"Instant Camera"** 📷 and **"Telegram"** ✉️!
- The **first photo ever posted** on Instagram (by founder Kevin Systrom) was of **his dog and a taco stand** 🐕🌮.
- Kevin Systrom's estimated net worth 💰 = **$2 Billion+** 💵🔥

---

## 📜 License

[MIT License](LICENSE)

---

# 🌟 Jam, Create & Inspire! 🎶🎨🐾

**Follow JamCatAI** 👉  
- [Instagram](https://instagram.com/JamCatCTO) 📷  
- [Website](https://jamcat-ai.vercel.app/) 🌐  

---

# 🎨 Repo Visual Summary

```
Instagram-Cat-Art-Generator/
├── input_images/           # Upload cat pics here
├── generated_art/          # AI-generated artworks
├── generate_art.py         # AI generation logic
├── post_to_instagram.py    # IG upload automation
├── main.py                 # Main execution script
├── .env                    # API keys (ignored by git)
└── README.md               # You're reading it! 😎
```
