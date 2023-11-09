#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file GUI_mycobot.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Import GUI module
import wx
import mycobot_ui
import multiprocessing

global_var = multiprocessing.Value('i', 0)


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
gui_mycobot_spec = ["implementation_id", "GUI_mycobot", 
         "type_name",         "GUI_mycobot", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class GUI_mycobot
# @brief ModuleDescription
# 
# 
# </rtc-template>
class GUI_mycobot(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_poseOut = OpenRTM_aist.instantiateDataType(RTC.TimedPose3D)
        """
        """
        self._poseOutOut = OpenRTM_aist.OutPort("poseOut", self._d_poseOut)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
		
        # Set OutPort buffers
        self.addOutPort("poseOut",self._poseOutOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
        self.process_a = multiprocessing.Process(target=gui_thread)
        self.process_a.start()
    
        return RTC.RTC_OK
	
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
        self.process_a.join()
    
        return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        global global_var
        with global_var.get_lock():
            #print(global_var.value)
            if global_var.value==1:
                self._d_poseOut.data.position.x=0.2
                self._d_poseOut.data.position.y=0.0
                self._d_poseOut.data.position.z=0.1

                self._poseOutOut.write()
                global_var.value = 0
                print("write1")
            if global_var.value==2:
                self._d_poseOut.data.position.x=0.0
                self._d_poseOut.data.position.y=0.2
                self._d_poseOut.data.position.z=0.1

                self._poseOutOut.write()
                global_var.value = 0
                print("write2")
            if global_var.value==3:
                self._d_poseOut.data.position.x=0.0
                self._d_poseOut.data.position.y=0.0
                self._d_poseOut.data.position.z=0.0

                self._poseOutOut.write()
                global_var.value = 0
                print("write3")
            if global_var.value==4:
                self._d_poseOut.data.position.x=0.0
                self._d_poseOut.data.position.y=-0.2
                self._d_poseOut.data.position.z=0.1

                self._poseOutOut.write()
                global_var.value = 0
                print("write4")
            if global_var.value==5:
                self._d_poseOut.data.position.x=-0.2
                self._d_poseOut.data.position.y=0.0
                self._d_poseOut.data.position.z=0.15

                self._poseOutOut.write()
                global_var.value = 0
                print("write5")
    
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK

class mycobot_uiMyFrame1(mycobot_ui.MyFrame1):
    def __init__(self,parent):
        mycobot_ui.MyFrame1.__init__(self,parent)

        font = wx.Font(25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.m_staticText2.SetFont(font)

        self.m_button1.SetMinSize((100,100))
        font = wx.Font(25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) 
        self.m_button1.SetFont(font)
        self.m_button1.SetBackgroundColour((176,196,222))

        self.m_button5.SetMinSize((100,100))
        font = wx.Font(25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) 
        self.m_button5.SetFont(font)
        self.m_button5.SetBackgroundColour((176,196,222))

        self.m_button6.SetMinSize((230,100))
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) 
        self.m_button6.SetFont(font)
        self.m_button6.SetBackgroundColour((25,25,112))
        self.m_button6.SetForegroundColour(wx.Colour(255,255,255))

        self.m_button7.SetMinSize((100,100))
        font = wx.Font(25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) 
        self.m_button7.SetFont(font)
        self.m_button7.SetBackgroundColour((176,196,222))

        self.m_button9.SetMinSize((100,100))
        font = wx.Font(25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) 
        self.m_button9.SetFont(font)
        self.m_button9.SetBackgroundColour((176,196,222))
       
    
    def m_button1OnButtonClick(self, event):#FRONT
        button = event.GetEventObject()
        color = button.GetBackgroundColour()
        dark_color = wx.Colour(color.Red() * 0.8, color.Green() * 0.8, color.Blue() * 0.8)
        button.SetBackgroundColour(dark_color)
        global global_var
        with global_var.get_lock():
            global_var.value=1
        #time.sleep(2)
        button.Refresh()
        wx.CallLater(100,self.reset_button_color,button,color)
        #button.SetBackgroundColour(color)
        #button.Refresh()

    def m_button5OnButtonClick(self, event):#LEFT
        button = event.GetEventObject()
        color = button.GetBackgroundColour()
        dark_color = wx.Colour(color.Red() * 0.8, color.Green() * 0.8, color.Blue() * 0.8)
        button.SetBackgroundColour(dark_color)
        global global_var
        with global_var.get_lock():
            global_var.value=2
        button.Refresh()
        wx.CallLater(100,self.reset_button_color,button,color)

    def m_button6OnButtonClick(self, event):#INITIAL
        button = event.GetEventObject()
        color = button.GetBackgroundColour()
        dark_color = wx.Colour(color.Red() * 0.6, color.Green() * 0.6, color.Blue() * 0.6)
        button.SetBackgroundColour(dark_color)
        global global_var
        with global_var.get_lock():
            global_var.value=3
        button.Refresh()
        wx.CallLater(100,self.reset_button_color,button,color)

    def m_button7OnButtonClick(self, event):#RIGHT
        button = event.GetEventObject()
        color = button.GetBackgroundColour()
        dark_color = wx.Colour(color.Red() * 0.8, color.Green() * 0.8, color.Blue() * 0.8)
        button.SetBackgroundColour(dark_color)
        global global_var
        with global_var.get_lock():
            global_var.value=4
        button.Refresh()
        wx.CallLater(100,self.reset_button_color,button,color)

    def m_button9OnButtonClick(self, event):#BACK
        button = event.GetEventObject()
        color = button.GetBackgroundColour()
        dark_color = wx.Colour(color.Red() * 0.8, color.Green() * 0.8, color.Blue() * 0.8)
        button.SetBackgroundColour(dark_color)
        global global_var
        with global_var.get_lock():
            global_var.value=5
        button.Refresh()
        wx.CallLater(100,self.reset_button_color,button,color)

    def reset_button_color(self,getbutton,getcolor):
        getbutton.SetBackgroundColour(getcolor)
        getbutton.Refresh()


'''	
class mycobot_uiMyFrame1( mycobot_ui.MyFrame1 ):
	def __init__( self, parent ):
		mycobot_ui.MyFrame1.__init__( self, parent )

    # Handlers for MyFrame1 events.
	def m_button1OnButtonClick( self, event ):
		# TODO: Implement m_button1OnButtonClick
		global global_var
        with global_var.get_lock():
             global_var.value=1

	def m_button5OnButtonClick( self, event ):
		# TODO: Implement m_button5OnButtonClick
		pass

	def m_button6OnButtonClick( self, event ):
		# TODO: Implement m_button6OnButtonClick
		pass

	def m_button7OnButtonClick( self, event ):
		# TODO: Implement m_button7OnButtonClick
		pass

	def m_button9OnButtonClick( self, event ):
		# TODO: Implement m_button9OnButtonClick
		pass
'''
        
def gui_thread():
    app = wx.App(False)
    frame = mycobot_uiMyFrame1(None)
    frame.Show()
    app.MainLoop()



def GUI_mycobotInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=gui_mycobot_spec)
    manager.registerFactory(profile,
                            GUI_mycobot,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    GUI_mycobotInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("GUI_mycobot" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

