class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        swapped = 0
        while True:
            swapped = self.robot_bubbles()
            # print('swapped ? ', swapped)
            self.restart()
            # print('updated list', self._list)
            if swapped == 0:
                break



    def restart(self):
        self._position = 0

    def check_position(self):
        # print('check triggered')
        # print(self._position)
        return self._position
    
    def item_check(self):
        return self._list[self.check_position()]
    
    def robot_item(self):
        return self._item
    
    def robot_bubbles(self):
        old_list = [*self._list]
        # print('old_list', self._list)
        swap_count = 0
        # print('item on the assembly belt before robot initial pick up: ', self.item_check())
        # print('position of robot', self.check_position())
        # self.swap_item()
        # print('robot picked up: ', self.robot_item())
        # print('on the assembly belt after pickup: ', self.item_check())

        while self.can_move_right():
            # print('robot item: ', self.robot_item(), 'belt item: ', self.item_check())
            if self.robot_item() == None:
                 self.swap_item()
                #  print('robot had nothing and picked up: ', self.robot_item())
                 self.move_right()
                #  print('moved to position: ', self.check_position())
            
            # print('robot currently has: ', self.robot_item())
            # print('item on the belt: ', self.item_check())
            

            if self.compare_item() == 1:  #robot item is > than belt item
                # print('robot item > belt item')
                # print('robot item: ', self.robot_item(), 'belt item: ', self.item_check())
                self.swap_item()
                # print('swapped item!', self.item_check(), 'for ', self.robot_item())
                self.move_left()
                # print('robot stepped back to swap')
                self.swap_item()  
                # print('swapped item again with previous', self.item_check(), 'for ', self.robot_item())
                if not self.light_is_on():
                    self.set_light_on()
                    # print('robot turned on his swap alert light.')
                swap_count = swap_count + 1
                self.move_right()
                # self.move_right()
                # print('Robot stepped ahead two steps to continue')

                # print('robot currently has: ', self.robot_item())
                # print('item on the belt: ', self.item_check())
                # print('current position: ', self.check_position())
            else: 
                # print('robot item <= belt item. step back 1')
                # print('robot item: ', self.robot_item(), 'belt item: ', self.item_check())
                self.move_left()
                self.swap_item()  #put back the item picked up since it wasn't greater than the 2nd of the pair.
                # print('robot went back and replaced the item: ', self.item_check(), 'in position: ', self.check_position())
                self.move_right()
                # self.move_right()
                pass #go to next iteration of while loop
        
        # print('robot has reached the end of the aseembly belt')
        new_list = self._list
        # print('\noldlist', old_list)
        # print('\nnewlist', new_list)
        self.set_light_off()
        return swap_count
        

                


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()

    # print(robot._list)

##TODO UPER:
# Understand: 
# because the robot cannot jump to different parts of the list, so easily, need a sequential sorting algorithm.
# cannot access self.position, so will use the move helper methods to shift the robot.  
# to minimize the movement of the robot, bubble sort will be selected.  it is a robot after all, so whenever it gets to the end of the list (call it assembly line) it will "robotically" go back to the beginning of the line and compare adjacent items again until it goes through the entire assembly line, and not making any more swaps. 
# 
# Planning:
# Bubble sort algorithm, moving the robot using the predefined methods.
# define a new method "restart" which pushes the robot back to the beginning of the assembly line.
# have the robot keep track of the swaps made using the set_light_on.  only 1 swap is required to restart on the line
# (how to keep track of position wehre nothing is there?)

# pseudocode:
# 1. check to see the robot is at the beginning of the line.  if the can move left returns false, the robot is at the starting point.  
# 2. swap_item to pick up the first item.  none for item #0.  set pickup_point = robot-none <=> item,  drop_off robot-item <=> none
# 3. move right
# 4. compare_item. if the value is -1, swap the item because it is less.  keep track of the position swap_point = item <=> item
# 5. else keep going till value is -1.  go to step 8 for logical next step.
# 5. move left and swap item with none. set the drop_off_point.    
# 6. move back to the swap_point
# 7. swap_item to pick it up.  now none is in it's place.  
#(need to keep track of current position that has none in it.)
#8. keep moving to the right and compare_item until -1 is returned. then swap_item and move left to where the item has Nothing there.  (pickup_point) (how to keep track of position wehre nothing is there?)
# 9. when robot reaches end of line, if light is on.  light will be on when swap_count has reached two.  (1st swap count doesn't count because not accounting for pickinp up 1st item.  
# )
#/ *** how to distinguish between drop_off and pickup_points ? 

# pickup = robot-none <=> item in assembly line
# dropoff = robot-item <=> none in assembly line
# swap_point robot-item <=> item in assembly line 