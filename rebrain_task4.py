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
dic_list=[]

for i in range(len(log)):
    str_log = log[i].split()
    dic_log = {
        'time': " ".join(str_log[:3]),
        'pc_name': str_log[3],
        'service_name': (str_log[4])[:-1],
        'message': " ".join(str_log[5:])
    }
    dic_list.append(dic_log)

# task 3
# print (dic_list)
# for i in range(len(dic_list)):
#     print ( dic_list[i]["time"])

print([a["time"] for a in dic_list])

# task 4
for i in range(len(dic_list)):
    str_date = dic_list[i]["time"].split()
    dic_list[i]["date"] = " ".join(str_date[:2])
    dic_list[i]["time"] = str_date[2]

print("\n")
print([a["time"] for a in dic_list])
print("\n")

# task 5
print([a["message"] for a in dic_list if a["pc_name"] == 'PC0078'])
print("\n")

# task 6
dic_list = dict(zip(range(100,110),dic_list))

# task 7
print (dic_list[104])