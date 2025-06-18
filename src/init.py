from netpyne import sim  # import netpyne init module

# cfg, netParams = sim.loadFromIndexFile('index.npjson')
# read cfg and netParams from command line arguments if available; otherwise use default

# Mock up
# if not exists('x86_64'):
#     execute('nrnivmodl mod')
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='src/cfg.py', netParamsDefault='src/netParams.py')
sim.createSimulateAnalyze(netParams = netParams, simConfig = cfg)  # create and simulate network

## TODO: Calculate synchronization

## TODO: Change to HH models