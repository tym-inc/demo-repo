from js import webgraphics

async def main():
    webgraphics.create_canvas(600, 600)
    while True:
        x = webgraphics.get_mouse_x()
        y = webgraphics.get_mouse_y()
        webgraphics.draw_circle(10, x, y)
        await webgraphics.pause(50)
    
    
if __name__ == '__main__':
    await main()