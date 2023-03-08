l = [{"name":"jenny", "edad":15},{"name":"luz", "edad":1},{"name":"y", "edad":7}]
l.sort(key=lambda voluntario:voluntario["edad"], reverse=True)
print("ordenado", l[0]["name"])

