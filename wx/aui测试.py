# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow( self )
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        self.m_mgr.AddPane( self.m_panel2, wx.aui.AuiPaneInfo() .Top() .MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 819,499 ) ).Row( 0 ).Position( 1 ).BestSize( wx.Size( 300,200 ) ).Layer( 1 ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel3 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,50 ), wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl1 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button2 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button3 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_button4 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )


        self.m_panel3.SetSizer( bSizer2 )
        self.m_panel3.Layout()
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.m_panel4.SetSizer( bSizer3 )
        self.m_panel4.Layout()
        bSizer3.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl3 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.m_panel5.SetSizer( bSizer4 )
        self.m_panel5.Layout()
        bSizer4.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel2.SetSizer( bSizer1 )
        self.m_panel2.Layout()
        bSizer1.Fit( self.m_panel2 )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )

        self.m_menu1.AppendSeparator()

        self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem3 )

        self.m_menubar1.Append( self.m_menu1, u"MyMenu" )

        self.m_menu2 = wx.Menu()
        self.m_menuItem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem6 )

        self.m_menuItem7 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem7 )

        self.m_menubar1.Append( self.m_menu2, u"MyMenu" )

        self.SetMenuBar( self.m_menubar1 )

        self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.m_mgr.Update()
        self.Centre( wx.BOTH )

    def __del__( self ):
        self.m_mgr.UnInit()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show(True)
    app.MainLoop()
