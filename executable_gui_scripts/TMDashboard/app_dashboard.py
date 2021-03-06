# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import module_analytics as anal
import module_splanner as sp
import module_reporter as rp
import module_talentdocs as td

thispath = os.path.dirname(os.path.realpath(__file__))
###########################################################################
# Class dashboardFrame
###########################################################################


class dashboardFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"TM: TOTAL Dashboard",
                          pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL,
                             wx.FONTWEIGHT_NORMAL, False, "Museo 500"))
        self.SetBackgroundColour(wx.Colour(0, 177, 169))

        mainsizer = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self, wx.ID_ANY, u"TOTAL Dashboard",
                                   wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.title.Wrap(-1)

        self.title.SetFont(wx.Font(14, wx.FONTFAMILY_MODERN,
                                   wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Museo 500"))
        self.title.SetForegroundColour(wx.Colour(255, 255, 255))

        mainsizer.Add(self.title, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        gridSizer = wx.GridSizer(0, 2, 0, 0)

        bsizer1 = wx.BoxSizer(wx.VERTICAL)

        self.title_analytics = wx.StaticText(
            self, wx.ID_ANY, u"Talent Analytics", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.title_analytics.Wrap(-1)

        bsizer1.Add(self.title_analytics, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btn_analytics = wx.Button(
            self, wx.ID_ANY, u"Talent Analytics", wx.DefaultPosition, wx.DefaultSize, 0)
        bsizer1.Add(self.btn_analytics, 0, wx.ALL, 5)

        gridSizer.Add(bsizer1, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bsizer2 = wx.BoxSizer(wx.VERTICAL)

        self.title_sp = wx.StaticText(
            self, wx.ID_ANY, u"Succession Planner", wx.DefaultPosition, wx.DefaultSize, 0)
        self.title_sp.Wrap(-1)

        bsizer2.Add(self.title_sp, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btn_splanner = wx.Button(
            self, wx.ID_ANY, u"Succession Planner", wx.DefaultPosition, wx.DefaultSize, 0)
        bsizer2.Add(self.btn_splanner, 0, wx.ALL, 5)

        gridSizer.Add(bsizer2, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bsizer3 = wx.BoxSizer(wx.VERTICAL)

        self.title_reporter = wx.StaticText(
            self, wx.ID_ANY, u"Reporter", wx.DefaultPosition, wx.DefaultSize, 0)
        self.title_reporter.Wrap(-1)

        bsizer3.Add(self.title_reporter, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btn_reporter = wx.Button(
            self, wx.ID_ANY, u"Reporter", wx.DefaultPosition, wx.DefaultSize, 0)
        bsizer3.Add(self.btn_reporter, 0, wx.ALL, 5)

        gridSizer.Add(bsizer3, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bsizer4 = wx.BoxSizer(wx.VERTICAL)

        self.title_talentdoc = wx.StaticText(
            self, wx.ID_ANY, u"TalentDocs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.title_talentdoc.Wrap(-1)

        bsizer4.Add(self.title_talentdoc, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btn_talentdoc = wx.Button(
            self, wx.ID_ANY, u"TalentDocs", wx.DefaultPosition, wx.DefaultSize, 0)
        bsizer4.Add(self.btn_talentdoc, 0, wx.ALL, 5)

        gridSizer.Add(bsizer4, 1, wx.ALIGN_CENTER, 5)

        mainsizer.Add(gridSizer, 1, wx.EXPAND, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"for Top Talent Management, PETRONAS",
                                           wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText7.Wrap(-1)

        self.m_staticText7.SetFont(wx.Font(
            8, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Museo 500"))

        mainsizer.Add(self.m_staticText7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(mainsizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_analytics.Bind(wx.EVT_BUTTON, self.openframe_analytics)
        self.btn_splanner.Bind(wx.EVT_BUTTON, self.openframe_splanner)
        self.btn_reporter.Bind(wx.EVT_BUTTON, self.openframe_reporter)
        self.btn_talentdoc.Bind(wx.EVT_BUTTON, self.openframe_talentdocs)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def openframe_analytics(self, event):
        analytic = analyticsFrame(self)
        analytic.Show()

    def openframe_splanner(self, event):
        splanner = splannerFrame(self)
        splanner.Show()

    def openframe_reporter(self, event):
        reporter = reporterFrame(self)
        reporter.Show()

    def openframe_talentdocs(self, event):
        talentdocs = talentdocsFrame(self)
        talentdocs.Show()


###########################################################################
# Class analyticsFrame
###########################################################################

class analyticsFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"TM: Talent Analytics", pos=wx.DefaultPosition, size=wx.Size(
            500, 448), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL,
                             wx.FONTWEIGHT_NORMAL, False, "Museo 500"))
        self.SetBackgroundColour(wx.Colour(0, 177, 169))

        mainsizer = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self, wx.ID_ANY, u"Talent Analytics",
                                   wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.title.Wrap(-1)

        self.title.SetFont(wx.Font(14, wx.FONTFAMILY_MODERN,
                                   wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Museo 500"))
        self.title.SetForegroundColour(wx.Colour(255, 255, 255))
        self.title.SetBackgroundColour(wx.Colour(0, 177, 169))

        mainsizer.Add(self.title, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ui_sizer = wx.BoxSizer(wx.HORIZONTAL)

        input_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Input"), wx.VERTICAL)

        self.txt_zhpla = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"1. ZHPLA file (.xlsx)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_zhpla.Wrap(-1)

        input_sizer.Add(self.txt_zhpla, 0, wx.ALL, 5)

        self.zhpla_picker = wx.FilePickerCtrl(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        input_sizer.Add(self.zhpla_picker, 0, wx.ALL, 5)

        self.txt_zpdev = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"2. ZPDEV file (.xlsx)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_zpdev.Wrap(-1)

        input_sizer.Add(self.txt_zpdev, 0, wx.ALL, 5)

        self.zpdev_picker = wx.FilePickerCtrl(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        input_sizer.Add(self.zpdev_picker, 0, wx.ALL, 5)

        self.txt_zpdevretire = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"2. ZPDEV Retire file (.xlsx)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_zpdevretire.Wrap(-1)

        input_sizer.Add(self.txt_zpdevretire, 0, wx.ALL, 5)

        self.zpdevretire_picker = wx.FilePickerCtrl(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        input_sizer.Add(self.zpdevretire_picker, 0, wx.ALL, 5)

        ui_sizer.Add(input_sizer, 1, wx.EXPAND, 5)

        process_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Process"), wx.VERTICAL)

        self.rdbtn_cleanonly = wx.RadioButton(process_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Clean Only", wx.DefaultPosition, wx.DefaultSize, 0)
        process_sizer.Add(self.rdbtn_cleanonly, 0, wx.ALL, 5)

        self.rdbtn_combine = wx.RadioButton(process_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Combine Only", wx.DefaultPosition, wx.DefaultSize, 0)
        process_sizer.Add(self.rdbtn_combine, 0, wx.ALL, 5)

        self.rdbtn_cleancombine = wx.RadioButton(process_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Clean + Combine", wx.DefaultPosition, wx.DefaultSize, 0)
        process_sizer.Add(self.rdbtn_cleancombine, 0, wx.ALL, 5)

        self.chbox_autoopen = wx.CheckBox(process_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Open when finished", wx.DefaultPosition, wx.DefaultSize, 0)
        process_sizer.Add(self.chbox_autoopen, 0, wx.ALL, 5)

        self.btn_process = wx.Button(process_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Process Data", wx.DefaultPosition, wx.DefaultSize, 0)
        process_sizer.Add(self.btn_process, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ui_sizer.Add(process_sizer, 1, wx.EXPAND, 5)

        output_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Output"), wx.VERTICAL)

        self.btn_openfolder = wx.Button(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Open Folder", wx.DefaultPosition, wx.DefaultSize, 0)
        output_sizer.Add(self.btn_openfolder, 0, wx.ALL, 5)

        self.btn_openzhpla = wx.Button(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"ZHPLA", wx.DefaultPosition, wx.DefaultSize, 0)
        output_sizer.Add(self.btn_openzhpla, 0, wx.ALL, 5)

        self.btn_openzpdev = wx.Button(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"ZPDEV", wx.DefaultPosition, wx.DefaultSize, 0)
        output_sizer.Add(self.btn_openzpdev, 0, wx.ALL, 5)

        self.btn_openanalytics = wx.Button(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Talent Analytics", wx.DefaultPosition, wx.DefaultSize, 0)
        output_sizer.Add(self.btn_openanalytics, 0, wx.ALL, 5)

        ui_sizer.Add(output_sizer, 1, wx.EXPAND, 5)

        mainsizer.Add(ui_sizer, 1, wx.EXPAND, 5)

        self.txt_message = wx.StaticText(
            self, wx.ID_ANY, u"Welcome to TM Analytics", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_message.Wrap(-1)

        self.txt_message.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        mainsizer.Add(self.txt_message, 0, wx.ALL, 5)

        self.SetSizer(mainsizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_process.Bind(wx.EVT_BUTTON, self.processData)
        self.btn_openfolder.Bind(wx.EVT_BUTTON, self.openFolder)
        self.btn_openzhpla.Bind(wx.EVT_BUTTON, self.openzhpla)
        self.btn_openzpdev.Bind(wx.EVT_BUTTON, self.openzpdev)
        self.btn_openanalytics.Bind(wx.EVT_BUTTON, self.openanalytics)

        # Variables
        self.output_zhpla = ''
        self.output_zpdev = ''
        self.output_analytics = ''
        self.output_folder = ''

        self.btn_openzhpla.Disable()
        self.btn_openzpdev.Disable()
        self.btn_openanalytics.Disable()
        self.btn_openfolder.Disable()

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def disableUI(self):
        self.zhpla_picker.Disable()
        self.zpdev_picker.Disable()
        self.zpdevretire_picker.Disable()
        self.rdbtn_cleanonly.Disable()
        self.rdbtn_combine.Disable()
        self.rdbtn_cleancombine.Disable()
        self.btn_process.Disable()
        self.chbox_autoopen.Disable()

    def enableUI(self):
        self.zhpla_picker.Enable()
        self.zpdev_picker.Enable()
        self.zpdevretire_picker.Enable()
        self.rdbtn_cleanonly.Enable()
        self.rdbtn_combine.Enable()
        self.rdbtn_cleancombine.Enable()
        self.btn_process.Enable()
        self.chbox_autoopen.Enable()

    def processData(self, event):
        try:
            self.disableUI()
            self.txt_message.SetLabelText('Running processes...')
            zhplapath = self.zhpla_picker.GetPath()
            zpdevpath = self.zpdev_picker.GetPath()
            zpdev_retirepath = self.zpdevretire_picker.GetPath()

            if self.rdbtn_cleanonly.GetValue():
                operation_type = 1
            elif self.rdbtn_combine.GetValue():
                operation_type = 2
            elif self.rdbtn_cleancombine.GetValue():
                operation_type = 3

            data_dict, operation_type = anal.preProcess(
                zhplapath, zpdevpath, zpdev_retirepath, operation_type)
            df_dictionary, logString = anal.mainProcess(
                data_dict, operation_type)

            for key, value in df_dictionary.items():
                outputfile = os.path.join(
                    thispath, (key + anal.current_month).upper() + '.xlsx')
                print(outputfile)

                self.output_zhpla = outputfile if key == 'zhpla' else ''
                self.output_zpdev = outputfile if key == 'zpdev' else ''
                self.output_analytics = outputfile if key == 'analytics' else ''

                value.to_excel(outputfile, index=None)
                if self.chbox_autoopen.GetValue():
                    os.startfile(outputfile)

            self.enableOutputButton(df_dictionary)
        except Exception as e:
            print('Process failed:', e)
        finally:
            self.enableUI()
            self.txt_message.SetLabelText(logString)

    def enableOutputButton(self, df_dictionary):
        self.btn_openfolder.Enable()
        if 'zhpla' in df_dictionary:
            self.btn_openzhpla.Enable()
        if 'zpdev' in df_dictionary:
            self.btn_openzpdev.Enable()
        if 'analytics' in df_dictionary:
            self.btn_openanalytics.Enable()

    def openFolder(self, event):
        os.startfile(thispath)

    def openzhpla(self, event):
        os.startfile(self.output_zhpla)

    def openzpdev(self, event):
        os.startfile(self.output_zpdev)

    def openanalytics(self, event):
        os.startfile(self.output_analytics)


###########################################################################
# Class splannerFrame
###########################################################################

class splannerFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"TM: Succession Planner", pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL,
                             wx.FONTWEIGHT_NORMAL, False, "Museo 500"))
        self.SetBackgroundColour(wx.Colour(0, 177, 169))

        mainsizer = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self, wx.ID_ANY, u"Succession Planner",
                                   wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.title.Wrap(-1)

        self.title.SetFont(wx.Font(14, wx.FONTFAMILY_MODERN,
                                   wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Museo 500"))
        self.title.SetForegroundColour(wx.Colour(255, 255, 255))
        self.title.SetBackgroundColour(wx.Colour(0, 177, 169))

        mainsizer.Add(self.title, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ui_sizer = wx.BoxSizer(wx.HORIZONTAL)

        input_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Input"), wx.VERTICAL)

        self.txt_selectfile = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Select sp file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_selectfile.Wrap(-1)

        input_sizer.Add(self.txt_selectfile, 0, wx.ALL, 5)

        self.sp_picker = wx.FilePickerCtrl(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        input_sizer.Add(self.sp_picker, 0, wx.ALL, 5)

        self.txt_selectmediafolder = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Select media folder (optional)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_selectmediafolder.Wrap(-1)

        input_sizer.Add(self.txt_selectmediafolder, 0, wx.ALL, 5)

        self.mediafolder_picker = wx.DirPickerCtrl(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        input_sizer.Add(self.mediafolder_picker, 0, wx.ALL, 5)

        self.chbox_autoopen = wx.CheckBox(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Open when finished", wx.DefaultPosition, wx.DefaultSize, 0)
        input_sizer.Add(self.chbox_autoopen, 0, wx.ALL, 5)

        self.btn_process = wx.Button(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Generate SP", wx.DefaultPosition, wx.DefaultSize, 0)
        input_sizer.Add(self.btn_process, 0, wx.ALL, 5)

        ui_sizer.Add(input_sizer, 1, wx.EXPAND, 5)

        output_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Output"), wx.VERTICAL)

        self.btn_openfolder = wx.Button(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Open Folder", wx.DefaultPosition, wx.DefaultSize, 0)
        output_sizer.Add(self.btn_openfolder, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ui_sizer.Add(output_sizer, 1, wx.EXPAND, 5)

        mainsizer.Add(ui_sizer, 1, wx.EXPAND, 5)

        self.txt_message = wx.StaticText(
            self, wx.ID_ANY, u"Welcome to Succession Planner", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_message.Wrap(-1)

        self.txt_message.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        mainsizer.Add(self.txt_message, 0, wx.ALL, 5)

        self.SetSizer(mainsizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_process.Bind(wx.EVT_BUTTON, self.process_sp)
        self.btn_openfolder.Bind(wx.EVT_BUTTON, self.openFolder)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def process_sp(self, event):
        sp_path = self.sp_picker.GetPath()
        mediafolder = self.mediafolder_picker.GetPath()
        try:
            if sp_path == '':
                messageString = 'Please select an sp file first'
            else:
                self.txt_message.SetLabelText('Running process...')
                presentation, outputfile = sp.mainProcess(
                    sp_path, mediafolder, thispath)
                print(outputfile)
                if self.chbox_autoopen.GetValue():
                    os.startfile(outputfile)
                messageString = 'SP successfully generated.'
        except Exception as e:
            messageString = 'An error occured: ' + str(e)
        finally:
            self.txt_message.SetLabelText(messageString)

    def openFolder(self, event):
        os.startfile(thispath)


###########################################################################
# Class reporterFrame
###########################################################################

class reporterFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"TM: Talent Reporter", pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL,
                             wx.FONTWEIGHT_NORMAL, False, "Museo 500"))
        self.SetBackgroundColour(wx.Colour(0, 177, 169))

        mainsizer = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self, wx.ID_ANY, u"Talent Reporter",
                                   wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.title.Wrap(-1)

        self.title.SetFont(wx.Font(14, wx.FONTFAMILY_MODERN,
                                   wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Museo 500"))
        self.title.SetForegroundColour(wx.Colour(255, 255, 255))
        self.title.SetBackgroundColour(wx.Colour(0, 177, 169))

        mainsizer.Add(self.title, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ui_sizer = wx.BoxSizer(wx.HORIZONTAL)

        input_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Source file"), wx.VERTICAL)

        self.txt_selectfile = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Select report file (.pdf)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_selectfile.Wrap(-1)

        input_sizer.Add(self.txt_selectfile, 0, wx.ALL, 5)

        self.report_picker = wx.FilePickerCtrl(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        input_sizer.Add(self.report_picker, 0, wx.ALL, 5)

        self.txt_filename = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"filename.pdf", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_filename.Wrap(-1)

        input_sizer.Add(self.txt_filename, 0, wx.ALL, 5)

        self.txt_selectreporttype = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Select report type:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_selectreporttype.Wrap(-1)

        input_sizer.Add(self.txt_selectreporttype, 0, wx.ALL, 5)

        # choice_pdftypeChoices = [u"BePCB", u"CV", u"LC"]
        self.choice_pdftype = wx.Choice(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
        # self.choice_pdftype.SetSelection(0)

        # choice_pdftypeChoices = [u"BePCB", u"CV", u"LC"]
        # self.choice_pdftype = wx.Choice(input_sizer.GetStaticBox(
        # ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_pdftypeChoices, 0)
        # self.choice_pdftype.SetSelection(0)
        input_sizer.Add(self.choice_pdftype, 0, wx.ALL | wx.EXPAND, 5)

        ui_sizer.Add(input_sizer, 1, wx.EXPAND, 5)

        output_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Output"), wx.VERTICAL)

        self.chbox_autoopen = wx.CheckBox(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Auto Open", wx.DefaultPosition, wx.DefaultSize, 0)
        output_sizer.Add(self.chbox_autoopen, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btn_split = wx.Button(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Split", wx.DefaultPosition, wx.DefaultSize, 0)
        output_sizer.Add(self.btn_split, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txt_reportcount = wx.StaticText(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Report count:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_reportcount.Wrap(-1)

        output_sizer.Add(self.txt_reportcount, 0, wx.ALL, 5)

        self.btn_openfolder = wx.Button(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Open folder", wx.DefaultPosition, wx.DefaultSize, 0)
        output_sizer.Add(self.btn_openfolder, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ui_sizer.Add(output_sizer, 1, wx.EXPAND, 5)

        mainsizer.Add(ui_sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.txt_message = wx.StaticText(
            self, wx.ID_ANY, u"Welcome to Reporter", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_message.Wrap(-1)

        self.txt_message.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        mainsizer.Add(self.txt_message, 0, wx.ALL, 5)

        self.SetSizer(mainsizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_split.Bind(wx.EVT_BUTTON, self.splitReport)
        self.btn_openfolder.Bind(wx.EVT_BUTTON, self.openFolder)
        self.report_picker.Bind(wx.EVT_FILEPICKER_CHANGED, self.changefilename)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def disableUI(self):
        self.report_picker.Disable()
        self.choice_pdftype.Disable()
        self.chbox_autoopen.Disable()

    def enableUI(self):
        self.report_picker.Enable()
        self.choice_pdftype.Enable()
        self.chbox_autoopen.Enable()

    def splitReport(self, event):
        inputfile = self.report_picker.GetPath()
        pdftypeindex = self.choice_pdftype.GetSelection()  # return int
        try:
            if not inputfile == '' and not pdftypeindex < 0:
                print('type', pdftypeindex)
                self.disableUI()
                outputlist, outputfolder = rp.mainProcess(
                    inputfile, pdftypeindex, thispath)

                if self.chbox_autoopen.GetValue():
                    os.startfile(outputfolder)

                self.txt_reportcount.SetLabelText(
                    'Report count: {}'.format(str(len(outputlist))))
                messageString = 'Reports successfully generated'
            else:
                messageString = 'Please select a valid file and report type first'
        except Exception as e:
            print(e)
            messageString = 'Error occured: {}'.format(str(e))
        finally:
            self.txt_message.SetLabelText(messageString)
            self.enableUI()

    def openFolder(self, event):
        os.startfile(thispath)

    def setChoiceList(self):
        self.choice_pdftype.Clear()
        self.choice_pdftype.Append(rp.report_typelist)

    def changefilename(self, event):
        filepath = self.report_picker.GetPath()
        if os.path.exists(filepath):
            self.txt_filename.SetLabelText(
                os.path.basename(filepath))

            self.setChoiceList()
        else:
            if filepath == '':
                self.txt_filename.SetLabelText('filename.pdf')
                self.txt_message.SetLabelText('Please select a valid file')
            else:
                self.txt_filename.SetLabelText('?')
                self.txt_message.SetLabelText('Invalid pdf file/path!')
###########################################################################
# Class talentdocsFrame
###########################################################################


class talentdocsFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"TM: TalentDocs", pos=wx.DefaultPosition, size=wx.Size(
            540, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL,
                             wx.FONTWEIGHT_NORMAL, False, "Museo 500"))
        self.SetBackgroundColour(wx.Colour(0, 177, 169))

        mainsizer = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(
            self, wx.ID_ANY, u"TalentDocs", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.title.Wrap(-1)

        self.title.SetFont(wx.Font(
            14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Museo 500"))
        self.title.SetForegroundColour(wx.Colour(255, 255, 255))
        self.title.SetBackgroundColour(wx.Colour(0, 177, 169))

        mainsizer.Add(self.title, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ui_sizer = wx.BoxSizer(wx.HORIZONTAL)

        input_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Input"), wx.VERTICAL)

        self.txt_filepicker = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Select file (.xlsx)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_filepicker.Wrap(-1)

        input_sizer.Add(self.txt_filepicker, 0, wx.ALL, 5)

        self.file_picker = wx.FilePickerCtrl(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        input_sizer.Add(self.file_picker, 0, wx.ALL, 5)

        self.txt_filename = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"filename.xlsx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_filename.Wrap(-1)

        input_sizer.Add(self.txt_filename, 0, wx.ALL, 5)

        selectsheet_sizer = wx.BoxSizer(wx.HORIZONTAL)

        sheet_sizer = wx.BoxSizer(wx.VERTICAL)

        self.txt_selectsheet = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Select sheet", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_selectsheet.Wrap(-1)

        sheet_sizer.Add(self.txt_selectsheet, 0, wx.ALL, 5)

        choice_sheetChoices = []
        self.choice_sheet = wx.Choice(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_sheetChoices, 0)
        self.choice_sheet.SetSelection(0)
        sheet_sizer.Add(self.choice_sheet, 0, wx.ALL, 5)

        selectsheet_sizer.Add(sheet_sizer, 1, wx.EXPAND, 5)

        column_sizer = wx.BoxSizer(wx.VERTICAL)

        self.txt_selectcolumn = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Select ID column", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_selectcolumn.Wrap(-1)

        column_sizer.Add(self.txt_selectcolumn, 0, wx.ALL, 5)

        choice_columnChoices = []
        self.choice_column = wx.Choice(input_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_columnChoices, 0)
        self.choice_column.SetSelection(0)
        column_sizer.Add(self.choice_column, 0, wx.ALL, 5)

        selectsheet_sizer.Add(column_sizer, 1, wx.EXPAND, 5)

        input_sizer.Add(selectsheet_sizer, 1, wx.EXPAND, 5)

        self.txt_idcount = wx.StaticText(input_sizer.GetStaticBox(
        ), wx.ID_ANY, u"ID Count: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_idcount.Wrap(-1)

        self.txt_idcount.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        input_sizer.Add(self.txt_idcount, 0, wx.ALL, 5)

        ui_sizer.Add(input_sizer, 1, wx.EXPAND, 5)

        process_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Process"), wx.VERTICAL)

        self.txt_selectfile = wx.StaticText(process_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Select file to download:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_selectfile.Wrap(-1)

        process_sizer.Add(self.txt_selectfile, 0, wx.ALL, 5)

        choice_filetypeChoices = [u"BePCB", u"CV",
                                  u"DC", u"DW", u"LC", u"Profile Picture"]
        self.choice_filetype = wx.Choice(process_sizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_filetypeChoices, 0)
        self.choice_filetype.SetSelection(0)
        process_sizer.Add(self.choice_filetype, 0, wx.ALL | wx.EXPAND, 5)

        self.btn_process = wx.Button(process_sizer.GetStaticBox(
        ), wx.ID_ANY, u"Process", wx.DefaultPosition, wx.DefaultSize, 0)
        process_sizer.Add(self.btn_process, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ui_sizer.Add(process_sizer, 1, wx.EXPAND, 5)

        output_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Output"), wx.VERTICAL)

        self.btn_openfolder = wx.Button(output_sizer.GetStaticBox(
        ), wx.ID_ANY, u"open folder", wx.DefaultPosition, wx.DefaultSize, 0)
        output_sizer.Add(self.btn_openfolder, 0,
                         wx.ALIGN_CENTER | wx.ALL, 5)

        ui_sizer.Add(output_sizer, 1, wx.EXPAND, 5)

        mainsizer.Add(ui_sizer, 1, wx.EXPAND, 5)

        self.txt_message = wx.StaticText(
            self, wx.ID_ANY, u"Welcome to TalentDocs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_message.Wrap(-1)

        self.txt_message.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        mainsizer.Add(self.txt_message, 0, wx.ALL, 5)

        self.SetSizer(mainsizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.file_picker.Bind(
            wx.EVT_FILEPICKER_CHANGED, self.onFileChanged)
        self.choice_sheet.Bind(wx.EVT_CHOICE, self.showColumns)
        self.choice_column.Bind(wx.EVT_CHOICE, self.setIdCount)
        self.btn_process.Bind(wx.EVT_BUTTON, self.downloadFiles)
        self.btn_openfolder.Bind(wx.EVT_BUTTON, self.openFolder)

        self.df_sheet = None
        self.filepath = None
        self.sheetname = None
        self.columnname = None
        self.idlist = []
        self.outputfolder = thispath

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def disableUI(self):
        self.file_picker.Disable()
        self.choice_sheet.Disable()
        self.choice_column.Disable()
        self.choice_filetype.Disable()
        self.btn_process.Disable()

    def enableUI(self):
        self.file_picker.Enable()
        self.choice_sheet.Enable()
        self.choice_column.Enable()
        self.choice_filetype.Enable()
        self.btn_process.Enable()

    def onFileChanged(self, event):
        filepath = self.file_picker.GetPath()
        if os.path.exists(filepath):
            self.filepath = filepath
            self.txt_filename.SetLabelText(os.path.basename(filepath))
            self.txt_message.SetLabelText('File path is valid')
            self.choice_sheet.Clear()
            self.choice_sheet.Append(td.getSheetname(filepath))
        else:
            self.txt_filename.SetLabelText('?')
            self.txt_message.SetLabelText('Invalid file path!')

    def showColumns(self, event):
        self.sheetname = self.choice_sheet.GetStringSelection()
        self.df_sheet, columnlist = td.getDF_Columns(
            self.filepath, self.sheetname)
        self.choice_column.Append(columnlist)
        self.txt_message.SetLabelText('Sheet is selected')

    def setIdCount(self, event):
        self.columnname = self.choice_column.GetStringSelection()
        self.idlist = td.getIDlist(
            self.df_sheet, self.columnname)
        self.txt_idcount.SetLabelText(
            'ID Count: {}'.format(str(len(self.idlist))))
        self.txt_message.SetLabelText('ID column is selected')

    def downloadFiles(self, event):
        try:
            if not self.filepath == None and not self.sheetname == None and not self.columnname == None:
                self.disableUI()
                self.txt_message.SetLabelText('Running processes...')
                filetypeIndex = self.choice_filetype.GetSelection()
                successful_list, failed_list, outputfolder = td.downloadFiles(
                    self.idlist, filetypeIndex, self.outputfolder)
                if not failed_list:
                    messageString = 'Successfully executed: All IDs docs successfully retrieved'
                else:
                    messageString = 'Successfully executed: Some IDs docs failed to be retrieved'
                os.startfile(outputfolder)
            else:
                messageString = 'Please insert all the required input first.'
        except Exception as e:
            messageString = 'Error: ', str(e)
        finally:
            self.txt_message.SetLabelText(messageString)
            self.enableUI()

    def openFolder(self, event):
        os.startfile(self.outputfolder)


class MainApp(wx.App):
    def OnInit(self):
        mainFrame = dashboardFrame(None)
        mainFrame.Show(True)
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
