def insidebox(pos,rect):
    if pos.X>rect.topleft.X and pos.Y < rect.topleft.Y and pos.X < rect.bottomright.X and pos.Y > rect.bottomright.Y:
        return true
'''If a point is greater than the x value of the the top left corner of a rectangle and less than the y value,
while also being less than the x value and greater than the y of the bottom right corner it must be inide the rectangle.
