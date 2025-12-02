from pythonping import ping
import datetime
import time
import os
import colorama
from colorama import Fore, Style
import pyautogui
__author__ = "Mons (https://blog.mons.ws)"
colorama.init()
sleep_interval = 30  # (In seconds) Check Interval
with open('settings.xml') as file:
    lines = file.read().splitlines()
source = {}
for line in lines:
    key, value = line.split(':')
    source.update({key: value})

def stat_ip_logs(ping, ip_source, name_source):  # Logging function if ping is high
    if ping <= 20:
        show_res = Fore.GREEN + "ONLINE" + Style.RESET_ALL
    elif ping <= 50:
        show_res = Fore.CYAN + "FREZEE" + Style.RESET_ALL
    elif ping <= 300:
        show_res = Fore.YELLOW + "SLEEP" + Style.RESET_ALL
    else:
        show_res = Fore.RED + "OFFLINE" + Style.RESET_ALL + '\a'
        error_logs = open("error_logs.txt", 'a')
        error_logs.write(cur_date_t + ' | PING: ' + str(ping) + ' | OFFLINE |  ' + ip_source + ' | ' + name_source + "\n")  # Write to file, date, ping, status, ip source, name source
        error_logs.close()
        pyautogui.alert("ВНИМАНИЕ!\nПроблемы с доступом к узлу:\nИмя: " + name_source + "\nIP: " + ip_source + "\nВремя: " + cur_date_t + "\nПинг: " + str(ping), timeout=5)
    return show_res

while True:
    now = datetime.datetime.now()  # Current Date
    cur_date_t = now.strftime("%d.%m.%Y %H:%M %S")  # Formatting the date output
    os.system('cls||clear')  # Clear the console
    print('\n PINGc >-| Date:', cur_date_t, '| Check Interval:', sleep_interval, 'sec.\n')
    print('\t | Name            | IP address                | Ping     | Status')
    print('\t |-----------------|---------------------------|----------|--------------')
    
    results = []
    max_name_len = 15  # Минимальная ширина для имени
    max_ip_len = 15    # Минимальная ширина для IP
    
   
    for key, value in source.items():
        if key and value:
            rlw = ping(key, size=30, count=4).rtt_avg_ms
            status = stat_ip_logs(rlw, key, value)
            
            max_name_len = max(max_name_len, len(value))
            max_ip_len = max(max_ip_len, len(key))
            
            results.append({
                'name': value,
                'ip': key,
                'ping': rlw,
                'status': status
            })
    
    for result in results:
        name_str = result['name'].ljust(max_name_len)
        ip_str = result['ip'].ljust(max_ip_len)
        ping_str = f"{result['ping']:.1f}".ljust(8)
        
        print(f'\t | {name_str} | {ip_str} | {ping_str} | {result["status"]}')

    print('\t |-----------------|---------------------------|----------|----------------')
    print('\t |', sleep_interval, 'sec. - Current Check Interval')
    print('\t |', Fore.GREEN + "ONLINE" + Style.RESET_ALL, '- ping less than 20 msec.')
    print('\t |', Fore.CYAN + "FREZEE" + Style.RESET_ALL, '- ping more than 40 msec.')
    print('\t |', Fore.YELLOW + "SLEEP" + Style.RESET_ALL, '- ping more than 300 msec.')
    print('\t |', Fore.RED + "OFFLINE" + Style.RESET_ALL, '- ping more than 1500 ms.')
    print('\t |')
    print('\t |--------------------------------------\n')
    
    # Countdown timer
    for x in range(sleep_interval):
        print('\r\t Refresh after:  ' + str(sleep_interval - x), end=" sec.s \r")
        time.sleep(1)
    continue
