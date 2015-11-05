#!bin/bash
#prev gt 75X_mcRun2_HeavyIon_v1

hltGetConfiguration /users/ginnocen/HLTHeavyFlavourTrackingPPCutBased/V5 --full --offline --mc --unprescale --process TEST --globaltag 75X_mcRun2_asymptotic_v6 --l1-emulator 'stage1,gt' --l1Xml L1Menu_Collisions2015_lowPU_v4_L1T_Scales_20141121.xml --output none --max-events 20 --input root://xrootd.unl.edu//store/user/jisun/Pythia_D0pt15p0_Pthat15_TuneZ2_5020GeV_GENSIM_75x_1015/Pythia_D0pt15p0_Pthat15_TuneZ2_5020GeV_reco_75x_1015/94c15f02ac462193a29b82695967e4a9/step3_RAW2DIGI_L1Reco_RECO_100_1_wdG.root > hlt_MC_stage1.py 

sed -i '/process = cms.Process( "TEST" )/a process.load("setup_cff")' hlt_MC_stage1.py

echo 'process.load('\''L1Trigger.L1TCalorimeter.caloConfigStage1HI_cfi'\'')' >> hlt_MC_stage1.py
echo 'process.caloStage1Params.regionPUSType = cms.string("zeroWall")' >> hlt_MC_stage1.py

echo 'process.load("HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi")'>> hlt_MC_stage1.py
echo 'process.load("GeneratorInterface.HiGenCommon.HeavyIon_cff")'>> hlt_MC_stage1.py


#echo 'from L1Trigger.L1TCommon.customsPostLS1 import customiseSimL1EmulatorForPostLS1_HI
#customiseSimL1EmulatorForPostLS1_HI(process) ' >> hlt_MC_stage1.py

#echo '' >> hlt_MC_stage1.py

#perl -pi -e 's/ElectronicsMap = cms.string/#ElectronicsMap = cms.string/g' hlt_MC_stage1.py

perl -pi -e 's/useHF = cms.untracked.bool/useHF = cms.bool/g' hlt_MC_stage1.py
#perl -pi -e 's/L1_SingleMu3_BptxAND/L1_ZeroBias/g' hlt_MC_stage1.py


echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> hlt_MC_stage1.py
echo 'process.hltbitanalysis.HLTProcessName = cms.string("TEST")' >> hlt_MC_stage1.py
echo 'process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )' >> hlt_MC_stage1.py
echo 'process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","TEST")' >> hlt_MC_stage1.py
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> hlt_MC_stage1.py
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> hlt_MC_stage1.py
echo 'process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("openHLT_HF.root"))' >> hlt_MC_stage1.py
                                   

echo 'process.caloStage1Params.jetSeedThreshold = cms.double(3.0)' >> hlt_MC_stage1.py 
echo 'process.load("L1Trigger.L1TCalorimeter.caloConfigStage1PP_cfi")' >> hlt_MC_stage1.py
echo 'process.caloConfig' >> hlt_MC_stage1.py
                                   
echo 'process.load('\''Configuration/StandardSequences/FrontierConditions_GlobalTag_condDBv2_cff'\'')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
recordOverrides = { ('\''L1RCTParametersRcd'\'', None) : ('\''L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactors_NewTau_FullEGTransparency_v1'\'', None) }      
process.GlobalTag = GlobalTag(process.GlobalTag, '\''75X_mcRun2_asymptotic_v1'\'', recordOverrides)
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")' >>  hlt_MC_stage1.py

### adding gen particle info & timing

echo '                                                                             
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")    
process.HiGenParticleAna.stableOnly = cms.untracked.bool(False)                     
process.ana_step = cms.Path(process.heavyIon*                                       
      process.HiGenParticleAna                                                      
)                                                                                   
'>> hlt_MC_stage1.py

echo '
process.Timing=cms.Service("Timing",
    useJobReport = cms.untracked.bool(True)
    )
'>> hlt_MC_stage1.py

cmsRun hlt_MC_stage1.py >& triggerCheck.log
