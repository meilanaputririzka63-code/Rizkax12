import turtle

t = turtle.Turtle()

def kotak(warna, y):
    t.penup(); t.goto(-100, y); t.pendown()
    t.color("black", warna); t.begin_fill()
    for _ in range(2):
        t.forward(200); t.right(50) # Panjang 200, Lebar 50
        t.right(40); t.forward(50); t.right(90)
    t.end_fill()

# Gambar bagian Merah (atas)
kotak("red", 50)
# Gambar bagian Putih (bawah)
kotak("white", 0)

turtle.done()