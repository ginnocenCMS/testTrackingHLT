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

void Draw_Event_L1seed_PP()
{
	TH1::SetDefaultSumw2();
    gStyle->SetOptFit(0);
    gStyle->SetOptStat(0);
    gStyle->SetOptTitle(0);


	TFile * input = new TFile("openHLT_HF_ppHLTHeavyFlavourTracking_MBseed_Pythia_D0pt35p0_Pthat35_1019.root");
	TTree * hlttree = ( TTree * ) input->Get("hltbitanalysis/HltTree");
	TTree * gentree = ( TTree * ) input->Get("HiGenParticleAna/hi");
	gentree->AddFriend(hlttree);
	hlttree->AddFriend(gentree);

	TH1D * eventfired_Dpt10_MBseed = new TH1D("eventfired_Dpt10_MBseed","eventfired_Dpt10_MBseed",2,0,2);
	TH1D * eventfired_Dpt10_S1Jet8seed = new TH1D("eventfired_Dpt10_S1Jet8seed","eventfired_Dpt10_S1Jet8seed",2,0,2);
	TH1D * eventfired_Dpt10_S1Jet16seed = new TH1D("eventfired_Dpt10_S1Jet16seed","eventfired_Dpt10_S1Jet16seed",2,0,2);
	TH1D * eventfired_Dpt10_S1Jet28seed = new TH1D("eventfired_Dpt10_S1Jet28seed","eventfired_Dpt10_S1Jet28seed",2,0,2);
	TH1D * eventfired_Dpt10_S1Jet40seed = new TH1D("eventfired_Dpt10_S1Jet40seed","eventfired_Dpt10_S1Jet40seed",2,0,2);
	TH1D * eventfired_Dpt10_S1Jet44seed = new TH1D("eventfired_Dpt10_S1Jet44seed","eventfired_Dpt10_S1Jet44seed",2,0,2);
	TH1D * eventfired_Dpt10_S1Jet56seed = new TH1D("eventfired_Dpt10_S1Jet56seed","eventfired_Dpt10_S1Jet56seed",2,0,2);
	TH1D * eventfired_Dpt10_S1Jet92seed = new TH1D("eventfired_Dpt10_S1Jet92seed","eventfired_Dpt10_S1Jet92seed",2,0,2);
	
	eventfired_Dpt10_MBseed->SetLineWidth(2.0);
	eventfired_Dpt10_S1Jet8seed->SetLineWidth(2.0);
	eventfired_Dpt10_S1Jet16seed->SetLineWidth(2.0);
	eventfired_Dpt10_S1Jet28seed->SetLineWidth(2.0);
	eventfired_Dpt10_S1Jet40seed->SetLineWidth(2.0);
	eventfired_Dpt10_S1Jet44seed->SetLineWidth(2.0);
	eventfired_Dpt10_S1Jet56seed->SetLineWidth(2.0);
	eventfired_Dpt10_S1Jet92seed->SetLineWidth(2.0);

	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt10_pp_v1>>eventfired_Dpt10_MBseed","HLT_DmesonTrackingGlobal_Dpt10_pp_v1","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt10_pp_v1>>eventfired_Dpt10_S1Jet8seed","HLT_DmesonTrackingGlobal_Dpt10_pp_v1&&L1_SingleS1Jet8_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt10_pp_v1>>eventfired_Dpt10_S1Jet16seed","HLT_DmesonTrackingGlobal_Dpt10_pp_v1&&L1_SingleS1Jet16_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt10_pp_v1>>eventfired_Dpt10_S1Jet28seed","HLT_DmesonTrackingGlobal_Dpt10_pp_v1&&L1_SingleS1Jet28_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt10_pp_v1>>eventfired_Dpt10_S1Jet40seed","HLT_DmesonTrackingGlobal_Dpt10_pp_v1&&L1_SingleS1Jet40_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt10_pp_v1>>eventfired_Dpt10_S1Jet44seed","HLT_DmesonTrackingGlobal_Dpt10_pp_v1&&L1_SingleJet44_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt10_pp_v1>>eventfired_Dpt10_S1Jet56seed","HLT_DmesonTrackingGlobal_Dpt10_pp_v1&&L1_SingleS1Jet56_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt10_pp_v1>>eventfired_Dpt10_S1Jet92seed","HLT_DmesonTrackingGlobal_Dpt10_pp_v1&&L1_SingleJet92_BptxAND","goff");

	TH1D * Events_Dpt10_MBseed = new TH1D( "Events_Dpt10_MBseed", "Events_Dpt10_MBseed", 8, 0, 8);
	TH1D * fraction_Events_Dpt10_L1Jetseed = new TH1D( "fraction_Events_Dpt10_L1Jetseed","fraction_Events_Dpt10_L1Jetseed", 8, 0, 8);
	fraction_Events_Dpt10_L1Jetseed->SetLineWidth(2.0);

	cout << "Dpt 20 fired events: " << eventfired_Dpt10_MBseed->GetEntries() << endl;

	for( int i = 0; i < 8; i++ )
	{
		Events_Dpt10_MBseed->SetBinContent( i+1, eventfired_Dpt10_MBseed->GetEntries());
		Events_Dpt10_MBseed->SetBinError( i+1, TMath::Sqrt(eventfired_Dpt10_MBseed->GetEntries()));
	}

	fraction_Events_Dpt10_L1Jetseed->SetBinContent(1, eventfired_Dpt10_MBseed->GetEntries());
	fraction_Events_Dpt10_L1Jetseed->SetBinError( 1, TMath::Sqrt(eventfired_Dpt10_MBseed->GetEntries()));

	fraction_Events_Dpt10_L1Jetseed->SetBinContent( 2, eventfired_Dpt10_S1Jet8seed->GetEntries());
	fraction_Events_Dpt10_L1Jetseed->SetBinError( 2, TMath::Sqrt(eventfired_Dpt10_S1Jet8seed->GetEntries()));

	fraction_Events_Dpt10_L1Jetseed->SetBinContent( 3, eventfired_Dpt10_S1Jet16seed->GetEntries());
	fraction_Events_Dpt10_L1Jetseed->SetBinError( 3, TMath::Sqrt(eventfired_Dpt10_S1Jet16seed->GetEntries()));

	fraction_Events_Dpt10_L1Jetseed->SetBinContent( 4, eventfired_Dpt10_S1Jet28seed->GetEntries());
	fraction_Events_Dpt10_L1Jetseed->SetBinError( 4, TMath::Sqrt(eventfired_Dpt10_S1Jet28seed->GetEntries()));

	fraction_Events_Dpt10_L1Jetseed->SetBinContent( 5, eventfired_Dpt10_S1Jet40seed->GetEntries());
	fraction_Events_Dpt10_L1Jetseed->SetBinError( 5, TMath::Sqrt(eventfired_Dpt10_S1Jet40seed->GetEntries()));

	fraction_Events_Dpt10_L1Jetseed->SetBinContent( 6, eventfired_Dpt10_S1Jet44seed->GetEntries());
	fraction_Events_Dpt10_L1Jetseed->SetBinError( 6, TMath::Sqrt(eventfired_Dpt10_S1Jet44seed->GetEntries()));

	fraction_Events_Dpt10_L1Jetseed->SetBinContent( 7, eventfired_Dpt10_S1Jet56seed->GetEntries());
	fraction_Events_Dpt10_L1Jetseed->SetBinError( 7, TMath::Sqrt(eventfired_Dpt10_S1Jet56seed->GetEntries()));

	fraction_Events_Dpt10_L1Jetseed->SetBinContent( 8, eventfired_Dpt10_S1Jet92seed->GetEntries());
	fraction_Events_Dpt10_L1Jetseed->SetBinError( 8, TMath::Sqrt(eventfired_Dpt10_S1Jet92seed->GetEntries()));

	for( int i = 0; i < 8; i++ )
		cout << " bin content: " << fraction_Events_Dpt10_L1Jetseed->GetBinContent( i+1 ) << endl; 

	fraction_Events_Dpt10_L1Jetseed->Divide( fraction_Events_Dpt10_L1Jetseed, Events_Dpt10_MBseed, 1.0, 1.0, "B");

	fraction_Events_Dpt10_L1Jetseed->SetLineColor(2.0);

	TCanvas * cfg_evtfraction_Dpt10_L1seed = new TCanvas("cfg_evtfraction_Dpt10_L1seed","cfg_evtfraction_Dpt10_L1seed",600,600);
    cfg_evtfraction_Dpt10_L1seed->SetGridx();
	cfg_evtfraction_Dpt10_L1seed->SetGridy();
	cfg_evtfraction_Dpt10_L1seed->SetGrid();

	fraction_Events_Dpt10_L1Jetseed->GetXaxis()->SetTitle("L1Jet* seed");
	fraction_Events_Dpt10_L1Jetseed->GetYaxis()->SetTitle("Event fraction: L1Jet* seed/MB seed");
	fraction_Events_Dpt10_L1Jetseed->GetYaxis()->SetRangeUser(0.,1.2);
	fraction_Events_Dpt10_L1Jetseed->Draw();

	for( int i = 0; i < 8; i++ )
		cout << " fraction: " << fraction_Events_Dpt10_L1Jetseed->GetBinContent( i+1 ) << " +/- " << fraction_Events_Dpt10_L1Jetseed->GetBinError( i+1 ) << endl; 

	cfg_evtfraction_Dpt10_L1seed->SaveAs("plots/cfg_evtfraction_Dpt10_L1seed_AllMB_D0pt35p0_Pthat35_PP.png");
	cfg_evtfraction_Dpt10_L1seed->SaveAs("plots/cfg_evtfraction_Dpt10_L1seed_AllMB_D0pt35p0_Pthat35_PP.pdf");


	TH1D * eventfired_Dpt20_MBseed = new TH1D("eventfired_Dpt20_MBseed","eventfired_Dpt20_MBseed",2,0,2);
	TH1D * eventfired_Dpt20_S1Jet8seed = new TH1D("eventfired_Dpt20_S1Jet8seed","eventfired_Dpt20_S1Jet8seed",2,0,2);
	TH1D * eventfired_Dpt20_S1Jet16seed = new TH1D("eventfired_Dpt20_S1Jet16seed","eventfired_Dpt20_S1Jet16seed",2,0,2);
	TH1D * eventfired_Dpt20_S1Jet28seed = new TH1D("eventfired_Dpt20_S1Jet28seed","eventfired_Dpt20_S1Jet28seed",2,0,2);
	TH1D * eventfired_Dpt20_S1Jet40seed = new TH1D("eventfired_Dpt20_S1Jet40seed","eventfired_Dpt20_S1Jet40seed",2,0,2);
	TH1D * eventfired_Dpt20_S1Jet44seed = new TH1D("eventfired_Dpt20_S1Jet44seed","eventfired_Dpt20_S1Jet44seed",2,0,2);
	TH1D * eventfired_Dpt20_S1Jet56seed = new TH1D("eventfired_Dpt20_S1Jet56seed","eventfired_Dpt20_S1Jet56seed",2,0,2);
	TH1D * eventfired_Dpt20_S1Jet92seed = new TH1D("eventfired_Dpt20_S1Jet92seed","eventfired_Dpt20_S1Jet92seed",2,0,2);
	
	eventfired_Dpt20_MBseed->SetLineWidth(2.0);
	eventfired_Dpt20_S1Jet8seed->SetLineWidth(2.0);
	eventfired_Dpt20_S1Jet16seed->SetLineWidth(2.0);
	eventfired_Dpt20_S1Jet28seed->SetLineWidth(2.0);
	eventfired_Dpt20_S1Jet40seed->SetLineWidth(2.0);
	eventfired_Dpt20_S1Jet44seed->SetLineWidth(2.0);
	eventfired_Dpt20_S1Jet56seed->SetLineWidth(2.0);
	eventfired_Dpt20_S1Jet92seed->SetLineWidth(2.0);

	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt20_pp_v1>>eventfired_Dpt20_MBseed","HLT_DmesonTrackingGlobal_Dpt20_pp_v1","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt20_pp_v1>>eventfired_Dpt20_S1Jet8seed","HLT_DmesonTrackingGlobal_Dpt20_pp_v1&&L1_SingleS1Jet8_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt20_pp_v1>>eventfired_Dpt20_S1Jet16seed","HLT_DmesonTrackingGlobal_Dpt20_pp_v1&&L1_SingleS1Jet16_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt20_pp_v1>>eventfired_Dpt20_S1Jet28seed","HLT_DmesonTrackingGlobal_Dpt20_pp_v1&&L1_SingleS1Jet28_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt20_pp_v1>>eventfired_Dpt20_S1Jet40seed","HLT_DmesonTrackingGlobal_Dpt20_pp_v1&&L1_SingleS1Jet40_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt20_pp_v1>>eventfired_Dpt20_S1Jet44seed","HLT_DmesonTrackingGlobal_Dpt20_pp_v1&&L1_SingleJet44_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt20_pp_v1>>eventfired_Dpt20_S1Jet56seed","HLT_DmesonTrackingGlobal_Dpt20_pp_v1&&L1_SingleS1Jet56_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt20_pp_v1>>eventfired_Dpt20_S1Jet92seed","HLT_DmesonTrackingGlobal_Dpt20_pp_v1&&L1_SingleJet92_BptxAND","goff");

	TH1D * Events_Dpt20_MBseed = new TH1D( "Events_Dpt20_MBseed", "Events_Dpt20_MBseed", 8, 0, 8);
	TH1D * fraction_Events_Dpt20_L1Jetseed = new TH1D( "fraction_Events_Dpt20_L1Jetseed","fraction_Events_Dpt20_L1Jetseed", 8, 0, 8);
	fraction_Events_Dpt20_L1Jetseed->SetLineWidth(2.0);

	cout << "Dpt 20 fired events: " << eventfired_Dpt20_MBseed->GetEntries() << endl;

	for( int i = 0; i < 8; i++ )
	{
		Events_Dpt20_MBseed->SetBinContent( i+1, eventfired_Dpt20_MBseed->GetEntries());
		Events_Dpt20_MBseed->SetBinError( i+1, TMath::Sqrt(eventfired_Dpt20_MBseed->GetEntries()));
	}

	fraction_Events_Dpt20_L1Jetseed->SetBinContent(1, eventfired_Dpt20_MBseed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 1, TMath::Sqrt(eventfired_Dpt20_MBseed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 2, eventfired_Dpt20_S1Jet8seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 2, TMath::Sqrt(eventfired_Dpt20_S1Jet8seed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 3, eventfired_Dpt20_S1Jet16seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 3, TMath::Sqrt(eventfired_Dpt20_S1Jet16seed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 4, eventfired_Dpt20_S1Jet28seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 4, TMath::Sqrt(eventfired_Dpt20_S1Jet28seed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 5, eventfired_Dpt20_S1Jet40seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 5, TMath::Sqrt(eventfired_Dpt20_S1Jet40seed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 6, eventfired_Dpt20_S1Jet44seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 6, TMath::Sqrt(eventfired_Dpt20_S1Jet44seed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 7, eventfired_Dpt20_S1Jet56seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 7, TMath::Sqrt(eventfired_Dpt20_S1Jet56seed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 8, eventfired_Dpt20_S1Jet92seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 8, TMath::Sqrt(eventfired_Dpt20_S1Jet92seed->GetEntries()));

	for( int i = 0; i < 8; i++ )
		cout << " bin content: " << fraction_Events_Dpt20_L1Jetseed->GetBinContent( i+1 ) << endl; 

	fraction_Events_Dpt20_L1Jetseed->Divide( fraction_Events_Dpt20_L1Jetseed, Events_Dpt20_MBseed, 1.0, 1.0, "B");

	fraction_Events_Dpt20_L1Jetseed->SetLineColor(2.0);

	TCanvas * cfg_evtfraction_Dpt20_L1seed = new TCanvas("cfg_evtfraction_Dpt20_L1seed","cfg_evtfraction_Dpt20_L1seed",600,600);
    cfg_evtfraction_Dpt20_L1seed->SetGridx();
	cfg_evtfraction_Dpt20_L1seed->SetGridy();
	cfg_evtfraction_Dpt20_L1seed->SetGrid();

	fraction_Events_Dpt20_L1Jetseed->GetXaxis()->SetTitle("L1Jet* seed");
	fraction_Events_Dpt20_L1Jetseed->GetYaxis()->SetTitle("Event fraction: L1Jet* seed/MB seed");
	fraction_Events_Dpt20_L1Jetseed->GetYaxis()->SetRangeUser(0.,1.2);
	fraction_Events_Dpt20_L1Jetseed->Draw();

	for( int i = 0; i < 8; i++ )
		cout << " fraction: " << fraction_Events_Dpt20_L1Jetseed->GetBinContent( i+1 ) << " +/- " << fraction_Events_Dpt20_L1Jetseed->GetBinError( i+1 ) << endl; 

	cfg_evtfraction_Dpt20_L1seed->SaveAs("plots/cfg_evtfraction_Dpt20_L1seed_AllMB_D0pt35p0_Pthat35_PP.png");
	cfg_evtfraction_Dpt20_L1seed->SaveAs("plots/cfg_evtfraction_Dpt20_L1seed_AllMB_D0pt35p0_Pthat35_PP.pdf");

	TH1D * eventfired_Dpt30_MBseed = new TH1D("eventfired_Dpt30_MBseed","eventfired_Dpt30_MBseed",2,0,2);
	TH1D * eventfired_Dpt30_S1Jet8seed = new TH1D("eventfired_Dpt30_S1Jet8seed","eventfired_Dpt30_S1Jet8seed",2,0,2);
	TH1D * eventfired_Dpt30_S1Jet16seed = new TH1D("eventfired_Dpt30_S1Jet16seed","eventfired_Dpt30_S1Jet16seed",2,0,2);
	TH1D * eventfired_Dpt30_S1Jet28seed = new TH1D("eventfired_Dpt30_S1Jet28seed","eventfired_Dpt30_S1Jet28seed",2,0,2);
	TH1D * eventfired_Dpt30_S1Jet40seed = new TH1D("eventfired_Dpt30_S1Jet40seed","eventfired_Dpt30_S1Jet40seed",2,0,2);
	TH1D * eventfired_Dpt30_S1Jet44seed = new TH1D("eventfired_Dpt30_S1Jet44seed","eventfired_Dpt30_S1Jet44seed",2,0,2);
	TH1D * eventfired_Dpt30_S1Jet56seed = new TH1D("eventfired_Dpt30_S1Jet56seed","eventfired_Dpt30_S1Jet56seed",2,0,2);
	TH1D * eventfired_Dpt30_S1Jet92seed = new TH1D("eventfired_Dpt30_S1Jet92seed","eventfired_Dpt30_S1Jet92seed",2,0,2);
	
	eventfired_Dpt30_MBseed->SetLineWidth(2.0);
	eventfired_Dpt30_S1Jet8seed->SetLineWidth(2.0);
	eventfired_Dpt30_S1Jet16seed->SetLineWidth(2.0);
	eventfired_Dpt30_S1Jet28seed->SetLineWidth(2.0);
	eventfired_Dpt30_S1Jet40seed->SetLineWidth(2.0);
	eventfired_Dpt30_S1Jet44seed->SetLineWidth(2.0);
	eventfired_Dpt30_S1Jet56seed->SetLineWidth(2.0);
	eventfired_Dpt30_S1Jet92seed->SetLineWidth(2.0);

	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt30_pp_v1>>eventfired_Dpt30_MBseed","HLT_DmesonTrackingGlobal_Dpt30_pp_v1","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt30_pp_v1>>eventfired_Dpt30_S1Jet8seed","HLT_DmesonTrackingGlobal_Dpt30_pp_v1&&L1_SingleS1Jet8_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt30_pp_v1>>eventfired_Dpt30_S1Jet16seed","HLT_DmesonTrackingGlobal_Dpt30_pp_v1&&L1_SingleS1Jet16_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt30_pp_v1>>eventfired_Dpt30_S1Jet28seed","HLT_DmesonTrackingGlobal_Dpt30_pp_v1&&L1_SingleS1Jet28_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt30_pp_v1>>eventfired_Dpt30_S1Jet40seed","HLT_DmesonTrackingGlobal_Dpt30_pp_v1&&L1_SingleS1Jet40_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt30_pp_v1>>eventfired_Dpt30_S1Jet44seed","HLT_DmesonTrackingGlobal_Dpt30_pp_v1&&L1_SingleJet44_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt30_pp_v1>>eventfired_Dpt30_S1Jet56seed","HLT_DmesonTrackingGlobal_Dpt30_pp_v1&&L1_SingleS1Jet56_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt30_pp_v1>>eventfired_Dpt30_S1Jet92seed","HLT_DmesonTrackingGlobal_Dpt30_pp_v1&&L1_SingleJet92_BptxAND","goff");

	TH1D * Events_Dpt30_MBseed = new TH1D( "Events_Dpt30_MBseed", "Events_Dpt30_MBseed", 8, 0, 8);
	TH1D * fraction_Events_Dpt30_L1Jetseed = new TH1D( "fraction_Events_Dpt30_L1Jetseed","fraction_Events_Dpt30_L1Jetseed", 8, 0, 8);
	fraction_Events_Dpt30_L1Jetseed->SetLineWidth(2.0);

	cout << "Dpt 20 fired events: " << eventfired_Dpt30_MBseed->GetEntries() << endl;

	for( int i = 0; i < 8; i++ )
	{
		Events_Dpt30_MBseed->SetBinContent( i+1, eventfired_Dpt30_MBseed->GetEntries());
		Events_Dpt30_MBseed->SetBinError( i+1, TMath::Sqrt(eventfired_Dpt30_MBseed->GetEntries()));
	}

	fraction_Events_Dpt30_L1Jetseed->SetBinContent(1, eventfired_Dpt30_MBseed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 1, TMath::Sqrt(eventfired_Dpt30_MBseed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 2, eventfired_Dpt30_S1Jet8seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 2, TMath::Sqrt(eventfired_Dpt30_S1Jet8seed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 3, eventfired_Dpt30_S1Jet16seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 3, TMath::Sqrt(eventfired_Dpt30_S1Jet16seed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 4, eventfired_Dpt30_S1Jet28seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 4, TMath::Sqrt(eventfired_Dpt30_S1Jet28seed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 5, eventfired_Dpt30_S1Jet40seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 5, TMath::Sqrt(eventfired_Dpt30_S1Jet40seed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 6, eventfired_Dpt30_S1Jet44seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 6, TMath::Sqrt(eventfired_Dpt30_S1Jet44seed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 7, eventfired_Dpt30_S1Jet56seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 7, TMath::Sqrt(eventfired_Dpt30_S1Jet56seed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 8, eventfired_Dpt30_S1Jet92seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 8, TMath::Sqrt(eventfired_Dpt30_S1Jet92seed->GetEntries()));

	for( int i = 0; i < 8; i++ )
		cout << " bin content: " << fraction_Events_Dpt30_L1Jetseed->GetBinContent( i+1 ) << endl; 

	fraction_Events_Dpt30_L1Jetseed->Divide( fraction_Events_Dpt30_L1Jetseed, Events_Dpt30_MBseed, 1.0, 1.0, "B");

	fraction_Events_Dpt30_L1Jetseed->SetLineColor(2.0);

	TCanvas * cfg_evtfraction_Dpt30_L1seed = new TCanvas("cfg_evtfraction_Dpt30_L1seed","cfg_evtfraction_Dpt30_L1seed",600,600);
    cfg_evtfraction_Dpt30_L1seed->SetGridx();
	cfg_evtfraction_Dpt30_L1seed->SetGridy();
	cfg_evtfraction_Dpt30_L1seed->SetGrid();

	fraction_Events_Dpt30_L1Jetseed->GetXaxis()->SetTitle("L1Jet* seed");
	fraction_Events_Dpt30_L1Jetseed->GetYaxis()->SetTitle("Event fraction: L1Jet* seed/MB seed");
	fraction_Events_Dpt30_L1Jetseed->GetYaxis()->SetRangeUser(0.,1.2);
	fraction_Events_Dpt30_L1Jetseed->Draw();

	for( int i = 0; i < 8; i++ )
		cout << " fraction: " << fraction_Events_Dpt30_L1Jetseed->GetBinContent( i+1 ) << " +/- " << fraction_Events_Dpt30_L1Jetseed->GetBinError( i+1 ) << endl; 


	cfg_evtfraction_Dpt30_L1seed->SaveAs("plots/cfg_evtfraction_Dpt30_L1seed_AllMB_D0pt35p0_Pthat35_PP.png");
	cfg_evtfraction_Dpt30_L1seed->SaveAs("plots/cfg_evtfraction_Dpt30_L1seed_AllMB_D0pt35p0_Pthat35_PP.pdf");


	TH1D * eventfired_Dpt40_MBseed = new TH1D("eventfired_Dpt40_MBseed","eventfired_Dpt40_MBseed",2,0,2);
	TH1D * eventfired_Dpt40_S1Jet8seed = new TH1D("eventfired_Dpt40_S1Jet8seed","eventfired_Dpt40_S1Jet8seed",2,0,2);
	TH1D * eventfired_Dpt40_S1Jet16seed = new TH1D("eventfired_Dpt40_S1Jet16seed","eventfired_Dpt40_S1Jet16seed",2,0,2);
	TH1D * eventfired_Dpt40_S1Jet28seed = new TH1D("eventfired_Dpt40_S1Jet28seed","eventfired_Dpt40_S1Jet28seed",2,0,2);
	TH1D * eventfired_Dpt40_S1Jet40seed = new TH1D("eventfired_Dpt40_S1Jet40seed","eventfired_Dpt40_S1Jet40seed",2,0,2);
	TH1D * eventfired_Dpt40_S1Jet44seed = new TH1D("eventfired_Dpt40_S1Jet44seed","eventfired_Dpt40_S1Jet44seed",2,0,2);
	TH1D * eventfired_Dpt40_S1Jet56seed = new TH1D("eventfired_Dpt40_S1Jet56seed","eventfired_Dpt40_S1Jet56seed",2,0,2);
	TH1D * eventfired_Dpt40_S1Jet92seed = new TH1D("eventfired_Dpt40_S1Jet92seed","eventfired_Dpt40_S1Jet92seed",2,0,2);
	
	eventfired_Dpt40_MBseed->SetLineWidth(2.0);
	eventfired_Dpt40_S1Jet8seed->SetLineWidth(2.0);
	eventfired_Dpt40_S1Jet16seed->SetLineWidth(2.0);
	eventfired_Dpt40_S1Jet28seed->SetLineWidth(2.0);
	eventfired_Dpt40_S1Jet40seed->SetLineWidth(2.0);
	eventfired_Dpt40_S1Jet44seed->SetLineWidth(2.0);
	eventfired_Dpt40_S1Jet56seed->SetLineWidth(2.0);
	eventfired_Dpt40_S1Jet92seed->SetLineWidth(2.0);

	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt40_pp_v1>>eventfired_Dpt40_MBseed","HLT_DmesonTrackingGlobal_Dpt40_pp_v1","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt40_pp_v1>>eventfired_Dpt40_S1Jet8seed","HLT_DmesonTrackingGlobal_Dpt40_pp_v1&&L1_SingleS1Jet8_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt40_pp_v1>>eventfired_Dpt40_S1Jet16seed","HLT_DmesonTrackingGlobal_Dpt40_pp_v1&&L1_SingleS1Jet16_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt40_pp_v1>>eventfired_Dpt40_S1Jet28seed","HLT_DmesonTrackingGlobal_Dpt40_pp_v1&&L1_SingleS1Jet28_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt40_pp_v1>>eventfired_Dpt40_S1Jet40seed","HLT_DmesonTrackingGlobal_Dpt40_pp_v1&&L1_SingleS1Jet40_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt40_pp_v1>>eventfired_Dpt40_S1Jet44seed","HLT_DmesonTrackingGlobal_Dpt40_pp_v1&&L1_SingleJet44_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt40_pp_v1>>eventfired_Dpt40_S1Jet56seed","HLT_DmesonTrackingGlobal_Dpt40_pp_v1&&L1_SingleS1Jet56_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt40_pp_v1>>eventfired_Dpt40_S1Jet92seed","HLT_DmesonTrackingGlobal_Dpt40_pp_v1&&L1_SingleJet92_BptxAND","goff");

	TH1D * Events_Dpt40_MBseed = new TH1D( "Events_Dpt40_MBseed", "Events_Dpt40_MBseed", 8, 0, 8);
	TH1D * fraction_Events_Dpt40_L1Jetseed = new TH1D( "fraction_Events_Dpt40_L1Jetseed","fraction_Events_Dpt40_L1Jetseed", 8, 0, 8);
	fraction_Events_Dpt40_L1Jetseed->SetLineWidth(2.0);

	cout << "Dpt 20 fired events: " << eventfired_Dpt40_MBseed->GetEntries() << endl;

	for( int i = 0; i < 8; i++ )
	{
		Events_Dpt40_MBseed->SetBinContent( i+1, eventfired_Dpt40_MBseed->GetEntries());
		Events_Dpt40_MBseed->SetBinError( i+1, TMath::Sqrt(eventfired_Dpt40_MBseed->GetEntries()));
	}

	fraction_Events_Dpt40_L1Jetseed->SetBinContent(1, eventfired_Dpt40_MBseed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 1, TMath::Sqrt(eventfired_Dpt40_MBseed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 2, eventfired_Dpt40_S1Jet8seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 2, TMath::Sqrt(eventfired_Dpt40_S1Jet8seed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 3, eventfired_Dpt40_S1Jet16seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 3, TMath::Sqrt(eventfired_Dpt40_S1Jet16seed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 4, eventfired_Dpt40_S1Jet28seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 4, TMath::Sqrt(eventfired_Dpt40_S1Jet28seed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 5, eventfired_Dpt40_S1Jet40seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 5, TMath::Sqrt(eventfired_Dpt40_S1Jet40seed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 6, eventfired_Dpt40_S1Jet44seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 6, TMath::Sqrt(eventfired_Dpt40_S1Jet44seed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 7, eventfired_Dpt40_S1Jet56seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 7, TMath::Sqrt(eventfired_Dpt40_S1Jet56seed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 8, eventfired_Dpt40_S1Jet92seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 8, TMath::Sqrt(eventfired_Dpt40_S1Jet92seed->GetEntries()));

	for( int i = 0; i < 8; i++ )
		cout << " bin content: " << fraction_Events_Dpt40_L1Jetseed->GetBinContent( i+1 ) << endl; 

	fraction_Events_Dpt40_L1Jetseed->Divide( fraction_Events_Dpt40_L1Jetseed, Events_Dpt40_MBseed, 1.0, 1.0, "B");

	fraction_Events_Dpt40_L1Jetseed->SetLineColor(2.0);

	TCanvas * cfg_evtfraction_Dpt40_L1seed = new TCanvas("cfg_evtfraction_Dpt40_L1seed","cfg_evtfraction_Dpt40_L1seed",600,600);
    cfg_evtfraction_Dpt40_L1seed->SetGridx();
	cfg_evtfraction_Dpt40_L1seed->SetGridy();
	cfg_evtfraction_Dpt40_L1seed->SetGrid();

	fraction_Events_Dpt40_L1Jetseed->GetXaxis()->SetTitle("L1Jet* seed");
	fraction_Events_Dpt40_L1Jetseed->GetYaxis()->SetTitle("Event fraction: L1Jet* seed/MB seed");
	fraction_Events_Dpt40_L1Jetseed->GetYaxis()->SetRangeUser(0.,1.2);
	fraction_Events_Dpt40_L1Jetseed->Draw();

	for( int i = 0; i < 8; i++ )
		cout << " fraction: " << fraction_Events_Dpt40_L1Jetseed->GetBinContent( i+1 ) << " +/- " << fraction_Events_Dpt40_L1Jetseed->GetBinError( i+1 ) << endl; 

	cfg_evtfraction_Dpt40_L1seed->SaveAs("plots/cfg_evtfraction_Dpt40_L1seed_AllMB_D0pt35p0_Pthat35_PP.png");
	cfg_evtfraction_Dpt40_L1seed->SaveAs("plots/cfg_evtfraction_Dpt40_L1seed_AllMB_D0pt35p0_Pthat35_PP.pdf");

	TH1D * eventfired_Dpt60_MBseed = new TH1D("eventfired_Dpt60_MBseed","eventfired_Dpt60_MBseed",2,0,2);
	TH1D * eventfired_Dpt60_S1Jet8seed = new TH1D("eventfired_Dpt60_S1Jet8seed","eventfired_Dpt60_S1Jet8seed",2,0,2);
	TH1D * eventfired_Dpt60_S1Jet16seed = new TH1D("eventfired_Dpt60_S1Jet16seed","eventfired_Dpt60_S1Jet16seed",2,0,2);
	TH1D * eventfired_Dpt60_S1Jet28seed = new TH1D("eventfired_Dpt60_S1Jet28seed","eventfired_Dpt60_S1Jet28seed",2,0,2);
	TH1D * eventfired_Dpt60_S1Jet40seed = new TH1D("eventfired_Dpt60_S1Jet40seed","eventfired_Dpt60_S1Jet40seed",2,0,2);
	TH1D * eventfired_Dpt60_S1Jet44seed = new TH1D("eventfired_Dpt60_S1Jet44seed","eventfired_Dpt60_S1Jet44seed",2,0,2);
	TH1D * eventfired_Dpt60_S1Jet56seed = new TH1D("eventfired_Dpt60_S1Jet56seed","eventfired_Dpt60_S1Jet56seed",2,0,2);
	TH1D * eventfired_Dpt60_S1Jet92seed = new TH1D("eventfired_Dpt60_S1Jet92seed","eventfired_Dpt60_S1Jet92seed",2,0,2);
	
	eventfired_Dpt60_MBseed->SetLineWidth(2.0);
	eventfired_Dpt60_S1Jet8seed->SetLineWidth(2.0);
	eventfired_Dpt60_S1Jet16seed->SetLineWidth(2.0);
	eventfired_Dpt60_S1Jet28seed->SetLineWidth(2.0);
	eventfired_Dpt60_S1Jet40seed->SetLineWidth(2.0);
	eventfired_Dpt60_S1Jet44seed->SetLineWidth(2.0);
	eventfired_Dpt60_S1Jet56seed->SetLineWidth(2.0);
	eventfired_Dpt60_S1Jet92seed->SetLineWidth(2.0);

	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt60_pp_v1>>eventfired_Dpt60_MBseed","HLT_DmesonTrackingGlobal_Dpt60_pp_v1","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt60_pp_v1>>eventfired_Dpt60_S1Jet8seed","HLT_DmesonTrackingGlobal_Dpt60_pp_v1&&L1_SingleS1Jet8_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt60_pp_v1>>eventfired_Dpt60_S1Jet16seed","HLT_DmesonTrackingGlobal_Dpt60_pp_v1&&L1_SingleS1Jet16_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt60_pp_v1>>eventfired_Dpt60_S1Jet28seed","HLT_DmesonTrackingGlobal_Dpt60_pp_v1&&L1_SingleS1Jet28_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt60_pp_v1>>eventfired_Dpt60_S1Jet40seed","HLT_DmesonTrackingGlobal_Dpt60_pp_v1&&L1_SingleS1Jet40_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt60_pp_v1>>eventfired_Dpt60_S1Jet44seed","HLT_DmesonTrackingGlobal_Dpt60_pp_v1&&L1_SingleJet44_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt60_pp_v1>>eventfired_Dpt60_S1Jet56seed","HLT_DmesonTrackingGlobal_Dpt60_pp_v1&&L1_SingleS1Jet56_BptxAND","goff");
	gentree->Draw("HLT_DmesonTrackingGlobal_Dpt60_pp_v1>>eventfired_Dpt60_S1Jet92seed","HLT_DmesonTrackingGlobal_Dpt60_pp_v1&&L1_SingleJet92_BptxAND","goff");

	TH1D * Events_Dpt60_MBseed = new TH1D( "Events_Dpt60_MBseed", "Events_Dpt60_MBseed", 8, 0, 8);
	TH1D * fraction_Events_Dpt60_L1Jetseed = new TH1D( "fraction_Events_Dpt60_L1Jetseed","fraction_Events_Dpt60_L1Jetseed", 8, 0, 8);
	fraction_Events_Dpt60_L1Jetseed->SetLineWidth(2.0);

	cout << "Dpt 20 fired events: " << eventfired_Dpt60_MBseed->GetEntries() << endl;

	for( int i = 0; i < 8; i++ )
	{
		Events_Dpt60_MBseed->SetBinContent( i+1, eventfired_Dpt60_MBseed->GetEntries());
		Events_Dpt60_MBseed->SetBinError( i+1, TMath::Sqrt(eventfired_Dpt60_MBseed->GetEntries()));
	}

	fraction_Events_Dpt60_L1Jetseed->SetBinContent(1, eventfired_Dpt60_MBseed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 1, TMath::Sqrt(eventfired_Dpt60_MBseed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 2, eventfired_Dpt60_S1Jet8seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 2, TMath::Sqrt(eventfired_Dpt60_S1Jet8seed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 3, eventfired_Dpt60_S1Jet16seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 3, TMath::Sqrt(eventfired_Dpt60_S1Jet16seed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 4, eventfired_Dpt60_S1Jet28seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 4, TMath::Sqrt(eventfired_Dpt60_S1Jet28seed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 5, eventfired_Dpt60_S1Jet40seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 5, TMath::Sqrt(eventfired_Dpt60_S1Jet40seed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 6, eventfired_Dpt60_S1Jet44seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 6, TMath::Sqrt(eventfired_Dpt60_S1Jet44seed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 7, eventfired_Dpt60_S1Jet56seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 7, TMath::Sqrt(eventfired_Dpt60_S1Jet56seed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 8, eventfired_Dpt60_S1Jet92seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 8, TMath::Sqrt(eventfired_Dpt60_S1Jet92seed->GetEntries()));

	for( int i = 0; i < 8; i++ )
		cout << " bin content: " << fraction_Events_Dpt60_L1Jetseed->GetBinContent( i+1 ) << endl; 

	fraction_Events_Dpt60_L1Jetseed->Divide( fraction_Events_Dpt60_L1Jetseed, Events_Dpt60_MBseed, 1.0, 1.0, "B");

	fraction_Events_Dpt60_L1Jetseed->SetLineColor(2.0);

	TCanvas * cfg_evtfraction_Dpt60_L1seed = new TCanvas("cfg_evtfraction_Dpt60_L1seed","cfg_evtfraction_Dpt60_L1seed",600,600);
    cfg_evtfraction_Dpt60_L1seed->SetGridx();
	cfg_evtfraction_Dpt60_L1seed->SetGridy();
	cfg_evtfraction_Dpt60_L1seed->SetGrid();

	fraction_Events_Dpt60_L1Jetseed->GetXaxis()->SetTitle("L1Jet* seed");
	fraction_Events_Dpt60_L1Jetseed->GetYaxis()->SetTitle("Event fraction: L1Jet* seed/MB seed");
	fraction_Events_Dpt60_L1Jetseed->GetYaxis()->SetRangeUser(0.,1.2);
	fraction_Events_Dpt60_L1Jetseed->Draw();

	for( int i = 0; i < 8; i++ )
		cout << " fraction: " << fraction_Events_Dpt60_L1Jetseed->GetBinContent( i+1 ) << " +/- " << fraction_Events_Dpt60_L1Jetseed->GetBinError( i+1 ) << endl; 

	cfg_evtfraction_Dpt60_L1seed->SaveAs("plots/cfg_evtfraction_Dpt60_L1seed_AllMB_D0pt35p0_Pthat35_PP.png");
	cfg_evtfraction_Dpt60_L1seed->SaveAs("plots/cfg_evtfraction_Dpt60_L1seed_AllMB_D0pt35p0_Pthat35_PP.pdf");
}
