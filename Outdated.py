def main():
    months = [
        "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ]
    while True:
    date_str = input("Date: ").strip().replace(" ", "")
    if "/" in date_str:
        month, day, year = date_str.split("/")
        month = int(month)
        day = int(day)
        year = int(year)

    elif "," in date_str:
        month_name, rest = date_str.split(" ", 1)
        day, year = rest.split(",")
        month = months.index(month_name) + 1
        day = int(day.strip())
        year = int(year.strip())

    else:
        raise ValueError("Invalid format")

    if not (1 <= month <= 12 and 1 <= day <= 31):
        raise ValueError("Invalid date")

    print(f"{year:04d}-{month:02d}-{day:02d}")
    break

main()