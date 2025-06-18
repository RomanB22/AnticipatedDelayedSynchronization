from netpyne import specs

try:
    from __main__ import cfg  # import SimConfig object with params from parent module
except:
    from cfg import cfg

netParams = specs.NetParams()   # object of class NetParams to store the network parameters
netParams.version = 1

netParams.defaultThreshold = 0.0  # spike threshold, 10 mV is NetCon default, lower it for all cells
###############################################################################
# NETWORK PARAMETERS
###############################################################################

# Population parameters
netParams.popParams['SenderE'] = {'cellType': 'SenderE_Izhi', 'numCells': 400} # add dict with params for this pop
netParams.popParams['SenderI'] = {'cellType': 'SenderI_Izhi', 'numCells': 100} # add dict with params for this pop
netParams.popParams['ReceiverE'] = {'cellType': 'ReceiverE_Izhi', 'numCells': 400} # add dict with params for this pop
netParams.popParams['ReceiverI'] = {'cellType': 'ReceiverI_Izhi', 'numCells': 100} # add dict with params for this pop

# Cell parameters list
## SenderE cell properties (Izhi)
SenderE_Izhi = {'secs': {}}
SenderE_Izhi['secs']['soma'] = {'geom': {}, 'pointps': {}}                        # soma params dict
SenderE_Izhi['secs']['soma']['geom'] = {'diam': 10.0, 'L': 10.0, 'cm': 31.831}    # soma geometry
SenderE_Izhi['secs']['soma']['pointps']['Izhi'] = {'mod':'Izhi2007b', 'C':1, 'k':0.7, 'vr':-60, 'vt':-40, 'vpeak':35, 
                                                   'a':'0.03*uniform(0.9,1.1)', 'b':'-2*uniform(0.9,1.1)', 'c':'-50*uniform(0.9,1.1)', 'd':'100*uniform(0.9,1.1)', 
                                                   'celltype':1}
netParams.cellParams['SenderE_Izhi'] = SenderE_Izhi  # add dict to list of cell properties

## SenderI cell properties (Izhi)
SenderI_Izhi = {'secs': {}}
SenderI_Izhi['secs']['soma'] = {'geom': {}, 'pointps': {}}                        # soma params dict
SenderI_Izhi['secs']['soma']['geom'] = {'diam': 10.0, 'L': 10.0, 'cm': 31.831}    # soma geometry
SenderI_Izhi['secs']['soma']['pointps']['Izhi'] = {'mod':'Izhi2007b', 'C':0.2, 'k':1.0, 'vr':-55, 'vt':-40, 'vpeak':25, 
                                                   'a':'0.2*uniform(0.9,1.1)', 'b':'-2*uniform(0.9,1.1)', 'c':'-45*uniform(0.9,1.1)', 'd':'-55*uniform(0.9,1.1)', 'celltype':5}
netParams.cellParams['SenderI_Izhi'] = SenderI_Izhi  # add dict to list of cell properties

## ReceiverE cell properties (Izhi)
netParams.cellParams['ReceiverE_Izhi'] = SenderE_Izhi  # add dict to list of cell properties

## ReceiverI cell properties (Izhi)
netParams.cellParams['ReceiverI_Izhi'] = SenderI_Izhi  # add dict to list of cell properties

###############################################################################
## Synaptic mechs
###############################################################################
netParams.synMechParams['NMDA'] = {'mod': 'MyExp2SynNMDABB', 'tau1NMDA': 15, 'tau2NMDA': 150, 'e': 0}
netParams.synMechParams['AMPA'] = {'mod': 'MyExp2SynBB', 'tau1': 0.05, 'tau2': 5.3, 'e': 0}
netParams.synMechParams['GABAA'] = {'mod': 'MyExp2SynBB', 'tau1': 0.07, 'tau2': 18.2, 'e': -80}

