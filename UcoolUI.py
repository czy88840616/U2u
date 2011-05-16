#encoding=gbk
import SimpleHTTPServer
import SocketServer
import os
import subprocess
import sys
import thread
import threading
import Server
import wx

__author__ = 'czy-thinkpad'
PORT = 8800

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
    def run(self):
        pass
    def stop(self):
        self.thread_stop = True

class PortHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def setWEBROOT(WEBROOT):
        PortHandler.WEBROOT = WEBROOT
    setWEBROOT = staticmethod(setWEBROOT)
    
    def translate_path(self, path):
        os.chdir(PortHandler.WEBROOT)
        return SimpleHTTPServer.SimpleHTTPRequestHandler.translate_path(self, path)

class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.icon = self.MakeIcon(wx.Image(("u2u.png"), wx.BITMAP_TYPE_PNG))
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_TASKBAR_RIGHT_DOWN, self.OnContextMenu)
        
    def MakeIcon(self, img):
        img = img.Scale(16, 16)
        icon = wx.IconFromBitmap(img.ConvertToBitmap() )
        return icon

    def OnLeftDown(self, event):
        self.frame.Show(True)
        self.RemoveIcon()

    def OnRightDown(self, event):
        self.Destroy()
        self.frame.Destroy()

    def OnContextMenu(self, event):
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.Bind(wx.EVT_MENU, self.OnRightDown, id=self.popupID1)
        menu = wx.Menu()
        item = wx.MenuItem(menu, self.popupID1, "�˳�")
        menu.AppendItem(item)
        self.frame.PopupMenu(menu)
        menu.Destroy()

    def Set(self):
        self.SetIcon(self.icon, 'Ucool 2 You')
        
class UcoolFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, style=wx.MINIMIZE_BOX|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.CAPTION,
                          title=title, size=(400,100))
        # ����һ��������ڷſؼ�
        panel = wx.Panel(self, -1)

        wx.StaticText(panel, -1, "ѡ�����Ŀ¼:", (10, 15))

        # Ŀ¼ѡ��ť
        self.txtDirSelect = wx.StaticText(panel, -1, "...", (100, 10), size=(200,20), style=wx.ST_NO_AUTORESIZE)
        self.txtDirSelect.SetBackgroundColour('white')

        self.txtServiceStatus = wx.StaticText(panel, -1, "�������δ����", (100, 45))
        self.txtServiceStatus.SetForegroundColour('red')

        btnDirSelect = wx.Button(panel, -1, "���", pos = (310,8))

        self.btnServerToggle = wx.ToggleButton(panel, -1, "��������", pos = (10, 40))

        #bind event
        self.Bind(wx.EVT_BUTTON, self.onDirSelected, btnDirSelect)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.onPortChange, self.btnServerToggle)

        # tray icon
        self.trayIcon = TaskBarIcon(self)
        self.Bind(wx.EVT_ICONIZE, self.onTaskBar)

        self.Show(True)

    def onDirSelected(self, event):
        dialog = wx.DirDialog(None,"Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            if len(dialog.GetPath()) > 15:
                self.txtDirSelect.SetLabel(dialog.GetPath()[:20] + '...')
            else:
                self.txtDirSelect.SetLabel(dialog.GetPath()[:20])
            self.txtDirSelect.SetToolTipString(dialog.GetPath())
            self.PROXYPATH = dialog.GetPath()
        dialog.Destroy()

    # ����˿��л�
    def onPortChange(self, event):
        if not hasattr(self, 'PROXYPATH'):
            dlg = wx.MessageDialog(self, '��ѡ��һ��Ŀ¼��', style=wx.OK)
            dlg.ShowModal()
            return
        if self.btnServerToggle.GetValue():
            # ������һ���߳��ܶ˿�
            self.serverChange(True)
            self.txtServiceStatus.SetForegroundColour('LIME GREEN')
            self.txtServiceStatus.SetLabel("��������Ѿ�����")
            self.btnServerToggle.SetLabel("�رմ���")
        else:
            self.serverChange(False)
            self.txtServiceStatus.SetForegroundColour('red')
            self.txtServiceStatus.SetLabel("�������δ����")
            self.btnServerToggle.SetLabel("��������")

    def serverChange(self, open):
        if open:
            self.p = subprocess.Popen('python Server.py ' + self.PROXYPATH)
        else:
            try:
                self.p.terminate()
            except:
                print 'over'
            finally:
                self.p.kill()

    def serverStart(self, WEBROOT):
        PortHandler.setWEBROOT(WEBROOT)
        httpd = SocketServer.TCPServer(("", PORT), PortHandler)
        httpd.serve_forever()

    def onTaskBar(self, event):
        self.Show(False)
        self.trayIcon.Set()
class UI:
    # ui��ʼ��
    def __init__(self):
        app = wx.App(False)
        UcoolFrame(None, "Ucool 2 You")
        app.MainLoop()
