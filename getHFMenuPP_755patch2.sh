#!bin/bash
#prev gt 75X_mcRun2_HeavyIon_v1
#works in 755_patch1, not good setup for 755

hltGetConfiguration /users/ginnocen/GlobaTrackingPPmenuHFlowpu/V20 --full --offline --mc --unprescale --process TEST --globaltag 75X_mcRun2_asymptotic_ppAt5TeV_v0 --output none  --max-events -1 --l1-emulator 'stage1,gt' --l1Xml L1Menu_Collisions2015_5TeV_pp_reference_L1T_Scales_20141121.xml --input file:/afs/cern.ch/work/j/jisun/public/HFTrig_75x/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_1000_2_mqi.root > hlt_MC_stage1_pp_755patch2.py 

sed -i '/process = cms.Process( "TEST" )/a process.load("setup_cff")' hlt_MC_stage1_pp_755patch2.py

perl -pi -e 's/useHF = cms.untracked.bool/useHF = cms.bool/g' hlt_MC_stage1_pp_755patch2.py

echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> hlt_MC_stage1_pp_755patch2.py
echo 'process.hltbitanalysis.HLTProcessName = cms.string("TEST")' >> hlt_MC_stage1_pp_755patch2.py
echo 'process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )' >> hlt_MC_stage1_pp_755patch2.py
echo 'process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","TEST")' >> hlt_MC_stage1_pp_755patch2.py
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> hlt_MC_stage1_pp_755patch2.py
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> hlt_MC_stage1_pp_755patch2.py
echo 'process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("openHLT_HF.root"))' >> hlt_MC_stage1_pp_755patch2.py

echo 'process.load("L1Trigger.L1TCalorimeter.caloConfigStage1PP_cfi") ' >> hlt_MC_stage1_pp_755patch2.py
                                   
echo 'process.load('\''Configuration/StandardSequences/FrontierConditions_GlobalTag_condDBv2_cff'\'')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
recordOverrides = { ('\''L1RCTParametersRcd'\'', None) : ('\''L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactorsV4_HIDisabledFGHOE'\'', None) }
process.GlobalTag = GlobalTag(process.GlobalTag, '\''75X_mcRun2_asymptotic_ppAt5TeV_v0'\'', recordOverrides)
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")' >> hlt_MC_stage1_pp_755patch2.py

echo '
process.load('\''L1Trigger.L1TCalorimeter.caloStage1Params_cfi'\'')
process.caloStage1Params.jetSeedThreshold = cms.double(3.0)
process.caloStage1Params.jetCalibrationLUTFile = cms.FileInPath("L1Trigger/L1TCalorimeter/data/Jet_Stage1_2015_v3.txt")
process.caloStage1Params.regionPUSParams = cms.vdouble(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)+cms.vdouble(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
'>> hlt_MC_stage1_pp_755patch2.py

echo '
process.Timing=cms.Service("Timing",
    useJobReport = cms.untracked.bool(True)
    )
'>> hlt_MC_stage1_pp_755patch2.py
