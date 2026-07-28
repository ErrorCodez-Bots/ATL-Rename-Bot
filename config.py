import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20293219")
API_HASH = os.environ.get("API_HASH", "4aef7d9e065d92f4a95736eaeb93d3ac")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "8605444314:AAHZxA7RHBZxBIzUPFlQFQiRYk16a77zldg") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "")

CHANNEL = os.environ.get("CHANNEL", "ATL_Univers") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","BYNF_TamilChat") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","ATL_Univers") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","HMF_Owner_1")
STRING = os.environ.get("STRING", "BQE1pmMAU2rFVha4YI8H1Wi9agAYXDeiBTgcq5UQ_tUeFqBXMf9elvU505O4hMoPf25MgQ9S08IiI-U0S7Y0uz6r0B7_yx6VIrtehllyrydYdnYrIDDc6u-EGDzRg1gpyPUy7Qg1M3a0A80Yn39nce_W3HsmwT5GcUr3uB2NUbIu4B3W67olI5j780OrFwjBh_aAWHf11uSMBkqeGdNbxMmJK3rG4cA8-TxPiMAJsYcI6S2yvq-5Y4jdqz7IUizFVvTI6K_SLWcqU91PxQc8oIAyNx7_GznAX8xmNgyvmMwPmbum5xBVlQB0U85223ChDgNRuFtypIgWVmDMlNNxLfLYg9gmDQAAAAGXWVHVAA")

DB_NAME = os.environ.get("DB_NAME","renameone")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://kakashibot8:zenitsuchan@cluster0.h0hl0gc.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/file/86539aa8e0ad585ec5c16-0f344a9092a61bbd6c.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6834180565').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003179370080"))
