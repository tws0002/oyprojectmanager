# -*- coding: utf-8 -*-
import glob

import os, itertools, re



# lower letters
import shutil

trChars = dict()

trChars[u'\xc3\xa7'] = 'c'
trChars[u'\xc4\x9f'] = 'g'
trChars[u'\xc4\xb1'] = 'i'
trChars[u'\xc3\xb6'] = 'o'
trChars[u'\xc5\x9f'] = 's'
trChars[u'\xc3\xbc'] = 'u'

# upper letters
trChars[u'\xc3\x87'] = 'C'
trChars[u'\xc4\x9e'] = 'G'
trChars[u'\xc4\xb0'] = 'I'
trChars[u'\xc3\x96'] = 'O'
trChars[u'\xc5\x9e'] = 'S'
trChars[u'\xc3\x9c'] = 'U'

validFileNameChars = r' abcdefghijklmnoprqstuvwxyzABCDEFGHIJKLMNOPRQSTUVWXYZ0123456789._-'
validTextChars = validFileNameChars + r'!^+%&(){}[]:;?,|@`\'"/=*~$#'

validFileNameCharsPattern = re.compile(r'[\w\.\-\ ]+')
validTextCharsPattern = re.compile( r'[\w\.\-\ !\^+%&\(\)\{\}\[\]:;?,|\\@`\'"/=*~$#]+' )

def all_equal(elements):
    """return True if all the elements are equal, otherwise False.
    """
    first_element = elements[0]
    
    for other_element in elements[1:]:
        if other_element != first_element: return False
    
    return True


def common_prefix(*sequences):
    """return a list of common elements at the start of all sequences, then a
    list of lists that are the unique tails of each sequence.
    """
    
    # if there are no sequences at all, we're done
    if not sequences: return[], []
    # loop in parallel on the sequences
    common = []
    for elements in itertools.izip(*sequences):
        # unless all elements are equal, bail out of the loop
        if not all_equal(elements): break
        
        # got one more common element, append it and keep looping
        common.append(elements[0])
    
    # return the common prefix and unique tails
    return common, [sequence[len(common):] for sequence in sequences]


def relpath(p1, p2, sep=os.path.sep, pardir=os.path.pardir):
    """return a relative path from p1 equivalent to path p2.
    
    In particular:
    
        the empty string, if p1 == p2;
        p2, if p1 and p2 have no common prefix.
    
    """
    
    # replace any trailing slashes at the end
    p1 = re.sub(r"[/]+$", "" , p1)
    p1 = re.sub(r"[\\]+$", "",  p1)
    
    common, (u1, u2) = common_prefix(p1.split(sep), p2.split(sep))
    if not common:
        return p2 # leave path absolute if nothing at all in common
    
    return sep.join([pardir]*len(u1) + u2 )


def abspath(p1, p2):
    """Converts the p2 to abspath by joining it with p1
    
    The output is always normalized, so for windows all the path separators
    will be backslashes where on other systems it will be forward slashes. 
    """

    if not os.path.isabs(p2):
        return os.path.normpath(os.path.join(p1, p2))
    
    return p2


def createFolder(folderPath):
    """utility method that creates a folder if it doesn't exists
    """
    
    exists = os.path.exists(folderPath)
    
    if not exists:
        os.makedirs(folderPath)
    
    return exists


def mkdir(path):
    """Creates a directory in the given path
    """
    
    try:
        os.makedirs(path)
    except OSError:
        pass


def sort_string_numbers(str_list):
    """sorts strings with embedded numbers
    """
    
    def embedded_numbers(s):
        re_digits = re.compile(r'(\d+)')
        pieces = re_digits.split(str(s))
        pieces[1::2] = map(int, pieces[1::2])
        return pieces
    
    return sorted(str_list, key=embedded_numbers)


