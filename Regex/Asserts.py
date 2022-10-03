import re
msg = 'Geometry type "point" is not supported'
result = re.match(r'^Geometry type ".+" is not supported$', msg)
print(result)
assert re.match(r'^Geometry type ".+" is not supported$', msg)
# assert result