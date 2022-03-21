class maheserror(ValueError):
    print("error caused by user")
if 10==10:
    raise maheserror(10)