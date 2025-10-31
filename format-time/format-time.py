hours = int(input("Enter the hours(24 hours format): "))
minutes = input("Enter the minutes: ")
if int(minutes) <= 9:
    minutes = "0"+minutes
if hours == 0:
    print(f"12:{minutes} AM")
elif hours == 12:
    print(f"12:{minutes} PM")
elif hours < 12:
    print(f"{hours}:{minutes} AM")
elif hours < 24:
    print(f"{hours%12}:{minutes} PM")
