# 📣 Tilmoch — reklama va o'sish rejasi

## 1. Kimlar uchun (maqsadli auditoriya)

| Auditoriya | Nima kerak | Asosiy funksiya |
|---|---|---|
| Xitoydan tovar olib keluvchi tadbirkorlar | Sotuvchi bilan gaplashish, narx varag'ini tushunish | 💬 Suhbat rejimi, 📷 Rasm, 📖 Iboralar |
| Kargo va logistika kompaniyalari | Hujjat, invoys, yuk ma'lumotlari | 📄 Hujjat, 📚 Lug'at, 🏢 Biznes tarif |
| Guanchjou, Yiwu, Urumchiga boradiganlar | Taksi, mehmonxona, bozor | ✈️ Sayohat va 🏬 Bozor iboralari, 🎙 Ovoz |
| Til o'rganuvchilar va talabalar | So'z yodlash, talaffuz | 🧠 So'z testi, 🔊 Tinglash, pinyin |
| Marketplace sotuvchilari (Uzum, Wildberries) | Mahsulot tavsifini tarjima qilish | ✍️ Matn, 📄 Hujjat |

## 2. Birinchi hafta — sinov (20–30 kishi)

- [ ] Botni serverga qo'ying, `ADMIN_IDS` ga o'zingizni yozing.
- [ ] 20–30 ta tanish tadbirkorga yuboring: "Sinab ko'ring, fikringizni ayting".
- [ ] Har kuni ertalab keladigan 🗓 hisobotni kuzating: qaysi til yo'nalishi va funksiya ko'p ishlatilmoqda.
- [ ] 🚨 Xato xabarlari kelsa — tuzating.
- [ ] Har bir sinovchiga `/premium_ber ID 30` bilan 1 oy Premium sovg'a qiling — ular eng yaxshi targ'ibotchi.

## 3. Qayerda reklama qilish

- Xitoy bilan savdo qiluvchilarning Telegram guruhlari ("Xitoydan tovar", "Kargo Toshkent", "Optom Xitoy").
- Kargo kompaniyalarining kanallari — hamkorlik: ular mijozlariga botni tavsiya qiladi, siz ularga bepul Biznes tarif berasiz.
- Xitoy tili o'quv markazlari va universitetlar (Toshkent Davlat Sharqshunoslik universiteti) talabalari guruhlari.
- Instagram Reels va TikTok — qisqa videolar (pastdagi ssenariylar).
- Uzum/Wildberries sotuvchilari jamoalari.

## 4. Tayyor post matnlari

**Guruhlar uchun (qisqa):**
> 🇨🇳 Xitoylik sotuvchi bilan tilni bilmasdan gaplashing!
> Ovozli xabar yuborasiz — bot xitoychaga tarjima qilib, ovoz bilan qaytaradi.
> 📷 Narx varag'ini rasmga oling — darhol o'zbekchada.
> 📄 Invoys va shartnomalarni Word/PDF holida tarjima qiladi.
> Bepul: @TilmochPlusBot