def unique(s):
    """ Return a list of elements in s in arbitrary order, but without
    duplicates.
    """
    
    # Try using a set first, because it's the fastest and will usually work
    try:
        return list(set(s))
    except TypeError:
        pass # Move on to the next method
    
    # Since you can't hash all elements, try sorting, to bring equal items
    # together and then weed them out in a single pass
    t = list(s)
    try:
        t.sort()
    except TypeError:
        del t # Move on to the next method
    else:
        # the sort worked, so we are fine
        # do weeding
        return [x for i, x in enumerate(t) if not i or x != t[i-1]]
    # Brute force is all that's left
    u = []
    for x in s:
        if x not in u:
            u.append(x)
    
    return u


def convertRangeToList(_range):
    """a shotRange is a string that contains numeric data with "," and "-"
    characters
    
    1-4 expands to 1,2,3,4
    10-5 expands to 5,6,7,8,9,10
    1,4-7 expands to 1,4,5,6,7
    1,4-7,11-4 expands to 1,4,5,6,7,8,9,10,11
    """
    
    shotList = [] * 0
    
    assert(isinstance(_range, (str, unicode) ) )
    
    # first split for ","
    groups = _range.split(",")
    
    for group in groups:
        # try to split for "-"
        ranges = group.split("-")
        
        if len(ranges) > 1:
            if ranges[0] != '' and ranges[1] != '':
                minRange = min( int(ranges[0]), int(ranges[1]))
                maxRange = max( int(ranges[0]), int(ranges[1]))
                
                for number in range(minRange, maxRange+1):
                    if number not in shotList:
                        shotList.append( number )
        else:
            number = int(ranges[0])
            if number not in shotList:
                shotList.append(number)
    
    shotList.sort()
    
    return shotList


def matchRange(_range):
    """validates the range string
    """
    
    assert(isinstance(_range, (str, unicode)))
    
    pattern = re.compile('[0-9\-,]+')
    matchObj = re.match( pattern, _range )
    
    if matchObj:
        _range = matchObj.group()
    else:
        _range = ''
    
    return _range



def stringConditioner(
    text,
    allowSpaces=False,
    allowNumbers=True,
    allowNumbersAtBeginning=False,
    allowUnderScores=False,
    upperCaseOnly=False,
    capitalize=True
    ):
    """removes any spaces, underscores, and turkish characters from the name
    """
    
    textFixed = unicode( text )
    
    textFixed = multiple_replace( textFixed, trChars )
    
    # remove all the white spaces and slashes
    patternString = '\t\n\r\f\v\\\/,\.;~!"\'^+%&()=?*{}\-'
    
    if not allowSpaces:
        patternString += ' '
    
    if not allowNumbers:
        patternString += '0-9'
    
    if not allowUnderScores:
        patternString += "_"
    
    if allowNumbers and not allowNumbersAtBeginning:
        preMatchString = re.compile( '^[0-9]+')
        textFixed = preMatchString.sub("",textFixed)
    
    matchString = '[' + patternString + ']+'
    
    pattern = re.compile(matchString)
    textFixed = pattern.sub("",textFixed)
    
    if capitalize:
        textFixed = textFixed.capitalize()
    
    if upperCaseOnly:
        textFixed = textFixed.upper()
    
    return textFixed


def multiple_replace( text, adict ):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

def fixWindowsPath(path):
    """replaces / with \ for windows
    """
    
    return unicode(path).replace(u'/',u'\\')

def findFiles(pattern, search_path, pathsep=os.pathsep):
    return glob.glob(os.path.join(path,pattern))




def getChildFolders(path, returnFullPath=False):
    """returns the child folders for the given path
    """
    childFolders = os.listdir( path )
    childFolders = filter( os.path.isdir, map( os.path.join, [path] * len(childFolders), childFolders ) )
    
    if returnFullPath:
        return childFolders
    else:
        return map( os.path.basename, childFolders )




def getChildFiles(path, returnFullPath=False):
    """returns the child files for the given path
    """
    childFiles = os.listdir( path )
    childFiles = filter( os.path.isfile, map( os.path.join, [path] * len(childFiles), childFiles ) )
    
    if returnFullPath:
        return childFiles
    else:
        return map( os.path.basename, childFiles )




