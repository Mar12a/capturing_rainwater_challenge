def capturing_rainwater(heights):
  map = []
  max_height = max(heights, default = 0)
  for j in range(max_height):
      map.append([])
  for i in range(len(heights)):
    for k in range(max_height):
      if heights[i] > k:
        map[k].append(1)
      else: 
        map[k].append(0)
  #print(map)

  water = []
  for i in range(len(map)):
    for j in range(1, len(map[i])):
      if map[i][j] == 0 and map[i][j-1] == 1: 
        for k in range(j+1, len(map[i])):
          if map[i][k] == 1 and map[i][k-1] == 0:
            water.append([[i,j], [i,k-1]])
            break

  volume = 0
  for i in range(len(water)):
      volume = volume + (water[i][1][1] - water[i][0][1] + 1)
  return volume

test_array = [4, 2, 1, 3, 0, 1, 2]
print(capturing_rainwater(test_array))

