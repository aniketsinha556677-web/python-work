def message(times):
    if times == 0:
        return

    print("Keep Learning Python")
    message(times - 1)

message(3)