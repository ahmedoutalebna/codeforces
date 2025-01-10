def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (flowerbed[i-1] == 0 or i == 0) and (flowerbed[i+1] == 0 or i == len(flowerbed)-1 ):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return False

print(canPlaceFlowers([1,0,0,0,1]
, 2))