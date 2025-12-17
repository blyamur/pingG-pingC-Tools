from pythonping import ping
import datetime
import time
import os
import colorama
from colorama import Fore, Style
import pyautogui
import socket
import threading
__author__ = "Mons (https://blog.mons.ws)"
colorama.init()
sleep_interval = 30

# === Вспомогательная функция с таймаутом для разрешения DNS ===
def resolve_hostname(hostname, timeout=3):
    ip = [None]
    def _resolve():
        try:
            ip[0] = socket.gethostbyname(hostname)
        except Exception:
            ip[0] = None
    thread = threading.Thread(target=_resolve)
    thread.daemon = True
    thread.start()
    thread.join(timeout=timeout)
    return ip[0]

# === Загрузка настроек ===
with open('settings.xml', encoding='utf-8') as file:
    lines = file.read().splitlines()
source = {}
for line in lines:
    if ':' in line:
        key, value = line.split(':', 1)
        source[key.strip()] = value.strip()

def stat_ip_logs(ping_val, ip_source, name_source):
    if ping_val is None:
        show_res = Fore.RED + "UNREACHABLE" + Style.RESET_ALL + '\a'
        with open("error_logs.txt", 'a', encoding='utf-8') as f:
            f.write(f"{cur_date_t} | PING: N/A | UNREACHABLE | {ip_source} | {name_source}\n")
        pyautogui.alert(
            f"ВНИМАНИЕ!\nНевозможно достичь узла:\nИмя: {name_source}\nIP/Хост: {ip_source}\nВремя: {cur_date_t}",
            timeout=5000
        )
        return show_res

    if ping_val <= 35:
        show_res = Fore.GREEN + "ONLINE" + Style.RESET_ALL
    elif ping_val <= 60:
        show_res = Fore.CYAN + "FREZEE" + Style.RESET_ALL
    elif ping_val <= 300:
        show_res = Fore.YELLOW + "SLEEP" + Style.RESET_ALL
    else:
        show_res = Fore.RED + "OFFLINE" + Style.RESET_ALL + '\a'
        with open("error_logs.txt", 'a', encoding='utf-8') as f:
            f.write(f"{cur_date_t} | PING: {ping_val:.1f} | OFFLINE | {ip_source} | {name_source}\n")
        #pyautogui.alert(
        #   f"ВНИМАНИЕ!\nПроблемы с доступом к узлу:\nИмя: {name_source}\nIP: {ip_source}\nВремя: {cur_date_t}\nПинг: {ping_val:.1f}",
        #   timeout=5000
        #)
    return show_res

while True:
    now = datetime.datetime.now()
    cur_date_t = now.strftime("%d.%m.%Y %H:%M:%S")
    os.system('cls || clear')
    print(f'\n PINGc >-| Date: {cur_date_t} | Check Interval: {sleep_interval} sec.\n')
    print('\t | Name      >  IP address             >  Ping  >\t Status')
    print('\t |--------------------------------------')

    for host, name in source.items():
        if not host or not name:
            continue

        # Шаг 1: попытка разрешить хост с таймаутом
        try:
            # Если это уже IP — пропускаем резолв
            socket.inet_aton(host)
            target_ip = host
        except socket.error:
            # Это hostname — разрешаем с таймаутом
            target_ip = resolve_hostname(host, timeout=3)
            if target_ip is None:
                ping_val = None
                status_display = stat_ip_logs(None, host, name)
                print(f'\t |  {name:<12} > {host:<24} > N/A   >\t  {status_display}')
                continue

        # Шаг 2: пингуем только по IP (надёжно)
        try:
            response = ping(target_ip, size=32, count=3, timeout=2)
            ping_val = response.rtt_avg_ms
        except Exception:
            ping_val = None

        status_display = stat_ip_logs(ping_val, host, name)
        ping_str = "N/A" if ping_val is None else f"{ping_val:.1f}"
        print(f'\t |  {name:<12} > {host:<24} > {ping_str:>6} >\t  {status_display}')

    print('\t |--------------------------------------')
    print(f'\t | {sleep_interval} sec. - Current Check Interval')
    print('\t |', Fore.GREEN + "ONLINE" + Style.RESET_ALL, '- ping ≤ 35 ms')
    print('\t |', Fore.CYAN + "FREZEE" + Style.RESET_ALL, '- ping ≤ 60 ms')
    print('\t |', Fore.YELLOW + "SLEEP" + Style.RESET_ALL, '- ping ≤ 300 ms')
    print('\t |', Fore.RED + "OFFLINE/UNREACHABLE" + Style.RESET_ALL, '- ping > 300 ms or host not resolved')
    print('\t |--------------------------------------\n')

    # Таймер обновления
    for x in range(sleep_interval):
        print(f'\r\t Refresh after: {sleep_interval - x} sec.   ', end='', flush=True)
        time.sleep(1)
