from netpyne import specs
from netpyne.batch import Batch

def batch():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        params['convergence'] = [5, 10, 20, 100]
        
        params['bkgRate'] = [1e-5, 20, 200, 2000]
        params['bkgNoise'] = [0.7]
        params['bkgDelay'] = ['uniform(0.8,1.2)']
        params['bkgSenderE'] = [0.3]
        params['bkgSenderI'] = [0]
        params['bkgReceiverE'] = [0]
        params['bkgReceiverI'] = [0]
        params['weightEE'] = [0.03]
        params['weightEI'] = [0.02]
        params['weightIE'] = [0.02]
        params['weightII'] = [0.01]
        params['delay'] = [1e-3]

        # create Batch object with parameters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='src/cfg.py', netParamsFile='src/netParams.py',)

        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'ASDS'
        b.saveFolder = 'ASDS_batch'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin',
                    'jobName': 'ASDS_batch',
                    'cores': 1,
                    'script': 'src/init.py',
                    'skip': True}

        # Run batch simulations
        b.run()

# Main code
if __name__ == '__main__':
        batch()