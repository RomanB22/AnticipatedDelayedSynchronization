from netpyne import specs

cfg = specs.SimConfig()

cfg.transient = 500
cfg.duration = 1000 # Duration of the simulation, in ms
cfg.dt = 0.1
 # Internal integration timestep to use
cfg.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
cfg.createNEURONObj = True  # create HOC objects when instantiating network
cfg.createPyStruct = True  # create Python structure (simulator-independent) when instantiating network
cfg.timing = True  # show timing  and save to file
cfg.verbose = False # show detailed messages

# Recording
cfg.recordCells = []  # list of cells to record from
cfg.recordTraces = {
    'V_izhi':{'sec':'soma', 'loc':0.5, 'pointps':'Izhi', 'var':'v'}
}
cfg.recordStim = False  # record spikes of cell stims
cfg.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)
cfg.printRunTime = 0.1

# Saving
cfg.workingDir = '.'  # Where to save data files
cfg.saveFolder = 'data/'  # Set file output name
cfg.simLabel = 'TwoPops_sync'  # Set file output name
cfg.savePickle = False # Whether or not to write spikes etc. to a .mat file
cfg.saveJson = True # Whether or not to write spikes etc. to a .mat file
cfg.saveMat = False # Whether or not to write spikes etc. to a .mat file
cfg.saveTxt = False # save spikes and conn to txt file
cfg.saveDpk = False # save to a .dpk pickled file

# Analysis and plotting
timeRangePlotting = [cfg.transient, cfg.duration]

cfg.analysis['plotRaster'] = {'orderInverse': False, 'saveFig': True, 'timeRange': timeRangePlotting} #True # Whether or not to plot a raster
cfg.analysis['plotTraces'] = {'include': [(pop, 0) for pop in ['SenderE', 'SenderI', 'ReceiverE', 'ReceiverI']], 'saveFig': True, 'timeRange': timeRangePlotting} # plot recorded traces for this list of cells
cfg.analysis['plotSpikeHist'] = {'include': ['SenderE', 'SenderI', 'ReceiverE', 'ReceiverI'], 'saveFig': True, 'timeRange': timeRangePlotting} #True # Whether or not to plot a raster

cfg.convergence = 50 # 5, 10, 20, 100
# Synaptic weights
cfg.bkgRate = 2000
cfg.bkgNoise = 0.7
cfg.bkgDelay = 'uniform(0.8,1.2)'
cfg.bkgSenderE = 0.3
cfg.bkgSenderI = 0
cfg.bkgReceiverE = 0
cfg.bkgReceiverI = 0

weightEE = 0.03
weightEI = 0.02
weightIE = 0.02
weightII = 0.01
delay = 1e-5#'uniform(0.8,1.5)'

cfg.weightSERE = weightEE
cfg.delaySERE = delay

cfg.weightSERI = weightEI
cfg.delaySERI = delay

cfg.weightRERI = weightEI
cfg.delayRERI = delay

cfg.weightRIRE = weightIE
cfg.delayRIRE = delay

cfg.weightRIRI = weightII
cfg.delayRIRI = delay

cfg.weightSISE = weightIE
cfg.delaySISE = delay

cfg.weightSESI = weightEI
cfg.delaySESI = delay

cfg.weightSISI = weightII
cfg.delaySISI = delay