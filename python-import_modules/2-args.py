#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]  # Exclude the script name
    argc = len(argv)
    if argc == 0:
        print(f"{argc} arguments.")
    else:
        print(f"{argc} argument{'s' if argc > 1 else ''}:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")