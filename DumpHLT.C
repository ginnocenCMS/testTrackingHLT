#include <TFile.h>
#include <TChain.h>
#include <TTree.h>
#include <TMath.h>
#include <TH2F.h>

#include <iostream>
#include <vector>
#include <algorithm>

void DumpHLT(int interation=0)
{

  int flagiteration=-1;
  if (interation==0) flagiteration=4;
  if (interation==1) flagiteration=7;
  if (interation==2) flagiteration=5;
  if (interation==3) flagiteration=6;
  
  TString inputfile_Offline = "HiForest_Offline_nRy.root";
  TString inputfile_HLT = "trackanalyzerHLT_output_HIIterTrackingV22_nRy.root";
  
  TFile*finput_Offline=new TFile(inputfile_Offline.Data());
  TFile*finput_HLT=new TFile(inputfile_HLT.Data());
  
  TChain *ftrackTree_Offline = (TChain*)finput_Offline->Get("anaTrack/trackTree");
  TChain *ftrackTree_HLT = (TChain*)finput_HLT->Get("anaTrack/trackTree");
  
  TH1F*htrkPt_Offline=new TH1F("htrkPt_Offline","htrkPt_Offline",50,0,50);
  TH1F*htrkPhi_Offline=new TH1F("htrkPhi_Offline","htrkPhi_Offline",50,-5,5);
  TH1F*htrkEta_Offline=new TH1F("htrkEta_Offline","htrkEta_Offline",50,-5,5);
  TH1F*htrkPt_HLT=new TH1F("htrkPt_HLT","htrkPt_HLT",50,0,50);
  TH1F*htrkPhi_HLT=new TH1F("htrkPhi_HLT","htrkPhi_HLT",50,-5,5);
  TH1F*htrkEta_HLT=new TH1F("htrkEta_HLT","htrkEta_HLT",50,-5,5);

  float xVtx_Offline;
  float yVtx_Offline;
  float zVtx_Offline;
  int nTrk_Offline;
  Float_t trkPt_Offline[10000];
  Float_t trkEta_Offline[10000];
  Float_t trkPhi_Offline[10000];
  Float_t trkAlgo_Offline[10000];
  bool highPurity_Offline[10000];

  float xVtx_HLT;
  float yVtx_HLT;
  float zVtx_HLT;
  int nTrk_HLT;
  Float_t trkPt_HLT[10000]; 
  Float_t trkEta_HLT[10000]; 
  Float_t trkPhi_HLT[10000]; 
  Float_t trkAlgo_HLT[10000];
  bool highPurity_HLT[10000];

  ftrackTree_Offline->SetBranchAddress("xVtx",&xVtx_Offline);
  ftrackTree_Offline->SetBranchAddress("yVtx",&yVtx_Offline);
  ftrackTree_Offline->SetBranchAddress("zVtx",&zVtx_Offline);
  ftrackTree_Offline->SetBranchAddress("nTrk",&nTrk_Offline);
  ftrackTree_Offline->SetBranchAddress("trkPt",trkPt_Offline);
  ftrackTree_Offline->SetBranchAddress("trkEta",trkEta_Offline);
  ftrackTree_Offline->SetBranchAddress("trkPhi",trkPhi_Offline);
  ftrackTree_Offline->SetBranchAddress("trkAlgo",trkAlgo_Offline);
  ftrackTree_Offline->SetBranchAddress("highPurity",highPurity_Offline);
  
  ftrackTree_HLT->SetBranchAddress("xVtx",&xVtx_HLT);
  ftrackTree_HLT->SetBranchAddress("yVtx",&yVtx_HLT);
  ftrackTree_HLT->SetBranchAddress("zVtx",&zVtx_HLT);
  ftrackTree_HLT->SetBranchAddress("nTrk",&nTrk_HLT);
  ftrackTree_HLT->SetBranchAddress("trkPt",trkPt_HLT);
  ftrackTree_HLT->SetBranchAddress("trkEta",trkEta_HLT);
  ftrackTree_HLT->SetBranchAddress("trkPhi",trkPhi_HLT);
  ftrackTree_HLT->SetBranchAddress("trkAlgo",trkAlgo_HLT);
  ftrackTree_HLT->SetBranchAddress("highPurity",highPurity_HLT);


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
      if(trkAlgo_Offline[itrack_Offline]==flagiteration && TMath::Abs(trkEta_Offline[itrack_Offline]<2.4) && highPurity_Offline[itrack_Offline]==1){ 
        htrkPt_Offline->Fill(trkPt_Offline[itrack_Offline]);
        htrkPhi_Offline->Fill(trkPhi_Offline[itrack_Offline]);
        htrkEta_Offline->Fill(trkEta_Offline[itrack_Offline]);
      }
    }
    for(int itrack_HLT=0;itrack_HLT<nTrk_HLT;itrack_HLT++) {
      if(trkAlgo_HLT[itrack_HLT]==flagiteration && TMath::Abs(trkEta_HLT[itrack_HLT]<2.4) && highPurity_HLT[itrack_HLT]==1){ 
        htrkPt_HLT->Fill(trkPt_HLT[itrack_HLT]);
        htrkPhi_HLT->Fill(trkPhi_HLT[itrack_HLT]);
        htrkEta_HLT->Fill(trkEta_HLT[itrack_HLT]);
      }
    }
  }
  
  
  htrkPt_HLT->SetLineWidth(3);
  htrkPhi_HLT->SetLineWidth(3);
  htrkEta_HLT->SetLineWidth(3);

  htrkPt_Offline->SetLineWidth(2);
  htrkPhi_Offline->SetLineWidth(2);
  htrkEta_Offline->SetLineWidth(2);
  
  TCanvas *cplots=new TCanvas("cplots","cplots",1000,400);
  cplots->Divide(3,1);
  cplots->cd(1);
  htrkPt_HLT->SetLineColor(2);
  htrkPt_HLT->Draw();
  htrkPt_Offline->Draw("same");
  cplots->cd(2);
  htrkEta_HLT->SetLineColor(2);
  htrkEta_HLT->Draw();
  htrkEta_Offline->Draw("same");
  cplots->cd(3);
  htrkPhi_HLT->SetLineColor(2);
  htrkPhi_HLT->Draw();
  htrkPhi_Offline->Draw("same");
  cplots->SaveAs(Form("cplots_iteration%d.pdf",interation));
      
  TFile*fout=new TFile(Form("test_iteration%d.root",interation),"recreate");
  fout->cd();
  htrkPt_Offline->Write();
  htrkPhi_Offline->Write();
  htrkEta_Offline->Write();
  htrkPt_HLT->Write();
  htrkPhi_HLT->Write();
  htrkEta_HLT->Write();
}
