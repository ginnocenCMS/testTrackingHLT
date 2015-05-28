testTrackingHLT
============

This repository is meant to perform tests on HLT HI tracking.

Setting your environment:
* cmsrel CMSSW_7_4_3
* cd CMSSW_7_4_3/src
* cmsenv
* git cms-merge-topic -u CmsHI:forest_CMSSW_7_4_1_patch1
* scram build -j4

Then clone the code:
* cd HeavyIonsAnalysis/JetAnalysis/test/
* git clone git@github.com:ginnocen/testTrackingHLT.git

