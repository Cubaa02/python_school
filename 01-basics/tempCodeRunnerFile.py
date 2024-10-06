def next_christmas_on_sunday():
    y = this_year
    while True:
        xmas_date = date(y, 12, 25)
        if xmas_date.weekday() == 6:
            return y
        y += 1

next_xmas_y = next_christmas_on_sunday()

print(f"\nNext Sunday christmas is in year {next_xmas_y}.")