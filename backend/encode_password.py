from urllib.parse import quote_plus

password = "@1234anishaY"   # replace with your actual password
encoded_password = quote_plus(password)
print(encoded_password)