#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <TFile.h>
#include <TH1F.h>
#include <TH2D.h>
#include <TMath.h>
#include <TF1.h>
#include <TNamed.h>
#include <TNtuple.h>
#include <TTree.h>
#include <TMath.h>
#include <TCanvas.h>
#include <TStyle.h>
#include <TLatex.h>

void Draw_Dpt_L1seed()
{
	TH1::SetDefaultSumw2();
    gStyle->SetOptFit(0);
    gStyle->SetOptStat(0);
    gStyle->SetOptTitle(0);


	TFile * input = new TFile("openHLT_HF_Pyquen_D0pt35p0_Pthat35_50k_tketa2p0_newGT.root");
	TTree * hlttree = ( TTree * ) input->Get("hltbitanalysis/HltTree");
	TTree * gentree = ( TTree * ) input->Get("HiGenParticleAna/hi");
	gentree->AddFriend(hlttree);
	hlttree->AddFriend(gentree);


	TH1D * dpt_gen_Dpt20_MBseed = new TH1D("dpt_gen_Dpt20_MBseed","dpt_gen_Dpt20_MBseed",8,0,80);
	TH1D * dpt_gen_Dpt20_S1Jet8seed = new TH1D("dpt_gen_Dpt20_S1Jet8seed","dpt_gen_Dpt20_S1Jet8seed",8,0,80);
	TH1D * dpt_gen_Dpt20_S1Jet16seed = new TH1D("dpt_gen_Dpt20_S1Jet16seed","dpt_gen_Dpt20_S1Jet16seed",8,0,80);
	TH1D * dpt_gen_Dpt20_S1Jet28seed = new TH1D("dpt_gen_Dpt20_S1Jet28seed","dpt_gen_Dpt20_S1Jet28seed",8,0,80);
	TH1D * dpt_gen_Dpt20_S1Jet40seed = new TH1D("dpt_gen_Dpt20_S1Jet40seed","dpt_gen_Dpt20_S1Jet40seed",8,0,80);
	TH1D * dpt_gen_Dpt20_S1Jet44seed = new TH1D("dpt_gen_Dpt20_S1Jet44seed","dpt_gen_Dpt20_S1Jet44seed",8,0,80);
	TH1D * dpt_gen_Dpt20_S1Jet56seed = new TH1D("dpt_gen_Dpt20_S1Jet56seed","dpt_gen_Dpt20_S1Jet56seed",8,0,80);
	TH1D * dpt_gen_Dpt20_S1Jet92seed = new TH1D("dpt_gen_Dpt20_S1Jet92seed","dpt_gen_Dpt20_S1Jet92seed",8,0,80);
//
//	TH1D * dpt_gen_Dpt20_MBseed = new TH1D("dpt_gen_Dpt20_MBseed","dpt_gen_Dpt20_MBseed",40,0,80);
//	TH1D * dpt_gen_Dpt20_S1Jet8seed = new TH1D("dpt_gen_Dpt20_S1Jet8seed","dpt_gen_Dpt20_S1Jet8seed",40,0,80);
//	TH1D * dpt_gen_Dpt20_S1Jet16seed = new TH1D("dpt_gen_Dpt20_S1Jet16seed","dpt_gen_Dpt20_S1Jet16seed",40,0,80);
//	TH1D * dpt_gen_Dpt20_S1Jet28seed = new TH1D("dpt_gen_Dpt20_S1Jet28seed","dpt_gen_Dpt20_S1Jet28seed",40,0,80);
//	TH1D * dpt_gen_Dpt20_S1Jet40seed = new TH1D("dpt_gen_Dpt20_S1Jet40seed","dpt_gen_Dpt20_S1Jet40seed",40,0,80);
//	TH1D * dpt_gen_Dpt20_S1Jet44seed = new TH1D("dpt_gen_Dpt20_S1Jet44seed","dpt_gen_Dpt20_S1Jet44seed",40,0,80);
//	TH1D * dpt_gen_Dpt20_S1Jet56seed = new TH1D("dpt_gen_Dpt20_S1Jet56seed","dpt_gen_Dpt20_S1Jet56seed",40,0,80);
//	TH1D * dpt_gen_Dpt20_S1Jet92seed = new TH1D("dpt_gen_Dpt20_S1Jet92seed","dpt_gen_Dpt20_S1Jet92seed",40,0,80);
//
	dpt_gen_Dpt20_MBseed->SetLineWidth(2.0);
	dpt_gen_Dpt20_S1Jet8seed->SetLineWidth(2.0);
	dpt_gen_Dpt20_S1Jet16seed->SetLineWidth(2.0);
	dpt_gen_Dpt20_S1Jet28seed->SetLineWidth(2.0);
	dpt_gen_Dpt20_S1Jet40seed->SetLineWidth(2.0);
	dpt_gen_Dpt20_S1Jet44seed->SetLineWidth(2.0);
	dpt_gen_Dpt20_S1Jet56seed->SetLineWidth(2.0);
	dpt_gen_Dpt20_S1Jet92seed->SetLineWidth(2.0);

	gentree->Draw("pt>>dpt_gen_Dpt20_MBseed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1","goff");
	gentree->Draw("pt>>dpt_gen_Dpt20_S1Jet8seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleS1Jet8_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt20_S1Jet16seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleS1Jet16_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt20_S1Jet28seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleS1Jet28_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt20_S1Jet40seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleS1Jet40_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt20_S1Jet44seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleJet44_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt20_S1Jet56seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleS1Jet56_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt20_S1Jet92seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleJet92_BptxAND","goff");

	dpt_gen_Dpt20_S1Jet8seed->Divide( dpt_gen_Dpt20_S1Jet8seed, dpt_gen_Dpt20_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt20_S1Jet16seed->Divide( dpt_gen_Dpt20_S1Jet16seed, dpt_gen_Dpt20_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt20_S1Jet28seed->Divide( dpt_gen_Dpt20_S1Jet28seed, dpt_gen_Dpt20_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt20_S1Jet40seed->Divide( dpt_gen_Dpt20_S1Jet40seed, dpt_gen_Dpt20_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt20_S1Jet44seed->Divide( dpt_gen_Dpt20_S1Jet44seed, dpt_gen_Dpt20_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt20_S1Jet56seed->Divide( dpt_gen_Dpt20_S1Jet56seed, dpt_gen_Dpt20_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt20_S1Jet92seed->Divide( dpt_gen_Dpt20_S1Jet92seed, dpt_gen_Dpt20_MBseed, 1.0, 1.0, "B");

	dpt_gen_Dpt20_S1Jet8seed->SetLineColor(8.0);
	dpt_gen_Dpt20_S1Jet16seed->SetLineColor(6.0);
	dpt_gen_Dpt20_S1Jet28seed->SetLineColor(1.0);
	dpt_gen_Dpt20_S1Jet40seed->SetLineColor(7.0);
	dpt_gen_Dpt20_S1Jet44seed->SetLineColor(4.0);
	dpt_gen_Dpt20_S1Jet56seed->SetLineColor(2.0);
	dpt_gen_Dpt20_S1Jet92seed->SetLineColor(50);

	TCanvas * cfg_Dpt20_L1seed = new TCanvas("cfg_Dpt20_L1seed","cfg_Dpt20_L1seed",600,600);
    cfg_Dpt20_L1seed->SetGridx();
	cfg_Dpt20_L1seed->SetGridy();
	cfg_Dpt20_L1seed->SetGrid();

	dpt_gen_Dpt20_S1Jet8seed->GetXaxis()->SetTitle("Gen D^{0} p_{T} (GeV/c)");
	dpt_gen_Dpt20_S1Jet8seed->GetYaxis()->SetTitle("L1Jet* seed/MB seed");
	dpt_gen_Dpt20_S1Jet8seed->GetYaxis()->SetRangeUser(0.,1.2);
	dpt_gen_Dpt20_S1Jet8seed->Draw();
	dpt_gen_Dpt20_S1Jet16seed->Draw("same");
	dpt_gen_Dpt20_S1Jet28seed->Draw("same");
	dpt_gen_Dpt20_S1Jet40seed->Draw("same");
	dpt_gen_Dpt20_S1Jet44seed->Draw("same");
	dpt_gen_Dpt20_S1Jet56seed->Draw("same");
	dpt_gen_Dpt20_S1Jet92seed->Draw("same");

	cfg_Dpt20_L1seed->SaveAs("plots/cfg_Dpt20_L1seed_AllMB_tketa2p0_D0pt35p0_Pthat35.png");
	cfg_Dpt20_L1seed->SaveAs("plots/cfg_Dpt20_L1seed_AllMB_tketa2p0_D0pt35p0_Pthat35.pdf");

	TH1D * dpt_gen_Dpt40_MBseed = new TH1D("dpt_gen_Dpt40_MBseed","dpt_gen_Dpt40_MBseed",8,0,80);
	TH1D * dpt_gen_Dpt40_S1Jet8seed = new TH1D("dpt_gen_Dpt40_S1Jet8seed","dpt_gen_Dpt40_S1Jet8seed",8,0,80);
	TH1D * dpt_gen_Dpt40_S1Jet16seed = new TH1D("dpt_gen_Dpt40_S1Jet16seed","dpt_gen_Dpt40_S1Jet16seed",8,0,80);
	TH1D * dpt_gen_Dpt40_S1Jet28seed = new TH1D("dpt_gen_Dpt40_S1Jet28seed","dpt_gen_Dpt40_S1Jet28seed",8,0,80);
	TH1D * dpt_gen_Dpt40_S1Jet40seed = new TH1D("dpt_gen_Dpt40_S1Jet40seed","dpt_gen_Dpt40_S1Jet40seed",8,0,80);
	TH1D * dpt_gen_Dpt40_S1Jet44seed = new TH1D("dpt_gen_Dpt40_S1Jet44seed","dpt_gen_Dpt40_S1Jet44seed",8,0,80);
	TH1D * dpt_gen_Dpt40_S1Jet56seed = new TH1D("dpt_gen_Dpt40_S1Jet56seed","dpt_gen_Dpt40_S1Jet56seed",8,0,80);
	TH1D * dpt_gen_Dpt40_S1Jet92seed = new TH1D("dpt_gen_Dpt40_S1Jet92seed","dpt_gen_Dpt40_S1Jet92seed",8,0,80);

	dpt_gen_Dpt40_MBseed->SetLineWidth(2.0);
	dpt_gen_Dpt40_S1Jet8seed->SetLineWidth(2.0);
	dpt_gen_Dpt40_S1Jet16seed->SetLineWidth(2.0);
	dpt_gen_Dpt40_S1Jet28seed->SetLineWidth(2.0);
	dpt_gen_Dpt40_S1Jet40seed->SetLineWidth(2.0);
	dpt_gen_Dpt40_S1Jet44seed->SetLineWidth(2.0);
	dpt_gen_Dpt40_S1Jet56seed->SetLineWidth(2.0);
	dpt_gen_Dpt40_S1Jet92seed->SetLineWidth(2.0);

	gentree->Draw("pt>>dpt_gen_Dpt40_MBseed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1","goff");
	gentree->Draw("pt>>dpt_gen_Dpt40_S1Jet8seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleS1Jet8_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt40_S1Jet16seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleS1Jet16_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt40_S1Jet28seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleS1Jet28_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt40_S1Jet40seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleS1Jet40_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt40_S1Jet44seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleJet44_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt40_S1Jet56seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleS1Jet56_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt40_S1Jet92seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleJet92_BptxAND","goff");

	dpt_gen_Dpt40_S1Jet8seed->Divide( dpt_gen_Dpt40_S1Jet8seed, dpt_gen_Dpt40_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt40_S1Jet16seed->Divide( dpt_gen_Dpt40_S1Jet16seed, dpt_gen_Dpt40_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt40_S1Jet28seed->Divide( dpt_gen_Dpt40_S1Jet28seed, dpt_gen_Dpt40_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt40_S1Jet40seed->Divide( dpt_gen_Dpt40_S1Jet40seed, dpt_gen_Dpt40_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt40_S1Jet44seed->Divide( dpt_gen_Dpt40_S1Jet44seed, dpt_gen_Dpt40_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt40_S1Jet56seed->Divide( dpt_gen_Dpt40_S1Jet56seed, dpt_gen_Dpt40_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt40_S1Jet92seed->Divide( dpt_gen_Dpt40_S1Jet92seed, dpt_gen_Dpt40_MBseed, 1.0, 1.0, "B");

	dpt_gen_Dpt40_S1Jet8seed->SetLineColor(8.0);
	dpt_gen_Dpt40_S1Jet16seed->SetLineColor(6.0);
	dpt_gen_Dpt40_S1Jet28seed->SetLineColor(1.0);
	dpt_gen_Dpt40_S1Jet40seed->SetLineColor(7.0);
	dpt_gen_Dpt40_S1Jet44seed->SetLineColor(4.0);
	dpt_gen_Dpt40_S1Jet56seed->SetLineColor(2.0);
	dpt_gen_Dpt40_S1Jet92seed->SetLineColor(50);

	TCanvas * cfg_Dpt40_L1seed = new TCanvas("cfg_Dpt40_L1seed","cfg_Dpt40_L1seed",600,600);
    dpt_gen_Dpt40_S1Jet8seed->GetXaxis()->SetTitle("Gen D^{0} p_{T} (GeV/c)");
    dpt_gen_Dpt40_S1Jet8seed->GetYaxis()->SetTitle("L1Jet* seed/MB seed");
	dpt_gen_Dpt40_S1Jet8seed->GetYaxis()->SetRangeUser(0.,1.2);
	dpt_gen_Dpt40_S1Jet8seed->Draw();
	dpt_gen_Dpt40_S1Jet16seed->Draw("same");
	dpt_gen_Dpt40_S1Jet28seed->Draw("same");
	dpt_gen_Dpt40_S1Jet40seed->Draw("same");
	dpt_gen_Dpt40_S1Jet44seed->Draw("same");
	dpt_gen_Dpt40_S1Jet56seed->Draw("same");
	dpt_gen_Dpt40_S1Jet92seed->Draw("same");

	cfg_Dpt40_L1seed->SaveAs("plots/cfg_Dpt40_L1seed_AllMB_tketa2p0_D0pt35p0_Pthat35.png");
	cfg_Dpt40_L1seed->SaveAs("plots/cfg_Dpt40_L1seed_AllMB_tketa2p0_D0pt35p0_Pthat35.pdf");

	TH1D * dpt_gen_Dpt60_MBseed = new TH1D("dpt_gen_Dpt60_MBseed","dpt_gen_Dpt60_MBseed",8,0,80);
	TH1D * dpt_gen_Dpt60_S1Jet8seed = new TH1D("dpt_gen_Dpt60_S1Jet8seed","dpt_gen_Dpt60_S1Jet8seed",8,0,80);
	TH1D * dpt_gen_Dpt60_S1Jet16seed = new TH1D("dpt_gen_Dpt60_S1Jet16seed","dpt_gen_Dpt60_S1Jet16seed",8,0,80);
	TH1D * dpt_gen_Dpt60_S1Jet28seed = new TH1D("dpt_gen_Dpt60_S1Jet28seed","dpt_gen_Dpt60_S1Jet28seed",8,0,80);
	TH1D * dpt_gen_Dpt60_S1Jet40seed = new TH1D("dpt_gen_Dpt60_S1Jet40seed","dpt_gen_Dpt60_S1Jet40seed",8,0,80);
	TH1D * dpt_gen_Dpt60_S1Jet44seed = new TH1D("dpt_gen_Dpt60_S1Jet44seed","dpt_gen_Dpt60_S1Jet44seed",8,0,80);
	TH1D * dpt_gen_Dpt60_S1Jet56seed = new TH1D("dpt_gen_Dpt60_S1Jet56seed","dpt_gen_Dpt60_S1Jet56seed",8,0,80);
	TH1D * dpt_gen_Dpt60_S1Jet92seed = new TH1D("dpt_gen_Dpt60_S1Jet92seed","dpt_gen_Dpt60_S1Jet92seed",8,0,80);

	dpt_gen_Dpt60_MBseed->SetLineWidth(2.0);
	dpt_gen_Dpt60_S1Jet8seed->SetLineWidth(2.0);
	dpt_gen_Dpt60_S1Jet16seed->SetLineWidth(2.0);
	dpt_gen_Dpt60_S1Jet28seed->SetLineWidth(2.0);
	dpt_gen_Dpt60_S1Jet40seed->SetLineWidth(2.0);
	dpt_gen_Dpt60_S1Jet44seed->SetLineWidth(2.0);
	dpt_gen_Dpt60_S1Jet56seed->SetLineWidth(2.0);
	dpt_gen_Dpt60_S1Jet92seed->SetLineWidth(2.0);

	gentree->Draw("pt>>dpt_gen_Dpt60_MBseed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1","goff");
	gentree->Draw("pt>>dpt_gen_Dpt60_S1Jet8seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleS1Jet8_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt60_S1Jet16seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleS1Jet16_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt60_S1Jet28seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleS1Jet28_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt60_S1Jet40seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleS1Jet40_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt60_S1Jet44seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleJet44_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt60_S1Jet56seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleS1Jet56_BptxAND","goff");
	gentree->Draw("pt>>dpt_gen_Dpt60_S1Jet92seed","abs(pdg)==421&&abs(eta)<2&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleJet92_BptxAND","goff");

	dpt_gen_Dpt60_S1Jet8seed->Divide( dpt_gen_Dpt60_S1Jet8seed, dpt_gen_Dpt60_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt60_S1Jet16seed->Divide( dpt_gen_Dpt60_S1Jet16seed, dpt_gen_Dpt60_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt60_S1Jet28seed->Divide( dpt_gen_Dpt60_S1Jet28seed, dpt_gen_Dpt60_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt60_S1Jet40seed->Divide( dpt_gen_Dpt60_S1Jet40seed, dpt_gen_Dpt60_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt60_S1Jet44seed->Divide( dpt_gen_Dpt60_S1Jet44seed, dpt_gen_Dpt60_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt60_S1Jet56seed->Divide( dpt_gen_Dpt60_S1Jet56seed, dpt_gen_Dpt60_MBseed, 1.0, 1.0, "B");
	dpt_gen_Dpt60_S1Jet92seed->Divide( dpt_gen_Dpt60_S1Jet92seed, dpt_gen_Dpt60_MBseed, 1.0, 1.0, "B");

	dpt_gen_Dpt60_S1Jet8seed->SetLineColor(8.0);
	dpt_gen_Dpt60_S1Jet16seed->SetLineColor(6.0);
	dpt_gen_Dpt60_S1Jet28seed->SetLineColor(1.0);
	dpt_gen_Dpt60_S1Jet40seed->SetLineColor(7.0);
	dpt_gen_Dpt60_S1Jet44seed->SetLineColor(4.0);
	dpt_gen_Dpt60_S1Jet56seed->SetLineColor(2.0);
	dpt_gen_Dpt60_S1Jet92seed->SetLineColor(50);

	TCanvas * cfg_Dpt60_L1seed = new TCanvas("cfg_Dpt60_L1seed","cfg_Dpt60_L1seed",600,600);
    dpt_gen_Dpt60_S1Jet8seed->GetXaxis()->SetTitle("Gen D^{0} p_{T} (GeV/c)");
    dpt_gen_Dpt60_S1Jet8seed->GetYaxis()->SetTitle("L1Jet* seed/MB seed");
	dpt_gen_Dpt60_S1Jet8seed->GetYaxis()->SetRangeUser(0.,1.2);
	dpt_gen_Dpt60_S1Jet8seed->Draw();
	dpt_gen_Dpt60_S1Jet16seed->Draw("same");
	dpt_gen_Dpt60_S1Jet28seed->Draw("same");
	dpt_gen_Dpt60_S1Jet40seed->Draw("same");
	dpt_gen_Dpt60_S1Jet44seed->Draw("same");
	dpt_gen_Dpt60_S1Jet56seed->Draw("same");
	dpt_gen_Dpt60_S1Jet92seed->Draw("same");

	cfg_Dpt60_L1seed->SaveAs("plots/cfg_Dpt60_L1seed_AllMB_tketa2p0_D0pt35p0_Pthat35.png");
	cfg_Dpt60_L1seed->SaveAs("plots/cfg_Dpt60_L1seed_AllMB_tketa2p0_D0pt35p0_Pthat35.pdf");
}
