#proper gt MCHI2_74_V3
#use auto:run2_mc_HIon for running in 75.
#use this menu: /users/zhchen/HISingleTrack/V16 for single track trigger
#use this menu: /users/ginnocen/HLTb_Jet80Tracking/V18 for b jet menu

#file:/afs/cern.ch/work/i/istaslis/public/forGM/step2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_PU_100_1_2fl.root
#root://xrootd.cmsaf.mit.edu//store/user/mnguyen/Hydjet_Quenched_MinBias_5020GeV/HydjetMB_740pre8_MCHI2_74_V3_53XBS_DIGI-RAW/6da45e4e90741bc03dbd9aec5f36c050/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_100_1_nRy.root

hltGetConfiguration /users/ginnocen/HLTHeavyFlavourTracking/V49 --full --offline --mc --unprescale --process TEST --globaltag 75X_mcRun2_HeavyIon_v1 --l1-emulator 'stage1,gt' --l1Xml L1Menu_CollisionsHeavyIons2015.v3.xml --output none --max-events 100 --input file:/afs/cern.ch/work/g/ginnocen/public/SamplesForHFHLTStudies/ExampleFiles/ExampleFileDFlatPt/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU_100_1_VHc.root > hlt_MC_stage1_TRK2_HIcode.py 

sed -i '/process = cms.Process( "TEST" )/a process.load("setup_cff")' hlt_MC_stage1_TRK2_HIcode.py

echo '' >> hlt_MC_stage1_TRK2_HIcode.py

#openHLT.root
echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> hlt_MC_stage1_TRK2_HIcode.py
echo 'process.hltbitanalysis.HLTProcessName = cms.string("TEST")' >> hlt_MC_stage1_TRK2_HIcode.py
echo 'process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )' >> hlt_MC_stage1_TRK2_HIcode.py
echo 'process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","TEST")' >> hlt_MC_stage1_TRK2_HIcode.py
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> hlt_MC_stage1_TRK2_HIcode.py
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> hlt_MC_stage1_TRK2_HIcode.py               
echo 'process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("openHLT.root"))' >> hlt_MC_stage1_TRK2_HIcode.py


echo 'process.load("HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi")'>> hlt_MC_stage1_TRK2_HIcode.py   ###TO BE ADDED TO RUN HIGENANALYZER
echo 'process.load("GeneratorInterface.HiGenCommon.HeavyIon_cff")'>> hlt_MC_stage1_TRK2_HIcode.py       ###TO BE ADDED TO RUN HIGENANALYZER

echo '' >> hlt_MC_stage1_TRK2_HIcode.py

echo '
# for HLT
if hasattr(process, "hltCsc2DRecHits"):
    process.hltCsc2DRecHits.wireDigiTag  = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")
    process.hltCsc2DRecHits.stripDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCStripDigi")
# for the L1 emulator
if hasattr(process, "cscReEmulTriggerPrimitiveDigis"):
    process.cscReEmulTriggerPrimitiveDigis.CSCComparatorDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi")
    process.cscReEmulTriggerPrimitiveDigis.CSCWireDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")
' >> hlt_MC_stage1_TRK2_HIcode.py

echo '' >> hlt_MC_stage1_TRK2_HIcode.py

echo '
from L1Trigger.L1TCommon.customsPostLS1 import customiseSimL1EmulatorForPostLS1_HI
customiseSimL1EmulatorForPostLS1_HI(process)
' >> hlt_MC_stage1_TRK2_HIcode.py

#echo ' 
#process.Output = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string ("output_HIIterTrackingV22_nRy.root"),
#    outputCommands = cms.untracked.vstring("keep *")
#)
#process.DQMOutput = cms.EndPath( process.Output )
#' >> hlt_MC_stage1_TRK2_HIcode.py

cmsRun hlt_MC_stage1_TRK2_HIcode.py >& triggerCheckMC_stage1_TRK2_HIcode.log


echo '                                                                             
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")    ###TO BE ADDED TO RUN HIGENANALYZER
process.HiGenParticleAna.stableOnly = cms.untracked.bool(False)                     ###TO BE ADDED TO RUN HIGENANALYZER
process.ana_step = cms.Path(process.heavyIon*                                       ###TO BE ADDED TO RUN HIGENANALYZER
      process.HiGenParticleAna                                                      ###TO BE ADDED TO RUN HIGENANALYZER
)                                                                                   ###TO BE ADDED TO RUN HIGENANALYZER
'>> hlt_MC_stage1_TRK2_HIcode.py

echo '
process.Timing=cms.Service("Timing",
    useJobReport = cms.untracked.bool(True)
    )

'>> hlt_MC_stage1_TRK2_HIcode.py


echo '
from CondCore.DBCommon.CondDBSetup_cfi import *
process.beamspot = cms.ESSource("PoolDBESSource",CondDBSetup,
                                toGet = cms.VPSet(cms.PSet( record = cms.string("BeamSpotObjectsRcd"),
                                                            tag= cms.string("RealisticHICollisions2011_STARTHI50_mc")
                                                            )),
                                connect =cms.string("frontier://FrontierProd/CMS_COND_31X_BEAMSPOT")
                                )
process.es_prefer_beamspot = cms.ESPrefer("PoolDBESSource","beamspot")
'>> hlt_MC_stage1_TRK2_HIcode.py
