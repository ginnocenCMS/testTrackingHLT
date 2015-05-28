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
  TString inputfile_Offline = "HiForest_Offline_nRy.root";
  TString inputfile_HLT = "trackanalyzerHLT_output_HIIterTrackingV22_nRy.root";
  
  TFile*finput_Offline=new TFile(inputfile_Offline.Data());
  TFile*finput_HLT=new TFile(inputfile_HLT.Data());
  
  TChain *ftrackTree_Offline = (TChain*)finput_Offline->Get("anaTrack/trackTree");
  TChain *ftrackTree_HLT = (TChain*)finput_HLT->Get("anaTrack/trackTree");
  
  TH1F*hpT_Offline=new TH1F("hpT_Offline","hpT_Offline",100,0,100);
  TH1F*hpT_HLT=new TH1F("hpT_HLT","hpT_HLT",100,0,100);

  float xVtx_Offline;
  float yVtx_Offline;
  float zVtx_Offline;
  int nTrk_Offline;
  Float_t trkPt_Offline[10000];
  Float_t trkAlgo_Offline[10000];

  float xVtx_HLT;
  float yVtx_HLT;
  float zVtx_HLT;
  int nTrk_HLT;
  Float_t trkPt_HLT[10000]; 
  Float_t trkAlgo_HLT[10000];

  ftrackTree_Offline->SetBranchAddress("xVtx",&xVtx_Offline);
  ftrackTree_Offline->SetBranchAddress("yVtx",&yVtx_Offline);
  ftrackTree_Offline->SetBranchAddress("zVtx",&zVtx_Offline);
  ftrackTree_Offline->SetBranchAddress("nTrk",&nTrk_Offline);
  ftrackTree_Offline->SetBranchAddress("trkPt",trkPt_Offline);
  ftrackTree_Offline->SetBranchAddress("trkAlgo",trkAlgo_Offline);
  
  ftrackTree_HLT->SetBranchAddress("xVtx",&xVtx_HLT);
  ftrackTree_HLT->SetBranchAddress("yVtx",&yVtx_HLT);
  ftrackTree_HLT->SetBranchAddress("zVtx",&zVtx_HLT);
  ftrackTree_HLT->SetBranchAddress("nTrk",&nTrk_HLT);
  ftrackTree_HLT->SetBranchAddress("trkPt",trkPt_HLT);
  ftrackTree_HLT->SetBranchAddress("trkAlgo",trkAlgo_HLT);


  Long64_t l_entries = ftrackTree_Offline->GetEntries();
  cout<<"l_entries="<<l_entries<<endl;
    for(Long64_t j = 0; j < l_entries; ++j){
    ftrackTree_Offline->GetEntry(j);
    ftrackTree_HLT->GetEntry(j);
    cout<<"************** event="<<j<<endl;
    cout<<" with xVtx_Offline="<<xVtx_Offline<<endl;
    cout<<" with xVtx_HLT="<<xVtx_HLT<<endl;

    cout<<" with yVtx_Offline="<<yVtx_Offline<<endl;
    cout<<" with yVtx_HLT="<<yVtx_HLT<<endl;

    cout<<" with zVtx_Offline="<<zVtx_Offline<<endl;
    cout<<" with zVtx_HLT="<<zVtx_HLT<<endl;
    
    cout<<" with nTrk_Offline="<<nTrk_Offline<<endl;
    cout<<" with nTrk_HLT="<<nTrk_HLT<<endl;
    
    for(int itrack_Offline=0;itrack_Offline<nTrk_Offline;itrack_Offline++) {
      if(trkAlgo_Offline[itrack_Offline]==4) hpT_Offline->Fill(trkPt_Offline[itrack_Offline]);
    }
    for(int itrack_HLT=0;itrack_HLT<nTrk_HLT;itrack_HLT++) {
      if(trkAlgo_HLT[itrack_HLT]==4) hpT_HLT->Fill(trkPt_HLT[itrack_HLT]);
    }
  }
  
  TFile*fout=new TFile("test.root","recreate");
  fout->cd();
  hpT_Offline->Write();
  hpT_HLT->Write();
}
