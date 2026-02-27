import turtle

# Setup layar
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(3)

def pindah(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# 1. Persegi Panjang
pindah(-300, 100)
t.write("Persegi Panjang", align="center")
for _ in range(2):
    t.forward(120)
    t.right(90)
    t.forward(60)
    t.right(90)

# 2. Segitiga (Sama Sisi)
pindah(-100, 100)
t.write("Segitiga", align="center")
for _ in range(3):
    t.forward(100)
    t.left(120)

# 3. Trapezium
pindah(100, 100)
t.write("Trapezium", align="center")
t.forward(120)   # Sisi bawah
t.left(120)
t.forward(60)    # Sisi miring kiri
t.left(60)
t.forward(60)    # Sisi atas
t.left(60)
t.forward(60)    # Sisi miring kanan
t.setheading(0)  # Reset arah ke kanan

# 4. Jajar Genjang
pindah(-200, -100)
t.write("Jajar Genjang", align="center")
for _ in range(2):
    t.forward(100)
    t.left(60)
    t.forward(50)
    t.left(120)

# 5. Belah Ketupat
pindah(50, -100)
t.write("Belah Ketupat", align="center")
t.left(45) # Putar arah agar membentuk berlian
for _ in range(4):
    t.forward(80)
    t.left(90)

t.hideturtle()
screen.mainloop()