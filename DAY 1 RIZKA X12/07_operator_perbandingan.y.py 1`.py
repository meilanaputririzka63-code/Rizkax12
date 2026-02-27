# persegi
s = float(input("Sisi persegi: "))
print(f"Luas: {s*s}, Keliling: {4*s}")

# Persegi Panjang 
p = float(input("Panjang: "))
l = float(input("Lebar: "))
print(f"Luas: {p*l}, Keliling: {2*{p+l}}")

# Trapesium 
a = float(input("Sisi atas: "))
b = float(input("Sisi Bawah: "))
t = float(input("Tinggi: "))
sm = float(input("Sisi miring: "))
print(f"Luas: {0.5 * (a + b) * t}, Keliling: {a + b + {2 * sm}}")