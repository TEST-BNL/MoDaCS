#System Imports
import json, ast, logging, os
#from objgraph import InstanceType
from array import array

#Qt Imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal
from asyncore import read

        
class JSONFileField():
    def __init__(self, filename=None, fieldname=None, parent=None, fieldType=object, compact=False, removeTemp=True):
        self.subfields = {}
        self.subelements = {}
        self.level = 1
        #self.predefined = predefined
        self.brackets = {list: {'start':'[', 'end':']'}, object: {'start':'{', 'end':'}'}}
        self.fieldType = fieldType
        self.indt = ''
        self.removeTempFiles = removeTemp
        self.isCompact = compact
        
        if parent is None and filename is None:
            raise Exception('No path or parent specified, no data will be written')
            return None
        try:
            self.dataFile = parent.dataFile + '_' + fieldname
            self.rootFile = parent.dataFile
            self.level = parent.level + 1
        except:  
            self.dataFile = filename
            self.rootFile = filename
        
        if self.isCompact:
            self.newLine = ''
            self.indt = ''
            self.parentindt = ''
        else:
            self.newLine = '\n'
            self.indt = '\t'*self.level
            self.parentindt = '\t'*(self.level - 1)
        self.startdelimiter = self.newLine
        
        
        self.isOpen = True
        #if not self.predefined:
        with open(self.dataFile, 'w') as out_file:
            out_file.write(self.brackets[self.fieldType]['start'])

    
    def write(self, d, recnum=None, timestamp=None, compact=None, prefix=''):
        if not self.isOpen:
            raise Exception("Cannot write to closed field.")
            return False
            
        if compact is None:
            compact = self.isCompact

        with open(self.dataFile, 'a') as out_file: 
            
            if compact:
                out_data = prefix + json.dumps(d, skipkeys=True, indent=None, default=lambda o: self.objdump(o))
            else:
                out_data = (prefix + json.dumps(d, skipkeys=True, indent='\t', default=lambda o: self.objdump(o))).replace('\n', '\n' + self.indt)

            if timestamp is None and recnum is None:
                #if self.predefined and prefix == '':
                #    out_file.write(out_data)    
                #else:
                out_file.write(self.startdelimiter + self.indt + out_data)
            elif timestamp is None:
                out_file.write(self.startdelimiter + self.indt + '[' + str(recnum) + ', ' + out_data + ']')
            elif recnum is None:
                out_file.write(self.startdelimiter + self.indt + '[' + str(timestamp) + ', ' + out_data + ']')
            else:
                out_file.write(self.startdelimiter + self.indt + '[' + str(timestamp) + ', ' + str(recnum) + ', ' + out_data + ']')
                
        if self.startdelimiter == self.newLine or self.startdelimiter == '':
            self.startdelimiter = ',' + self.startdelimiter
            
        return True

    def addField(self, fieldname, fieldType=object):
        if self.isOpen:
            if self.fieldType is list:
                raise Exception("Cannot add field to 'list' type.")
                return None
            newfield = JSONFileField(fieldname=fieldname, parent=self, fieldType=fieldType, compact=self.isCompact, removeTemp=self.removeTempFiles)
            self.subfields[fieldname] = newfield
            return newfield
    
    def addElement(self, elname, data, compact=None):
        if self.write(data, prefix='"' + elname + '":', compact=compact):
            self.subelements[elname] = type(data)
        
    def _closeSubFields(self, out_file):
        first = True
        if len(self.subfields) > 0:
            
            if self.level > 1:
                out_file.write(self.parentindt)                
            for name, field in self.subfields.items():
                    
                out_file.write(self.startdelimiter + self.indt + '"' + name + '":')
                
                if self.startdelimiter == self.newLine or self.startdelimiter == '':
                    self.startdelimiter = ',' + self.newLine

                with open(field.dataFile, 'r') as in_file:
                    d = in_file.read(1024*1024)
                    while d:
                        out_file.write(d)
                        d = in_file.read(1024*1024)
                field.close(out_file)
                if self.removeTempFiles:
                    os.remove(field.dataFile)
        #if not self.predefined:
        out_file.write(self.newLine + self.parentindt + self.brackets[self.fieldType]['end']) 
                   
    def close(self, out_file=None):
        if self.isOpen:
            self.isOpen = False
            
            if out_file is None:
                with open(self.rootFile, 'a') as out_file:
                    self._closeSubFields(out_file)                    
            else:
                self._closeSubFields(out_file)
        else:
            raise Warning('Field already closed.')      
        
        
    def readField(self, field):
        with open(field.dataFile, 'r') as in_file:
            data = in_file.read()
        if field.isOpen:
            data += (self.newLine + field.brackets[field.fieldType]['end'])
        return data
    
    def readAll(self):
        out = ''
        first = True
        data = self.readField(self)
        
        if self.level > 0:
            out += self.indt
        for field, name in self.subfields:
            if first:
                out.append('"' + name + '":')
                first = False
            else:
                out.append(',' + self.newLine + '"' + name + '":')
            data += self.readField(field)
        return data

    def objdump(self, o):
        try:
            return o.__dict__
        except:   
            return "Python Object"
    
        
    def __getitem__(self,key):
        try:
            return self.subfields[key]
        except:
            return self.subelements[key]
    
    def __str__(self):
        return self.readAll()
        
    def __setitem__(self, key, value):
        return self.addElement(key, data=value)
        

class QSignalHandler(logging.Handler):          #logging handler that emits all log entries through a specified signal
    
    def __init__(self, sig):
        super().__init__()
        self.sig = sig

    def emit(self, record):
        msg = self.format(record)
        self.sig.emit(msg)

    def write(self, m):
        pass

class Sig(QtCore.QObject):                      #Signal "wrapper" to allow programmatic definition of signals
    s = QtCore.pyqtSignal(object, object)
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def emit(self, object):
        self.s.emit(object, self.name)
        
    def connect(self, obj):
        self.s.connect(obj)

class RunningThreads(QtCore.QObject):
    allDone = QtCore.pyqtSignal()
    countChange = QtCore.pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        self.active_threads = []
        
    def __len__(self):
        return len(self.active_threads)
        
    def watchThread(self, thrd):
        if thrd.isRunning():
            self._addItem(thrd)
            #print("Thread added imm.: %s" % thrd)
        else:
            thrd.started.connect(lambda thrd=thrd: self._addItem(thrd))
        thrd.finished.connect(lambda thrd=thrd: self._removeItem(thrd))
        #print("Thread watched: %s" % thrd)
        
    def _addItem(self, thrd):
        #print("Thread added: %s" % thrd)
        if thrd not in self.active_threads:
            self.active_threads.append(thrd)
        self.countChange.emit(len(self.active_threads))
        #print(self.active_threads)
    
    def _removeItem(self, thrd):
        #print("Thread stopped: %s" % thrd)
        try:
            self.active_threads.remove(thrd)
        except Exception as e:
            raise Exception("Error tracking active threads: %s" % e)
        #print(self.active_threads)
        finally:          
            if len(self.active_threads) == 0:
                self.allDone.emit()
            else:
                self.countChange.emit(len(self.active_threads)) 
                        
class SBlock:
    def __init__(self, obj):
        self.target = obj
        
    def __enter__(self):
        self.target.blockSignals(True)
        return self.target
        
    def __exit__(self, *args):
        self.target.blockSignals(False) 
