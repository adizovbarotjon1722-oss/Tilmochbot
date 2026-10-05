# 🌏 Tilmoch — Xitoy · Ingliz · Rus tarjimon

> Xitoylik, inglizzabon va rusiyzabon hamkor bilan tilni bilmasdan gaplashish vositasi.

/start bosilgandan keyin bot har bir yuborilgan **matn, ovoz, rasm va hujjatni** avtomatik tarjima qilib boradi.

## Imkoniyatlar

| Bo'lim | Nima qiladi |
|---|---|
| ✍️ Matn | Tilni o'zi aniqlaydi, boshqa tillarga tarjima qiladi. O'zbek kirill → lotin. |
| 🎙 Ovoz | Ovozli xabar, audio, dumaloq video, video → matn + tarjima + **ovozli javob** (o'zbekcha ham) |
| 📷 Rasm | Narx varag'i, quti, skrinshot, hujjat rasmi → matnni o'qib tarjima qiladi |
| 📄 Hujjat | Word (.docx) formatini saqlab tarjima qiladi, PDF → tarjima qilingan Word, TXT |
| 💬 Suhbat rejimi | 🇺🇿⇄🇨🇳, 🇺🇿⇄🇬🇧, 🇬🇧⇄🇨🇳, 🇺🇿⇄🇷🇺, 🇷🇺⇄🇨🇳 — hamkor bilan jonli muloqot |
| 📖 Biznes iboralar | 8 bo'lim, 64 ta tayyor ibora (narx, buyurtma, yetkazish, to'lov, sifat, sayohat, bozor) — pinyin va ovoz bilan |
| 📚 Shaxsiy lug'at | Kompaniya/mahsulot nomlari doim bir xil tarjima qilinadi yoki umuman tarjima qilinmaydi |
| 🧠 So'z testi | Saqlangan so'zlar va iboralar bo'yicha test, har kuni ertalab avtomatik |
| 💎 Premium / 🏢 Biznes | Kunlik limitlar, Telegram Stars va Click/Payme orqali to'lov |
| 🎁 Do'st taklif | Har 3 ta do'st uchun 7 kun Premium bepul |
| 📢 Majburiy obuna | Ixtiyoriy: botdan foydalanish uchun kanalingizga obuna |
| 🔒 Maxfiy rejim | Shartnoma kabi matnlar tarixda saqlanmaydi (1 soatdan keyin o'chadi) |
| 💾 Zaxira nusxa | Har kuni baza nusxasi olinadi va adminga yuboriladi |
| 🚨 Xato xabari | Bot xato bersa, adminga darhol batafsil xabar keladi |
| 📊 Statistika | `/stats` va har kuni soat 9:00 da avtomatik hisobot |
| 🌐 Inline | Istalgan chatda `@botingiz matn` |
| 👋 30 soniyalik tanishuv | Yangi foydalanuvchi: banner → "Qaysi til?" → rejim avtomatik sozlanadi → namunaviy tarjima va ovoz |
| 🎁 Xush kelibsiz sovg'asi | Yangi foydalanuvchiga 3 kun Premium |
| 💡 Maslahatlar | Birinchi 3 kun — kuniga bitta maslahat (ovoz → rasm → iboralar) |
| 🔁 Qaytarish xabari | 3 kun kirmaganlarga haftaning 5 ta foydali iborasi |
| 📤 Ulashish | Har bir tarjima ostida — do'stga yuborish (bot havolasi bilan) |
| 👥 Ishonch belgisi | Foydalanuvchilar 100 dan oshsa, /start da "1 200+ foydalanuvchi" ko'rinadi |
| 👥 Guruhlar | `/tr` — matn, ovoz yoki rasmga javoban |

## Tezkor ishga tushirish (5 qadam)

1. **Bot yarating:** [@BotFather](https://t.me/BotFather) → `/newbot` → token oling.
2. **BotFather sozlamalari:**
   - Username tavsiyalari (yaratishda): `@TilmochPlusBot`, `@Tilmoch24Bot`, `@JonliTilmochBot`, `@TilmochXitoyBot`
   - `/setuserpic` → `assets/logo.png` faylini yuboring (tayyor logo)
   - `/mybots` → bot → Edit Bot → **Edit Description Picture** → `assets/description_640x360.jpg`
   - Bot nomi ("Tilmoch — Xitoy · Ingliz · Rus tarjimon"), tavsif va buyruqlarni bot ishga tushganda **o'zi o'rnatadi**.
   - `/setinline` → "Tarjima uchun matn yozing" (inline rejim)
   - `/setprivacy` → Disable (guruhlarda `/tr` ishlashi uchun)
3. **Sozlang:** `cp .env.example .env` → `BOT_TOKEN` va `ADMIN_IDS` ni yozing.
4. **Ishga tushiring:** `docker compose up -d --build`
5. **Tekshiring:** botga `/start` yozing, keyin `/stats` (admin sifatida).

## Serverga joylash (24/7)

### Tavsiya: VPS + Docker (oyiga ~4–6 $)
Hetzner, DigitalOcean, Timeweb yoki mahalliy hosting — Ubuntu 22.04/24.04.
```bash
# serverda
sudo apt update && sudo apt install -y docker.io docker-compose-v2 git
git clone <sizning-repo> tilmoch_bot && cd tilmoch_bot   # yoki zipni yuklab oching
cp .env.example .env && nano .env                             # token va kalitlar
sudo docker compose up -d --build
sudo docker compose logs -f                                   # loglar
```
Yangilash: yangi fayllarni yuklang → `sudo docker compose up -d --build`.

### Docker'siz (systemd)
```bash
sudo apt install -y python3-venv ffmpeg tesseract-ocr tesseract-ocr-uzb tesseract-ocr-chi-sim tesseract-ocr-rus
sudo cp -r . /opt/tilmoch_bot && cd /opt/tilmoch_bot
python3 -m venv venv && venv/bin/pip install -r requirements.txt
sudo cp tilmoch-bot.service /etc/systemd/system/
sudo systemctl enable --now tilmoch-bot
journalctl -u tilmoch-bot -f
```

### Kompyuterda sinash (Windows/Mac)
Python 3.11+, [ffmpeg](https://ffmpeg.org/download.html) va [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) o'rnating, so'ng:
```bash
python -m venv venv && venv\Scripts\activate      # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python bot.py
```

## Kalitlar (sifatni oshirish)

| Kalit | Qayerdan | Nima beradi | Narx |
|---|---|---|---|
| `STT_API_KEY` | [Groq](https://console.groq.com/keys) | Whisper — ovozni juda aniq tanish, shovqinda ham | Bepul tarif |
| `LLM_API_KEY` (OpenAI) | [platform.openai.com](https://platform.openai.com/api-keys) | AI tarjima + rasmni AI bilan o'qish | gpt-4o-mini — juda arzon |
| `LLM_API_KEY` (DeepSeek) | [platform.deepseek.com](https://platform.deepseek.com) | AI tarjima (rasm yo'q, `LLM_VISION=0`) | Eng arzon |
| `PAYMENT_PROVIDER_TOKEN` | @BotFather → Payments → Click / Payme | So'mda to'lov qabul qilish | Komissiya |

Kalit bo'lmasa ham bot to'liq ishlaydi: tarjima — Google (zaxira: MyMemory), ovoz — Google, rasm — Tesseract, to'lov — Telegram Stars.
`LLM_PREMIUM_ONLY=1` bo'lsa, AI tarjima faqat pullik foydalanuvchilar uchun ishlaydi — xarajat nazorat ostida.

## Admin buyruqlari

| Buyruq | Vazifasi |
|---|---|
| `/stats` | Foydalanuvchilar, faollik, tarjimalar, to'lovlar, eng ko'p til yo'nalishlari |
| `/xabar` | Biror xabarga javoban — hamma foydalanuvchilarga tarqatish |
| `/premium_ber 123456789 30 [business]` | Foydalanuvchiga qo'lda Premium berish |
| `/backup` | Bazaning zaxira nusxasini darhol olish |

## Loyiha tuzilishi

```
bot.py                  — ishga tushirish, profil, middleware, rejalashtiruvchi
app/config.py           — barcha sozlamalar (.env)
app/translator.py       — tarjima: AI → Google → MyMemory, til aniqlash, lug'at, pinyin, kirill→lotin
app/speech.py           — ovoz: Whisper/Google tanish, Edge neyron ovozlar
app/ocr.py              — rasm o'qish: AI vision → Tesseract
app/documents.py        — DOCX/PDF/TXT tarjimasi
app/phrases.py          — biznes iboralar to'plami
app/limits.py           — tariflar va kunlik limitlar
app/core.py             — tarjima kartasi dizayni
app/keyboards.py        — barcha tugmalar
app/db.py               — SQLite: foydalanuvchilar, tarix, lug'at, limitlar, to'lovlar
app/middlewares.py      — ro'yxatga olish, majburiy obuna, xatolarni adminga yuborish
app/scheduler.py        — kunlik test, zaxira nusxa, hisobot, Premium eslatmasi, maxfiy yozuvlarni tozalash
app/handlers/           — common, translate, extras, premium, admin (+inline)
app/handlers/menu.py    — qisqa menyu ("➕ Yana")
assets/logo.png         — bot logosi (profil rasmi)
assets/banner.jpg       — /start banneri
assets/description_640x360.jpg — Start'dan oldingi tavsif rasmi
MARKETING.md            — reklama va o'sish rejasi
ROADMAP.md              — bajarilgan ishlar va keyingi qadamlar
```
