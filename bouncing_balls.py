import numpy as np
from js import webgraphics
import json

async def main():
    webgraphics.create_canvas(600, 600)
    balls = []
    for i in range(1000):
        balls.append(Ball())
    while True:
        circles = []
        for ball in balls:
            ball.update()
            ball.draw(circles)
        webgraphics.draw_many_circles(json.dumps(circles))
        await webgraphics.pause(20)
        
class Ball:
    def __init__(self):
        self.x = np.random.uniform(0, 600)
        self.y = np.random.uniform(0, 600)
        self.dx = np.random.uniform(3,10)
        self.dy = np.random.uniform(3,10)
        
    def update(self):
        if self.x < 0 or self.x > 600:
            self.dx *= -1
        if self.y < 0 or self.y > 600:
            self.dy *= -1
        
        self.x += self.dx
        self.y += self.dy
        
    def draw(self, circles):
        circles.append((5, self.x, self.y))
    
    
if __name__ == '__main__':
    await main()
