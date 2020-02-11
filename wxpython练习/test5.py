import wx
import wx.xrc
import wx.grid

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_grid1 = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 5, 5 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelSize( 30 )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelSize( 80 )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        gbSizer2.Add( self.m_grid1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        m_checkList1Choices = []
        self.m_checkList1 = wx.CheckListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0 )
        gbSizer2.Add( self.m_checkList1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_button1, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.m_panel1.SetSizer( gbSizer2 )
        self.m_panel1.Layout()
        gbSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu2 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem1 )

        self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem2 )

        self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem3 )

        self.m_menubar1.Append( self.m_menu2, u"MyMenu" )

        self.m_menu3 = wx.Menu()
        self.m_menuItem4 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem4 )

        self.m_menuItem5 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem5 )

        self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem6 )

        self.m_menubar1.Append( self.m_menu3, u"MyMenu" )

        self.m_menu4 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.Append( self.m_menuItem7 )

        self.m_menuItem8 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.Append( self.m_menuItem8 )

        self.m_menuItem9 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.Append( self.m_menuItem9 )

        self.m_menubar1.Append( self.m_menu4, u"MyMenu" )

        self.m_menu5 = wx.Menu()
        self.m_menuItem10 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu5.Append( self.m_menuItem10 )

        self.m_menuItem11 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu5.Append( self.m_menuItem11 )

        self.m_menuItem12 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu5.Append( self.m_menuItem12 )

        self.m_menubar1.Append( self.m_menu5, u"MyMenu" )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName("123")
        self.Frame = MyFrame1(None)
        self.Frame.Show()
        return True

if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()