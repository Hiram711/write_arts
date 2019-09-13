from turtle import *


def write_in_arts(mystr, font='米芾书法字体', fontsize=60):
    pendown()
    write(mystr, font=(font, fontsize, 'normal'))
    penup()


def garland():  # 阳刻
    pensize(2)
    pencolor('red')
    pendown()
    for i in range(4):
        forward(56)
        left(90)
    write('雨散\n花人', font=('经典繁方篆', 20, 'normal'))
    penup()


def diaglyph():  # 阴刻
    pensize(3)
    pencolor('white')
    fillcolor('red')
    begin_fill()
    for i in range(4):
        forward(56)
        left(90)
    end_fill()
    write('雨散\n花人', font=('经典繁方篆', 20, 'normal'))
    penup()


def action():
    saying = ['可怜今夕月，向何处，去悠悠？',
              '是别有人间，那边才见，光影东头？',
              '是天外。空汗漫，但长风浩浩送中秋？',
              '飞镜无根谁系？嫦娥不嫁谁留？']
    penup()

    goto(150, -265)
    st0 = '\n'.join(saying[0].replace('，', '').replace('？', ''))
    write_in_arts(st0, fontsize=40)

    goto(40, -390)
    st1 = '\n'.join(saying[1].replace('，', '').replace('？', ''))
    write_in_arts(st1, fontsize=40)

    goto(-70, -450)
    st2 = '\n'.join(saying[2].replace('，', '').replace('？', '').replace('。', ''))
    write_in_arts(st2, fontsize=40)

    goto(-180, -330)
    st3 = '\n'.join(saying[3].replace('，', '').replace('？', '').replace('。', ''))
    write_in_arts(st3, fontsize=40)

    goto(-250, 0)
    write_in_arts('张\n杰', fontsize=15)

    goto(-270, -70)
    garland()

    goto(-270, -140)
    diaglyph()

    hideturtle()
    done()


if __name__ == '__main__':
    action()
