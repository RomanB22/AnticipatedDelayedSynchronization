from netpyne import specs

cfg = specs.SimConfig()

cfg.duration = 1500
cfg.dt = 0.1
cfg.hparams = {'v_init': -65.0}
cfg.verbose = False
cfg.recordTraces = {'V_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'v'}}  # Dict with traces to record
cfg.recordStim = False
cfg.recordStep = 0.1            # Step size in ms to save data (eg. V traces, LFP, etc)
cfg.savePickle = False        # Save params, network and sim output to pickle file
cfg.saveDat = False
cfg.printRunTime = 0.1

#------------------------------------------------------------------------------
# Saving
#------------------------------------------------------------------------------
cfg.saveFolder = 'data'         # Set file output name
cfg.simLabel = '00'         # Set file output name
cfg.savePickle = False
cfg.saveJson = True
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams']#, 'net']
# cfg.recordLFP = [[50, 50, 50]]

cfg.analysis['plotRaster'] = {'timeRange': [0, cfg.duration], 'saveFig': True}
cfg.analysis['plotTraces'] = {'timeRange': [0, cfg.duration], 'include': [(pop, i) for pop in ('E','I') for i in range(10)], 'saveFig': True}  # Plot recorded traces for this list of cells
# cfg.analysis['plotLFPTimeSeries'] = {'showFig': True, 'saveFig': True}
#cfg.analysis['plotShape'] = {'includePre': ['all'],'includePost': [0,800,1000],'cvar':'numSyns','dist':0.7, 'saveFig': True}