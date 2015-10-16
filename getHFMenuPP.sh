#!bin/bash
#prev gt 75X_mcRun2_HeavyIon_v1

hltGetConfiguration /users/ginnocen/ppHLTHeavyFlavourTracking/V8 --full --offline --mc --process TEST --globaltag 75X_mcRun2_HeavyIon_v6 --l1-emulator 'stage1,gt' --l1Xml L1Menu_CollisionsHeavyIons2015.v3_KKHecked.xml --output none --max-events 20 --input  root://xrootd.cmsaf.mit.edu//store/user/twang/Pyquen_DiJet_pt40_5020GeV_GEN_SIM_PU_20150813/Pyquen_DiJet_pt40_5020GeV_step2_20150813/00a3c06d28c9e39d8c4f520dd28e45dd/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU_103_1_NAb.root > hlt_MC_stage1_PP.py

sed -i '/process = cms.Process( "TEST" )/a process.load("setup_cff")' hlt_MC_stage1_PP.py

echo 'process.load('\''L1Trigger.L1TCalorimeter.caloConfigStage1HI_cfi'\'')' >> hlt_MC_stage1_PP.py
echo 'process.caloStage1Params.regionPUSType = cms.string("zeroWall")' >> hlt_MC_stage1_PP.py

echo 'process.load("HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi")'>> hlt_MC_stage1_PP.py
echo 'process.load("GeneratorInterface.HiGenCommon.HeavyIon_cff")'>> hlt_MC_stage1_PP.py


#echo 'from L1Trigger.L1TCommon.customsPostLS1 import customiseSimL1EmulatorForPostLS1_HI
#customiseSimL1EmulatorForPostLS1_HI(process) ' >> hlt_MC_stage1_PP.py

#echo '' >> hlt_MC_stage1_PP.py

#perl -pi -e 's/ElectronicsMap = cms.string/#ElectronicsMap = cms.string/g' hlt_MC_stage1_PP.py

perl -pi -e 's/useHF = cms.untracked.bool/useHF = cms.bool/g' hlt_MC_stage1_PP.py
#perl -pi -e 's/L1_SingleMu3_BptxAND/L1_ZeroBias/g' hlt_MC_stage1_PP.py


echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> hlt_MC_stage1_PP.py
echo 'process.hltbitanalysis.HLTProcessName = cms.string("TEST")' >> hlt_MC_stage1_PP.py
echo 'process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )' >> hlt_MC_stage1_PP.py
echo 'process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","TEST")' >> hlt_MC_stage1_PP.py
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> hlt_MC_stage1_PP.py
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> hlt_MC_stage1_PP.py
echo 'process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("openHLT_HF.root"))' >> hlt_MC_stage1_PP.py
                                   
                                   
echo 'from CondCore.DBCommon.CondDBSetup_cfi import *
process.beamspot = cms.ESSource("PoolDBESSource",CondDBSetup,
                                toGet = cms.VPSet(cms.PSet( record = cms.string('\''BeamSpotObjectsRcd'\''),
                                                            tag= cms.string('\''RealisticHICollisions2011_STARTHI50_mc'\'')
                                                            )),
                                connect =cms.string('\''frontier://FrontierProd/CMS_COND_31X_BEAMSPOT'\'')
                                )
process.es_prefer_beamspot = cms.ESPrefer("PoolDBESSource","beamspot")' >> hlt_MC_stage1_PP.py
                                   

echo 'process.load('\''Configuration/StandardSequences/FrontierConditions_GlobalTag_condDBv2_cff'\'')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
recordOverrides = { ('\''L1RCTParametersRcd'\'', None) : ('\''L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactorsV4_HIDisabledFGHOE'\'', None) }
process.GlobalTag = GlobalTag(process.GlobalTag, '\''75X_mcRun2_HeavyIon_v6'\'', recordOverrides)
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")' >> hlt_MC_stage1_PP.py

### adding gen particle info & timing

echo '                                                                             
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")    
process.HiGenParticleAna.stableOnly = cms.untracked.bool(False)                     
process.ana_step = cms.Path(process.heavyIon*                                       
      process.HiGenParticleAna                                                      
)                                                                                   
'>> hlt_MC_stage1_PP.py

echo '
process.Timing=cms.Service("Timing",
    useJobReport = cms.untracked.bool(True)
    )
'>> hlt_MC_stage1_PP.py

cmsRun hlt_MC_stage1_PP.py >& triggerCheck.log