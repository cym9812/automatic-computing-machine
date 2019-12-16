import wx
import wx.xrc


class Calculator ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"计算器", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.number1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.number1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        operatorChoices = [u"+", u"-", u"*", u"/"]
        self.operator = wx.ComboBox( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, operatorChoices, wx.CB_READONLY )
        self.operator.SetSelection( 0 )
        bSizer2.Add( self.operator, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.number2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.number2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.compute = wx.Button( self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.compute, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.result = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
        bSizer2.Add( self.result, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        self.compute.Bind(wx.EVT_BUTTON, self.compute_result)

    def __del__( self ):
        pass

    def compute_result(self, event):
        if self.operator.GetValue() == "+":
            self.result.SetValue(str(int(self.number1.GetValue()) + int(self.number2.GetValue())))
        elif self.operator.GetValue() == "-":
            self.result.SetValue(str(int(self.number1.GetValue()) - int(self.number2.GetValue())))
        elif self.operator.GetValue() == "*":
            self.result.SetValue(str(int(self.number1.GetValue()) * int(self.number2.GetValue())))
        else:
            self.result.SetValue(str(int(self.number1.GetValue()) / int(self.number2.GetValue())))


if __name__ == '__main__':
    app = wx.App()
    frame = Calculator(None)
    frame.Show(True)
    app.MainLoop()
