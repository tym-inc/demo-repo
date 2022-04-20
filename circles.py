import numpy as np
from js import webgraphics

async def main():
    webgraphics.create_canvas(600, 600)
    for i in range(7):
        print(i)
        x = np.random.uniform(0, 600)
        y = np.random.uniform(0, 600)
        webgraphics.draw_circle(50, x, y)
        await webgraphics.pause(200)
    
    
if __name__ == '__main__':
    await main()
