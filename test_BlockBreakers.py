import unittest
import pygame
from BlockBreakers import paddle, ball, block_list, detect_collision

class TestBlockBreaker(unittest.TestCase):

    def test_paddle_movement(self):
        paddle.left = 300  
        paddle.right = 500
        self.assertEqual(paddle.left, 300)
        self.assertEqual(paddle.right, 500)
        
        paddle.left -= 10
        paddle.right += 10
        self.assertEqual(paddle.left, 290)
        self.assertEqual(paddle.right, 510)

    def test_collision_detection(self):
        ball.x = 400
        ball.y = 300
        dx, dy = 1, -1
        
        paddle.left = 380
        paddle.right = 580
        paddle.top = 580
        paddle.bottom = 600

        dx, dy = detect_collision(dx, dy, ball, paddle)

        self.assertEqual(dx, -1)
        self.assertEqual(dy, 1)

    def test_blocks(self):
        self.assertEqual(len(block_list), 40)
            
        block = block_list[0]
        index = ball.collidelist(block_list)
        self.assertEqual(index, 0)
            
        block_list.pop(0)
        self.assertEqual(len(block_list), 39)

if __name__ == '__main__':
    unittest.main()