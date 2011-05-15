#encoding=gbk
import Server
import wx

__author__ = 'czy-thinkpad'

class UcoolFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, style=wx.MINIMIZE_BOX|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.CAPTION,
                          title=title, size=(500,100))
        # 创建一个面板用于放控件
        panel = wx.Panel(self, -1)

        wx.StaticText(panel, -1, "选择代理目录:", (10, 15))

        # 目录选择按钮
        self.txtDirSelect = wx.StaticText(panel, -1, "...", (100, 10), size=(200,20), style=wx.ST_NO_AUTORESIZE)
        self.txtDirSelect.SetBackgroundColour('white')

        self.txtServiceStatus = wx.StaticText(panel, -1, "代理服务未启动", (100, 45))
        self.txtServiceStatus.SetForegroundColour('red')

        btnDirSelect = wx.Button(panel, -1, "浏览", pos = (400,10))

        self.btnServerToggle = wx.ToggleButton(panel, -1, "开启代理", pos = (10, 40))

        #bind event
        self.Bind(wx.EVT_BUTTON, self.onDirSelected, btnDirSelect)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.onPortChange, self.btnServerToggle)

        self.Show(True)

    def onDirSelected(self, event):
        dialog = wx.DirDialog(None,"Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.txtDirSelect.SetLabel(dialog.GetPath())
            self.txtDirSelect.SetToolTipString(dialog.GetPath())
        dialog.Destroy()

    # 服务端口切换
    def onPortChange(self, event):
        if self.btnServerToggle.GetValue():
            self.txtServiceStatus.SetForegroundColour('blue')
            self.txtServiceStatus.SetLabel("代理服务已经启动")
            self.btnServerToggle.SetLabel("关闭代理")
        else:
            self.txtServiceStatus.SetForegroundColour('red')
            self.txtServiceStatus.SetLabel("代理服务未启动")
            self.btnServerToggle.SetLabel("开启代理")
        
class UI:
    # ui初始化
    def __init__(self):
        app = wx.App(False)
        UcoolFrame(None, "Ucool 2 You")
        app.MainLoop()
