#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]  # Exclude the script name
    total = sum(int(arg) for arg in argv) if argv else 0
    print(total)