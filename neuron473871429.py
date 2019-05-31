'''
Defines a class, Neuron473871429, of neurons from Allen Brain Institute's model 473871429

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473871429:
    def __init__(self, name="Neuron473871429", x=0, y=0, z=0):
        '''Instantiate Neuron473871429.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473871429_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Nr5a1-Cre_Ai14_IVSCC_-177834.03.02.01_472399664_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473871429_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 100.0
            sec.e_pas = -90.0601425171
        for sec in self.apic:
            sec.cm = 2.57
            sec.g_pas = 0.000928244451449
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000437943770973
        for sec in self.dend:
            sec.cm = 2.57
            sec.g_pas = 9.90102776109e-05
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.00368293
            sec.gbar_Ih = 0.0341661
            sec.gbar_NaTs = 0.378086
            sec.gbar_Nap = 0.00036632
            sec.gbar_K_P = 0.00404644
            sec.gbar_K_T = 0.0016478
            sec.gbar_SK = 0.000105283
            sec.gbar_Kv3_1 = 0.475705
            sec.gbar_Ca_HVA = 0.000377324
            sec.gbar_Ca_LVA = 0.000807931
            sec.gamma_CaDynamics = 0.00788121
            sec.decay_CaDynamics = 765.429
            sec.g_pas = 2.70497e-06
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

