import turtle

# Setup layar
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(5)

def pindah_dan_warna(x, y, warna_isi):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(warna_isi)
    t.begin_fill()

# 1. Persegi Panjang (Warna Merah)
pindah_dan_warna(-300, 150, "red")
for _ in range(2):
    t.forward(120)
    t.right(90)
    t.forward(60)
    t.right(90)
t.end_fill()

# 2. Segitiga (Warna Kuning)
pindah_dan_warna(-100, 150, "yellow")
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

# 3. Trapezium (Warna Hijau)
pindah_dan_warna(100, 150, "green")
t.forward(120)
t.left(120)
t.forward(60)
t.left(60)
t.forward(60)
t.left(60)
t.forward(60)
t.end_fill()
t.setheading(0) # Reset arah

# 4. Jajar Genjang (Warna Biru)
pindah_dan_warna(-200, -100, "blue")
for _ in range(2):
    t.forward(100)
    t.left(60)
    t.forward(50)
    t.left(120)
t.end_fill()

# 5. Segilima / Pentagon (Warna Ungu)
pindah_dan_warna(100, -100, "purple")
for _ in range(5):
    t.forward(70)
    t.left(72) # Sudut segilima: 360/5 = 72
t.end_fill()

t.hideturtle()
screen.mainloop()