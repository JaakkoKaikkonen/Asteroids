def distanceSquared(x1, y1, x2, y2):
    deltaX = x2 - x1
    deltaY = y2 - y1
    return deltaX * deltaX + deltaY * deltaY

def circleCollision(x1, y1, radius1, x2, y2, radius2):
    return distanceSquared(x1, y1, x2, y2) < ((radius1 + radius2) * (radius1 + radius2))