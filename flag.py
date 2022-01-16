import hashlib

str = 'run_get_flag'

hl = hashlib.md5()

hl.update(str.encode(encoding='utf-8'))

print(hl.hexdigest())

