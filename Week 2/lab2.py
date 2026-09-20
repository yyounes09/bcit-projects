try:

    KB = 1024
    MB = 1048576
    GB = 1073741824

    num_entries = input("Please enter the number of entries per second: ")
    entry_size = input("Please enter the average number of bytes per entry: ")

    kb_size = (int(num_entries) * int(entry_size)) / KB
    mb_size = (int(num_entries) * int(entry_size)) / MB
    gb_size = (int(num_entries) * int(entry_size)) / GB

    print()
    print("Storage Estimates")

    print(f"Per minute: {60 * kb_size}KB") 
    print(f"Per hour: {3600 * mb_size}MB") 
    print(f"Per day: {86400 * gb_size}GB") 

except:

    print("Please enter a valid whole number!")

