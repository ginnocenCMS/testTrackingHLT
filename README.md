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

How to run the code:
* open getJetMenu_TRK_HIcode.sh
* make sure that the Global Tag, the HLT menu and the test file are the ones you want
* source getJetMenu_TRK_HIcode.sh. This will produce a python script
* cmsRun hlt_MC_stage1_TRK2_HIcode.py
