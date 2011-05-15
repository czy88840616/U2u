#fileencoding=gbk
import os

__author__ = 'czy-thinkpad'
import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,500))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

#        create a statusbar
        self.CreateStatusBar()

        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&打开", " open a file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " info about this")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " exit")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)


        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []

        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &" + str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        self.Show(True)

    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)

        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self, e):
        self.Close(True)  # Close the frame.

    def OnOpen(self, e):
        """open a file"""
        self.dirname = ""
        dlg = wx.FileDialog(self, "choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MyFrame(None, "Hello world")
app.MainLoop()
