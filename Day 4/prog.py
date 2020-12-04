import re


def check_byr(s):
    return 1920 <= int(s) <= 2002


def check_iyr(s):
    return 2010 <= int(s) <= 2020


def check_eyr(s):
    return 2020 <= int(s) <= 2030


def check_height(s):
    match = re.match(r'^([0-9]+)(cm|in)$', s)
    if match:
        g = match.groups()
        return (g[1] == "cm" and 150 <= int(g[0]) <= 193) or (g[1] == "in" and 59 <= int(g[0]) <= 76)


def check_hcl(s):
    return re.match(r'^#[0-9a-f]{6}$', s)


def check_pid(s):
    return re.match(r'^[0-9]{9}$', s)


def check_ecl(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


with open("input") as f:
    entries = f.read().strip().split("\n\n")
    passports = []
    for entry in entries:
        passport = {}
        for e in entry.replace("\n", " ").split(" "):
            k, v = e.split(":")
            passport[k] = v
        passports.append(passport)

    valid1 = 0
    valid2 = 0

    for p in passports:
        if all(key in p for key in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
            valid1 += 1
            if check_byr(p["byr"]):
                if check_iyr(p["iyr"]):
                    if check_eyr(p["eyr"]):
                        if check_height(p["hgt"]):
                            if check_hcl(p["hcl"]):
                                if check_ecl(p["ecl"]):
                                    if check_pid(p["pid"]):
                                        valid2 += 1

    print("Part 1: ", valid1, "\nPart 2: ", valid2)
