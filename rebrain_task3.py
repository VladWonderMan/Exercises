storage_use=[
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768,  'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768,  'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287,  'used': 9522710872},
]

#task 1
storage_number = input("Please enter number of a storage device(0-6):\n")

#task 2
if storage_number.isdigit():
    if int(storage_number) >= 0 and int(storage_number) <= 6:

        total = storage_use[int(storage_number)]['total']
        used = storage_use[int(storage_number)]['used']
        used_percent =  int((used / total) * 100)
        
#task 3.1
        total_GB = int(total / (1024 ** 3))
        used_GB = int(used / (1024 ** 3))
        left_percent = int(100 - used_percent)
        left_GB = int(total_GB - used_GB)
        print (f"\ntotal: {total_GB}Gb \nused: {used_GB}Gb {used_percent}% \nleft: {left_GB}Gb {left_percent}%\n")

        if left_GB < 10 or left_percent < 5:
            print (f"storage {storage_number} has critical low disk space")
#task 3.2
        elif left_GB < 30 or left_percent < 10:
            print (f"storage {storage_number} has low disk space")
        else:
# task 3.3
            print (f"storage {storage_number}  has enough disk space")
    else:
        print("number must to between 0 and 6")
else:
    print("this is not a number.")
