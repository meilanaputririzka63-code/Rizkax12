import turtle
import math

# Pengaturan Layar
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#1e1e1e") # Latar belakang gelap seperti editor kode
screen.title("Logo SMK Prestasi Prima - Precise Version")

t = turtle.Turtle()
t.speed(0)
turtle.tracer(0, 0)

# 1. Fungsi Menggambar Lingkaran Berwarna
def draw_filled_circle(radius, color, y_offset=0):
    t.penup()
    t.goto(0, -radius + y_offset)
    t.pendown()
    t.color("black")
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# 2. Fungsi Teks Melingkar (Custom untuk Atas & Bawah)
def draw_curved_text(text, radius, start_angle, direction):
    for i, char in enumerate(text):
        angle = start_angle + (i * direction * (180 / (len(text) * 1.2)))
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        t.penup()
        t.goto(x, y)
        t.setheading(angle + (90 if direction < 0 else -90))
        t.pendown()
        t.write(char, align="center", font=("Arial", 18, "bold"))

# 3. Fungsi Gambar Tangan (Ikon Tengah)
def draw_hand_icon():
    t.penup()
    t.goto(-40, -50)
    t.pendown()
    t.color("white")
    t.fillcolor("#e32a22") # Merah ikon
    t.pensize(4)
    t.begin_fill()
    # Logika koordinat membentuk tangan sederhana
    t.setheading(90)
    t.forward(60)
    t.circle(-15, 180) # Jari kelingking
    t.setheading(90)
    t.forward(20)
    t.circle(-15, 180) # Jari manis
    t.setheading(90)
    t.forward(30)
    t.circle(-15, 180) # Jari tengah
    t.setheading(90)
    t.forward(80)      # Jari telunjuk (paling tinggi)
    t.circle(-15, 180)
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(30)
    t.end_fill()
    
    # Titik putih di ujung telunjuk
    t.penup()
    t.goto(-10, 80)
    t.dot(20, "white")

# --- PROSES MENGGAMBAR ---

# Lingkaran Biru Luar
draw_filled_circle(250, "#1d5291")

# Lingkaran Putih (Border Teks)
draw_filled_circle(235, "white")
draw_filled_circle(225, "#1d5291") # Balik ke biru untuk kontras

# Lingkaran Putih Dalam (Area Tangan)
draw_filled_circle(170, "white")

# Menambahkan Teks Melingkar
t.color("black")
draw_curved_text("SEKOLAH MENENGAH KEJURUAN", 190, 155, -1)
draw_curved_text("PRESTASI PRIMA", 190, 225, 1)

# Menambahkan Bintang
def draw_star(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.color("black")
    t.begin_fill()
    for _ in range(5):
        t.forward(20)
        t.right(144)
    t.end_fill()

draw_star(-215, -10)
draw_star(200, -10)

# Menggambar Tangan di Tengah
draw_hand_icon()

t.hideturtle()
turtle.update()
turtle.done()