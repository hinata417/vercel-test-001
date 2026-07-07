import sys

from lib import calc_total

if __name__ == "__main__":
    print(calc_total([float(x) for x in sys.argv[1:]]))
