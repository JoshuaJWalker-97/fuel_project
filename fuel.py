def main():
    while True:

        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split("/"))
            if x > y or y == 0:
                raise ValueError
            fuel = (x / y) * 100
            if fuel <= 1:
                print("E")
            elif fuel >= 99:
                print("F")
            else:
                print(f"{fuel:.0f}%")
            break
        except (ValueError, ZeroDivisionError):
            continue

if __name__ == "__main__":
    main()
