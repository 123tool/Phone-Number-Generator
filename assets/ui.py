import os
import platform

# Color Palette
G = '\033[92m' # Green
Y = '\033[93m' # Yellow
R = '\033[91m' # Red
C = '\033[96m' # Cyan
W = '\033[0m'  # White
B = '\033[94m' # Blue

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def banner():
    print(f"""
{C}  _      ______          _____   _____ 
{C} | |    |  ____|   /\   |  __ \ / ____|
{B} | |    | |__     /  \  | |  | | (___  
{B} | |    |  __|   / /\ \ | |  | |\___ \ 
{W} | |____| |____ / ____ \| |__| |____) |
{W} |______|______/_/    \_\_____/|_____/ 
{Y}        GENERATE & VALIDATE PRO
{G}      Developed by Spy-E & 123tool{W}
    """)

def log(msg, status="info"):
    marks = {"info": f"{B}[*]", "success": f"{G}[+]", "error": f"{R}[-]", "warn": f"{Y}[!]"}
    print(f"{marks.get(status, '[*]')} {W}{msg}")
