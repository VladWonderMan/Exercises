# task 1
log = [
'May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
'May 20 11:01:12 PC-00102 PackageKit: daemon start',
'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.',
]


# task 2
str_log = log[1].split()
dic_log = {
    'time': " ".join(str_log[:3]),
    'pc_name': str_log[3],
    'service_name': (str_log[4])[:-1],
    'message': " ".join(str_log[5:])
}
print (dic_log)


# task 3
str_number = input(f"Please type a string number(between 0-{(len(log)-1)}):\n")
if int(str_number) <=10 and int(str_number) >=0:
    str_log = log[int(str_number)].split()
    dic_log = {
    'time': " ".join(str_log[:3]),
    'pc_name': str_log[3],
    'service_name': (str_log[4])[:-1],
    'message': " ".join(str_log[5:])
}
print (f"{dic_log['pc_name']}: {dic_log['message']}")

# task 4.1
list1=['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']
# task 4.2
list2=['time','pc_name','service_name','message']
#task 4.3
print(dict(zip(list2,list1)))

#task 5
dict_1=dict(zip(list2,list1))

list3=[]
list3.append(dict_1.copy())
list3.append(dic_log.copy())
print(list3)

#task 6
print (list(set(list3[0].values()) & set(list3[1].values())))