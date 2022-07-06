import unittest
from main import ToyBot


bot = ToyBot()


class HappyPathTesting(unittest.TestCase):

    def test_a(self):
        """
        Given test example from Code Challenge Document
        """
        bot.place('0', '0', 'NORTH')
        bot.move()
        self.assertEqual(bot.report(), '0,1,NORTH')

    def test_b(self):
        """
        Given test example from Code Challenge Document
        """
        bot.place('0', '0', 'NORTH')
        bot.left()
        self.assertEqual(bot.report(), '0,0,WEST')

    def test_c(self):
        """
        Given test example from Code Challenge Document
        """
        bot.place('1', '2', 'EAST')
        bot.move()
        bot.move()
        bot.left()
        bot.move()
        self.assertEqual(bot.report(), '3,3,NORTH')

    def test_left_right(self):
        bot.place('3', '3', 'EAST')
        bot.move()
        bot.left()
        bot.right()
        self.assertEqual(bot.report(), '4,3,EAST')

    def test_double_place(self):
        bot.place('4', '4', 'WEST')
        bot.place('3', '3', 'EAST')
        self.assertEqual(bot.report(), '3,3,EAST')

    def test_double_place_with_move(self):
        bot.place('4', '4', 'WEST')
        bot.place('3', '3', 'EAST')
        bot.move()
        self.assertEqual(bot.report(), '4,3,EAST')

    def test_move_backwards_x_axis(self):
        bot.place('4', '4', 'WEST')
        bot.place('3', '3', 'WEST')
        bot.move()
        self.assertEqual(bot.report(), '2,3,WEST')
        bot.move()
        self.assertEqual(bot.report(), '1,3,WEST')


class SadPathTesting(unittest.TestCase):

    def test_wrong_place_input_case_1(self):
        """
        Toy bot will fall for over placing in x axis too much
        """
        x = '6'
        y = '6'
        facing = 'WEAST'
        place = bot.place(x, y, facing)
        self.assertNotEqual(place, True)

    def test_wrong_place_input_case_2(self):
        """
        Toy bot will fall for over placing in x axis
        """
        x = '5'
        y = '6'
        facing = 'WEAST'
        place = bot.place(x, y, facing)
        self.assertNotEqual(place, True)

    def test_wrong_place_input_case_3(self):
        """
        Toy bot will fall for over placing in y axis too much
        """
        x = '4'
        y = '6'
        facing = 'WEAST'
        place = bot.place(x, y, facing)
        self.assertNotEqual(place, True)

    def test_wrong_place_input_case_4(self):
        """
        Toy bot will fall for over placing in y axis
        """
        x = '4'
        y = '5'
        facing = 'WEAST'
        place = bot.place(x, y, facing)
        self.assertNotEqual(place, True)

    def test_wrong_place_input_case_5(self):
        """
        Unavailable direction
        """
        x = '4'
        y = '3'
        facing = 'WEAST'
        place = bot.place(x, y, facing)
        self.assertNotEqual(place, True)

    def test_wrong_place_input_case_6(self):
        """
        Attempt to put decimal in axis position
        """
        x = '1.1'
        y = '3'
        facing = 'WEAST'
        place = bot.place(x, y, facing)
        self.assertNotEqual(place, True)

    def test_wrong_place_input_case_7(self):
        """
        Attempt to put negative in axis position
        """
        x = '-1'
        y = '3'
        facing = 'WEAST'
        place = bot.place(x, y, facing)
        self.assertNotEqual(place, True)

    def test_over_movement(self):
        """
        Continuously attempt to move even if ToyBot will fall
        """
        x = '3'
        y = '3'
        facing = 'NORTH'
        bot.place(x, y, facing)
        bot.move()  # 'y' will be 4 which is the limit
        report_from_valid_move_y = bot.report()
        # Continuously attempt to move on 'y' axis
        bot.move()
        bot.move()
        self.assertEqual(report_from_valid_move_y, bot.report())
        bot.move()
        self.assertEqual(report_from_valid_move_y, bot.report())
        bot.right()  # try 'x' axis
        bot.move()  # 'x' will be 4 which is the limit
        report_from_valid_move_x = bot.report()
        # Continuously attempt to move on 'x' axis
        bot.move()
        self.assertEqual(report_from_valid_move_x, bot.report())
        bot.move()
        bot.move()
        self.assertEqual(report_from_valid_move_x, bot.report())


if __name__ == '__main__':
    unittest.main()
