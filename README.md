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


# Offline check
This is the offline check macro by Jing.

Macro
https://github.com/boundino/Dntuple/tree/master/TestMacros/trigPre

Instruction
- `git clone https://github.com/boundino/Dntuple.git`
- `cd Dntuple/TestMacros/trigPre`
- Instruction to the macro 'triggerturnon.C'
 + Preselection in line 12
 + Change pthat in line 13
 + Input file in line 14
   * cgate: /mnt/hadoop/cms/store/user/jwang/Dmeson/5p02TeV/
    * lxplus: /afs/cern.ch/work/w/wangj/public/Dmeson/
 + Plot efficiency vs. variables by calling function plotTurnOn()
- `root triggerturnon.C+`


# Event matching
This is the event matching and Dntuple production macro by Jing. This macro combines Dfinder and openHLT root files into one event-matched Dfinder file, and produces Dntuple file.

Macro
- https://github.com/boundino/Dntuple/tree/master/EvtMatching
- https://github.com/boundino/Dntuple/tree/master/CodeForNtupleProduction

Instruction
- `git clone https://github.com/boundino/Dntuple.git`
- `cd Dntuple/EvtMatching`
- Instruction to the macro 'evtmatching.C'
 + *(You need to merge Dfinder files before processing event matching)*
 + Change input files (Dfinder and openHLT root files) and output file location in line 9
- `root evtmatching.C+`
- `cd ../CodeForNtupleProduction`
- Instruction to the macro 'loophlt.C'
 + Change the file (into the event-matched file you obtained) and output file location in line 31
 + *(Modify the corresponding lines in loophlt.C and loophlt.h if you want to change the braches to save)*
- `root loophlt.C+`
