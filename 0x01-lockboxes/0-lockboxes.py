
#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened or not.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    num_boxes = len(boxes)
    keys = set()
    opened_boxes = []
    current_box = 0

    while current_box < num_boxes:
        previous_box = current_box
        opened_boxes.append(current_box)
        keys.update(boxes[current_box])
        
        for key in keys:
            if key != 0 and key < num_boxes and key not in opened_boxes:
                current_box = key
                break

        if previous_box != current_box:
            continue
        else:
            break

    for i in range(num_boxes):
        if i not in opened_boxes and i != 0:
            return False

    return True
