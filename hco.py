import os
import time
import json
import pyfiglet
import phonenumbers

from colorama import *
from tabulate import tabulate

from phonenumbers import (
    geocoder,
    carrier,
    timezone,
    number_type,
    PhoneNumberFormat,
    format_number
)

init(autoreset=True)

G=Fore.GREEN+Style.BRIGHT
Y=Fore.YELLOW+Style.BRIGHT
C=Fore.CYAN+Style.BRIGHT
R=Fore.RED+Style.BRIGHT

HISTORY="history.txt"


def clear():
    os.system("clear")


def banner():

    clear()

    print(
        G+
        pyfiglet.figlet_format(
            "HCO NUMBER INFO",
            font="slant"
        )
    )

    print(Y+"━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(C+"     By Azhar Team HCO")
    print(Y+"━━━━━━━━━━━━━━━━━━━━━━━━━━\n")


def loading():

    print(
        C+
        "[+] Processing",
        end=""
    )

    for i in range(5):

        print(
            G+" ■",
            end="",
            flush=True
        )

        time.sleep(.3)

    print("\n")


def get_type(v):

    m={

0:"FIXED",

1:"MOBILE",

2:"FIXED+MOBILE",

3:"TOLL FREE",

4:"PREMIUM",

5:"SHARED",

6:"VOIP",

7:"PERSONAL"

}

    return m.get(v,"UNKNOWN")


def save(data):

    with open(
        HISTORY,
        "a",
        encoding="utf8"
    ) as f:

        f.write(
            json.dumps(data)
            +"\n"
        )


def export(info):

    with open(
        "result.txt",
        "w",
        encoding="utf8"
    ) as f:

        for x in info:

            f.write(
                f"{x[0]} : {x[1]}\n"
            )

    print(
        G+
        "\n[✓] Exported → result.txt"
    )


def social_links(num):

    print(
        Y+
        "\n[+] SOCIAL ACTIONS\n"
    )

    links=[

[
"WhatsApp",
f"https://wa.me/{num.replace('+','')}"
],

[
"Telegram",
"https://t.me/"
],

[
"Instagram",
"https://instagram.com/"
],

[
"Facebook",
"https://facebook.com/"
],

[
"Snapchat",
"https://snapchat.com"

]

]

    print(
        tabulate(
            links,
            headers=[
                "Platform",
                "Open"
            ],
            tablefmt="rounded_grid"
        )
    )


def scan():

    banner()

    num=input(
        C+
        "┌──( Number )──[+Country]\n└─$ "
    )

    try:

        parsed=phonenumbers.parse(
            num
        )

        loading()

        valid=phonenumbers.is_valid_number(
            parsed
        )

        possible=phonenumbers.is_possible_number(
            parsed
        )

        country=geocoder.description_for_number(
            parsed,
            "en"
        )

        net=carrier.name_for_number(
            parsed,
            "en"
        )

        tz=timezone.time_zones_for_number(
            parsed
        )

        info=[

["🟢 STATUS",
"VALID" if valid else "INVALID"],

["🟡 POSSIBLE",
possible],

["🌍 COUNTRY",
country],

["🏳 REGION",
phonenumbers.region_code_for_number(parsed)],

["📡 NETWORK",
net],

["📞 TYPE",
get_type(
number_type(parsed)
)],

["🌐 CODE",
"+"+
str(
parsed.country_code
)],

["🕒 TIMEZONE",
tz[0]
if tz
else "-"],

["📋 INTERNATIONAL",

format_number(
parsed,
PhoneNumberFormat.INTERNATIONAL
)],

["☎ NATIONAL",

format_number(
parsed,
PhoneNumberFormat.NATIONAL
)],

["🔢 E164",

format_number(
parsed,
PhoneNumberFormat.E164
)],

["🔗 RFC3966",

format_number(
parsed,
PhoneNumberFormat.RFC3966
)],

["📱 NATIONAL NO",
parsed.national_number],

["📏 LENGTH",

len(
str(
parsed.national_number
)
)],

["🧾 RAW INPUT",
num]

]

        print(
            G+
            "[+] SYSTEM ATTRIBUTES\n"
        )

        print(
            tabulate(
                info,
                tablefmt="double_grid"
            )
        )

        save(
            dict(info)
        )

        social_links(
            num
        )

        print(
            G+
            "\nSCAN COMPLETE ✓"
        )

        print(
            Y+
"""
[1] Export
[2] Menu
"""
        )

        c=input("> ")

        if c=="1":

            export(
                info
            )

        input(
            "\nEnter..."
        )

        menu()

    except:

        print(
            R+
            "\nInvalid Number"
        )

        input()

        menu()


def history():

    banner()

    try:

        with open(
            HISTORY
        ) as f:

            print(
                G+
                f.read()
            )

    except:

        print(
            R+
            "No History"
        )

    input()

    menu()


def lock():

    banner()

    print(
        R+
        "🔒 THIS TOOL IS LOCKED"
    )

    print(
        Y+
        "\nSubscribe To Hackers Colony Termux"
    )

    input(
        "\nPress Enter..."
    )

    os.system(
' am start -a android.intent.action.VIEW -d "https://youtube.com/@hackers_colony_termux" '
    )

    print(
        G+
        "\nRedirecting..."
    )

    time.sleep(3)

    menu()


def menu():

    banner()

    print(
        G+
"""
[1] Scan
[2] History
[3] Exit
"""
    )

    c=input("> ")

    if c=="1":

        scan()

    elif c=="2":

        history()

    else:

        exit()


lock()
