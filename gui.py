de 0.6.8 on Tue Apr 7 14:56:26 2015
#
import wx
import subprocess
# begin wxGlade: dependencies
import gettext
# end wxGlade
# begin wxGlade: extracode
# end wxGlade
class MyFrame(wx.Frame):
def __init__(self, *args, **kwds):
# begin wxGlade: MyFrame.__init__
kwds["style"] = wx.DEFAULT_FRAME_STYLE
wx.Frame.__init__(self, *args, **kwds)
self.button_1 = wx.Button(self, wx.ID_ANY, _("Start"))
self.button_2 = wx.Button(self, wx.ID_ANY, _("Stop"))
self.button_3 = wx.Button(self, wx.ID_ANY, _("Restart"))
self.button_4 = wx.Button(self, wx.ID_ANY, _("button_4"))
self.label_1 = wx.StaticText(self, wx.ID_ANY, _("label_1"))
self.__set_properties()
self.__do_layout()
self.Bind(wx.EVT_BUTTON, self.ButtonStart, self.button_1)
self.Bind(wx.EVT_BUTTON, self.ButtonStop, self.button_2)
self.Bind(wx.EVT_BUTTON, self.RestartButton, self.button_3)
# end wxGlade
def __set_properties(self):
# begin wxGlade: MyFrame.__set_properties
self.SetTitle(_("frame_1"))
self.label_1.SetFont(wx.Font(19, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Cantarell"))
# end wxGlade
def __do_layout(self):
# begin wxGlade: MyFrame.__do_layout
sizer_1 = wx.BoxSizer(wx.VERTICAL)
sizer_1.Add(self.button_1, 0, 0, 0)
sizer_1.Add(self.button_2, 0, 0, 0)
sizer_1.Add(self.button_3, 0, 0, 0)
sizer_1.Add(self.button_4, 0, 0, 0)
sizer_1.Add(self.label_1, 0, 0, 0)
self.SetSizer(sizer_1)
sizer_1.Fit(self)
self.Layout()
# end wxGlade
def ButtonStart(self, event): # wxGlade: MyFrame.<event_handler>
self.label_1.SetLabel("Test")
def ButtonStop(self, event): # wxGlade: MyFrame.<event_handler>
event.Skip()
def RestartButton(self, event): # wxGlade: MyFrame.<event_handler>
event.Skip()
# end of class MyFrame
if __name__ == "__main__":
gettext.install("app") # replace with the appropriate catalog name
app = wx.PySimpleApp(0)
wx.InitAllImageHandlers()
frame_1 = MyFrame(None, wx.ID_ANY, "")
app.SetTopWindow(frame_1)
frame_1.Show()
app.MainLoop()
