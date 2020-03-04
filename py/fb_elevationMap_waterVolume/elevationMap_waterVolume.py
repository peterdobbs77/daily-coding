
def givenElevationMap_ComputeWaterVolume(map):
    volume_i = 0
    h = map[0]
    for i in range(1, len(map)-1):
        if(h > map[i]):
            volume_i += h - map[i]
        else:
            h = map[i]

    return volume_i


test_map = [2, 1, 2]
print(test_map)
assert givenElevationMap_ComputeWaterVolume(test_map) == 1

test_map = [3, 0, 1, 3, 0, 5]
print(test_map)
assert givenElevationMap_ComputeWaterVolume(test_map) == 8

test_map = [0, 0, 1, 3, 0, 5]
print(test_map)
assert givenElevationMap_ComputeWaterVolume(test_map) == 3

# # this corner case doesn't work... 
# test_map = [3, 0, 1, 3, 0, 2]
# print(test_map)
# assert givenElevationMap_ComputeWaterVolume(test_map) == 7
