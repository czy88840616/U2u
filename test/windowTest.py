'''file doc string'''

import wx

class Frame(wx.Frame):
    def __init__(self, image):
        temp = image.ConvertToBitmap()
        size = image.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self, None, -1, "hello world", wx.DefaultPosition, size)
        self.bmp = wx.StaticBitmap(parent=self,bitmap=temp )


class App(wx.App):
    def OnInit(self):
        image = wx.Image("test.jpg", wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = App()
    app.MainLoop()
    
if __name__ == '__main__':
    main()