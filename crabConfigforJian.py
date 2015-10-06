from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HeavyFlavourHLT_newRCT_V49_Dptflat0to150'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hlt_MC_stage1.py'
config.JobType.inputFiles = ['rssLimit']
config.JobType.outputFiles = ['openHLT.root']
config.Data.inputDataset = '/SingleD0FlatPt5To150_pythia8_5TeV_750auto_v2/mnguyen-SingleD0FlatPt5To150_pythia8_5TeV_750auto_RAW_v2-7d608b8a2b68a861141642eea11e19d3/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 100
config.Data.outLFNDirBase = '/store/user/ginnocen/HeavyFlavourHLT_newRCT_V49_Dptflat0to150'
config.Data.publication = False

config.Site.storageSite = 'T2_US_MIT'

config.Debug.extraJDL = ['+DESIRED_SITES="T2_US_MIT"']
