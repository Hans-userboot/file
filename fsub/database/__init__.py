from fsub.database.but import *
from fsub.database.data import *
from fsub.database.func import *

# Contoh pengaplikasian di handler pesan/perintah
@app.on_message(filters.private & filters.incoming)
async def handle_fsub(client, message):
    user_id = message.from_user.id
    
    # Biasanya fungsi dari modul fsub mengembalikan True jika sudah join, dan False jika belum
    # Nama fungsinya bisa bervariasi (misal: is_subscribed, check_user, dll.)
    if not await is_subscribed(client, user_id): 
        # Jika belum join, kirim tombol yang diambil dari fsub.database.but
        await message.reply_text(
            "Kamu harus join channel dulu!",
            reply_markup=fsub_buttons() # Ini hanya contoh nama fungsi tombolnya
        )
        return # Menghentikan proses agar perintah bot tidak jalan
        
    # ---- Batas kode jika user sudah join, taruh kode utama botmu di bawah ini ----
