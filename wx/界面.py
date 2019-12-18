# -*- coding: utf-8 -*-
import random
import sys
import time
import threading
import multiprocessing as mp
import wx
import wx.grid
import wx.xrc


class Mainframe(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            1280, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.Colour(224, 224, 224))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        basic_info = wx.StaticBoxSizer(wx.StaticBox(
            self.m_panel4, wx.ID_ANY, u"基本信息"), wx.VERTICAL)

        self.m_panel15 = wx.Panel(basic_info.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText31 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)

        gbSizer4.Add(self.m_staticText31, wx.GBPosition(0, 0), wx.GBSpan(
            1, 1), wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 50)

        self.m_textCtrl27 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl27, wx.GBPosition(0, 1),
                     wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText311 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText311.Wrap(-1)

        gbSizer4.Add(self.m_staticText311, wx.GBPosition(0, 2),
                     wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 50)

        self.m_textCtrl271 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl271, wx.GBPosition(
            0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText3111 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3111.Wrap(-1)

        gbSizer4.Add(self.m_staticText3111, wx.GBPosition(0, 4),
                     wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 50)

        self.m_textCtrl2711 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl2711, wx.GBPosition(
            0, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText31111 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31111.Wrap(-1)

        gbSizer4.Add(self.m_staticText31111, wx.GBPosition(0, 6),
                     wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 50)

        self.m_textCtrl27111 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl27111, wx.GBPosition(
            0, 7), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText44 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText44.Wrap(-1)

        gbSizer4.Add(self.m_staticText44, wx.GBPosition(1, 0), wx.GBSpan(
            1, 1), wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 50)

        self.m_textCtrl43 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl43, wx.GBPosition(
            1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText45 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText45.Wrap(-1)

        gbSizer4.Add(self.m_staticText45, wx.GBPosition(1, 2),
                     wx.GBSpan(1, 1), wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl44 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl44, wx.GBPosition(
            1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText46 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText46.Wrap(-1)

        gbSizer4.Add(self.m_staticText46, wx.GBPosition(1, 4),
                     wx.GBSpan(1, 1), wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl45 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl45, wx.GBPosition(
            1, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText47 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText47.Wrap(-1)

        gbSizer4.Add(self.m_staticText47, wx.GBPosition(1, 6),
                     wx.GBSpan(1, 1), wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl46 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl46, wx.GBPosition(
            1, 7), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText48 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText48.Wrap(-1)

        gbSizer4.Add(self.m_staticText48, wx.GBPosition(2, 0),
                     wx.GBSpan(1, 1), wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl48 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl48, wx.GBPosition(
            2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText49 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText49.Wrap(-1)

        gbSizer4.Add(self.m_staticText49, wx.GBPosition(2, 2),
                     wx.GBSpan(1, 1), wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl49 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl49, wx.GBPosition(
            2, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText50 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText50.Wrap(-1)

        gbSizer4.Add(self.m_staticText50, wx.GBPosition(2, 4),
                     wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        self.m_textCtrl50 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl50, wx.GBPosition(
            2, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText51 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)

        gbSizer4.Add(self.m_staticText51, wx.GBPosition(2, 6),
                     wx.GBSpan(1, 1), wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl51 = wx.TextCtrl(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        gbSizer4.Add(self.m_textCtrl51, wx.GBPosition(
            2, 7), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_panel15.SetSizer(gbSizer4)
        self.m_panel15.Layout()
        gbSizer4.Fit(self.m_panel15)
        basic_info.Add(self.m_panel15, 0, wx.EXPAND | wx.RIGHT, 5)

        self.m_panel4.SetSizer(basic_info)
        self.m_panel4.Layout()
        basic_info.Fit(self.m_panel4)
        bSizer1.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel5 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        test_stat = wx.StaticBoxSizer(wx.StaticBox(
            self.m_panel5, wx.ID_ANY, u"测试状态"), wx.VERTICAL)

        self.m_textCtrl20 = wx.TextCtrl(test_stat.GetStaticBox(
        ), wx.ID_ANY, u"未开始", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER | wx.TE_READONLY)
        test_stat.Add(self.m_textCtrl20, 0, wx.ALL |
                      wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel5.SetSizer(test_stat)
        self.m_panel5.Layout()
        test_stat.Fit(self.m_panel5)
        bSizer1.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel6 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        test_data = wx.StaticBoxSizer(wx.StaticBox(
            self.m_panel6, wx.ID_ANY, u"测试数据"), wx.VERTICAL)

        self.m_grid2 = wx.grid.Grid(test_data.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 120), 0)

        # Grid
        self.m_grid2.CreateGrid(20, 9)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid2.AutoSizeRows()
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        test_data.Add(self.m_grid2, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_panel6.SetSizer(test_data)
        self.m_panel6.Layout()
        test_data.Fit(self.m_panel6)
        bSizer1.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel7 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        operation = wx.StaticBoxSizer(wx.StaticBox(
            self.m_panel7, wx.ID_ANY, u"操作"), wx.VERTICAL)

        gSizer4 = wx.GridSizer(0, 3, 0, 0)

        self.button_start = wx.Button(operation.GetStaticBox(
        ), wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.button_start, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL |
                    wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.button_stop = wx.Button(operation.GetStaticBox(
        ), wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.button_stop, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL |
                    wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.button_quit = wx.Button(operation.GetStaticBox(
        ), wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.button_quit, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL |
                    wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        operation.Add(gSizer4, 1, wx.EXPAND, 5)

        self.m_panel7.SetSizer(operation)
        self.m_panel7.Layout()
        operation.Fit(self.m_panel7)
        bSizer1.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel8 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        test_cue = wx.StaticBoxSizer(wx.StaticBox(
            self.m_panel8, wx.ID_ANY, u"操作提示"), wx.VERTICAL)

        self.m_textCtrl52 = wx.TextCtrl(test_cue.GetStaticBox(
        ), wx.ID_ANY, u"确定产品信息无误后点击开始来进行测试", wx.DefaultPosition, wx.Size(-1, 120), wx.TE_READONLY)
        self.m_textCtrl52.SetMaxLength(0)
        self.m_textCtrl52.SetFont(wx.Font(
            30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        test_cue.Add(self.m_textCtrl52, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel8.SetSizer(test_cue)
        self.m_panel8.Layout()
        test_cue.Fit(self.m_panel8)
        bSizer1.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel9 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        test_detail = wx.StaticBoxSizer(wx.StaticBox(
            self.m_panel9, wx.ID_ANY, u"测试列状态"), wx.VERTICAL)

        self.gauge = wx.Gauge(test_detail.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize,
                              wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.gauge.SetValue(0)
        test_detail.Add(self.gauge, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel9.SetSizer(test_detail)
        self.m_panel9.Layout()
        test_detail.Fit(self.m_panel9)
        bSizer1.Add(self.m_panel9, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel10 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        connect_stat = wx.StaticBoxSizer(wx.StaticBox(
            self.m_panel10, wx.ID_ANY, u"通讯状态"), wx.VERTICAL)

        self.m_textCtrl53 = wx.TextCtrl(connect_stat.GetStaticBox(
        ), wx.ID_ANY, u"串口通讯正常", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        self.m_textCtrl53.SetBackgroundColour(wx.Colour(0, 255, 0))

        connect_stat.Add(self.m_textCtrl53, 0, wx.ALL |
                         wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel10.SetSizer(connect_stat)
        self.m_panel10.Layout()
        connect_stat.Fit(self.m_panel10)
        bSizer1.Add(self.m_panel10, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        self.count = 0

        # Connect Events
        self.button_start.Bind(wx.EVT_LEFT_DOWN, self.start_test)
        self.button_stop.Bind(wx.EVT_LEFT_DOWN, self.stop_test)
        self.button_quit.Bind(wx.EVT_LEFT_DOWN, self.quit_test)
        self.t = threading.Thread
        self.control_queue = mp.Queue()

    def __del__(self):
        pass

    def update_gauge(self, cq):
        q = mp.Queue()
        t = threading.Thread(target=timer, args=(q, cq))
        t.start()
        temp = 0
        while temp != "finish" and cq.empty():
            self.gauge.SetValue(temp)
            temp = q.get()
        self.m_textCtrl20.SetLabel("已完成")
        self.m_textCtrl20.SetBackgroundColour(wx.Colour(0, 255, 0))

    # Virtual event handlers, overide them in your derived class
    def start_test(self, event):
        while not self.control_queue.empty():       # 清空
            self.control_queue.get()
        self.m_textCtrl20.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.m_textCtrl20.SetLabel("进行中")
        self.t = threading.Thread(target=self.update_gauge, args=(self.control_queue,))
        self.t.start()

        '''
        self.gauge.SetValue(100)
        self.m_textCtrl20.SetBackgroundColour(wx.Colour(0, 255, 0))
        self.m_textCtrl20.SetLabel("进行中")
        '''

    def stop_test(self, event):
        self.control_queue.put("stop")
        self.gauge.SetValue(0)
        self.m_textCtrl20.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.m_textCtrl20.SetLabel("未开始")

    def quit_test(self, event):
        sys.exit(0)


def timer(q, cq):
    count = 0
    while count < 100 and cq.empty():
        count += random.randrange(1, 31)
        if count > 100:
            count = 100
        print(count)
        q.put(count)
        time.sleep(1)
    q.put("finish")


if __name__ == '__main__':
    app = wx.App()
    frame = Mainframe(None)
    frame.Show(True)
    app.MainLoop()
