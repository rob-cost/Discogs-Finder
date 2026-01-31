def get_string(prompt, allowed=None):
    while True:
        raw = input(prompt).strip()

        if not raw:
            print("Input cannot be empty")
            continue

        values = [v.strip().lower() for v in raw.split(",")]

        if allowed:
            invalid = [v for v in values if v not in allowed]
            if invalid:
                print(f"Invalid value(s): {', '.join(invalid)}")
                print("Please enter a value from discogs list")
                continue

        return values if len(values) > 1 else values[0]


def get_int(prompt):
    while True:
        value = input(prompt).strip()

        if value.isdigit():
            return int(value)

        print("Insert a correct number")


def get_year(prompt):
    while True:
        value = input(prompt).strip()

        if value.isdigit() and 1960 < int(value) < 2027:
            return int(value)

        if "-" in value:
            try:
                start, end = map(int, value.split("-"))
                if start < end:
                    return value
            except ValueError:
                pass

        print("Insert a right value")
