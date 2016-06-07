# coding: utf-8
import wx

class MyDialog(wx.Frame):

    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        panel=wx.Panel(self,-1,size=(300,250))
        wx.Button(panel,201,u'打开',pos=(70,100))
        self.Centre()

        wx.EVT_BUTTON(self,201,self.onOpen)

    def onOpen(self,event):
        dlg=wx.MessageDialog(None,u'你好，加油！',u'对话框',wx.YES_NO|wx.ICON_QUESTION)
        res=dlg.ShowModal()
        dlg.Destroy()

if __name__=='__main__':
    app=wx.App()
    frame=MyDialog(None,-1,u'对话框示例1')
    frame.Show()
    app.MainLoop()
