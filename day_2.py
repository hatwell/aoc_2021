import unittest

        

class TestSubmarine(unittest.TestCase):
    def test_submarine_starts_at_zero(self):
        sub = Submarine()
        self.assertEqual(sub.get_position(), (0,0))
        
    def test_can_move_in_one_direction(self):
        sub = Submarine()
        sub.move('forward 1')
        self.assertEqual(sub.get_position(), (1,0))
        
    def test_can_move_in_multiple_directions(self):
        sub = Submarine()
        sub.move('forward 1')
        sub.move('down 1')
        self.assertEqual(sub.get_position(), (1,1))
    
    def test_can_parse_instruction(self):
        instruction = Instruction('forward 1')
        instruction.parse_instruction_string()
        self.assertEqual(instruction.direction_and_distance, ('forward', 1))
        
movements = {
    'forward': lambda position_x, position_y, distance : (position_x + distance, position_y),
    'up':  lambda position_x, position_y, distance : (position_x ,  position_y - distance),
    'down': lambda position_x, position_y, distance : (position_x ,  position_y + distance)
}



        
class Submarine:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
           
    def get_position(self):
        return (self.horizontal_position,self.depth)
    
    def move(self, instruction):
        i = Instruction(instruction)
        i.parse_instruction_string()
        direction, distance = i.direction_and_distance
        (horizontal_position, depth) = movements[direction](self.horizontal_position, self.depth, distance)
        self.horizontal_position = horizontal_position
        self.depth = depth
        
class Instruction:
    def __init__(self, instruction_string) -> None:
        self.instruction_string = instruction_string
        self.direction_and_distance = None
    
    def parse_instruction_string(self):
        print(self.instruction_string.split(" "))
        self.direction = self.instruction_string.split(" ")[0].lower()
        self.distance = int(self.instruction_string.split(" ")[1])
        self.direction_and_distance = (self.direction, self.distance)

if __name__ == '__main__':
    unittest.main()