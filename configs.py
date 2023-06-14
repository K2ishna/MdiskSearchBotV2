import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "20592694"))
    API_HASH = os.getenv("API_HASH", "153183c69860f514b62f78d7c7e296f9")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6106262242:AAHa5slJrJ1nK19ynBF6fId-1eExkq6Rs34")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "movietadkka_search_bot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "BQB3gW6bpNakMcbkextOYNfVr8T1QbSNWGbItmjUWwx1iF5m7EM8MQN8Rf4wlz1cz94GKoxoUcTy7fxBK_1mU3p0boSxKsefiyP5DagoYyIF2PcuNOy9oG39gfR5zffQ39gIeZ5GFS6O_fgn1UUWquD2vjWV8DCRc-WkENafmgd_AiX9AyDRcSFsHdsv8YYzQh79QqvWDREgzuGGVcfr7u3LvVu6sOQf75k6rU7Xbb3-GN4ggtwCsftR-pikXLLydk9hJUpQ9Yt6d6HqaW1ykSJvMRE2m0Xnd90SjIv-b2zmEEJ3NY6V9pyhPW2Tpzb-FN1pc3JqkLVuS6GTTZkZhtD3ORah7gA")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001934627949") 
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Movietaddka_Search_Bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "957784558"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Vicky_Yaddav")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "MovietadkkaMovies")
#    GROUP_USERNAME = os.getenv("Movietadkka_Search")
    START_MSG = os.getenv("START_MSG", """**Hᴇʏ {}, 

I ᴀᴍ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Rᴏʙᴏᴛ 🔍.

I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Eᴠᴇʀʏ Mᴏᴠɪᴇ Iɴ Terabox Lɪɴᴋ 🔗

Jᴜsᴛ Tʏᴘᴇ ᴀ Mᴏᴠɪᴇ Nᴀᴍᴇ 🎬**""" ) https://telegra.ph/File382888372-06-14")
    HOME_TEXT = os.getenv("HOME_TEXT", """ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ.

ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅""" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001249072794")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://postbot:postbot@cluster0.ouwne8q.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001796458234"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "cynitebackup")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 180))
    MDISK_API = os.getenv("MDISK_API", "Qu7jX9V0Sn3q1JHdxjPp")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", """I ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! 

ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, 

i ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇxᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.

ᴅᴍ ꜰᴏʀ ᴀɴʏ Qᴜᴇʀʏ @Movietadkka 🤖""" )
    ABOUT_WATCH_TEXT = """
ʜᴇʏ ʙᴜᴅᴅʏ, 

ᴍᴅɪsᴋ - ᴀɢᴀʀ ᴀᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴍᴅɪsᴋ ʟɪɴᴋ sᴇ ᴍᴏᴠɪᴇ ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴍᴅɪsᴋ ᴡᴀʟᴇ ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ 


ᴛᴇʀᴀ ʙᴏx - ᴀɢᴀʀ ᴀᴘᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴛᴇʀᴀʙᴏx sᴇ ᴍᴏᴠɪᴇs ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄʜᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴛᴇʀᴀ ʙᴏx ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ

ʀᴇɢᴀʀᴅs - @CyniteBackup"""
    ABOUT_MDISK_TEXT = """
𝗠𝗱𝗶𝘀𝗸 𝗸𝗶 𝗹𝗶𝗻𝗸𝘀 𝗢𝗽𝗲𝗻 𝗔𝗶𝘀𝗲 𝗞𝗮𝗿𝗲👇🔥
वीडियो प्ले करने में कोई प्रोब्लम अ रही हो तो Mx Player App डाउनलोड करले😊👍

1) 𝘔𝘥𝘪𝘴𝘬 𝘬𝘪 𝘭𝘪𝘯𝘬 𝘱𝘦𝘳 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘦 𝘶𝘴𝘬𝘦 𝘣𝘢𝘢𝘥 1 𝘱𝘢𝘨𝘦 𝘬𝘩𝘶𝘭𝘦𝘨𝘢. 💜

