import turtle

# Pengaturan Layar
screen = turtle.Screen()
screen.bgcolor("black") # Latar belakang hitam agar warna bintang menyala
screen.title("Pola Bintang Geometris")

t = turtle.Turtle()
t.speed(0) # Kecepatan maksimal

# Daftar warna untuk setiap garis
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Fungsi untuk menggambar bintang spiral
def draw_star_spiral():
    for x in range(200):
        # Mengambil warna dari daftar secara berurutan
        t.pencolor(colors[x % 6])
        
        # Mengatur lebar garis yang semakin tebal
        t.width(x / 100 + 1)
        
        # Gerakan kura-kura: maju dan berbelok dengan sudut bintang
        t.forward(x * 1.5)
        t.left(144) # Sudut 144 derajat menciptakan bentuk bintang 5 sudut

# Mulai menggambar
t.penup()
t.goto(-50, 0)
t.pendown()

draw_star_spiral()

t.hideturtle()
turtle.done()