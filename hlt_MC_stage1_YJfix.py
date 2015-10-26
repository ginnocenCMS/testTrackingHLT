# /users/zhchen/HIIterTracking/V51 (CMSSW_7_5_3_patch1)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "TEST" )
process.load("setup_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/zhchen/HIIterTracking/V51')
)

process.hltESPCkfTrajectoryBuilderForHI = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "hltESPCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  intermediateCleaning = cms.bool( False ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTrackerForHI" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPCkfTrajectoryFilterForHI = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minPt = cms.double( 0.9 )
)
process.HLTPSetDetachedCkfTrajectoryBuilderForHI = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHI" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 0.0 ),
  maxPtForLooperReconstruction = cms.double( 0.0 ),
  bestHitOnly = cms.bool( True )
)
process.HLTPSetDetachedCkfTrajectoryFilterForHI = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 6 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 1 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  constantValueForLostHitsFractionFilter = cms.double( 0.701 )
)
process.HLTPSetLowPtCkfTrajectoryFilterForHI = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 6 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.4 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 1 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 )
)
process.HLTPSetLowPtCkfTrajectoryBuilderForHI = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 3 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtCkfTrajectoryFilterForHI" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  bestHitOnly = cms.bool( True )
)
process.HLTPSetPixelPairCkfTrajectoryFilterForHI = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  maxNumberOfHits = cms.int32( 100 )
)
process.HLTPSetPixelPairCkfTrajectoryBuilderForHI = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 3 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHI" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  bestHitOnly = cms.bool( True )
)
process.HLTSiStripClusterChargeCutForHI = cms.PSet(  value = cms.double( 2069.0 ) )
process.hltESPCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minPt = cms.double( 8.0 )
)
process.hltESPCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "hltESPCkfTrajectoryFilterForHIGlobalPt8" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  intermediateCleaning = cms.bool( False ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTrackerForHI" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetLowPtCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 6 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 8.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 1 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 )
)
process.HLTPSetLowPtCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtCkfTrajectoryFilterForHIGlobalPt8" ) ),
  maxCand = cms.int32( 3 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtCkfTrajectoryFilterForHIGlobalPt8" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  bestHitOnly = cms.bool( True )
)
process.HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 6 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 8.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 1 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  constantValueForLostHitsFractionFilter = cms.double( 0.701 )
)
process.HLTPSetDetachedCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8" ) ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 0.0 ),
  maxPtForLooperReconstruction = cms.double( 0.0 ),
  bestHitOnly = cms.bool( True )
)
process.HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet( 
  minPt = cms.double( 8.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  maxNumberOfHits = cms.int32( 100 )
)
process.HLTPSetPixelPairCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8" ) ),
  maxCand = cms.int32( 3 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  bestHitOnly = cms.bool( True )
)

process.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutForHI" ) ),
  nSigma = cms.double( 3.0 )
)
process.hltESPKFFittingSmootherForLoopers = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForLoopers" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForLoopers" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForLoopers" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForLoopers" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForLoopers" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.PropagatorWithMaterialForLoopers = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForLoopers" ),
  Mass = cms.double( 0.1396 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 4.0 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPFlexibleKFFittingSmoother = cms.ESProducer( "FlexibleKFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPFlexibleKFFittingSmoother" ),
  standardFitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  looperFitter = cms.string( "hltESPKFFittingSmootherForLoopers" )
)
process.hltESPRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPPixelCPETemplateReco = cms.ESProducer( "PixelCPETemplateRecoESProducer",
  DoLorentz = cms.bool( True ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPETemplateReco" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  speed = cms.int32( -2 ),
  UseClusterSplitter = cms.bool( False )
)
process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPRKTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPRKTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPFittingSmootherIT = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPFittingSmootherIT" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKTrajectorySmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPETemplateReco" ),
  ComponentName = cms.string( "hltESPTTRHBuilderAngleAndTemplate" )
)
process.hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedSeeds" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
)
process.MaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositeMaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPMeasurementTrackerForHI = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TID = cms.PSet( 
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTrackerForHI" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)

process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32( 813 ),
    Verbosity = cms.untracked.int32( 0 ),
    UnpackBxInEvent = cms.int32( 5 ),
    ActiveBoardsMask = cms.uint32( 0xffff ),
    DaqGtInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltCaloStage1Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage1::CaloSetup" ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    FWId = cms.uint32( 4294967295 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32(  ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltCaloStage1LegacyFormatDigis = cms.EDProducer( "L1TCaloUpgradeToGCTConverter",
    InputHFCountsCollection = cms.InputTag( 'hltCaloStage1Digis','HFBitCounts' ),
    InputHFSumsCollection = cms.InputTag( 'hltCaloStage1Digis','HFRingSums' ),
    bxMin = cms.int32( 0 ),
    bxMax = cms.int32( 0 ),
    InputCollection = cms.InputTag( "hltCaloStage1Digis" ),
    InputIsoTauCollection = cms.InputTag( 'hltCaloStage1Digis','isoTaus' ),
    InputRlxTauCollection = cms.InputTag( 'hltCaloStage1Digis','rlxTaus' )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( False ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    RecordLength = cms.vint32( 3, 0 ),
    TechnicalTriggersUnmasked = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    GmtInputTag = cms.InputTag( "hltGtDigis" ),
    TechnicalTriggersVetoUnmasked = cms.bool( True ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    CastorInputTag = cms.InputTag( "castorL1Digis" ),
    GctInputTag = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    BstLengthBytes = cms.int32( -1 )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    tauJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','tauJets' ),
    etHadSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    isoTauJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','isoTauJets' ),
    etTotalSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    centralBxOnly = cms.bool( True ),
    centralJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','cenJets' ),
    etMissSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    hfRingEtSumsSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    produceMuonParticles = cms.bool( True ),
    forwardJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','forJets' ),
    ignoreHtMiss = cms.bool( False ),
    htMissSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    produceCaloParticles = cms.bool( True ),
    muonSource = cms.InputTag( "hltGtDigis" ),
    isolatedEmSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','nonIsoEm' ),
    hfRingBitCountsSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" )
)
process.hltBPTXCoincidence = cms.EDFilter( "HLTLevel1Activity",
    technicalBits = cms.uint64( 0x1 ),
    ignoreL1Mask = cms.bool( True ),
    invert = cms.bool( False ),
    physicsLoBits = cms.uint64( 0x1 ),
    physicsHiBits = cms.uint64( 0x40000 ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    daqPartitions = cms.uint32( 1 ),
    bunchCrossings = cms.vint32( 0, -1, 1 )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltL1sZeroBias = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ZeroBias" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIIterativeTracking = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHISiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    IncludeErrors = cms.bool( False ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    UserErrorList = cms.vint32(  )
)
process.hltHISiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltHISiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( -1 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
process.hltHISiPixelClustersCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltHISiPixelClusters" ),
    onDemand = cms.bool( False )
)
process.hltHISiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltHISiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltHIPixelClusterVertices = cms.EDProducer( "HIPixelClusterVtxProducer",
    maxZ = cms.double( 30.0 ),
    zStep = cms.double( 0.1 ),
    minZ = cms.double( -30.0 ),
    pixelRecHits = cms.string( "hltHISiPixelRecHits" )
)
process.hltHIPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
process.hltHIPixel3ProtoTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      ComponentName = cms.string( "HIProtoTrackFilter" ),
      ptMin = cms.double( 1.0 ),
      tipMax = cms.double( 1.0 ),
      doVariablePtMin = cms.bool( True ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      siPixelRecHits = cms.InputTag( "hltHISiPixelRecHits" )
    ),
    passLabel = cms.string( "Pixel triplet tracks for vertexing" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "HITrackingRegionForPrimaryVtxProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.7 ),
        directionXCoord = cms.double( 1.0 ),
        directionZCoord = cms.double( 0.0 ),
        directionYCoord = cms.double( 1.0 ),
        useFoundVertices = cms.bool( True ),
        doVariablePtMin = cms.bool( True ),
        nSigmaZ = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFixedError = cms.bool( True ),
        fixedError = cms.double( 3.0 ),
        sigmaZVertex = cms.double( 3.0 ),
        siPixelRecHits = cms.InputTag( "hltHISiPixelRecHits" ),
        VertexCollection = cms.InputTag( "hltHIPixelClusterVertices" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.037 ),
        maxElement = cms.uint32( 100000 ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "none" ),
          clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
        )
      ),
      SeedingLayers = cms.InputTag( "hltHIPixelLayerTriplets" )
    )
)
process.hltHIPixelMedianVertex = cms.EDProducer( "HIPixelMedianVtxProducer",
    PeakFindThreshold = cms.uint32( 100 ),
    PeakFindMaxZ = cms.double( 30.0 ),
    FitThreshold = cms.int32( 5 ),
    TrackCollection = cms.InputTag( "hltHIPixel3ProtoTracks" ),
    PtMin = cms.double( 0.075 ),
    PeakFindBinsPerCm = cms.int32( 10 ),
    FitMaxZ = cms.double( 0.1 ),
    FitBinsPerCm = cms.int32( 500 )
)
process.hltHISelectedProtoTracks = cms.EDFilter( "HIProtoTrackSelection",
    src = cms.InputTag( "hltHIPixel3ProtoTracks" ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    maxD0Significance = cms.double( 5.0 ),
    minZCut = cms.double( 0.2 ),
    VertexCollection = cms.InputTag( "hltHIPixelMedianVertex" ),
    ptMin = cms.double( 0.0 ),
    nSigmaZ = cms.double( 5.0 )
)
process.hltHIPixelAdaptiveVertex = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  maxDistanceToBeam = cms.double( 0.1 ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "" )
      )
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet( 
      maxD0Significance = cms.double( 3.0 ),
      minPt = cms.double( 0.0 ),
      maxNormalizedChi2 = cms.double( 5.0 ),
      minSiliconLayersWithHits = cms.int32( 0 ),
      minPixelLayersWithHits = cms.int32( 2 ),
      trackQuality = cms.string( "any" ),
      numTracksThreshold = cms.int32( 2 ),
      algorithm = cms.string( "filterWithThreshold" )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltHISelectedProtoTracks" ),
    TkClusParameters = cms.PSet( 
      algorithm = cms.string( "gap" ),
      TkGapClusParameters = cms.PSet(  zSeparation = cms.double( 1.0 ) )
    )
)
process.hltHIBestAdaptiveVertex = cms.EDFilter( "HIBestVertexSelection",
    maxNumber = cms.uint32( 1 ),
    src = cms.InputTag( "hltHIPixelAdaptiveVertex" )
)
process.hltHISelectedVertex = cms.EDProducer( "HIBestVertexProducer",
    adaptiveVertexCollection = cms.InputTag( "hltHIBestAdaptiveVertex" ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    medianVertexCollection = cms.InputTag( "hltHIPixelMedianVertex" )
)
process.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltHITrackingSiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet( 
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "IteratedMedian" ),
      PedestalSubtractionFedMode = cms.bool( False ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( True ),
      useCMMeanMap = cms.bool( False ),
      CutToAvoidSignal = cms.double( 2.0 ),
      Fraction = cms.double( 0.2 ),
      minStripsToFit = cms.uint32( 4 ),
      consecThreshold = cms.uint32( 5 ),
      hitStripThreshold = cms.uint32( 40 ),
      Deviation = cms.uint32( 25 ),
      restoreThreshold = cms.double( 0.5 ),
      APVInspectMode = cms.string( "BaselineFollower" ),
      ForceNoRestore = cms.bool( False ),
      useRealMeanCM = cms.bool( False ),
      DeltaCMThreshold = cms.uint32( 20 ),
      nSigmaNoiseDerTh = cms.uint32( 4 ),
      nSaturatedStrip = cms.uint32( 2 ),
      APVRestoreMode = cms.string( "BaselineFollower" ),
      distortionThreshold = cms.uint32( 20 ),
      Iterations = cms.int32( 3 ),
      nSmooth = cms.uint32( 9 ),
      SelfSelectRestoreAlgo = cms.bool( False ),
      MeanCM = cms.int32( 0 ),
      CleaningSequence = cms.uint32( 1 ),
      slopeX = cms.int32( 3 ),
      slopeY = cms.int32( 4 ),
      ApplyBaselineRejection = cms.bool( True ),
      filteredBaselineMax = cms.double( 6.0 ),
      filteredBaselineDerivativeSumSquare = cms.double( 30.0 ),
      ApplyBaselineCleaner = cms.bool( True )
    ),
    Clusterizer = cms.PSet( 
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 ),
      setDetId = cms.bool( True ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    onDemand = cms.bool( False )
)
process.hltHISiStripClusters = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    stripClusterProducer = cms.string( "hltHITrackingSiStripRawToClustersFacility" ),
    pixelClusterProducer = cms.string( "hltHISiPixelClusters" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTrackerForHI" )
)
process.hltHIPixel3PrimTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( True ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      ComponentName = cms.string( "HIPixelTrackFilter" ),
      ptMin = cms.double( 0.9 ),
      tipMax = cms.double( 0.0 ),
      useClusterShape = cms.bool( False ),
      VertexCollection = cms.InputTag( "hltHISelectedVertex" ),
      nSigmaTipMaxTolerance = cms.double( 6.0 ),
      nSigmaLipMaxTolerance = cms.double( 0.0 ),
      lipMax = cms.double( 0.3 ),
      clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    passLabel = cms.string( "Pixel triplet primary tracks with vertex constraint" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.1 ),
        ptMin = cms.double( 0.9 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFoundVertices = cms.bool( True ),
        nSigmaZ = cms.double( 3.0 ),
        useFixedError = cms.bool( True ),
        fixedError = cms.double( 0.2 ),
        sigmaZVertex = cms.double( 3.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "TrackCleaner" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 1000000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "none" ),
          clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.037 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltHIPixelLayerTriplets" )
    )
)
process.hltHIPixelTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 1.0E9 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      propagator = cms.string( "PropagatorWithMaterialForHI" )
    ),
    InputVertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    InputCollection = cms.InputTag( "hltHIPixel3PrimTracks" ),
    originRadius = cms.double( 1.0E9 )
)
process.hltHIPrimTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIPixelTrackSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "none" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "hltESPCkfTrajectoryBuilderForHI" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHIGlobalPrimTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIPrimTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
    useHitsSplitting = cms.bool( True ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "initialStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter0TrackSelection = cms.EDProducer( "HIMultiTrackSelector",
    src = cms.InputTag( "hltHIGlobalPrimTracks" ),
    trackSelectors = cms.VPSet( 
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "loose" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( False ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 0.4, 4.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.2 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -1.0 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiInitialStepLoose" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 9999.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 0.4, 4.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "tight" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        dz_par2 = cms.vdouble( 5.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        nSigmaZ = cms.double( 9999.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.075 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.38 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiInitialStepTight" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.25 ),
        preFilterName = cms.string( "hiInitialStepLoose" ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 5.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "highPurity" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 3.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.05 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.77 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiInitialStep" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.15 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 3.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "hiInitialStepTight" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      )
    ),
    GBRForestLabel = cms.string( "HIMVASelectorIter4" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    GBRForestVars = cms.vstring( 'chi2perdofperlayer',
      'dxyperdxyerror',
      'dzperdzerror',
      'nhits',
      'nlayers',
      'eta' ),
    useVtxError = cms.bool( True ),
    useAnyMVA = cms.bool( True ),
    useVertices = cms.bool( True )
)
#process.hltHIIter1ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
 #   minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
 #   maxChi2 = cms.double( 9.0 ),
  #  trajectories = cms.InputTag( "hltHIGlobalPrimTracks" ),
   # oldClusterRemovalInfo = cms.InputTag( "" ),
    #stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacility" ),
 #   overrideTrkQuals = cms.InputTag( 'hltHIIter0TrackSelection','hiInitialStep' ),
  #  pixelClusters = cms.InputTag( "hltHISiPixelClusters" ),
   # TrackQuality = cms.string( "highPurity" )
#)

process.hltHIIter1ClustersRefRemoval = cms.EDProducer("HITrackClusterRemover",
     clusterLessSolution = cms.bool(True),
     trajectories = cms.InputTag("hltHIGlobalPrimTracks"),
     overrideTrkQuals = cms.InputTag( 'hltHIIter0TrackSelection','hiInitialStep' ),
     TrackQuality = cms.string('highPurity'),
     minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
     pixelClusters = cms.InputTag("hltHISiPixelClusters"),
     stripClusters = cms.InputTag("hltHITrackingSiStripRawToClustersFacility"),
     Common = cms.PSet(
         maxChi2 = cms.double(9.0),
     ),
     Strip = cms.PSet(
        # Yen-Jie's mod to preserve merged clusters
        maxSize = cms.uint32(2),
        maxChi2 = cms.double(9.0)
     )
)
process.hltHIIter1MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltHIIter1ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltHISiStripClusters" )
)
process.hltHIDetachedPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      skipClusters = cms.InputTag( "hltHIIter1ClustersRefRemoval" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      skipClusters = cms.InputTag( "hltHIIter1ClustersRefRemoval" )
    ),
    TIB = cms.PSet(  )
)
process.hltHIDetachedPixelTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( True ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      ComponentName = cms.string( "HIPixelTrackFilter" ),
      ptMin = cms.double( 0.95 ),
      tipMax = cms.double( 1.0 ),
      useClusterShape = cms.bool( False ),
      VertexCollection = cms.InputTag( "hltHISelectedVertex" ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      nSigmaLipMaxTolerance = cms.double( 0.0 ),
      lipMax = cms.double( 1.0 ),
      clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    passLabel = cms.string( "Pixel detached tracks with vertex constraint" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.5 ),
        ptMin = cms.double( 0.9 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFoundVertices = cms.bool( True ),
        nSigmaZ = cms.double( 4.0 ),
        useFixedError = cms.bool( True ),
        fixedError = cms.double( 0.5 ),
        sigmaZVertex = cms.double( 4.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "TrackCleaner" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 1000000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.0 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.0 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltHIDetachedPixelLayerTriplets" )
    )
)
process.hltHIDetachedPixelTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 1.0E9 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      propagator = cms.string( "PropagatorWithMaterialForHI" )
    ),
    InputVertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    InputCollection = cms.InputTag( "hltHIDetachedPixelTracks" ),
    originRadius = cms.double( 1.0E9 )
)
process.hltHIDetachedTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIDetachedPixelTrackSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter1MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryBuilderForHI" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHIDetachedGlobalPrimTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIDetachedTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter1MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "detachedTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter1TrackSelection = cms.EDProducer( "HIMultiTrackSelector",
    src = cms.InputTag( "hltHIDetachedGlobalPrimTracks" ),
    trackSelectors = cms.VPSet( 
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "loose" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( False ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 0.4, 4.0 ),
        applyAdaptedPVCuts = cms.bool( False ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.2 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -1.0 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiDetachedTripletStepLoose" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 9999.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 0.4, 4.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "tight" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        dz_par2 = cms.vdouble( 5.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( False ),
        min_eta = cms.double( -9999.0 ),
        nSigmaZ = cms.double( 9999.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.075 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.2 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiDetachedTripletStepTight" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.25 ),
        preFilterName = cms.string( "hiDetachedTripletStepLoose" ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 5.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "highPurity" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 3.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( False ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.05 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.09 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiDetachedTripletStep" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.15 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 3.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "hiDetachedTripletStepTight" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      )
    ),
    GBRForestLabel = cms.string( "HIMVASelectorIter7" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    GBRForestVars = cms.vstring( 'chi2perdofperlayer',
      'nhits',
      'nlayers',
      'eta' ),
    useVtxError = cms.bool( True ),
    useAnyMVA = cms.bool( True ),
    useVertices = cms.bool( True )
)
process.hltHIIter2ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltHIDetachedGlobalPrimTracks" ),
    oldClusterRemovalInfo = cms.InputTag( "hltHIIter1ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( 'hltHIIter1TrackSelection','hiDetachedTripletStep' ),
    pixelClusters = cms.InputTag( "hltHISiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltHIIter2MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltHIIter2ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltHISiStripClusters" )
)
process.hltHIPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      skipClusters = cms.InputTag( "hltHIIter2ClustersRefRemoval" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      skipClusters = cms.InputTag( "hltHIIter2ClustersRefRemoval" )
    ),
    TIB = cms.PSet(  )
)
process.hltHIPixelPairSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.005 ),
        ptMin = cms.double( 0.9 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFixedError = cms.bool( False ),
        sigmaZVertex = cms.double( 4.0 ),
        fixedError = cms.double( 0.2 ),
        useFoundVertices = cms.bool( True ),
        useFakeVertices = cms.bool( False ),
        nSigmaZ = cms.double( 4.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      FilterAtHelixStage = cms.bool( True ),
      FilterPixelHits = cms.bool( True ),
      FilterStripHits = cms.bool( False ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    ClusterCheckPSet = cms.PSet( 
      PixelClusterCollectionLabel = cms.InputTag( "hltHISiPixelClusters" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltHISiStripClusters" ),
      MaxNumberOfPixelClusters = cms.uint32( 500000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 5000000 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      GeneratorPSet = cms.PSet( 
        maxElement = cms.uint32( 5000000 ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
      ),
      SeedingLayers = cms.InputTag( "hltHIPixelLayerPairs" )
    ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreatorIT" ) )
)
process.hltHIPixelPairTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIPixelPairSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter2MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryBuilderForHI" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHIPixelPairGlobalPrimTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIPixelPairTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter2MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( True ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "pixelPairStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter2TrackSelection = cms.EDProducer( "HIMultiTrackSelector",
    src = cms.InputTag( "hltHIPixelPairGlobalPrimTracks" ),
    trackSelectors = cms.VPSet( 
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "loose" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( False ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 0.4, 4.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.2 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -1.0 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiPixelPairStepLoose" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 9999.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 0.4, 4.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "tight" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        dz_par2 = cms.vdouble( 5.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        nSigmaZ = cms.double( 9999.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.075 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.58 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiPixelPairStepTight" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.25 ),
        preFilterName = cms.string( "hiPixelPairStepLoose" ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 5.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "highPurity" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 3.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.05 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( 0.77 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiPixelPairStep" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.15 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 3.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "hiPixelPairStepTight" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      )
    ),
    GBRForestLabel = cms.string( "HIMVASelectorIter6" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    GBRForestVars = cms.vstring( 'chi2perdofperlayer',
      'dxyperdxyerror',
      'dzperdzerror',
      'nhits',
      'nlayers',
      'eta' ),
    useVtxError = cms.bool( True ),
    useAnyMVA = cms.bool( True ),
    useVertices = cms.bool( True )
)
process.hltHIIterTrackingMergedHighPurity = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( False ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltHIIter0TrackSelection:hiInitialStep','hltHIIter1TrackSelection:hiDetachedTripletStep','hltHIIter2TrackSelection:hiPixelPairStep' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( True ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( True ),
        tLists = cms.vint32( 0, 1, 2 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 1, 1, 1 ),
    TrackProducers = cms.VInputTag( 'hltHIGlobalPrimTracks','hltHIDetachedGlobalPrimTracks','hltHIPixelPairGlobalPrimTracks' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
process.hltHIIterTrackingMergedTight = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( False ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltHIIter0TrackSelection:hiInitialStepTight','hltHIIter1TrackSelection:hiDetachedTripletStepTight','hltHIIter2TrackSelection:hiPixelPairStepTight' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( True ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( True ),
        tLists = cms.vint32( 0, 1, 2 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 1, 1, 1 ),
    TrackProducers = cms.VInputTag( 'hltHIGlobalPrimTracks','hltHIDetachedGlobalPrimTracks','hltHIPixelPairGlobalPrimTracks' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltPreHIIterativeTrackingForGlobalPt8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIPixel3PrimTracksForGlobalPt8 = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( True ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      ComponentName = cms.string( "HIPixelTrackFilter" ),
      ptMin = cms.double( 8.0 ),
      tipMax = cms.double( 0.0 ),
      useClusterShape = cms.bool( False ),
      VertexCollection = cms.InputTag( "hltHISelectedVertex" ),
      nSigmaTipMaxTolerance = cms.double( 6.0 ),
      nSigmaLipMaxTolerance = cms.double( 0.0 ),
      lipMax = cms.double( 0.3 ),
      clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    passLabel = cms.string( "Pixel triplet primary tracks with vertex constraint" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.1 ),
        ptMin = cms.double( 4.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFoundVertices = cms.bool( True ),
        nSigmaZ = cms.double( 3.0 ),
        useFixedError = cms.bool( True ),
        fixedError = cms.double( 0.2 ),
        sigmaZVertex = cms.double( 3.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "TrackCleaner" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 1000000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "none" ),
          clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.037 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltHIPixelLayerTriplets" )
    )
)
process.hltHIPixelTrackSeedsForGlobalPt8 = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 1.0E9 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      propagator = cms.string( "PropagatorWithMaterialForHI" )
    ),
    InputVertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    InputCollection = cms.InputTag( "hltHIPixel3PrimTracksForGlobalPt8" ),
    originRadius = cms.double( 1.0E9 )
)
process.hltHIPrimTrackCandidatesForGlobalPt8 = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIPixelTrackSeedsForGlobalPt8" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "none" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "hltESPCkfTrajectoryBuilderForHIGlobalPt8" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHIGlobalPrimTracksForGlobalPt8 = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIPrimTrackCandidatesForGlobalPt8" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
    useHitsSplitting = cms.bool( True ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "initialStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter0TrackSelectionForGlobalPt8 = cms.EDProducer( "HIMultiTrackSelector",
    src = cms.InputTag( "hltHIGlobalPrimTracksForGlobalPt8" ),
    trackSelectors = cms.VPSet( 
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "loose" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( False ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 0.4, 4.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.2 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -1.0 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiInitialStepLoose" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 9999.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 0.4, 4.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "tight" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        dz_par2 = cms.vdouble( 5.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        nSigmaZ = cms.double( 9999.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.075 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.38 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiInitialStepTight" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.25 ),
        preFilterName = cms.string( "hiInitialStepLoose" ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 5.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "highPurity" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 3.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.05 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.77 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiInitialStep" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.15 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 3.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "hiInitialStepTight" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      )
    ),
    GBRForestLabel = cms.string( "HIMVASelectorIter4" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    GBRForestVars = cms.vstring( 'chi2perdofperlayer',
      'dxyperdxyerror',
      'dzperdzerror',
      'nhits',
      'nlayers',
      'eta' ),
    useVtxError = cms.bool( True ),
    useAnyMVA = cms.bool( True ),
    useVertices = cms.bool( True )
)
process.hltHIIter1ClustersRefRemovalForGlobalPt8 = cms.EDProducer( "TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltHIGlobalPrimTracksForGlobalPt8" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( 'hltHIIter0TrackSelectionForGlobalPt8','hiInitialStep' ),
    pixelClusters = cms.InputTag( "hltHISiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltHIIter1MaskedMeasurementTrackerEventForGlobalPt8 = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltHIIter1ClustersRefRemovalForGlobalPt8" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltHISiStripClusters" )
)
process.hltHIDetachedPixelLayerTripletsForGlobalPt8 = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      skipClusters = cms.InputTag( "hltHIIter1ClustersRefRemovalForGlobalPt8" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      skipClusters = cms.InputTag( "hltHIIter1ClustersRefRemovalForGlobalPt8" )
    ),
    TIB = cms.PSet(  )
)
process.hltHIDetachedPixelTracksForGlobalPt8 = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( True ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      ComponentName = cms.string( "HIPixelTrackFilter" ),
      ptMin = cms.double( 8.0 ),
      tipMax = cms.double( 1.0 ),
      useClusterShape = cms.bool( False ),
      VertexCollection = cms.InputTag( "hltHISelectedVertex" ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      nSigmaLipMaxTolerance = cms.double( 0.0 ),
      lipMax = cms.double( 1.0 ),
      clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    passLabel = cms.string( "Pixel detached tracks with vertex constraint" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.5 ),
        ptMin = cms.double( 4.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFoundVertices = cms.bool( True ),
        nSigmaZ = cms.double( 4.0 ),
        useFixedError = cms.bool( True ),
        fixedError = cms.double( 0.5 ),
        sigmaZVertex = cms.double( 4.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "TrackCleaner" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 1000000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.0 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.0 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltHIDetachedPixelLayerTripletsForGlobalPt8" )
    )
)
process.hltHIDetachedPixelTrackSeedsForGlobalPt8 = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 1.0E9 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      propagator = cms.string( "PropagatorWithMaterialForHI" )
    ),
    InputVertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    InputCollection = cms.InputTag( "hltHIDetachedPixelTracksForGlobalPt8" ),
    originRadius = cms.double( 1.0E9 )
)
process.hltHIDetachedTrackCandidatesForGlobalPt8 = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIDetachedPixelTrackSeedsForGlobalPt8" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter1MaskedMeasurementTrackerEventForGlobalPt8" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryBuilderForHIGlobalPt8" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHIDetachedGlobalPrimTracksForGlobalPt8 = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIDetachedTrackCandidatesForGlobalPt8" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter1MaskedMeasurementTrackerEventForGlobalPt8" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "detachedTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter1TrackSelectionForGlobalPt8 = cms.EDProducer( "HIMultiTrackSelector",
    src = cms.InputTag( "hltHIDetachedGlobalPrimTracksForGlobalPt8" ),
    trackSelectors = cms.VPSet( 
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "loose" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( False ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 0.4, 4.0 ),
        applyAdaptedPVCuts = cms.bool( False ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.2 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -1.0 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiDetachedTripletStepLoose" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 9999.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 0.4, 4.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "tight" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        dz_par2 = cms.vdouble( 5.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( False ),
        min_eta = cms.double( -9999.0 ),
        nSigmaZ = cms.double( 9999.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.075 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.2 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiDetachedTripletStepTight" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.25 ),
        preFilterName = cms.string( "hiDetachedTripletStepLoose" ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 5.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "highPurity" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 3.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( False ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.05 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.09 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiDetachedTripletStep" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.15 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 3.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "hiDetachedTripletStepTight" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      )
    ),
    GBRForestLabel = cms.string( "HIMVASelectorIter7" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    GBRForestVars = cms.vstring( 'chi2perdofperlayer',
      'nhits',
      'nlayers',
      'eta' ),
    useVtxError = cms.bool( True ),
    useAnyMVA = cms.bool( True ),
    useVertices = cms.bool( True )
)
process.hltHIIter2ClustersRefRemovalForGlobalPt8 = cms.EDProducer( "TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltHIDetachedGlobalPrimTracksForGlobalPt8" ),
    oldClusterRemovalInfo = cms.InputTag( "hltHIIter1ClustersRefRemovalForGlobalPt8" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( 'hltHIIter1TrackSelectionForGlobalPt8','hiDetachedTripletStep' ),
    pixelClusters = cms.InputTag( "hltHISiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltHIIter2MaskedMeasurementTrackerEventForGlobalPt8 = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltHIIter2ClustersRefRemovalForGlobalPt8" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltHISiStripClusters" )
)
process.hltHIPixelLayerPairsForGlobalPt8 = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      skipClusters = cms.InputTag( "hltHIIter2ClustersRefRemovalForGlobalPt8" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      skipClusters = cms.InputTag( "hltHIIter2ClustersRefRemovalForGlobalPt8" )
    ),
    TIB = cms.PSet(  )
)
process.hltHIPixelPairSeedsForGlobalPt8 = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.005 ),
        ptMin = cms.double( 4.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFixedError = cms.bool( False ),
        sigmaZVertex = cms.double( 4.0 ),
        fixedError = cms.double( 0.2 ),
        useFoundVertices = cms.bool( True ),
        useFakeVertices = cms.bool( False ),
        nSigmaZ = cms.double( 4.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      FilterAtHelixStage = cms.bool( True ),
      FilterPixelHits = cms.bool( True ),
      FilterStripHits = cms.bool( False ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    ClusterCheckPSet = cms.PSet( 
      PixelClusterCollectionLabel = cms.InputTag( "hltHISiPixelClusters" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltHISiStripClusters" ),
      MaxNumberOfPixelClusters = cms.uint32( 500000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 5000000 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      GeneratorPSet = cms.PSet( 
        maxElement = cms.uint32( 5000000 ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
      ),
      SeedingLayers = cms.InputTag( "hltHIPixelLayerPairsForGlobalPt8" )
    ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreatorIT" ) )
)
process.hltHIPixelPairTrackCandidatesForGlobalPt8 = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIPixelPairSeedsForGlobalPt8" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter2MaskedMeasurementTrackerEventForGlobalPt8" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryBuilderForHIGlobalPt8" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHIPixelPairGlobalPrimTracksForGlobalPt8 = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIPixelPairTrackCandidatesForGlobalPt8" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter2MaskedMeasurementTrackerEventForGlobalPt8" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( True ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "pixelPairStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter2TrackSelectionForGlobalPt8 = cms.EDProducer( "HIMultiTrackSelector",
    src = cms.InputTag( "hltHIPixelPairGlobalPrimTracksForGlobalPt8" ),
    trackSelectors = cms.VPSet( 
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "loose" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( False ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 0.4, 4.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.2 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -1.0 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiPixelPairStepLoose" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 9999.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 0.4, 4.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "tight" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        dz_par2 = cms.vdouble( 5.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        nSigmaZ = cms.double( 9999.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.075 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( -0.58 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiPixelPairStepTight" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.25 ),
        preFilterName = cms.string( "hiPixelPairStepLoose" ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 5.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        minHitsToBypassChecks = cms.uint32( 999 )
      ),
      cms.PSet(  max_d0 = cms.double( 100.0 ),
        minNumber3DLayers = cms.uint32( 0 ),
        max_lostHitFraction = cms.double( 1.0 ),
        applyAbsCutsIfNoPV = cms.bool( False ),
        qualityBit = cms.string( "highPurity" ),
        minNumberLayers = cms.uint32( 0 ),
        useMVA = cms.bool( True ),
        nSigmaZ = cms.double( 9999.0 ),
        dz_par2 = cms.vdouble( 3.0, 0.0 ),
        applyAdaptedPVCuts = cms.bool( True ),
        min_eta = cms.double( -9999.0 ),
        dz_par1 = cms.vdouble( 9999.0, 0.0 ),
        copyTrajectories = cms.untracked.bool( True ),
        vtxNumber = cms.int32( -1 ),
        keepAllTracks = cms.bool( False ),
        maxNumberLostLayers = cms.uint32( 999 ),
        max_relpterr = cms.double( 0.05 ),
        copyExtras = cms.untracked.bool( True ),
        minMVA = cms.double( 0.77 ),
        vertexCut = cms.string( "" ),
        max_z0 = cms.double( 100.0 ),
        min_nhits = cms.uint32( 8 ),
        name = cms.string( "hiPixelPairStep" ),
        max_minMissHitOutOrIn = cms.int32( 99 ),
        chi2n_no1Dmod_par = cms.double( 0.15 ),
        res_par = cms.vdouble( 99999.0, 99999.0 ),
        chi2n_par = cms.double( 0.3 ),
        max_eta = cms.double( 9999.0 ),
        d0_par2 = cms.vdouble( 3.0, 0.0 ),
        d0_par1 = cms.vdouble( 9999.0, 0.0 ),
        preFilterName = cms.string( "hiPixelPairStepTight" ),
        minHitsToBypassChecks = cms.uint32( 999 )
      )
    ),
    GBRForestLabel = cms.string( "HIMVASelectorIter6" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    GBRForestVars = cms.vstring( 'chi2perdofperlayer',
      'dxyperdxyerror',
      'dzperdzerror',
      'nhits',
      'nlayers',
      'eta' ),
    useVtxError = cms.bool( True ),
    useAnyMVA = cms.bool( True ),
    useVertices = cms.bool( True )
)
process.hltHIIterTrackingMergedHighPurityForGlobalPt8 = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( False ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltHIIter0TrackSelectionForGlobalPt8:hiInitialStep','hltHIIter1TrackSelectionForGlobalPt8:hiDetachedTripletStep','hltHIIter2TrackSelectionForGlobalPt8:hiPixelPairStep' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( True ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( True ),
        tLists = cms.vint32( 0, 1, 2 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 1, 1, 1 ),
    TrackProducers = cms.VInputTag( 'hltHIGlobalPrimTracksForGlobalPt8','hltHIDetachedGlobalPrimTracksForGlobalPt8','hltHIPixelPairGlobalPrimTracksForGlobalPt8' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
process.hltHIIterTrackingMergedTightForGlobalPt8 = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( False ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltHIIter0TrackSelectionForGlobalPt8:hiInitialStepTight','hltHIIter1TrackSelectionForGlobalPt8:hiDetachedTripletStepTight','hltHIIter2TrackSelectionForGlobalPt8:hiPixelPairStepTight' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( True ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( True ),
        tLists = cms.vint32( 0, 1, 2 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 1, 1, 1 ),
    TrackProducers = cms.VInputTag( 'hltHIGlobalPrimTracksForGlobalPt8','hltHIDetachedGlobalPrimTracksForGlobalPt8','hltHIPixelPairGlobalPrimTracksForGlobalPt8' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltCaloStage1Digis + process.hltCaloStage1LegacyFormatDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequenceBPTX = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.hltBPTXCoincidence + process.HLTBeamSpot )
process.HLTDoHILocalPixelSequence = cms.Sequence( process.hltHISiPixelDigis + process.hltHISiPixelClusters + process.hltHISiPixelClustersCache + process.hltHISiPixelRecHits )
process.HLTHIRecopixelvetexingSequence = cms.Sequence( process.hltHIPixelClusterVertices + process.hltHIPixelLayerTriplets + process.hltHIPixel3ProtoTracks + process.hltHIPixelMedianVertex + process.hltHISelectedProtoTracks + process.hltHIPixelAdaptiveVertex + process.hltHIBestAdaptiveVertex + process.hltHISelectedVertex )
process.HLTDoHITrackingLocalStripSequence = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltHITrackingSiStripRawToClustersFacility + process.hltHISiStripClusters )
process.HLTHIIterativeTrackingIteration0 = cms.Sequence( process.hltHIPixel3PrimTracks + process.hltHIPixelTrackSeeds + process.hltHIPrimTrackCandidates + process.hltHIGlobalPrimTracks + process.hltHIIter0TrackSelection )
process.HLTHIIterativeTrackingIteration1 = cms.Sequence( process.hltHIIter1ClustersRefRemoval + process.hltHIIter1MaskedMeasurementTrackerEvent + process.hltHIDetachedPixelLayerTriplets + process.hltHIDetachedPixelTracks + process.hltHIDetachedPixelTrackSeeds + process.hltHIDetachedTrackCandidates + process.hltHIDetachedGlobalPrimTracks + process.hltHIIter1TrackSelection )
process.HLTHIIterativeTrackingIteration2 = cms.Sequence( process.hltHIIter2ClustersRefRemoval + process.hltHIIter2MaskedMeasurementTrackerEvent + process.hltHIPixelLayerPairs + process.hltHIPixelPairSeeds + process.hltHIPixelPairTrackCandidates + process.hltHIPixelPairGlobalPrimTracks + process.hltHIIter2TrackSelection )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTHIIterativeTrackingIteration0ForGlobalPt8 = cms.Sequence( process.hltHIPixel3PrimTracksForGlobalPt8 + process.hltHIPixelTrackSeedsForGlobalPt8 + process.hltHIPrimTrackCandidatesForGlobalPt8 + process.hltHIGlobalPrimTracksForGlobalPt8 + process.hltHIIter0TrackSelectionForGlobalPt8 )
process.HLTHIIterativeTrackingIteration1ForGlobalPt8 = cms.Sequence( process.hltHIIter1ClustersRefRemovalForGlobalPt8 + process.hltHIIter1MaskedMeasurementTrackerEventForGlobalPt8 + process.hltHIDetachedPixelLayerTripletsForGlobalPt8 + process.hltHIDetachedPixelTracksForGlobalPt8 + process.hltHIDetachedPixelTrackSeedsForGlobalPt8 + process.hltHIDetachedTrackCandidatesForGlobalPt8 + process.hltHIDetachedGlobalPrimTracksForGlobalPt8 + process.hltHIIter1TrackSelectionForGlobalPt8 )
process.HLTHIIterativeTrackingIteration2ForGlobalPt8 = cms.Sequence( process.hltHIIter2ClustersRefRemovalForGlobalPt8 + process.hltHIIter2MaskedMeasurementTrackerEventForGlobalPt8 + process.hltHIPixelLayerPairsForGlobalPt8 + process.hltHIPixelPairSeedsForGlobalPt8 + process.hltHIPixelPairTrackCandidatesForGlobalPt8 + process.hltHIPixelPairGlobalPrimTracksForGlobalPt8 + process.hltHIIter2TrackSelectionForGlobalPt8 )

process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltBoolFalse )
process.HLT_HIIterativeTracking_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sZeroBias + process.hltPreHIIterativeTracking + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHITrackingLocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.HLTHIIterativeTrackingIteration2 + process.hltHIIterTrackingMergedHighPurity + process.hltHIIterTrackingMergedTight + process.HLTEndSequence )
process.HLT_HIIterativeTrackingForGlobalPt8_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sZeroBias + process.hltPreHIIterativeTrackingForGlobalPt8 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHITrackingLocalStripSequence + process.HLTHIIterativeTrackingIteration0ForGlobalPt8 + process.HLTHIIterativeTrackingIteration1ForGlobalPt8 + process.HLTHIIterativeTrackingIteration2ForGlobalPt8 + process.hltHIIterTrackingMergedHighPurityForGlobalPt8 + process.hltHIIterTrackingMergedTightForGlobalPt8 + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtDigis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW )


process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.HLT_HIIterativeTracking_v1, process.HLT_HIIterativeTrackingForGlobalPt8_v1, process.HLTriggerFinalPath ))


process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/afs/cern.ch/user/t/twang/public/HLTSamples/D0pt35/step3_RAW2DIGI_L1Reco_RECO_100_1_wFV.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# adapt HLT modules to the correct process name
if 'hltTrigReport' in process.__dict__:
    process.hltTrigReport.HLTriggerResults                    = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressCosmicsOutputSmart' in process.__dict__:
    process.hltPreExpressCosmicsOutputSmart.hltResults = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressOutputSmart' in process.__dict__:
    process.hltPreExpressOutputSmart.hltResults        = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForHIOutputSmart' in process.__dict__:
    process.hltPreDQMForHIOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForPPOutputSmart' in process.__dict__:
    process.hltPreDQMForPPOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMResultsOutputSmart' in process.__dict__:
    process.hltPreHLTDQMResultsOutputSmart.hltResults  = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMOutputSmart' in process.__dict__:
    process.hltPreHLTDQMOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTMONOutputSmart' in process.__dict__:
    process.hltPreHLTMONOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltDQMHLTScalers' in process.__dict__:
    process.hltDQMHLTScalers.triggerResults                   = cms.InputTag( 'TriggerResults', '', 'TEST' )
    process.hltDQMHLTScalers.processname                      = 'TEST'

if 'hltDQML1SeedLogicScalers' in process.__dict__:
    process.hltDQML1SeedLogicScalers.processname              = 'TEST'

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '75X_mcRun2_HeavyIon_v6')
    process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'
    process.GlobalTag.pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
    for pset in process.GlobalTag.toGet.value():
        pset.connect = pset.connect.value().replace('frontier://FrontierProd/', 'frontier://FrontierProd/')
    # fix for multi-run processing
    process.GlobalTag.RefreshEachRun = cms.untracked.bool( False )
    process.GlobalTag.ReconnectEachRun = cms.untracked.bool( False )

# override the L1 menu from an Xml file
process.l1GtTriggerMenuXml = cms.ESProducer("L1GtTriggerMenuXmlProducer",
  TriggerMenuLuminosity = cms.string('startup'),
  DefXmlFile = cms.string('L1Menu_CollisionsHeavyIons2015.v3_KKHecked.xml'),
  VmeXmlFile = cms.string('')
)
process.L1GtTriggerMenuRcdSource = cms.ESSource("EmptyESSource",
  recordName = cms.string('L1GtTriggerMenuRcd'),
  iovIsRunNotTime = cms.bool(True),
  firstValid = cms.vuint32(1)
)
process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')

# customize the L1 emulator to run customiseL1EmulatorFromRaw with HLT to switchToSimStage1Digis
process.load( 'Configuration.StandardSequences.RawToDigi_cff' )
process.load( 'Configuration.StandardSequences.SimL1Emulator_cff' )
import L1Trigger.Configuration.L1Trigger_custom
#

# 2015 Run2 emulator
import L1Trigger.L1TCalorimeter.L1TCaloStage1_customForHLT
process = L1Trigger.L1TCalorimeter.L1TCaloStage1_customForHLT.customiseL1EmulatorFromRaw( process )

#
process = L1Trigger.Configuration.L1Trigger_custom.customiseResetPrescalesAndMasks( process )
# customize the HLT to use the emulated results
import HLTrigger.Configuration.customizeHLTforL1Emulator
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToL1Emulator( process )
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToSimStage1Digis( process )

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

# load the DQMStore and DQMRootOutputModule
process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)

process.DQMOutput = cms.EndPath( process.dqmOutput )

# add specific customizations
_customInfo = {}
_customInfo['menuType'  ]= "GRun"
_customInfo['globalTags']= {}
_customInfo['globalTags'][True ] = "auto:run2_hlt_GRun"
_customInfo['globalTags'][False] = "auto:run2_mc_GRun"
_customInfo['inputFiles']={}
_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
_customInfo['maxEvents' ]=  100
_customInfo['globalTag' ]= "75X_mcRun2_HeavyIon_v6"
_customInfo['inputFile' ]=  ['file:/afs/cern.ch/user/t/twang/public/HLTSamples/D0pt35/step3_RAW2DIGI_L1Reco_RECO_100_1_wFV.root']
_customInfo['realData'  ]=  False
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process,_customInfo)

process.load('L1Trigger.L1TCalorimeter.caloConfigStage1HI_cfi')
process.caloStage1Params.regionPUSType = cms.string("zeroWall")
process.load("HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi")
process.load("GeneratorInterface.HiGenCommon.HeavyIon_cff")
process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName = cms.string("TEST")
process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )
process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","TEST")
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("openHLT_HF.root"))
from CondCore.DBCommon.CondDBSetup_cfi import *
process.beamspot = cms.ESSource("PoolDBESSource",CondDBSetup,
                                toGet = cms.VPSet(cms.PSet( record = cms.string('BeamSpotObjectsRcd'),
                                                            tag= cms.string('RealisticHICollisions2011_STARTHI50_mc')
                                                            )),
                                connect =cms.string('frontier://FrontierProd/CMS_COND_31X_BEAMSPOT')
                                )
process.es_prefer_beamspot = cms.ESPrefer("PoolDBESSource","beamspot")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
recordOverrides = { ('L1RCTParametersRcd', None) : ('L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactorsV4_HIDisabledFGHOE', None) }
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_HeavyIon_v6', recordOverrides)
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
                                                                             
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")    
process.HiGenParticleAna.stableOnly = cms.untracked.bool(False)                     
process.ana_step = cms.Path(process.heavyIon*                                       
      process.HiGenParticleAna                                                      
)                                                                                   


process.Timing=cms.Service("Timing",
    useJobReport = cms.untracked.bool(True)
    )
process.hltOutputFULL = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "outputFULL_YJfix.root" ),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string( 'RECO' ),
        filterName = cms.untracked.string( '' )
    ),
    outputCommands = cms.untracked.vstring( 'keep *')
)
process.FULLOutput = cms.EndPath( process.hltOutputFULL )

