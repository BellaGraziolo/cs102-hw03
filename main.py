import sys
from statistics import mean


def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip("\n")
            sculpture = line.split(",")
            fun = []
            for u in sculpture:
                fun.append(float(u))
            av = mean(fun)
            print(f"{av}")


if __name__ == "__main__":
    main()
