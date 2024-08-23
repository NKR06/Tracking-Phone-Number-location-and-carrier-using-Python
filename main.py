import phonenumbers
from phonenumbers import geocoder, carrier


number = "+91 9849592383"  
parsed_number = phonenumbers.parse(number)


location = geocoder.description_for_number(parsed_number, "en")
phone_carrier = carrier.name_for_number(parsed_number, "en")

print(f"Location: {location}")
print(f"Carrier: {phone_carrier}")