def backupFile( fullPath, maximum_backupCount=None ):
    """backups a file by copying it and then renaming it by adding .#.bak
    to the end of the file name
    
    so a file called myText.txt will be backed up as myText.txt.1.bak
    if there is a file with that name than it will increase the backup number
    """
    
    # check if the file exists
    exists = os.path.exists( fullPath )
    
    if not exists:
        # just return without doing anything
        return
    
    # get the base name of the file
    baseName = os.path.basename( fullPath )
    
    # start the backup number from 1
    backupNo = 1
    backupExtension = '.bak'
    backupFileFullPath = ''
    
    # try to find maximum backup number
    # get the files
    backupNo = getMaximumBackupNumber(fullPath) + 1
    
    # now try to get the maximum backup number
    while True:
        
        backupFileFullPath = fullPath + '.' + str(backupNo) + backupExtension
        
        if os.path.exists( fullPath + '.' + str(backupNo) + backupExtension ):
            backupNo += 1
        else:
            break
    
    # now copy the file with the new name
    shutil.copy( fullPath, backupFileFullPath )
    
    if maximum_backupCount is not None:
        maintainMaximumBackupCount( fullPath, maximum_backupCount )
    
    




def getBackupFiles( fullPath ):
    """returns the backup files of the given file, returns None if couldn't
    find any
    """
    # for a file lets say .settings.xml the backup file should be names as
    # .settings.xml.1.bak
    # so our search pattern should be
    # .settings.xml.*.bak
    
    backUpExtension = '.bak'
    pattern = fullPath + '.*' + backUpExtension
    
    return sort_strings_with_embedded_numbers( glob.glob(pattern) )




def getBackupNumber(fullPath):
    """returns the backup number of the file
    """
    
    backupExtension = '.bak'
    # remove the backupExtension
    # and split the remaining
    # and use the last one as the backupVersion
    
    backupNumber = 0
    
    try:
        backupNumber = int(fullPath[0:-len(backupExtension)].split('.')[-1])
    except (IndexError, ValueError):
        backupNumber = 0
    
    return backupNumber




def getMaximumBackupNumber(fullPath):
    """returns the maximum backup number of the file
    """
    
    backupFiles = getBackupFiles( fullPath )
    maximumBackupNumber = 0
    
    if len(backupFiles):
        maximumBackupNumber = getBackupNumber( backupFiles[-1] )
    
    return maximumBackupNumber




def maintainMaximumBackupCount( fullPath, maximum_backup_count ):
    """keeps maximum of given number of backups for the given file
    """
    
    if maximum_backup_count is None:
        return
    
    # get the backup files
    backupFiles = getBackupFiles( fullPath )
    
    if len(backupFiles) > maximum_backup_count:
        # delete the older backups
        for backupFile in backupFiles[:-maximum_backup_count]:
            os.remove( backupFile )

def embedded_numbers(s):
    re_digits = re.compile(r'(\d+)')
    pieces = re_digits.split(str(s))
    pieces[1::2] = map(int, pieces[1::2])
    return pieces

def sort_strings_with_embedded_numbers(alist):
    """sorts a string with embedded numbers
    """
    return sorted(alist, key=embedded_numbers)

def padNumber(number, pad):
    """pads a number with zeros
    """
    return str(number).zfill(int(pad))

def invalidCharacterRemover( text, validChars ):
    """its a more stupid way to condition a text
    """
    
    conditionedText = ''
    
    for char in text:
        if char in validChars:
            conditionedText += char
    
    return conditionedText

def file_name_conditioner(fileName):
    """ conditions the file name by replacing the whitespaces and slashes and
    back slashes with underscore ("_") characters
    """
    
    assert(isinstance(fileName, (str, unicode) ) )
    
    fileName = multiple_replace( fileName, trChars )
    
    # make all uppercase
    fileName = fileName.upper()
    
    # replace all the white spaces and slashes
    # with underscore ("_") character
    pattern = re.compile('[\t\n\r\f\v\\\/ ]+')
    fileName = pattern.sub("_",fileName)
    
    return fileName