**Kanal uchun (batafsil):**
> 🌏 **Tilmoch** — Xitoy · Ingliz · Rus tarjimon
>
> ✍️ Matn — darhol tarjima
> 🎙 Ovoz — gapiring, tarjimani eshiting (o'zbekcha ovoz ham bor)
> 📷 Rasm — narx varag'i, quti, skrinshot
> 📄 Hujjat — Word va PDF
> 💬 Suhbat rejimi — xitoylik hamkor bilan jonli muloqot
> 📖 64 ta tayyor biznes ibora: narx, buyurtma, yetkazish, to'lov
>
> 👉 @TilmochPlusBot

## 5. Qisqa video ssenariylari (15–30 soniya)

1. **"Xitoylik sotuvchi bilan bot orqali gaplashdim"** — telefon ekrani yozib olinadi: o'zbekcha ovozli xabar → bot xitoycha ovoz chiqaradi → sotuvchining xitoycha javobi → o'zbekcha tarjima. Matn: "Xitoy tilini bilmayman, lekin savdolashdim 😄".
2. **"Narx varag'ini 3 soniyada tushunish"** — xitoycha narx varag'ini rasmga olish → bot o'zbekchada ko'rsatadi.
3. **"Yiwu bozorida kerak bo'ladigan 5 ta ibora"** — 📖 Iboralar bo'limidan ovoz bilan.
4. **"Shartnomani 1 daqiqada tarjima qildim"** — Word fayl yuboriladi → tarjima qilingan fayl qaytadi.

Har bir video oxirida: "Bot havolasi — profilda / izohda".

## 6. Do'st taklif qilish tizimi (botda tayyor)

- Har bir foydalanuvchida shaxsiy havola bor: 🎁 **Do'st taklif** tugmasi.
- Har 3 ta do'st uchun — 7 kun Premium (`.env`: `REFERRAL_TARGET`, `REFERRAL_BONUS_DAYS`).
- Limit tugaganda bot avtomatik ravishda "Do'st taklif qilish" tugmasini ko'rsatadi.

## 7. Majburiy obuna (ixtiyoriy)

Kanalingiz bo'lsa: `.env` → `REQUIRED_CHANNEL=@kanalingiz`, botni kanalga **admin** qiling.
Maslahat: buni foydalanuvchilar 500–1000 taga yetgandan keyin yoqing — boshida bu odamlarni qochirishi mumkin.

## 8. Daromad bosqichlari

| Bosqich | Foydalanuvchilar | Harakat |
|---|---|---|
| 1 | 0–500 | Hammasi bepul, fikr yig'ish, xatolarni tuzatish |
| 2 | 500–1000 | Premium yoqiladi (Stars), majburiy obuna, do'st taklifi faol |
| 3 | 1000+ | Click/Payme ulanadi, Biznes tarif kargo/import kompaniyalariga to'g'ridan-to'g'ri sotiladi |
| 4 | 5000+ | Kanallarga reklama joylash, hamkorlik (kargo, o'quv markazlari) |

## 9. Kuzatiladigan ko'rsatkichlar (`/stats` va kunlik hisobot)

- Yangi foydalanuvchilar / kun
- 7 kunlik faol foydalanuvchilar (qaytib kelish)
- Eng ko'p til yo'nalishlari — shu yo'nalish sifatini birinchi navbatda yaxshilang
- Ovoz / rasm / hujjat ulushi
- Botni bloklaganlar soni (ko'paysa — xabarlar ko'p yoki bot sekin)
- To'lovlar soni va summasi

## 10. Brend qoidalari

- **Nom:** Tilmoch (to'liq: "Tilmoch — Xitoy · Ingliz · Rus tarjimon").
- **Pozitsiya:** "tarjimon" emas — **"xitoylik hamkor bilan gaplashish vositasi"**. Reklamada doim shu foydani ayting.
- **Rang:** firuza → ko'k gradient (#10AAA8 → #043AAA). Logo, banner, kanal, video muqovalarida bir xil.
- **Ohang:** samimiy, qisqa, foydaga yo'naltirilgan. Har bir xabarda bitta aniq harakat ("Gapiring", "Rasm yuboring").
- **Tayyor materiallar:** `assets/logo.png`, `assets/banner.jpg`, `assets/description_640x360.jpg`.

## 11. Yangi foydalanuvchini ushlab qolish (botda avtomatik)

| Vaqt | Nima bo'ladi |
|---|---|
| 0 soniya | Banner + "Qaysi til bilan ishlaysiz?" |
| 10 soniya | Namunaviy tarjima "Bu qancha turadi?" → 这个多少钱？ + ovoz |
| 15 soniya | 🎁 3 kun Premium sovg'a, qisqa menyu |
| 1-kun | 💡 Ovozli tarjima maslahati |
| 2-kun | 💡 Rasm va hujjat tarjimasi maslahati |
| 3-kun | 💡 Biznes iboralar + Premium tugashi eslatmasi |
| 3+ kun kirmasa | Haftaning 5 ta foydali iborasi (reklama emas) |
