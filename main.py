from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]


#--------------TESTING-------------------

draw_line(250, 250, 500, 400, screen, color) #OCT 1
draw_line(250, 250, 500, 500, screen, [0,0,255]) #OCT 1-2
draw_line(250, 250, 400, 500, screen, [255,0,0]) #OCT 2
draw_line(250, 250, 250, 500, screen, color) #OCT 2-3 UNDEF
draw_line(250, 250, 100, 500, screen, [0,0,255]) #OCT 3
draw_line(250, 250, 0, 500, screen, [255,0,0]) #OCT 3-4
draw_line(250, 250, 0, 400, screen, color) #OCT 4
draw_line(250, 250, 0, 250, screen, [0,0,255]) #OCT 4-5
draw_line(250, 250, 0, 100, screen, [255,0,0]) #OCT 5
draw_line(250, 250, 0, 0, screen, color) #OCT 5-6
draw_line(250, 250, 100, 0, screen, [0,0,255]) #OCT 6

draw_line(250, 250, 250, 0, screen, [255,0,0]) #OCT 6-7 UNDEF

draw_line(250, 250, 400, 0, screen, color) #OCT 7
draw_line(250, 250, 500, 0, screen, [0,0,255]) #OCT 7-8
draw_line(250, 250, 500, 100, screen, [255,0,0]) #OCT 8
draw_line(250, 250, 500, 250, screen, [255,255,255]) #OCT 8-1



#draw_line(0, 400, 300, 300, screen, color)
#draw_line(0, 400, 200, 100, screen, [0,0,255])

#draw_line(400, 400, 200, 200, screen, [0,0,255])
#--------------TESTING-------------------


display(screen)
save_extension(screen, 'img.png')


