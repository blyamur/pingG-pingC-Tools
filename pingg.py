from pythonping import ping
import datetime
import time
import os
__author__ = "Mons (https://blog.mons.ws)"
sleep_interval = 30  # (In seconds) Check Interval
source = {'8.8.8.8': 'Google',  #list of addresses and names. For example 'IP or domain': 'Source name',
           'yandex.ru': 'ya.ru'}

def stat_ip_logs(ping,ip_source,name_source): #resource availability check function #Logging function if ping is high
    if ping <= 500:
        show_res ='ONLINE'
    elif ping <= 1500:
         show_res ='FREZEE'
    else:
        show_res ='OFFLINE'
        error_logs = open("error_logs.txt", 'a')
        error_logs.write(cur_date_t+' | OFFLINE '+' | '+ip_source+' | '+name_source+"\n") #Write to file, date, status, ip source, name source
        error_logs.close()
    return show_res
    print(show_res)

while True:
    now = datetime.datetime.now() #Current Date
    cur_date_t = now.strftime("%d.%m.%Y %H:%M %S") #Formatting the date output
    os.system('cls||clear') #Clear the console

    print('\n PINGg >-| Date:',cur_date_t,'| Check Interval:',sleep_interval,'sec.\n')
    print('\t|','Name      >  IP address             >  Ping  >\t Status')
    print('\t|');
    print('\t|--------------------------------------');
    print('\t|');
    for key, value in source.items():
        f_key, f_value = key, value
        if f_key and f_value: 
           rlw = ping (f_key, size= 30, count= 4).rtt_avg_ms
           print('\t|  %s    > %s            >' % (f_value,f_key),rlw,' >\t  ', stat_ip_logs(rlw,f_key,f_value))
        f_key, f_value = key, value
    print('\t|');
    print('\t|--------------------------------------');
    print('\t|');
    print('\t| ',sleep_interval,'sec. - Current Check Interval');
    print('\t| ',"ONLINE",' - ping less than 500 msec.')
    print('\t| ',"FREZEE",' - ping more than 500 msec.')
    print('\t| ',"OFFLINE",'- ping more than 1500 ms.')
    print('\t|');
    print('\t|--------------------------------------\n');
    #Countdown timer
    for x in reversed(range(sleep_interval)):
       print('\r \t ' + str(x), end="\r")
       time.sleep(1)
    continue
