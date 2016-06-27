import numpy as np
import os
import sys
import logmgr
#import loaddata 
#import utils
import grd_io

logger = logmgr.logger('varres')

class reader:
    def __init__(self, iname):
        '''Class for reading in the geometry data and setting it up.'''
        
        if(os.path.isfile(iname) == False):
            logger.error('IFG file: %s not found.'%(iname))
            sys.exit(1)

        if(os.path.isfile('%s.e'%(iname)) == False):
            logger.error('LOS E component file: %s.e not found.'%(iname))
            sys.exit(1)
        if(os.path.isfile('%s.n'%(iname)) == False):
            logger.error('LOS N component file: %s.n not found.'%(iname))
            sys.exit(1)
        if(os.path.isfile('%s.u'%(iname)) == False):
            logger.error('LOS U component file: %s.u not found.'%(iname))
            sys.exit(1)

        self.x,self.y,self.phs = grd_io.read_grd(iname)
        self.ny,self.nx = grd_io.grd_shape(iname)
        self.dx = np.float(self.x[1]-self.x[0])
        self.dy = np.float(self.y[1]-self.y[0])
        self.TL_east = np.float(self.x[0])
        self.TL_north = np.float(self.y[-1])
        self.wvl = 1.0
       
        self.iname = iname
        x,y,self.lose=grd_io.read_grd('%s.e'%(iname))
        x,y,self.losn=grd_io.read_grd('%s.n'%(iname))
        x,y,self.losu=grd_io.read_grd('%s.u'%(iname))
        self.geom=(self.lose,self.losn,self.losu)


        #self.phs = None
        #self.geom = []
        #self.x = None
        #self.y = None

#    def read_igram(self, scale=True, flip=False, mult=1.0):
#        fact = np.choose(scale,[1.0,self.wvl/(4*np.pi)])
#        fact = fact*mult
#
#        (phs,ngood) = loaddata.load_igram(self.iname,self.nx,self.ny,fact)
#        if flip:
#            self.phs = np.flipud(phs)
#        else:
#            self.phs = phs
#
#        logger.info('Original number of data points: %d'%(ngood))
#
#    def read_geom(self, az= False, defgeom=False, flip=False):
#        self.x = self.TL_east + np.arange(self.nx) * self.dx
#        self.y = self.TL_north + np.arange(self.ny) * self.dy
#        if flip:
#            self.y = self.y[::-1]
#
#        if defgeom:
#            self.geom = loaddata.get_los(self.rdict)
#
#        elif az:
#            self.geom = loaddata.get_azi(self.rdict)
#
#        elif self.sname is not None:
#            self.geom = loaddata.load_S(self.sname,self.nx,self.ny)
#            if flip:
#                for k in xrange(3):
#                    self.geom[k] = np.flipud(self.geom[k])
#
#        else:
#            for k in xrange(3):
#                self.geom[k] = 0
#
#
#
#
#
#############################################################
## Program is part of varres                                #
## Copyright 2012, by the California Institute of Technology#
## Contact: earthdef@gps.caltech.edu                        #
#############################################################
