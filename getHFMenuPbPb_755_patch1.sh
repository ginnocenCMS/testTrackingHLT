#!bin/bash
#prev gt 75X_mcRun2_HeavyIon_v1
#works in 755_patch1, not good setup for 755

hltGetConfiguration /users/ginnocen/HLTCleanedHFPbPbmenu755/V11 --full --offline --mc --process TEST --globaltag auto:run2_mc_HIon --l1-emulator 'stage1,gt' --l1Xml L1Menu_CollisionsHeavyIons2015_v3.xml --output none --max-events -1 --input  file:/afs/cern.ch/user/t/twang/public/HLTSamples/D0pt35/step3_RAW2DIGI_L1Reco_RECO_100_1_wFV.root > hlt_MC_stage1_PbPb_755_patch1.py

sed -i '/process = cms.Process( "TEST" )/a process.load("setup_cff")' hlt_MC_stage1_PbPb_755_patch1.py

perl -pi -e 's/useHF = cms.untracked.bool/useHF = cms.bool/g' hlt_MC_stage1_PbPb_755_patch1.py

echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> hlt_MC_stage1_PbPb_755_patch1.py
echo 'process.hltbitanalysis.HLTProcessName = cms.string("TEST")' >> hlt_MC_stage1_PbPb_755_patch1.py
echo 'process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )' >> hlt_MC_stage1_PbPb_755_patch1.py
echo 'process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","TEST")' >> hlt_MC_stage1_PbPb_755_patch1.py
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> hlt_MC_stage1_PbPb_755_patch1.py
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> hlt_MC_stage1_PbPb_755_patch1.py
echo 'process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("openHLT_HF.root"))' >> hlt_MC_stage1_PbPb_755_patch1.py

echo 'process.load('\''Configuration/StandardSequences/FrontierConditions_GlobalTag_condDBv2_cff'\'')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
recordOverrides = { ('\''L1RCTParametersRcd'\'', None) : ('\''L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactorsV4_HIDisabledFGHOE'\'', None) }
process.GlobalTag = GlobalTag(process.GlobalTag, '\''75X_mcRun2_HeavyIon_v7'\'', recordOverrides)
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")' >> hlt_MC_stage1_PbPb_755_patch1.py

#for D0 samples, need to overwrite the beamspot. But for Hyjet MB from Ta-wei, it should not be overwritten
#just needed if process samples related to HydjetMB_740pre8_MCHI2_74_V3_53XBS
echo 'from CondCore.DBCommon.CondDBSetup_cfi import *
process.beamspot = cms.ESSource("PoolDBESSource",CondDBSetup,
                                toGet = cms.VPSet(cms.PSet( record = cms.string('\''BeamSpotObjectsRcd'\''),
                                                            tag= cms.string('\''RealisticHICollisions2011_STARTHI50_mc'\'')
                                                            )),
                                connect =cms.string('\''frontier://FrontierProd/CMS_COND_31X_BEAMSPOT'\'')
                                )
process.es_prefer_beamspot = cms.ESPrefer("PoolDBESSource","beamspot")' >> hlt_MC_stage1_PbPb_755_patch1.py
                                   
echo '
process.load('\''L1Trigger.L1TCalorimeter.caloConfigStage1HI_cfi'\'')
process.load('\''L1Trigger.L1TCalorimeter.caloStage1Params_HI_cfi'\'')
'>> hlt_MC_stage1_PbPb_755_patch1.py

echo '
process.caloStage1Params.minimumBiasThresholds = cms.vint32(1,1,2,2)
'>> hlt_MC_stage1_PbPb_755_patch1.py

echo '
process.Timing=cms.Service("Timing",
    useJobReport = cms.untracked.bool(True)
    )
'>> hlt_MC_stage1_PbPb_755_patch1.py