2) 𝘞𝘢𝘩𝘢 𝘱𝘢𝘳 4 𝘉𝘶𝘵𝘵𝘰𝘯 𝘏𝘰𝘨𝘢 𝘴𝘗𝘭𝘢𝘺 𝘞𝘪𝘵 𝘔𝘹 𝘗𝘭𝘢𝘺𝘦𝘳𝘴𝘈𝘯𝘥 𝘚𝘱 𝘗𝘭𝘢𝘺𝘦𝘳.😉

3) 𝘈𝘱𝘬𝘰 𝘔𝘹 𝘗𝘭𝘢𝘺𝘦𝘳 𝘗𝘢𝘳 𝘓𝘪𝘬𝘩𝘰 𝘏𝘶𝘦 𝘒𝘰 𝘊𝘩𝘰𝘰𝘴𝘦 𝘒𝘢𝘳𝘯𝘢 𝘏𝘢𝘪😍

4) 𝘐𝘴𝘬𝘦 𝘉𝘢𝘢𝘥 𝘈𝘨𝘢𝘳 𝘈𝘱𝘬𝘰 𝘖𝘯𝘭𝘪𝘯𝘦 𝘋𝘦𝘬𝘩𝘯𝘢 𝘏𝘢𝘪 𝘛𝘰 𝘞𝘢𝘵𝘤𝘩 𝘖𝘯𝘭𝘪𝘯𝘦 𝘗𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘦 💻

5) 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘒𝘢𝘳𝘯𝘦 𝘒𝘦 𝘓𝘪𝘺𝘦 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘉𝘶𝘵𝘵𝘰𝘯 𝘗𝘢𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘦 ⬇

6)𝘕𝘢𝘩𝘪 𝘛𝘰 𝘈𝘱𝘱 𝘕𝘪𝘤𝘩𝘦 𝘋𝘪𝘺𝘦 𝘎𝘢𝘺𝘦 Watch Video 𝘗𝘢𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘬𝘦 𝘗𝘶𝘳𝘢 𝘚𝘵𝘦𝘱 𝘓𝘪𝘷𝘦 𝘗𝘩𝘰𝘵𝘰 𝘔𝘦 𝘋𝘦𝘬𝘩 𝘚𝘬𝘢𝘵𝘦 𝘏𝘢𝘪😇"""
    ABOUT_TERABOX_TEXT = """
𝗧𝗲𝗿𝗮𝗕𝗼𝘅 𝗸𝗶 𝗹𝗶𝗻𝗸𝘀 𝗢𝗽𝗲𝗻 𝗔𝗶𝘀𝗲 𝗞𝗮𝗿𝗲👇🔥
वीडियो प्ले करने में कोई प्रोब्लम अ रही हो तो इक बार रजिस्ट्रेशन कर ले फिर आप बिना एड के विडियो अच्छे से चला पाएंगे थैंक्यू 😊👍

https://terabox.com/s/1QZGvLaoU_VMaSCDT2NNvOQ

1) 𝘛𝘦𝘳𝘢𝘣𝘰𝘹 𝘬𝘪 𝘭𝘪𝘯𝘬 𝘱𝘦𝘳 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘦 𝘶𝘴𝘬𝘦 𝘣𝘢𝘢𝘥 𝘢𝘪𝘴𝘢 𝘱𝘢𝘨𝘦 𝘬𝘩𝘶𝘭𝘦𝘨𝘢.

2) 𝘜𝘱𝘱𝘢𝘳 𝘴𝘪𝘥𝘦 𝘭𝘰𝘨𝘪𝘯/𝘙𝘦𝘨𝘪𝘴𝘵𝘳𝘢𝘵𝘪𝘰𝘯 𝘭𝘪𝘬𝘩𝘢 𝘩𝘰𝘨𝘢 𝘶𝘴𝘱𝘦 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘰.😉

