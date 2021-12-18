# task 1
log = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
#task 1.1
print (log[:15])
#task 1.2
print (log[24:34])
#task 1.3
print (log.replace('ideapad', 'PC-12092'))
#task 1.4
print (log.find('failed'))
#task 1.5
print (log.lower().count('s'))
#task 1.6
print (int(log[7:9])+int(log[10:12])+int(log[13:15]))

#task 2
log = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
split_log1 = log.split(' ')
split_log2 = log.split(':')
print (f'The PC {split_log1[3]} receive message from service "{split_log1[4]}" what says "{" ".join(split_log1[5:11])}" because "{(split_log2[-1]).strip()}" at {log[:15]}')