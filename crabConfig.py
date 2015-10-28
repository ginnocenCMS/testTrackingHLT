from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'hlt_MC_stage1.py'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['rssLimit']
config.JobType.outputFiles = ['openHLT.root']
config.section_('Data')
config.Data.inputDataset = '/Pyquen_D0tokaonpion_D0pt15p0_Pthat15_TuneZ2_Unquenched_5020GeV_GENSIM_75x_v2/mnguyen-D0pthat15-RECO_v2-2fbe1a61b2b7a96a0ed51c8b458e4279/USER'
config.Data.publication = False
config.Data.unitsPerJob = 100
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.publishDataName = '/store/user/ginnocen/HeavyFlavourHLT_MVA_41'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