3) 𝘗𝘩𝘪𝘳 𝘳𝘦𝘨𝘪𝘴𝘵𝘳𝘢𝘵𝘪𝘰𝘯 𝘬𝘢𝘳𝘰 𝘢𝘶𝘳 𝘭𝘪𝘧𝘦 𝘵𝘪𝘮𝘦 𝘧𝘳𝘦𝘦 𝘷𝘪𝘥𝘦𝘰𝘴 𝘣𝘪𝘯𝘢 𝘈𝘥𝘴 𝘬𝘦 𝘥𝘦𝘬𝘩𝘰😍

4) 𝘕𝘢𝘩𝘪 𝘛𝘰 𝘈𝘱𝘱 𝘕𝘪𝘤𝘩𝘦 𝘋𝘪𝘺𝘦 𝘎𝘢𝘺𝘦  𝘗𝘢𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘬𝘦 𝘗𝘶𝘳𝘢 𝘚𝘵𝘦𝘱 𝘓𝘪𝘷𝘦 𝘗𝘩𝘰𝘵𝘰 𝘔𝘦 𝘋𝘦𝘬𝘩 𝘚𝘬𝘢𝘵𝘦 𝘏𝘢𝘪😇"""

    ABOUT_HELP_TEXT = """

🍓 RᴇQᴜɪʀᴇᴍᴇɴᴛ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!

🍓 Sᴛᴇᴘ 1 - Aᴘᴋᴏ ᴇᴋ ɢʀᴏᴜᴘ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴍᴇᴍʙᴇʀꜱ ʙʜɪ ʜᴏ, ᴀᴜʀ ᴇᴋ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴀᴘᴋᴇ ꜱᴀʀᴇ ᴘᴏꜱᴛ ʜᴏɴɢᴇ!

🍓 Sᴛᴇᴘ 2 - ʙᴏᴛ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴀᴜʀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋᴀ ᴀᴅᴍɪɴ ʙᴀɴᴀɴᴀ ʜᴏɢᴀ.

🍓 Sᴛᴇᴘ 3 - ɢʀᴏᴜᴘ ᴍᴇ "/License" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ!

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ. 

🍓 Sᴛᴇᴘ 4 - ɢʀᴏᴜᴘ ᴍᴇ "/database - ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ɪᴅ" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ.

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ʙʜɪ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ 

🍓 Sᴛᴇᴘ 5 - ᴀʙ ᴀᴘᴋᴏ ᴀᴘɴᴇ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴘᴏꜱᴛ ᴅᴀʟɴɪ ʜᴏɢɪ,

ᴊɪꜱꜱᴇ ᴋɪ ᴀɢᴀʀ ɢʀᴏᴜᴘ ᴍᴇ ᴋᴏɪ ᴜꜱᴇʀ ꜱᴇᴀʀᴄʜ ᴋᴀʀᴇ ᴛᴏ ʏᴇ ʙᴏᴛ ᴜɴ ᴜꜱᴇʀ ᴋᴇ Qᴜᴀʀʏ ᴋᴏ ꜱᴀᴍᴀᴊʜ ᴋᴇ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ꜱᴇ ᴘᴏꜱᴛ ᴜᴛʜᴀ ᴋᴇ ᴜɴʜᴇ ᴅᴇ ᴘᴀʏᴇ.

🍓 Nᴏᴛᴇ : Bᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴊᴏɪɴ ʜᴏɴᴇ ᴄʜᴀʜɪʏᴇ,

ᴀɢᴀʀ ʙᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴀ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ɴʜɪ ᴋᴀʀ ʀᴀʜᴇ ʜᴀɪɴ ᴛᴏ ᴜɴʜᴇ ᴘᴇʀꜱᴏɴᴀʟ ᴍꜱɢ ᴋᴀʀᴇɴ.

👉 @CyniteSupport

"""

