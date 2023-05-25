# coding:UTF-8

from abaqus import *
from abaqus import *
from abaqusConstants import *
import xlrd2

framemodel = openMdb(pathName='F:/abaqusmodel/model_semic.cae')
s_1_path, s_2_path, s_3_path = getInputs(label='Enter information', fields=(
('Floor-1 displacement:', 'F:/abaqusmodel/dis_1.xlsx'),
('Floor-2 displacement:', 'F:/abaqusmodel/dis_2.xlsx'),
('Floor-3 displacement:', 'F:/abaqusmodel/dis_3.xlsx')))
s_1_xlrd = xlrd2.open_workbook(s_1_path)
s_2_xlrd = xlrd2.open_workbook(s_2_path)
s_3_xlrd = xlrd2.open_workbook(s_3_path)

s_1 = ()
s_2 = ()
s_3 = ()

for i in range(s_1_xlrd[0].nrows):
    s_1 = s_1 + ((float(s_1_xlrd[0].cell(i, 0).value), float(s_1_xlrd[0].cell(i, 1).value)),)
for i in range(s_2_xlrd[0].nrows):
    s_2 = s_2 + ((float(s_2_xlrd[0].cell(i, 0).value), float(s_2_xlrd[0].cell(i, 1).value)),)
for i in range(s_3_xlrd[0].nrows):
    s_3 = s_3 + ((float(s_3_xlrd[0].cell(i, 0).value), float(s_3_xlrd[0].cell(i, 1).value)),)


framemodel.models['Model-1'].amplitudes['dis_1'].setValues(timeSpan=STEP,
                                                               smooth=SOLVER_DEFAULT, data=s_1)
framemodel.models['Model-1'].amplitudes['dis_2'].setValues(timeSpan=STEP,
                                                               smooth=SOLVER_DEFAULT, data=s_2)
framemodel.models['Model-1'].amplitudes['dis_3'].setValues(timeSpan=STEP,
                                                               smooth=SOLVER_DEFAULT, data=s_3)

mdb.jobs['dyn_board'].submit()
mdb.jobs['dyn_board'].waitForCompletion()
o1 = session.openOdb(name='C:/Temp/dyn_board.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))