from werkzeug.security import check_password_hash, generate_password_hash
hash = generate_password_hash('kevin')
print(hash)
result = check_password_hash()