ESynMech = ['AMPA', 'NMDA']
ISynMech = ['GABAA']
AllMechs = ['AMPA', 'NMDA', 'GABAA']

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': cfg.bkgRate, 'noise': cfg.bkgNoise}
netParams.stimTargetParams['bg->SenderI_Izhi'] = {'source': 'bkg', 'conds': {'pop': 'SenderI'},
                                            'weight': cfg.bkgSenderI, 'delay': cfg.bkgDelay, 'synMech': ESynMech}
netParams.stimTargetParams['bg->SenderE_Izhi'] = {'source': 'bkg', 'conds': {'pop': 'SenderE'},
                                            'weight': cfg.bkgSenderE, 'delay': cfg.bkgDelay, 'synMech': ESynMech}
netParams.stimTargetParams['bg->ReceiverI_Izhi'] = {'source': 'bkg', 'conds': {'pop': 'ReceiverI'},
                                            'weight': cfg.bkgReceiverE, 'delay': cfg.bkgDelay, 'synMech': ESynMech}
netParams.stimTargetParams['bg->ReceiverE_Izhi'] = {'source': 'bkg', 'conds': {'pop': 'ReceiverE'},
                                            'weight': cfg.bkgReceiverI, 'delay': cfg.bkgDelay, 'synMech': ESynMech}

###############################################################################
# Setting connections
###############################################################################
# Internal in Sender population
netParams.connParams['SenderI->SenderE'] = {
    'preConds': {'pop': 'SenderI'}, 
    'postConds': {'pop': 'SenderE'},
    'convergence': cfg.convergence,
    'weight': cfg.weightSISE,
    'delay': cfg.delaySISE,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': ISynMech}

netParams.connParams['SenderE->SenderI'] = {
    'preConds': {'pop': 'SenderE'}, 
    'postConds': {'pop': 'SenderI'},
    'convergence': cfg.convergence,
    'weight': cfg.weightSESI,
    'delay': cfg.delaySESI,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': ESynMech}

netParams.connParams['SenderI->SenderI'] = {
    'preConds': {'pop': 'SenderI'}, 
    'postConds': {'pop': 'SenderI'},
    'convergence': cfg.convergence,
    'weight': cfg.weightSISI,
    'delay': cfg.delaySISI,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': ISynMech}

# Internal in Receiver population
netParams.connParams['ReceiverI->ReceiverE'] = {
    'preConds': {'pop': 'ReceiverI'}, 
    'postConds': {'pop': 'ReceiverE'},
    'convergence': cfg.convergence,
    'weight': cfg.weightRIRE,
    'delay': cfg.delayRIRE,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': ISynMech}


netParams.connParams['ReceiverE->ReceiverI'] = {
    'preConds': {'pop': 'ReceiverE'}, 
    'postConds': {'pop': 'ReceiverI'},
    'convergence': cfg.convergence,
    'weight': cfg.weightRERI,
    'delay': cfg.delayRERI,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': ESynMech}

netParams.connParams['ReceiverI->ReceiverI'] = {
    'preConds': {'pop': 'ReceiverI'}, 
    'postConds': {'pop': 'ReceiverI'},
    'convergence': cfg.convergence,
    'weight': cfg.weightRIRI,
    'delay': cfg.delayRIRI,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': ISynMech}

# Sender to Receiver connections
netParams.connParams['SenderE->ReceiverI'] = {
    'preConds': {'pop': 'SenderE'}, 
    'postConds': {'pop': 'ReceiverI'},
    'convergence': cfg.convergence,
    'weight': cfg.weightSERI,
    'delay': cfg.delaySERI,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': ESynMech}

netParams.connParams['SenderE->ReceiverE'] = {
    'preConds': {'pop': 'SenderE'}, 
    'postConds': {'pop': 'ReceiverE'},
    'convergence': cfg.convergence,
    'weight': cfg.weightSERE,
    'delay': cfg.delaySERE,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': ESynMech}