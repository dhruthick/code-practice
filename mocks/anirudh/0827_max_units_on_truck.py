'''
You are assigned to put some amount of boxes onto one truck. 
You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can 
be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes 
does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4

boxtype[0] = type 0, 1 box of type 0, 3 units 

Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
 
Constraints:

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106
'''

#[[5,10][3,9],[4,7],[2,5]] 50 27 14

def find_boxes(boxTypes, truckSize):
    max_units = 0
    remaining_boxes = truckSize
    boxTypes.sort(key = lambda  x:x[1], reverse=True)
    print(boxTypes)
    for box in boxTypes:
        if box[0] < remaining_boxes:
            max_units += box[0] * box[1]   
            remaining_boxes -= box[0]
            print("here {}".format(box))
            print("Remaining boxes {}".format(remaining_boxes))
            print("Max units {}".format(max_units))
        else:
            max_units += (remaining_boxes)*box[1]
            print("Max units last{}".format(max_units))
            print("here last {}".format(box))
            break
    return max_units

print(find_boxes([[1,3],[2,2],[3,1]], 4))
