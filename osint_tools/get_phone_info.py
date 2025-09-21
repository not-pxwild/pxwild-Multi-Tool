import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def main():
    number = input("Enter phone number (+countrycode...): ").strip()
    try:
        pn = phonenumbers.parse(number, None)
        if not phonenumbers.is_valid_number(pn):
            print("Invalid phone number."); return
        print("Country:", geocoder.description_for_number(pn, "en") or "-")
        print("Carrier:", carrier.name_for_number(pn, "en") or "-")
        print("Timezone:", ", ".join(timezone.time_zones_for_number(pn)) or "-")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
