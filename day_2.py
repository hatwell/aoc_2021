import unittest

        

class TestSubmarine(unittest.TestCase):
    # def test_submarine_starts_at_zero(self):
    #     sub = Submarine()
    #     self.assertEqual(sub.get_position(), (0,0))
        
    # def test_can_move_in_one_direction(self):
    #     sub = Submarine()
    #     sub.move('forward 1')
    #     self.assertEqual(sub.get_position(), (1,0))
        
    # def test_can_move_in_multiple_directions(self):
    #     sub = Submarine()
    #     sub.move('forward 1')
    #     sub.move('down 1')
    #     self.assertEqual(sub.get_position(), (1,0))
    
    # def test_can_parse_instruction(self):
    #     instruction = Instruction('forward 1')
    #     instruction.parse_instruction_string()
    #     self.assertEqual(instruction.direction_and_distance, ('forward', 1))
        
    def test_small_input(self):
        sub = move_submarine('test_input_2.txt')
        self.assertEqual(sub.get_position(), (15, 60))
    
    
    def test_can_do_the_thing(self):
        sub = move_submarine('day_2_input.txt')
        self.assertEqual(sub.get_position(), (1,1))





movements = {
    'down': lambda horizontal_position, depth, distance, aim : (horizontal_position ,  depth, aim + distance),
    'up':  lambda horizontal_position, depth, distance, aim : (horizontal_position ,  depth, aim - distance),
    'forward': lambda horizontal_position, depth, distance, aim : (horizontal_position + distance, depth + (aim*distance), aim),
}

class Submarine:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0

    def get_position(self):
        return (self.horizontal_position,self.depth)

    def move(self, instruction):
        i = Instruction(instruction)
        i.parse_instruction_string()
        direction, distance = i.direction_and_distance
        (horizontal_position, depth, aim) = movements[direction](self.horizontal_position, self.depth, distance, self.aim)
        self.horizontal_position = horizontal_position
        self.depth = depth
        self.aim = aim

class Instruction:
    def __init__(self, instruction_string) -> None:
        self.instruction_string = instruction_string
        self.direction_and_distance = None

    def parse_instruction_string(self):
        self.direction = self.instruction_string.replace("\n", "").split(" ")[0].lower()
        self.distance = int(self.instruction_string.split(" ")[1])
        self.direction_and_distance = (self.direction, self.distance)


def move_submarine(input_file):
    sub = Submarine()
    movements = open(input_file)
    for line in movements:
        sub.move(line)
        print(line, sub.get_position(), sub.aim)
    movements.close()
    return sub

if __name__ == '__main__':
    unittest.main()