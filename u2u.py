#encoding=gbk
import subprocess
import wx

class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.icon = self.MakeIcon(wx.Image(("u2u.png"), wx.BITMAP_TYPE_PNG))
#        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_TASKBAR_RIGHT_DOWN, self.OnContextMenu)
    def MakeIcon(self, img):
        img = img.Scale(16, 16)
        icon = wx.IconFromBitmap(img.ConvertToBitmap() )
        return icon
    
#    def OnLeftDown(self, event):
#        self.frame.Show()
#        self.RemoveIcon()
        
    def OnRightDown(self, event):
#        self.Destroy()
        self.frame.Close()
        
    def OnContextMenu(self, event):
        if not hasattr(self, "popExit"):
            self.popExit = wx.NewId()
            self.popSelectDir = wx.NewId()
            self.popStartServer = wx.NewId()
            self.popStopServer = wx.NewId()
            self.popHelp = wx.NewId()

            self.Bind(wx.EVT_MENU, self.onExit, id=self.popExit)
            self.Bind(wx.EVT_MENU, self.onDirSelected, id=self.popSelectDir)
            self.Bind(wx.EVT_MENU, self.serverStart, id=self.popStartServer)
            self.Bind(wx.EVT_MENU, self.serverStop, id=self.popStopServer)
            self.Bind(wx.EVT_MENU, self.HelpText, id=self.popHelp)

            # make a menu
            self.menu = menu = wx.Menu()
            # add some other items
            menu.AppendCheckItem(self.popSelectDir, '&Choose proxy directory')

            menu.AppendSeparator()
            menu.Append(self.popStartServer, "&Start proxy")
            mnuStop = wx.MenuItem(menu, self.popStopServer, '&Close proxy')
            mnuStop.Enable(False)
            menu.AppendItem(mnuStop)
            menu.AppendSeparator()

            menu.Append(self.popHelp, "&Help")
            menu.Append(self.popExit, "&Exit")

            # will be called before PopupMenu returns.
        self.PopupMenu(self.menu)
#        menu.Destroy()

    def Set(self):
        self.SetIcon(self.icon, 'ucool local tool for you')

    def onExit(self, event):
        self.RemoveIcon()
        self.Destroy()
        wx.App.ExitMainLoop(app)

    def onDirSelected(self, event):
        dialog = wx.DirDialog(self.frame, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.PROXYPATH = dialog.GetPath()
            self.menu.Check(self.popSelectDir, True)
        dialog.Destroy()

    def serverStart(self, event):
        if not hasattr(self, 'PROXYPATH'):
            dlg = wx.MessageDialog(self.frame, 'please select a directory first', style=wx.OK)
            dlg.ShowModal()
            return
        self.p = subprocess.Popen('python Server.py ' + self.PROXYPATH)
        self.menu.FindItemById(self.popStartServer).Enable(False)
        self.menu.FindItemById(self.popStopServer).Enable(True)

    def serverStop(self, event):
        try:
            self.p.terminate()
        except:
            print 'over'
        finally:
            self.p.kill()
        self.menu.FindItemById(self.popStartServer).Enable(True)
        self.menu.FindItemById(self.popStopServer).Enable(False)

    def HelpText(self, event):
        txtHelp = \
        'How to use？\n\
        1、choose a directory you want to proxy\n\
        2、start the service\n\
        3、please stop service when you want to switch directory\n\
        4、enjoy it and report bug\n'
        dlg=wx.MessageDialog(self.frame, txtHelp, "Help", style = wx.OK)
        dlg.ShowModal()
    
class UcoolFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size = (0, 0),
                              style= wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU)
        self.tbicon = TaskBarIcon(self)

        self.Show(False)
        self.tbicon.Set()

app = wx.App(False)
uFrame = UcoolFrame(None, "Ucool 2 You")
app.MainLoop()