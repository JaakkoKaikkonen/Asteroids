import math

def distanceSquared(x1, y1, x2, y2):
    deltaX = x2 - x1
    deltaY = y2 - y1
    return deltaX * deltaX + deltaY * deltaY

def circleCollision(x1, y1, radius1, x2, y2, radius2):
    return distanceSquared(x1, y1, x2, y2) < ((radius1 + radius2) * (radius1 + radius2))


#Inputs are lists of pairs
def convexPolygonCollisionSAT(vertices1, vertices2):

    for a in range(len(vertices1)):

        b = (a + 1) % len(vertices1)
        axisProjection = (-(vertices1[b][1] - vertices1[a][1]), vertices1[b][0] - vertices1[a][0])

        min1 = math.inf
        max1 = -math.inf
        for vertex in vertices1:
            dotProduct = (vertex[0] * axisProjection[0] + vertex[1] * axisProjection[1])
            min1 = min(min1, dotProduct)
            max1 = max(max1, dotProduct)

        min2 = math.inf
        max2 = -math.inf
        for vertex in vertices2:
            dotProduct = (vertex[0] * axisProjection[0] + vertex[1] * axisProjection[1])
            min2 = min(min2, dotProduct)
            max2 = max(max2, dotProduct)

        if (not(max2 >= min1 and max1 >= min2)):
            return False

    for a in range(len(vertices2)):

        b = (a + 1) % len(vertices2)
        axisProjection = (-(vertices2[b][1] - vertices2[a][1]), vertices2[b][0] - vertices2[a][0])

        min1 = math.inf
        max1 = -math.inf
        for vertex in vertices2:
            dotProduct = (vertex[0] * axisProjection[0] + vertex[1] * axisProjection[1])
            min1 = min(min1, dotProduct)
            max1 = max(max1, dotProduct)

        min2 = math.inf
        max2 = -math.inf
        for vertex in vertices1:
            dotProduct = (vertex[0] * axisProjection[0] + vertex[1] * axisProjection[1])
            min2 = min(min2, dotProduct)
            max2 = max(max2, dotProduct)

        if (not(max2 >= min1 and max1 >= min2)):
            return False

    return True