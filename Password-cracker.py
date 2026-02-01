import time
import string
import sys
import random
import os
import webbrowser

# ألوان مميزة وفخمة
G = "\033[1;32m"
R = "\033[1;31m"
C = "\033[1;36m"
Y = "\033[1;33m"
M = "\033[1;35m"
W = "\033[1;37m"
RESET = "\033[0m"

os.system("clear")

# بانر الأداة والاسم بحجم كبير وأنيق جداً
banner = f"""
{M}
██████╗ ██╗      ██████╗  ██████╗ ███████╗██╗  ██╗
██╔══██╗██║     ██╔═══██╗██╔════╝ ██╔════╝╚██╗██╔╝
██████╔╝██║     ██║   ██║██║  ███╗█████╗   ╚███╔╝ 
██╔══██╗██║     ██║   ██║██║   ██║██╔══╝   ██╔██╗ 
██████╔╝███████╗╚██████╔╝╚██████╔╝███████╗██╔╝ ██╗
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝

       THE LEGENDARY INSTA-HACK TOOL
                 by 3lloush

        Instagram: mr_abu_3lish.2
{RESET}
"""
print(banner)
time.sleep(3)

# ** حذف السطر الذي يطلب username الخاص **

# مدخلات المستخدم (الحساب المستهدف)
user = input(W + "Enter target Instagram username: " + RESET)

# فتح رابط الانستا مباشر على الحساب المستهدف
print(C + f"Launching encrypted connection to Instagram account: {user} ..." + RESET)
time.sleep(2)
webbrowser.open(f"https://instagram.com/{user}")

length = int(input(W + "Enter desired password length to simulate: " + RESET))

time.sleep(2)

# Progress بار متحرك فخم و عشوائي
print(C + "Calibrating Attack Power..." + RESET)
progress = 0
while progress < 100:
    progress += random.randint(3, 7)
    if progress > 100:
        progress = 100
    sys.stdout.write(f"\r[{('=' * (progress // 2)).ljust(50)}] {progress}%")
    sys.stdout.flush()
    time.sleep(random.uniform(0.15, 0.3))

print("\n")

# عملية استخراج بيانات وهمية بشكل متقدم
print(G + "Extracting encrypted password hashes from remote servers...\n" + RESET)
for _ in range(random.randint(20, 35)):
    fake_hash = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(48))
    print(f"HASH: {fake_hash}")
    time.sleep(random.uniform(0.05, 0.1))

print("\n")

# مجموعة الأحرف و الرموز
chars = (
    string.ascii_uppercase +
    string.ascii_lowercase +
    string.digits +
    "!@#$%^&*()-_=+"
)

# باسورد وهمي عشوائي وطويل
fake_pass = "".join(random.choice(chars) for _ in range(length))
guess = ""

print(C + "\nLaunching advanced brute-force attack...\n" + RESET)

def border():
    print("+----------------------------+----------------------------+----------------------------+")

border()

# تخمين بطيء وحرف بحرف مع مؤثرات عشوائية فخمة
for target in fake_pass:
    for c in chars:
        line = (
            f"| {G}{user:<26}{RESET} | "
            f"{G}{(guess + c):<26}{RESET} | "
            f"{R}Status: Searching... {random.choice(['|', '/', '-', '\\'])}{RESET}"
        )
        sys.stdout.write("\r" + line)
        sys.stdout.flush()

        time.sleep(random.uniform(0.6, 1.2))

        if c == target:
            guess += c
            print()
            border()
            break

# رسالة نهاية سينمائية مع شوية تأثيرات نصية
print(G + f"\n[+] PASSWORD CRACKED SUCCESSFULLY: {guess}\n" + RESET)
time.sleep(1.5)
print(G + "✅ Access Granted to target account." + RESET)
time.sleep(1.5)
print(G + "📥 Syncing direct messages and media..." + RESET)
time.sleep(2)
print(G + "🔒 Closing secure session..." + RESET)

print(M + """
═══════════════════════════════════════════════════════
              Powered by 3lloush Cyber Elite Lab
                 Instagram: mr_abu_3lish.2
═══════════════════════════════════════════════════════
""" + RESET)
