from tinydb import TinyDB, Query

db = TinyDB('./join_data.json')
User = Query()
Chat = Query()
user_data = db.table('cast')
fsub_db = db.table('fsub') # Diubah agar tidak bentrok dengan nama fungsi/modul
info_db = db.table('info')
caption_db = db.table('caption') # Diubah agar tidak bentrok dengan argumen teks caption


# ================= BROADCAST =================
async def present_user(user_id: int):
    found = user_data.contains(User._id == user_id)
    return found

async def add_user(user_id: int):
    user_data.insert({'_id': user_id})
    return

async def full_userbase():
    user_ids = [doc['_id'] for doc in user_data.all()]
    return user_ids

async def del_user(user_id: int):
    user_data.remove(User._id == user_id)
    return
    
# ================= FORCE SUBSCRIBE =================
async def cek_fsub(chat_id: int):
    found = fsub_db.contains(Chat._id == chat_id)
    return found

async def add_fsub(chat_id: int):
    fsub_db.insert({'_id': chat_id})
    return

async def full_fsub():
    # Mengambil semua ID channel wajib dari database TinyDB
    user_ids = [doc['_id'] for doc in fsub_db.all()]
    return user_ids

async def del_fsub(chat_id: int):
    fsub_db.remove(Chat._id == chat_id)
    return
    

# ================= SETTING INFO =================
async def add_setting(user_id, disable, anti):
    user = info_db.get(User._id == user_id)
    if user:
        info_db.update(
            {
                "disable": disable,
                "anti": anti,
            },
            User._id == user_id
        )
    else:
        info_db.insert(
            {
                "_id": user_id,
                "disable": disable,
                "anti": anti,
            }
        )

async def cek_setting(user_id):
    r = info_db.search(User._id == user_id)
    if r:
        return r
    else:
        return False
        
async def disable_info(user_id):
    r = info_db.get(User._id == user_id)
    if not r:
        return False
    return r["disable"]
    
async def anti_info(user_id):
    r = info_db.get(User._id == user_id)
    if not r:
        return True
    return r["anti"]

# ================= CUSTOM CAPTION =================
async def add_caption(user_id, text_caption): # Diubah menjadi text_caption agar tidak bentrok
    user = caption_db.get(User._id == user_id)
    if user:
        caption_db.update(
            {
                "caption": text_caption,
            },
            User._id == user_id
        )
    else:
        caption_db.insert(
            {
                "_id": user_id,
                "caption": text_caption,
            }
        )

async def caption_info(user_id):
    r = caption_db.get(User._id == user_id)
    if not r:
        return None
    return r["caption"]

async def full_fsub():
    user_ids = [doc['_id'] for doc in fsub.all()]
    return user_ids

async def del_fsub(chat_id: int):
    fsub.remove(Chat._id == chat_id)
    return
    

#data
async def add_setting(user_id, disable, anti):
    user = info.get(User._id == user_id)
    if user:
        info.update(
            {
                "disable": disable,
                "anti": anti,
            },
            User._id == user_id
        )
    else:
        info.insert(
            {
                "_id": user_id,
                "disable": disable,
                "anti": anti,
            }
        )

async def cek_setting(user_id):
    r = info.search(User._id == user_id)
    if r:
        return r
    else:
        return False
        
async def disable_info(user_id):
    r = info.get(User._id == user_id)
    if not r:
        return False
    return r["disable"]
    
async def anti_info(user_id):
    r = info.get(User._id == user_id)
    if not r:
        return True
    return r["anti"]

async def add_caption(user_id, caption):
    user = caption.get(User._id == user_id)
    if user:
        caption.update(
            {
                "caption": caption,
            },
            User._id == user_id
        )
    else:
        caption.insert(
            {
                "_id": user_id,
                "caption": caption,
            }
        )

async def caption_info(user_id):
    r = caption.get(User._id == user_id)
    if not r:
        return None
    return r["caption"]
