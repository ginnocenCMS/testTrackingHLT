from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'hlt_MC_stage1_TRK2_HIcode.py'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['rssLimit']
config.JobType.outputFiles = ['openHLT.root']
config.section_('Data')
config.Data.inputDataset = '/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/mnguyen-PyquenUnquenched_Dijet_pthat80_740pre8_MCHI2_74_V3_DIGI-RAW_v2-ee815b27030c232e2e0a7be48a50a463/USER'
config.Data.publication = False
config.Data.unitsPerJob = 100
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.publishDataName = 'Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_SingleTrackHLT'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_FR_GRIF_LLR']
config.Site.storageSite = 'T2_US_MIT'
