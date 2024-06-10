import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier

a=input("Enter phone number: ")
phoneNumber = phonenumbers.parse(a)
timeZone = timezone.time_zones_for_number(phoneNumber)
Carrier = carrier.name_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')
print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)
