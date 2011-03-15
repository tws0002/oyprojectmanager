#!/usr/bin/env python
#coding:utf-8
# Author:  Erkan OZgur Yilmaz
# Purpose: 
# Created: 11/21/2010

import sys
import platform
import os
import shutil
import re
import oyAuxiliaryFunctions as oyAux
from xml.dom import minidom
from oyProjectManager.utils import cache
from oyProjectManager.models import user, abstractClasses



__version__ = "11.3.15"






########################################################################
class Repository( abstractClasses.Singleton ):
    """Repository class gives informations about the servers, projects, users
    etc.
    
    =============
    Settings File
    =============
    
    oyProjectManager uses the OYPROJECTMANAGER_PATH environment variable to
    track the settings, if there is no OYPROJECTMANAGER_PATH variable in your
    current environment, the system will use the default settings, which
    probably will not work in your studio. You can set OYPROJECTMANAGER_PATH to
    a shared folder in your fileserver where all the users can access.
    
    oyProjectManager will look for these files in the OYPROJECTMANAGER_PATH:
    
     * defaultProjectSettings.xml
     * environmentSettings.xml
     * repositorySettings.xml
     * users.xml
    
    You can just duplicate the XML files under the settings folder of the
    package root to your own OYPROJECTMANAGER_PATH and modify them.
    
    These are the xml files that the oyProjectManager searches for:
    * defaultProjectSettings.xml:
      This file explains the default project settings for oyProjectManager. It
      is an XML file with these elements.
     
      * sequenceData:
        attributes:
        * shotPrefix: default is "SH", it is the prefix to be added before the
          shot number
        * shotPadding: default is 3, it is the number of padding going to be
          applied to find the string representation of the shot number. If the
          shot number is 5 and the shotPadding is set to 3 and the shotPrefix
          is "SH" then the final shot name will be SH005
        * revPrefix: default is "r", it is the revision variable prefix
        * revPadding: default is 2, it is the revision number padding, again
          for revision 3 the default values will output a string of "r03" for
          the revision string variable
        * verPrefix: default is "v", it is the version variable prefix
        * verPadding: default is 3, it is the version number padding and again
          for default values a file version of 14 will output a string of
          "v014" for the version string variable
        * timeUnit: default is pal, it is the time unit for the project,
          possible values are "pal, film, ntsc, game". This variable follows
          the Maya's time unit format
        
        children elements:
        * structure: it is the child of sequenceData. Structure element holds
          the project structure information. Every project will be created by
          using this project structure. There are two possible child elements:
          
          * shotDependent: shows the shot dependent folders. A shot dependent
            folder will contain shot folders. For example a folder called
            ANIMATION could be defined under shotDependent folders, then
            oyProjectManager will automatically place folders for every shot of
            the project. So if the project has three shots with shot numbers
            10, 14, 21 then the structure of the ANIMATION folder will be like:
              
              ANIMATION\
                SH010\
                SH014\
                SH021\
            
          * shotIndependent: shows the shot independent folder, or the rest of
            the project structure. So any other folder which doesn't have a
            direct relation with shots can be placed here. For example you can
            place folders for MODELS, RIGS, OUTGOING_FILES etc.
        
          * outputFolders: this is the object that holds OUTPUT elements
            
            * output: and output element shows the output folder of one
              spesific asset type. For example you can set the render output
              folder by setting the output folder of the RENDER asset type to a
              spesific folder relative to the project root. (This element
              should be a child of asset types, it is a bad desing)
          
        * assetTypes: This element contains information about asset types.
          attributes: None
          children:
            * type: this is an asset type
              attributes:
                * name: the name of the type
                * path: the project relative path for the asset files in this
                  type
                * shotDependent: it is a boolean value that specifies if this
                  asset type is shot dependent
                * environments: this attribute lists the environment names
                  where this asset type is valid through. It should list the
                  environment names in a comma separated value (CSV) format
                * playblastFolder: this is the attribute that shows the default
                  playblast/flipbook path for this kind of assets
        
        * shotData: This is the element that shows the current projects shot
          information
          
          children:
            * shot: the shot it self
              attributes:
                * name: this is the name of the shot, it just shows the number
                  and alternate letter part of the shot name, so for a shot
                  named "SH001A" the name attribute is "1A"
                * start: this is the global start frame of the shot
                * end: this is the global end frame of the shot
              
              children:
                * description: this is the text element that has the
                  description of the current shot. You can place any amount of
                  text inside this text element.
    
    * environmentSettings.xml:
      Shows the general environment settings. An environment in
      oyProjectManager terminology is a host application like Maya, Houdini,
      Nuke or Photoshop.
      
      Structure of the XML file:
      
      * environments: this node holds the environment objects and doesn't have
        any attribute
        
        children:
          * environment: this is a specific environment and has these
            attributes:
              * name: the name of the environment. It should be all upper case
              * extensions: the list of native file format extensions for the
                environment. For example, for Maya it should be "ma,mb", for
                Nuke it should be "nk", for Houdini it should be "hip" etc.
    
    * repositorySettings.xml: holds the fileserver and general unit information
      structure:
        * settings:
          children:
            * server: defines a file server, so you can use multiple servers in
              your studio and oyProjectManager will be able to manage the
              projects in different servers. (omitted for now)
              
              attributes:
                * name: the name of the server
                * serverPath: the path of the project folder in this server
                * projectFoldersName: the project folder name in this server
            
            * units: holds the default units for the system
              children:
                * timeUnits:
                  children:
                    * time:
                      attributes:
                        * name: the name of the unit
                        * fps: the corresponding FPS value for this unit
                * linearUnits:
                  children:
                    * linear:
                      attributes:
                        * name: the name of the unit, like centimeters
                        * short: the short name of the unit, like cm for
                          centimeters
                * angularUnits:
                  children:
                  * angle:
                    attributes:
                      * name: the name of the unit
                      * short: the short name of the unit
        * defaultFiles: this shows the 
          children:
            * file:
              attributes:
              * name: the name of the file with the extension
              * projectRelativePath: the project relative path of the file
    
    * users.xml: this file holds the user data
      nodes:
        * users: holds user nodes
        
          children:
          * user: a user node
          
            attributes:
              * initials: the initials of the users
              * name: the full name of the user
    """
    
    
    
    #----------------------------------------------------------------------
    def __init__(self):
        
        # initialize default variables
        # user name STALKER for forward compability
        self.repository_path_env_key = "STALKER_REPOSITORY_PATH"
        if not os.environ.has_key(self.repository_path_env_key):
            os.environ[self.repository_path_env_key] = ""
        
        # find where am I installed
        self._env_key = 'OYPROJECTMANAGER_PATH'
        self._settingsDirPath = self.getSettingsPath()
        
        
        # Repository Settings File ( repositorySettings.xml )
        self._repositorySettingsFileName = 'repositorySettings.xml'
        self._repositorySettingsFilePath = self._settingsDirPath
        self._repositorySettingsFileFullPath = os.path.join( self._repositorySettingsFilePath, self._repositorySettingsFileName )
        
        # Default Settings File ( defaultSettings.xml )
        self._defaultSettingsFileName = 'defaultProjectSettings.xml'
        self._defaultSettingsFilePath = self._settingsDirPath
        self._defaultSettingsFileFullPath = os.path.join( self._defaultSettingsFilePath, self._defaultSettingsFileName )
        
        # Default Files Folder Path ( _defaultFiles_ )
        self._defaultFilesFolderFullPath = os.path.join( self._settingsDirPath, '_defaultFiles_' )
        
        # JOBs folder settings ( M:/, JOBs )
        self._serverPath = ""
        self._windows_path = ""
        self._osx_path = ""
        self._linux_path = ""
        
        
        # ---------------------------------------------------
        # Last User File
        # ---------------------------------------------------
        self._lastUserFileName = '.lastUser'
        self._lastUserFilePath = self.homePath
        self._lastUserFileFullPath = os.path.join( self._lastUserFilePath, self._lastUserFileName )
        
        #self._localSettingsFileName = '.localSettings.xml'
        #self._localSettingsPath = self.getHomePath()
        #self._localSettingsFullPath = os.path( self._localSettingsPath, self._localSettingsFileName )
        
        # ---------------------------------------------------
        # Users Settings File
        # ---------------------------------------------------
        self._usersFileName = 'users.xml'
        self._usersFilePath = self._settingsDirPath
        self._usersFileFullPath = os.path.join( self._usersFilePath, self._usersFileName )
        self._users = [] * 0
        
        self._projects = [] * 0
        self._defaultFilesList = [] * 0
        
        # ---------------------------------------------------
        # UNITS
        # ---------------------------------------------------
        # 
        # Only time units are implemented for now,
        # the rest will be added when they are first needed
        # 
        self._timeUnits = {}
        #self._linearUnits = {}
        #self._angularUnits = {}
        
        # ---------------------------------------------------
        
        #self._LocalSettings()
        self._readSettings()
        self._readUsers()
        #self._updatePathVariables()
    
    
    
    #----------------------------------------------------------------------
    def _readSettings(self):
        """reads the repository settings from the xml file at the project root
        """
        
        # open the repository settings file
        xmlFile = minidom.parse( self._repositorySettingsFileFullPath )
        
        rootNode = xmlFile.childNodes[0]
        
        # -----------------------------------------------------
        # get the nodes
        settingsNode = rootNode.getElementsByTagName('settings')[0]
        serverNodes = settingsNode.getElementsByTagName('server')
        defaultFilesNode = rootNode.getElementsByTagName('defaultFiles')[0]
        
        #assert(isinstance(settingsNode, minidom.Element))
        #assert(isinstance(defaultFilesNode, minidom.Element))
        
        timeNodes = rootNode.getElementsByTagName('time')
        
        for timeNode in timeNodes:
            name = timeNode.getAttribute('name')
            fps = timeNode.getAttribute('fps')
            self._timeUnits[ name ] = fps
        
        # -----------------------------------------------------
        # read the server settings
        # for now just assume one server
        
        #self._projectsFolderName = serverNodes[0].getAttribute('projectsFolderName')
        #self.serverPath = serverNodes[0].getAttribute('serverPath')
        
        try:
            self.windows_path = serverNodes[0].getAttribute('windows_path')
            self.windows_path.replace("/", "\\")
        except AttributeError:
            pass
        
        try:
            self.linux_path = serverNodes[0].getAttribute('linux_path')
        except AttributeError:
            pass
        
        try:
            self.osx_path = serverNodes[0].getAttribute('osx_path')
        except AttributeError:
            pass
        
        
        
        # read and create the default files list
        for fileNode in defaultFilesNode.getElementsByTagName('file'):
            #assert(isinstance(fileNode, minidom.Element))
            #                                           fileName                          projectRelativePath                         sourcePath
            self._defaultFilesList.append( (fileNode.getAttribute('name'), fileNode.getAttribute('projectRelativePath') , self._defaultFilesFolderFullPath) )
        
        # -----------------------------------------------------
        # read the environment settings
        
    
    
    
    ##----------------------------------------------------------------------
    #def _updatePathVariables(self):
        #"""updates path variables
        #"""
    
    
    
    #----------------------------------------------------------------------
    #@cache.CachedMethod
    @property
    def projects(self):
        """returns projects names as a list
        """
        self.updateProjectList()
        return self._projects
    
    
    
    #----------------------------------------------------------------------
    @cache.CachedMethod
    @property
    def validProjects(self):
        """returns the projectNames only if they are valid projects.
        A project is only valid if there are some valid sequences under it
        """
        
        # get all projects and filter them
        self.updateProjectList()
        
        from oyProjectManager.models import project
        
        validProjectList = [] * 0
        
        for projName in self._projects:
            
            # get sequences of that project
            projObj = project.Project(projName)
            
            seqList = projObj.sequences()
            
            for seq in seqList:
                
                #assert(isinstance(seq, Sequence))
                if seq.isValid():
                    # it has at least one valid sequence
                    validProjectList.append( projName )
                    break
        
        return validProjectList
    
    
    
    #----------------------------------------------------------------------
    @property
    def users(self):
        """returns users as a list of User objects
        """
        return self._users
    
    
    
    #----------------------------------------------------------------------
    @property
    def userNames(self):
        """returns the user names
        """
        return [ userObj.name for userObj in self._users ]
    
    
    
    #----------------------------------------------------------------------
    @property
    def userInitials(self):
        """returns the user intials
        """
        return sorted([userObj.initials for userObj in self._users])
    
    
    
    #----------------------------------------------------------------------
    def _readUsers(self):
        """parses the usersFile
        """
        
        # check if the usersFile exists
        if not os.path.exists( self._usersFileFullPath ):
            return
        
        usersXML = minidom.parse( self._usersFileFullPath )
        
        rootNode = usersXML.childNodes[0]
        
        # -----------------------------------------------------
        # get the users node
        userNodes = rootNode.getElementsByTagName('user')
        
        self._users = [] * 0
        
        for node in userNodes:
            name = node.getAttribute('name')
            initials = node.getAttribute('initials')
            self._users.append( user.User(name, initials) )
    
    
    
    #----------------------------------------------------------------------
    def updateProjectList(self):
        """updates the project list variable
        """
        
        try:
            #self._projects = oyAux.getChildFolders( self._projectsFolderFullPath )
            self._projects = []
            
            child_folders = oyAux.getChildFolders( self.serverPath )
            for folder in child_folders:
                filtered_folder_name = re.sub(r".*?([^A-Z_]+)([A-Z0-9_]*)", r"\2", folder)
                if filtered_folder_name == folder:
                    self._projects.append(folder)
           
        except IOError:
            #print "server path doesn't exists, %s" % self._projectsFolderFullPath
            print "server path doesn't exists, %s" % self.serverPath
    
    
    
    #----------------------------------------------------------------------
    @property
    def projectsFullPath(self):
        """returns the projects folder full path
        
        ex : M:/JOBs
        """
        
        #return self._projectsFolderFullPath
        return self.serverPath
    
    
    
    #----------------------------------------------------------------------
    def serverPath():
        
        doc = """the server path"""
        
        def fget(self):
            platform_system = platform.system()
            python_version = platform.python_version()
            
            windows_string = "Windows"
            linux_string = "Linux"
            osx_string = "Darwin"
            
            if python_version.startswith("2.5"):
                windows_string = "Microsoft"

            if platform_system == linux_string:
                return self.linux_path
            elif platform_system == windows_string:
                self.windows_path.replace("/", "\\")
                return self.windows_path
            elif platform_system == osx_string:
                return self.osx_path
            
        
        def fset(self, serverPath):
            
            # add a trailing separator
            # in any cases os.path.join adds a trailing seperator
            
            platform_system = platform.system()

            python_version = platform.python_version()
            
            windows_string = "Windows"
            linux_string = "Linux"
            osx_string = "Darwin"
            
            if platform_system == linux_string:
                self.linux_path = serverPath
            elif platform_system == windows_string:
                serverPath = serverPath.replace("/", "\\")
                self.windows_path = serverPath
            elif platform_system == osx_string:
                self.osx_path = serverPath
            
            # set also the environment variables
            os.environ[self.repository_path_env_key] = serverPath
            
            self._projects = [] * 0
            
            self.updateProjectList()
        
        return locals()
    
    serverPath = property( **serverPath() )
    
    
    
    #----------------------------------------------------------------------
    def linux_path():
        def fget(self):
            return self._linux_path
        
        def fset(self, linux_path_in):
            #self._linux_path = self._validate_linux_path(linux_path_in)
            self._linux_path = linux_path_in
            os.environ[self.repository_path_env_key] = linux_path_in
        
        doc = """the linux path of the jobs server"""
        
        return locals()
    
    linux_path = property(**linux_path())
    
    
    
    #----------------------------------------------------------------------
    def windows_path():
        def fget(self):
            return self._windows_path
        
        def fset(self, windows_path_in):
            #self._windows_path = self._validate_windows_path(windows_path_in)
            self._windows_path = windows_path_in
            os.environ[self.repository_path_env_key] = windows_path_in
        
        doc = """the windows path of the jobs server"""
        
        return locals()
    
    windows_path = property(**windows_path())
    
    
    
    #----------------------------------------------------------------------
    def osx_path():
        def fget(self):
            return self._osx_path
        
        def fset(self, osx_path_in):
            #self._osx_path = self._validate_osx_path(osx_path_in)
            self._osx_path = osx_path_in
            os.environ[self.repository_path_env_key] = osx_path_in
        
        doc = """the osx path of the jobs server"""
        
        return locals()
    
    osx_path = property(**osx_path())
    
    
    
    #----------------------------------------------------------------------
    #def createStructureDataFromPath(self, structurePath ):
        #"""creates structure data of a given path
        #can be used to create new structure definitions for new projects
        #"""
        #structureData = [] * 0
        
        #for dirPath, dirNames, fileNames in os.walk(defaultProjectPath):
            #structureData.append( dirPath[len(defaultProjectPath)+1:len(dirPath)] )
        
        #structureData.sort()
        
        #return structureData
    
    
    
    #----------------------------------------------------------------------
    def createProject(self, projectName):
        """creates a new project on the server with the given project name
        """
        from oyProjectManager.models import project
        return project.Project( projectName )
    
    
    
    #----------------------------------------------------------------------
    @property
    def defaultFiles(self):
        """returns the default files list as list of tuples, the first element
        contains the file name, the second the project relative path, the third
        the source path
        
        this is the list that contains files those need to be copied to every
        project like workspace.mel for Maya
        """
        
        return self._defaultFilesList
    
    
    
    #----------------------------------------------------------------------
    @property
    def defaultSettingsFileFullPath(self):
        """returns the default settings file full path
        """
        return self._defaultSettingsFileFullPath
    
    
    
    #----------------------------------------------------------------------
    @property
    def homePath(self):
        """returns the homePath environment variable
        it is :
        /home/userName/ for linux
        C:\Documents and Settings\userName\My Documents for Windows
        C:/Users/userName/Documents for Windows 7 (be careful about the slashes)
        """
        
        homePathAsStr = os.path.expanduser("~")
        
        if os.name == 'nt':
            homePathAsStr = homePathAsStr.replace('/','\\')
        
        return homePathAsStr
    
    
    
    #----------------------------------------------------------------------
    def lastUser():
        doc = """returns and saves the last user initials if the lastUserFile file exists otherwise returns None"""
        
        def fget(self):
            lastUserInitials = None
            
            try:
                lastUserFile = open( self._lastUserFileFullPath )
            except IOError:
                pass
            else:
                lastUserInitials = lastUserFile.readline().strip()
                lastUserFile.close()
            
            return lastUserInitials
        
        def fset(self, userInitials):
            try:
                lastUserFile = open( self._lastUserFileFullPath, 'w' )
            except IOError:
                pass
            else:
                lastUserFile.write( userInitials )
                lastUserFile.close()
        
        return locals()
    
    lastUser = property( **lastUser() )
    
    
    
    #----------------------------------------------------------------------
    def getProjectAndSequenceNameFromFilePath(self, filePath):
        """returns the project name and sequence name from the path or fullPath
        """
        
        #assert(isinstance(filePath, (str, unicode)))
        
        if filePath is None:
            return None, None
        
        #if not filePath.startswith( self._projectsFolderFullPath ):
        if not filePath.startswith( self.serverPath ):
            return None, None
        
        #residual = filePath[ len(self._projectsFolderFullPath)+1 : ]
        residual = filePath[ len(self.serverPath)+1 : ]
        
        parts = residual.split(os.path.sep)
        
        if len(parts) > 1:
            return parts[0], parts[1]
        
        return None, None
    
    
    
    #----------------------------------------------------------------------
    @property
    def settingsDirPath(self):
        """returns the settings dir path
        """
        return self._settingsDirPath
    
    
    #----------------------------------------------------------------------
    @property
    def timeUnits(self):
        """returns timeUnits as a dictionary
        """
        return self._timeUnits
    
    
    ##----------------------------------------------------------------------
    #def _readLocalSettings(self):
        #"""reads the local settings file or creates it
        #"""
        
        ##check if there is a local settings file
        #if os.path.exists( self._localSettingsFullPath ):
            ## parse it
            #self._parseLocalSettings()
        #else:
            ## create it
            #self._saveLocalSettings()
            ## then parse it
            #self._parseLocalSettings()
    
    
    
    ##----------------------------------------------------------------------
    #def _parseLocalSettings(self):
        #"""parses the local settings xml file
        #"""
        
        #settingsFile = minidom.parse( self._localSettingsFullPath )
        
        #rootNode = settingsFile.childNodes[0]
        #programsNode = rootNode.childNodes[0]
        
        #allProgramNodes = programsNode.childNodes
        
        #for program in allProgramNodes:
            #programName = program.getAttr('name')
            
            #recentFilesNode = program.childNodes[0]
            #recentFiles = recentFilesNode.childNodes[0].wholeText.splitlines()
        
        
        
        # read the last user
        
        
        
        # read the program settings
        
    
    
    
    ##----------------------------------------------------------------------
    #def _saveLocalSettings(self):
        #"""saves the 
        #"""
    
    
    
    ##----------------------------------------------------------------------
    #def getRecentFile(self, environmentName):
        #"""returns the recent file from the given environment
        #"""
    
    
    
    #----------------------------------------------------------------------
    def getSettingsPath(self):
        """checks environment against having a variable called
        OYPROJECTMANAGER_PATH
        """
        
        if os.environ.has_key(self._env_key):
            # expand any user variable
            return os.path.expanduser(os.environ[self._env_key])
        else:
            return os.path.join(
                os.path.abspath(
                    os.path.dirname(
                        os.path.dirname(__file__)
                    )
                ),
                'settings')
    
