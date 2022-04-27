#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
from datetime import datetime
from MetroTransitAPI import getAPI, updateList, getTimes, Stops

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("fonts/5x7.bdf")
        largefont = graphics.Font()
        largefont.LoadFont("fonts/6x9.bdf")
        textColor = graphics.Color(255,0,0)
        pos = offscreen_canvas.width
        
        response = getAPI(Stops)
        updatedList = updateList(response)
        times = getTimes(updatedList)         
        
        while True:
            rawTime = datetime.now()
            currentTime = rawTime.strftime('%I:%M %p')
            offscreen_canvas.Clear()

            graphics.DrawText(offscreen_canvas, font, pos, 7, textColor, 'LAKE/LYNDALE')
            graphics.DrawText(offscreen_canvas, font, pos + 11, 15, textColor, 'UPCOMING')
            graphics.DrawText(offscreen_canvas, font, pos + 18, 23, textColor, 'BUSES')
            graphics.DrawText(offscreen_canvas, font, pos + 10, 31, textColor, str(currentTime))
            
            graphics.DrawText(offscreen_canvas, font,  pos + 126 - (len(times[1][0])*5), 7, textColor, times[1][0])
            graphics.DrawText(offscreen_canvas, font,  pos + 126 - (len(times[1][1])*5), 15, textColor, times[1][1])
            graphics.DrawText(offscreen_canvas, font,  pos + 126 - (len(times[1][2])*5), 23, textColor, times[1][2])
            graphics.DrawText(offscreen_canvas, font,  pos + 126 - (len(times[1][3])*5), 31, textColor, times[1][3])

            graphics.DrawText(offscreen_canvas, largefont, pos + 63, 7, textColor, times[0][0])
            graphics.DrawText(offscreen_canvas, largefont, pos + 63, 15, textColor, times[0][1])
            graphics.DrawText(offscreen_canvas, largefont, pos + 63, 23, textColor, times[0][2])
            graphics.DrawText(offscreen_canvas, largefont, pos + 63, 31, textColor, times[0][3])
            
            graphics.DrawText(offscreen_canvas, font, pos + 128, 7, textColor, 'LAKE/LYNDALE')
            graphics.DrawText(offscreen_canvas, font, pos + 128 + 10, 15, textColor, 'UPCOMING')
            graphics.DrawText(offscreen_canvas, font, pos + 128 + 18, 23, textColor, 'BUSES')
            graphics.DrawText(offscreen_canvas, font, pos + 128 +10, 31, textColor, str(currentTime))


            pos -=1      
            if (pos == 0):
                time.sleep(4)
            elif (pos == -64):
                time.sleep(55)                
            elif (pos == -128):
                time.sleep(4)
                response = getAPI(Stops)
                updatedList = updateList(response)
                times = getTimes(updatedList) 
                pos = offscreen_canvas.width - 64
            time.sleep(0.03)
            
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

        
   

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
        
        

