#!bin/bash
#prev gt 75X_mcRun2_HeavyIon_v1

hltGetConfiguration /users/ginnocen/HLTCleanedHFPbPbmenu755/V7 --full --offline --mc --process TEST --globaltag 75X_mcRun2_HeavyIon_v7 --l1-emulator 'stage1,gt' --l1Xml L1Menu_CollisionsHeavyIons2015_v2_L1T_Scales_20141121.xml --output none --max-events -1 --input  file:/afs/cern.ch/user/t/twang/public/HLTSamples/D0pt35/step3_RAW2DIGI_L1Reco_RECO_100_1_wFV.root > hlt_MC_stage1.py

sed -i '/process = cms.Process( "TEST" )/a process.load("setup_cff")' hlt_MC_stage1.py

echo 'process.load("HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi")'>> hlt_MC_stage1.py
echo 'process.load("GeneratorInterface.HiGenCommon.HeavyIon_cff")'>> hlt_MC_stage1.py

perl -pi -e 's/useHF = cms.untracked.bool/useHF = cms.bool/g' hlt_MC_stage1.py

echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> hlt_MC_stage1.py
echo 'process.hltbitanalysis.HLTProcessName = cms.string("TEST")' >> hlt_MC_stage1.py
echo 'process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )' >> hlt_MC_stage1.py
echo 'process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","TEST")' >> hlt_MC_stage1.py
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> hlt_MC_stage1.py
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> hlt_MC_stage1.py
echo 'process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("openHLT_HF.root"))' >> hlt_MC_stage1.py
                                   
                                   

#for D0 samples, need to overwrite the beamspot. But for Hyjet MB from Ta-wei, it should not be overwritten
echo 'from CondCore.DBCommon.CondDBSetup_cfi import *
process.beamspot = cms.ESSource("PoolDBESSource",CondDBSetup,
                                toGet = cms.VPSet(cms.PSet( record = cms.string('\''BeamSpotObjectsRcd'\''),
                                                            tag= cms.string('\''RealisticHICollisions2011_STARTHI50_mc'\'')
                                                            )),
                                connect =cms.string('\''frontier://FrontierProd/CMS_COND_31X_BEAMSPOT'\'')
                                )
process.es_prefer_beamspot = cms.ESPrefer("PoolDBESSource","beamspot")' >> hlt_MC_stage1.py
                                   

echo 'process.load('\''Configuration/StandardSequences/FrontierConditions_GlobalTag_condDBv2_cff'\'')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
recordOverrides = { ('\''L1RCTParametersRcd'\'', None) : ('\''L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactorsV4_HIDisabledFGHOE'\'', None) }
process.GlobalTag = GlobalTag(process.GlobalTag, '\''75X_mcRun2_HeavyIon_v7'\'', recordOverrides)
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")' >> hlt_MC_stage1.py

### adding gen particle info & timing

echo '                                                                             
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")    
process.HiGenParticleAna.stableOnly = cms.untracked.bool(False)                     
process.ana_step = cms.Path(process.heavyIon*                                       
      process.HiGenParticleAna                                                      
)                                                                                   
'>> hlt_MC_stage1.py

echo '
process.load('\''L1Trigger.L1TCalorimeter.caloConfigStage1HI_cfi'\'')
process.load('\''L1Trigger.L1TCalorimeter.caloStage1Params_HI_cfi'\'')
process.caloStage1Params.jetRegionMask = cms.int32(0b0000100000000000010000)
process.caloStage1Params.egEtaCut = cms.int32(0b0000001111111111000000)
process.caloStage1Params.tauRegionMask = cms.int32(0b1111111100000011111111)
process.caloStage1Params.centralityRegionMask = cms.int32(0b0000111111111111110000)
process.caloStage1Params.jetSeedThreshold = cms.double(0)
process.caloStage1Params.etSumEtThreshold        = cms.vdouble(0., 7.) #ET, HT
process.caloStage1Params.minimumBiasThresholds = cms.vint32(4,4,6,6)
process.caloStage1Params.centralityLUTFile = cms.FileInPath("L1Trigger/L1TCalorimeter/data/centrality_extended_LUT_preRun.txt")
'>> hlt_MC_stage1.py

echo '
process.Timing=cms.Service("Timing",
    useJobReport = cms.untracked.bool(True)
    )
'>> hlt_MC_stage1.py
