from netpyne import specs
try:
    from __main__ import cfg
except:
    from cfg import cfg

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters
netParams.defaultThreshold = 0.0
netParams.defineCellShapes = True       # sets 3d geometry aligned along the y-axis

###############################################################################
## Cell types
###############################################################################
## Izhi cell params (used in cell properties)
izhiParams = {}
izhiParams['RS'] = {'mod':'Izhi2007b', 'C':1, 'k':0.7, 'vr':-60, 'vt':-40, 'vpeak':35, 'a':0.03, 'b':-2, 'c':-50, 'd':100, 'celltype':1}
izhiParams['IB'] = {'mod':'Izhi2007b', 'C':1.5, 'k':1.2, 'vr':-75, 'vt':-45, 'vpeak':50, 'a':0.01, 'b':5, 'c':-56, 'd':130, 'celltype':2}
izhiParams['LTS'] = {'mod':'Izhi2007b', 'C':1.0, 'k':1.0, 'vr':-56, 'vt':-42, 'vpeak':40, 'a':0.03, 'b':8, 'c':-53, 'd':20, 'celltype':4}
izhiParams['FS'] = {'mod':'Izhi2007b', 'C':0.2, 'k':1.0, 'vr':-55, 'vt':-40, 'vpeak':25, 'a':0.2, 'b':-2, 'c':-45, 'd':-55, 'celltype':5}

## E cell params
cellRule = {'conds': {'cellType': 'E'}, 'secs': {}}
cellRule['secs']['soma'] = {'geom': {}, 'pointps':{}}  #  soma
cellRule['secs']['soma']['geom'] = {'diam': 10, 'L': 10, 'cm': 31.831}
cellRule['secs']['soma']['pointps']['Izhi'] = izhiParams['RS']
netParams.cellParams['E'] = cellRule  # add dict to list of cell properties

## I cell params
cellRule = {'conds': {'cellType': 'I'}, 'secs': {}}
cellRule['secs']['soma'] = {'geom': {}, 'pointps':{}}  #  soma
cellRule['secs']['soma']['geom'] = {'diam': 10, 'L': 10, 'cm': 31.831}
cellRule['secs']['soma']['pointps']['Izhi'] = izhiParams['FS']
netParams.cellParams['I'] = cellRule  # add dict to list of cell properties

###############################################################################
## Synaptic mechs
###############################################################################

netParams.synMechParams['AMPAf'] = {'mod': 'MyExp2SynBB', 'tau1': 0.05, 'tau2': 5.3, 'e': 0}
netParams.synMechParams['NMDA'] = {'mod': 'MyExp2SynNMDABB', 'tau1': 0.05, 'tau2': 5.3, 'tau1NMDA': 15, 'tau2NMDA': 150, 'r': 1, 'e': 0}
netParams.synMechParams['GABAf'] = {'mod': 'MyExp2SynBB', 'tau1': 0.07, 'tau2': 9.1, 'e': -80}
netParams.synMechParams['GABAs'] = {'mod': 'MyExp2SynBB', 'tau1': 0.2, 'tau2': 20, 'e': -80}
netParams.synMechParams['GABAss'] = {'mod': 'MyExp2SynBB', 'tau1': 20, 'tau2': 40, 'e': -80}


###############################################################################
## Populations
###############################################################################
netParams.popParams['E'] = {'cellType': 'E', 'numCells': 800}
netParams.popParams['I'] = {'cellType': 'I', 'numCells': 200}

###############################################################################
# Setting stimulation
###############################################################################
netParams.stimSourceParams['background_E'] = {'type': 'NetStim', 'rate': 50, 'noise': 0.5} # E background inputs

###############################################################################
# Current-clamp to cells
###############################################################################
netParams.stimSourceParams['IClamp_E'] =  {'type': 'IClamp', 'del': 2*cfg.dt, 'dur': 1e9, 'amp': -1}
netParams.stimSourceParams['IClamp_I'] =  {'type': 'IClamp', 'del': 2*cfg.dt, 'dur': 1e9, 'amp': -1}

netParams.stimTargetParams['IClamp_E->E'] = {
        'source': 'IClamp_E',
        'sec': 'soma',
        'loc': 0.5,
        'conds': {'pop': 'E'}}

netParams.stimTargetParams['IClamp_I->I'] = {
        'source': 'IClamp_I',
        'sec': 'soma',
        'loc': 0.5,
        'conds': {'pop': 'I'}}

###############################################################################
# Setting connections
###############################################################################

# E -> I, NMDA
netParams.connParams['E->I_NMDA'] = {'preConds': {'pop': 'E'}, 'postConds': {'pop': 'I'},
    'convergence': 100,
    'weight': 1.38e-3,
    'delay': 2,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'NMDA'}

# E -> I, AMPA
netParams.connParams['E->I_AMPA'] = {'preConds': {'pop': 'E'}, 'postConds': {'pop': 'I'},
    'convergence': 100,
    'weight': 0.36e-3,
    'delay': 2,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'AMPAf'}

# I -> E, GABA
netParams.connParams['I->E_GABA'] = {'preConds': {'pop': 'I'}, 'postConds': {'pop': 'E'},
    'convergence': 20,
    'weight': 72e-3,
    'delay': 2,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'GABAs'}

netParams.stimTargetParams['bgE->E'] = {'source': 'background_E', 'conds': {'pop': 'E'},
                                            'synMech': 'NMDA', 'weight': 1, 'delay': 'normal(5,3)'}
netParams.stimTargetParams['bgE->I'] = {'source': 'background_E', 'conds': {'pop': 'I'},
                                            'synMech': 'NMDA', 'weight': 1, 'delay': 'normal(5,3)'}
