import turtle
import colorsys
import random

# إعداد الشاشة
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spray Paint Mandala Effect")
screen.tracer(0, 0) # لتسريع الرسم وجعل الحركة تبدو كأنها "بث" فوري

t = turtle.Turtle()
t.hideturtle()
t.penup() # لضمان عدم رسم خطوط متصلة

# إعدادات الألوان
n = 100
h = 0

# حلقة الرسم (تأثير الرذاذ)
for i in range(500):
    # تغيير اللون بشكل ديناميكي
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    h += 1/n
    
    # تحديد مسار الرسم الأساسي
    t.forward(i * 0.5)
    t.right(59) # زاوية لعمل شكل حلزوني مبعثر
    
    # صنع تأثير الرذاذ (رسم نقاط عشوائية حول النقطة الحالية)
    for _ in range(15): # عدد حبات الرذاذ في كل خطوة
        x_offset = random.randint(-20, 20)
        y_offset = random.randint(-20, 20)
        
        # حفظ الموقع الحالي
        current_pos = t.pos()
        
        # التحرك لموقع الرذاذ العشوائي ورسم نقطة
        t.goto(current_pos[0] + x_offset, current_pos[1] + y_offset)
        t.dot(random.randint(1, 3)) # أحجام مختلفة للحبيبات
        
        # العودة للمسار الأصلي
        t.goto(current_pos)
    
    # تحديث الشاشة في كل دورة لرؤية الألوان وهي تتغير
    if i % 5 == 0:
        screen.update()

screen.exitonclick()