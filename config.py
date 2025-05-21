import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27079591")) #optional
API_HASH = getenv("API_HASH", "c81ae4c3dc026ea4bf49842a8ce4a5f9") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6346273488").split()))
OWNER_ID = int(getenv("OWNER_ID", "7078181502"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://files.catbox.moe/ppms0p.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://t.me/Bots_Are_Alive")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQFOSEgAlMHFqRsFC5Jjr_mn0dYy1Ds_0TamfWXHJgrdtWKjT3vMFHIkVmu50YcxeXOsiVD_u4oXvEWwhqOmW0d9AMuDiKRmxOaV9Yi0pCkj9xYArqCf7WT6eByHGrupVm5Gds1Qk3ftnmk7gViRJe_qrtq_zTWKXlJrDy3e1kvu2ssc6mzjCrwDFdb0agk_0nY4n44gZR6w3Kk9kPxEZT4zvyhKIIfH2RfLPf0R4eh9HQ0BARzgpD_InmN-yHTld4h9idfMzyj7Qm8amwj-fjCk_eeMm0wx9z37AUHQRvzRu5pDPksZi1LzNcjwuL8N5Kc57PJ707TXVVFNhRHcppA6kAG4WwAAAAHSq1hVAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
