#include <TFile.h>
#include <TChain.h>
#include <TTree.h>
#include <TMath.h>
#include <TH2F.h>

#include <iostream>
#include <vector>
#include <algorithm>

void DumpHLT()
{
  TString inputfileOffline = "HiForest_Offline_nRy.root";
  TString inputfileHLT = "trackanalyzerHLT_output_HIIterTrackingV22_nRy.root";
  
  TFile*finputOffline=new TFile(inputfileOffline.Data());
  TFile*finputHLT=new TFile(inputfileHLT.Data());
  
  TChain *ftrackTreeOffline = (TChain*)finputOffline->Get("anaTrack/trackTree");
  TChain *ftrackTreeHLT = (TChain*)finputHLT->Get("anaTrack/trackTree");

  float xVtxOffline;
  float yVtxOffline;
  float zVtxOffline;
  int nTrkVtxOffline;

  float xVtxHLT;
  float yVtxHLT;
  float zVtxHLT;
  int nTrkVtxHLT;

  
  ftrackTreeOffline->SetBranchAddress("xVtx",&xVtxOffline);
  ftrackTreeOffline->SetBranchAddress("yVtx",&yVtxOffline);
  ftrackTreeOffline->SetBranchAddress("zVtx",&zVtxOffline);
  ftrackTreeOffline->SetBranchAddress("nTrkVtx",&nTrkVtxOffline);
  
  ftrackTreeHLT->SetBranchAddress("xVtx",&xVtxHLT);
  ftrackTreeHLT->SetBranchAddress("yVtx",&yVtxHLT);
  ftrackTreeHLT->SetBranchAddress("zVtx",&zVtxHLT);
  ftrackTreeHLT->SetBranchAddress("nTrkVtx",&nTrkVtxHLT);

  Long64_t l_entries = ftrackTreeOffline->GetEntries();
  cout<<"l_entries="<<l_entries<<endl;
    for(Long64_t j = 0; j < l_entries; ++j){
    ftrackTreeOffline->GetEntry(j);
    ftrackTreeHLT->GetEntry(j);
    cout<<"************** event="<<j<<endl;
    cout<<" with xVtxOffline="<<xVtxOffline<<endl;
    cout<<" with xVtxHLT="<<xVtxHLT<<endl;

    cout<<" with yVtxOffline="<<yVtxOffline<<endl;
    cout<<" with yVtxHLT="<<yVtxHLT<<endl;

    cout<<" with zVtxOffline="<<zVtxOffline<<endl;
    cout<<" with zVtxHLT="<<zVtxHLT<<endl;
    
    cout<<" with nTrkVtxOffline="<<nTrkVtxOffline<<endl;
    cout<<" with nTrkVtxHLT="<<nTrkVtxHLT<<endl;

  }
}
