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

void Draw_Event_L1trackseed_pthat15()
{
	TH1::SetDefaultSumw2();
    gStyle->SetOptFit(0);
    gStyle->SetOptStat(0);
    gStyle->SetOptTitle(0);


	TFile * input = new TFile("./openHLT_HF_HLTHeavyFlavour_MVA_V13_Pyquen_D0tokaonpion_D0pt15p0_Pthat15_1016_MBseed_fix.root");
	TTree * hlttree = ( TTree * ) input->Get("hltbitanalysis/HltTree");
	TTree * gentree = ( TTree * ) input->Get("HiGenParticleAna/hi");
	gentree->AddFriend(hlttree);
	hlttree->AddFriend(gentree);

	TH1D * eventfired_Dpt20_MBseed = new TH1D("eventfired_Dpt20_MBseed","eventfired_Dpt20_MBseed",2,0,2);
	TH1D * eventfired_Dpt20_L1Track8seed = new TH1D("eventfired_Dpt20_L1Track8seed","eventfired_Dpt20_L1Track8seed",2,0,2);
	TH1D * eventfired_Dpt20_L1Track12seed = new TH1D("eventfired_Dpt20_L1Track12seed","eventfired_Dpt20_L1Track12seed",2,0,2);
	TH1D * eventfired_Dpt20_L1Track16seed = new TH1D("eventfired_Dpt20_L1Track16seed","eventfired_Dpt20_L1Track16seed",2,0,2);
	TH1D * eventfired_Dpt20_L1Track20seed = new TH1D("eventfired_Dpt20_L1Track20seed","eventfired_Dpt20_L1Track20seed",2,0,2);
	
	eventfired_Dpt20_MBseed->SetLineWidth(2.0);
	eventfired_Dpt20_L1Track8seed->SetLineWidth(2.0);
	eventfired_Dpt20_L1Track12seed->SetLineWidth(2.0);
	eventfired_Dpt20_L1Track16seed->SetLineWidth(2.0);
	eventfired_Dpt20_L1Track20seed->SetLineWidth(2.0);

	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt20_v1>>eventfired_Dpt20_MBseed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt20_v1>>eventfired_Dpt20_L1Track8seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleS1Jet8_BptxAND&&(L1_SingleTrack8_Centrality0_10||L1_SingleTrack8_Centrality10_30||L1_SingleTrack8_Centrality30_50||L1_SingleTrack8_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt20_v1>>eventfired_Dpt20_L1Track12seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleS1Jet16_BptxAND&&(L1_SingleTrack12_Centrality0_10||L1_SingleTrack12_Centrality10_30||L1_SingleTrack12_Centrality30_50||L1_SingleTrack12_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt20_v1>>eventfired_Dpt20_L1Track16seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleS1Jet28_BptxAND&&(L1_SingleTrack16_Centrality0_10||L1_SingleTrack16_Centrality10_30||L1_SingleTrack16_Centrality30_50||L1_SingleTrack16_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt20_v1>>eventfired_Dpt20_L1Track20seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt20_v1&&L1_SingleS1Jet40_BptxAND&&(L1_SingleTrack20_Centrality0_10||L1_SingleTrack20_Centrality10_30||L1_SingleTrack20_Centrality30_50||L1_SingleTrack20_Centrality50_100)","goff");

	TH1D * Events_Dpt20_MBseed = new TH1D( "Events_Dpt20_MBseed", "Events_Dpt20_MBseed", 5, 0, 5);
	TH1D * fraction_Events_Dpt20_L1Jetseed = new TH1D( "fraction_Events_Dpt20_L1Jetseed","fraction_Events_Dpt20_L1Jetseed", 5, 0, 5);
	fraction_Events_Dpt20_L1Jetseed->SetLineWidth(2.0);

	cout << "Dpt 20 fired events: " << eventfired_Dpt20_MBseed->GetEntries() << endl;

	for( int i = 0; i < 5; i++ )
	{
		Events_Dpt20_MBseed->SetBinContent( i+1, eventfired_Dpt20_MBseed->GetEntries());
		Events_Dpt20_MBseed->SetBinError( i+1, TMath::Sqrt(eventfired_Dpt20_MBseed->GetEntries()));
	}

	fraction_Events_Dpt20_L1Jetseed->SetBinContent(1, eventfired_Dpt20_MBseed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 1, TMath::Sqrt(eventfired_Dpt20_MBseed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 2, eventfired_Dpt20_L1Track8seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 2, TMath::Sqrt(eventfired_Dpt20_L1Track8seed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 3, eventfired_Dpt20_L1Track12seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 3, TMath::Sqrt(eventfired_Dpt20_L1Track12seed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 4, eventfired_Dpt20_L1Track16seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 4, TMath::Sqrt(eventfired_Dpt20_L1Track16seed->GetEntries()));

	fraction_Events_Dpt20_L1Jetseed->SetBinContent( 5, eventfired_Dpt20_L1Track20seed->GetEntries());
	fraction_Events_Dpt20_L1Jetseed->SetBinError( 5, TMath::Sqrt(eventfired_Dpt20_L1Track20seed->GetEntries()));


	for( int i = 0; i < 5; i++ )
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

	for( int i = 0; i < 5; i++ )
		cout << " fraction: " << fraction_Events_Dpt20_L1Jetseed->GetBinContent( i+1 ) << " +/- " << fraction_Events_Dpt20_L1Jetseed->GetBinError( i+1 ) << endl; 

	cfg_evtfraction_Dpt20_L1seed->SaveAs("plots/cfg_evtfraction_Dpt20_L1trackseed_AllMB_D0pt15p0_Pthat15.png");
	cfg_evtfraction_Dpt20_L1seed->SaveAs("plots/cfg_evtfraction_Dpt20_L1trackseed_AllMB_D0pt15p0_Pthat15.pdf");

	TH1D * eventfired_Dpt30_MBseed = new TH1D("eventfired_Dpt30_MBseed","eventfired_Dpt30_MBseed",2,0,2);
	TH1D * eventfired_Dpt30_L1Track8seed = new TH1D("eventfired_Dpt30_L1Track8seed","eventfired_Dpt30_L1Track8seed",2,0,2);
	TH1D * eventfired_Dpt30_L1Track12seed = new TH1D("eventfired_Dpt30_L1Track12seed","eventfired_Dpt30_L1Track12seed",2,0,2);
	TH1D * eventfired_Dpt30_L1Track16seed = new TH1D("eventfired_Dpt30_L1Track16seed","eventfired_Dpt30_L1Track16seed",2,0,2);
	TH1D * eventfired_Dpt30_L1Track20seed = new TH1D("eventfired_Dpt30_L1Track20seed","eventfired_Dpt30_L1Track20seed",2,0,2);
	
	eventfired_Dpt30_MBseed->SetLineWidth(2.0);
	eventfired_Dpt30_L1Track8seed->SetLineWidth(2.0);
	eventfired_Dpt30_L1Track12seed->SetLineWidth(2.0);
	eventfired_Dpt30_L1Track16seed->SetLineWidth(2.0);
	eventfired_Dpt30_L1Track20seed->SetLineWidth(2.0);

	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt30_v1>>eventfired_Dpt30_MBseed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt30_v1","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt30_v1>>eventfired_Dpt30_L1Track8seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt30_v1&&L1_SingleS1Jet8_BptxAND&&(L1_SingleTrack8_Centrality0_10||L1_SingleTrack8_Centrality10_30||L1_SingleTrack8_Centrality30_50||L1_SingleTrack8_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt30_v1>>eventfired_Dpt30_L1Track12seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt30_v1&&L1_SingleS1Jet16_BptxAND&&(L1_SingleTrack12_Centrality0_10||L1_SingleTrack12_Centrality10_30||L1_SingleTrack12_Centrality30_50||L1_SingleTrack12_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt30_v1>>eventfired_Dpt30_L1Track16seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt30_v1&&L1_SingleS1Jet28_BptxAND&&(L1_SingleTrack16_Centrality0_10||L1_SingleTrack16_Centrality10_30||L1_SingleTrack16_Centrality30_50||L1_SingleTrack16_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt30_v1>>eventfired_Dpt30_L1Track20seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt30_v1&&L1_SingleS1Jet40_BptxAND&&(L1_SingleTrack20_Centrality0_10||L1_SingleTrack20_Centrality10_30||L1_SingleTrack20_Centrality30_50||L1_SingleTrack20_Centrality50_100)","goff");

	TH1D * Events_Dpt30_MBseed = new TH1D( "Events_Dpt30_MBseed", "Events_Dpt30_MBseed", 5, 0, 5);
	TH1D * fraction_Events_Dpt30_L1Jetseed = new TH1D( "fraction_Events_Dpt30_L1Jetseed","fraction_Events_Dpt30_L1Jetseed", 5, 0, 5);
	fraction_Events_Dpt30_L1Jetseed->SetLineWidth(2.0);

	cout << "Dpt 20 fired events: " << eventfired_Dpt30_MBseed->GetEntries() << endl;

	for( int i = 0; i < 5; i++ )
	{
		Events_Dpt30_MBseed->SetBinContent( i+1, eventfired_Dpt30_MBseed->GetEntries());
		Events_Dpt30_MBseed->SetBinError( i+1, TMath::Sqrt(eventfired_Dpt30_MBseed->GetEntries()));
	}

	fraction_Events_Dpt30_L1Jetseed->SetBinContent(1, eventfired_Dpt30_MBseed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 1, TMath::Sqrt(eventfired_Dpt30_MBseed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 2, eventfired_Dpt30_L1Track8seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 2, TMath::Sqrt(eventfired_Dpt30_L1Track8seed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 3, eventfired_Dpt30_L1Track12seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 3, TMath::Sqrt(eventfired_Dpt30_L1Track12seed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 4, eventfired_Dpt30_L1Track16seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 4, TMath::Sqrt(eventfired_Dpt30_L1Track16seed->GetEntries()));

	fraction_Events_Dpt30_L1Jetseed->SetBinContent( 5, eventfired_Dpt30_L1Track20seed->GetEntries());
	fraction_Events_Dpt30_L1Jetseed->SetBinError( 5, TMath::Sqrt(eventfired_Dpt30_L1Track20seed->GetEntries()));


	for( int i = 0; i < 5; i++ )
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

	for( int i = 0; i < 5; i++ )
		cout << " fraction: " << fraction_Events_Dpt30_L1Jetseed->GetBinContent( i+1 ) << " +/- " << fraction_Events_Dpt30_L1Jetseed->GetBinError( i+1 ) << endl; 

	cfg_evtfraction_Dpt30_L1seed->SaveAs("plots/cfg_evtfraction_Dpt30_L1trackseed_AllMB_D0pt15p0_Pthat15.png");
	cfg_evtfraction_Dpt30_L1seed->SaveAs("plots/cfg_evtfraction_Dpt30_L1trackseed_AllMB_D0pt15p0_Pthat15.pdf");

	TH1D * eventfired_Dpt40_MBseed = new TH1D("eventfired_Dpt40_MBseed","eventfired_Dpt40_MBseed",2,0,2);
	TH1D * eventfired_Dpt40_L1Track8seed = new TH1D("eventfired_Dpt40_L1Track8seed","eventfired_Dpt40_L1Track8seed",2,0,2);
	TH1D * eventfired_Dpt40_L1Track12seed = new TH1D("eventfired_Dpt40_L1Track12seed","eventfired_Dpt40_L1Track12seed",2,0,2);
	TH1D * eventfired_Dpt40_L1Track16seed = new TH1D("eventfired_Dpt40_L1Track16seed","eventfired_Dpt40_L1Track16seed",2,0,2);
	TH1D * eventfired_Dpt40_L1Track20seed = new TH1D("eventfired_Dpt40_L1Track20seed","eventfired_Dpt40_L1Track20seed",2,0,2);
	
	eventfired_Dpt40_MBseed->SetLineWidth(2.0);
	eventfired_Dpt40_L1Track8seed->SetLineWidth(2.0);
	eventfired_Dpt40_L1Track12seed->SetLineWidth(2.0);
	eventfired_Dpt40_L1Track16seed->SetLineWidth(2.0);
	eventfired_Dpt40_L1Track20seed->SetLineWidth(2.0);

	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt40_v1>>eventfired_Dpt40_MBseed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt40_v1>>eventfired_Dpt40_L1Track8seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleS1Jet8_BptxAND&&(L1_SingleTrack8_Centrality0_10||L1_SingleTrack8_Centrality10_30||L1_SingleTrack8_Centrality30_50||L1_SingleTrack8_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt40_v1>>eventfired_Dpt40_L1Track12seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleS1Jet16_BptxAND&&(L1_SingleTrack12_Centrality0_10||L1_SingleTrack12_Centrality10_30||L1_SingleTrack12_Centrality30_50||L1_SingleTrack12_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt40_v1>>eventfired_Dpt40_L1Track16seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleS1Jet28_BptxAND&&(L1_SingleTrack16_Centrality0_10||L1_SingleTrack16_Centrality10_30||L1_SingleTrack16_Centrality30_50||L1_SingleTrack16_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt40_v1>>eventfired_Dpt40_L1Track20seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt40_v1&&L1_SingleS1Jet40_BptxAND&&(L1_SingleTrack20_Centrality0_10||L1_SingleTrack20_Centrality10_30||L1_SingleTrack20_Centrality30_50||L1_SingleTrack20_Centrality50_100)","goff");

	TH1D * Events_Dpt40_MBseed = new TH1D( "Events_Dpt40_MBseed", "Events_Dpt40_MBseed", 5, 0, 5);
	TH1D * fraction_Events_Dpt40_L1Jetseed = new TH1D( "fraction_Events_Dpt40_L1Jetseed","fraction_Events_Dpt40_L1Jetseed", 5, 0, 5);
	fraction_Events_Dpt40_L1Jetseed->SetLineWidth(2.0);

	cout << "Dpt 20 fired events: " << eventfired_Dpt40_MBseed->GetEntries() << endl;

	for( int i = 0; i < 5; i++ )
	{
		Events_Dpt40_MBseed->SetBinContent( i+1, eventfired_Dpt40_MBseed->GetEntries());
		Events_Dpt40_MBseed->SetBinError( i+1, TMath::Sqrt(eventfired_Dpt40_MBseed->GetEntries()));
	}

	fraction_Events_Dpt40_L1Jetseed->SetBinContent(1, eventfired_Dpt40_MBseed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 1, TMath::Sqrt(eventfired_Dpt40_MBseed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 2, eventfired_Dpt40_L1Track8seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 2, TMath::Sqrt(eventfired_Dpt40_L1Track8seed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 3, eventfired_Dpt40_L1Track12seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 3, TMath::Sqrt(eventfired_Dpt40_L1Track12seed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 4, eventfired_Dpt40_L1Track16seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 4, TMath::Sqrt(eventfired_Dpt40_L1Track16seed->GetEntries()));

	fraction_Events_Dpt40_L1Jetseed->SetBinContent( 5, eventfired_Dpt40_L1Track20seed->GetEntries());
	fraction_Events_Dpt40_L1Jetseed->SetBinError( 5, TMath::Sqrt(eventfired_Dpt40_L1Track20seed->GetEntries()));


	for( int i = 0; i < 5; i++ )
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

	for( int i = 0; i < 5; i++ )
		cout << " fraction: " << fraction_Events_Dpt40_L1Jetseed->GetBinContent( i+1 ) << " +/- " << fraction_Events_Dpt40_L1Jetseed->GetBinError( i+1 ) << endl; 

	cfg_evtfraction_Dpt40_L1seed->SaveAs("plots/cfg_evtfraction_Dpt40_L1trackseed_AllMB_D0pt15p0_Pthat15.png");
	cfg_evtfraction_Dpt40_L1seed->SaveAs("plots/cfg_evtfraction_Dpt40_L1trackseed_AllMB_D0pt15p0_Pthat15.pdf");

	TH1D * eventfired_Dpt60_MBseed = new TH1D("eventfired_Dpt60_MBseed","eventfired_Dpt60_MBseed",2,0,2);
	TH1D * eventfired_Dpt60_L1Track8seed = new TH1D("eventfired_Dpt60_L1Track8seed","eventfired_Dpt60_L1Track8seed",2,0,2);
	TH1D * eventfired_Dpt60_L1Track12seed = new TH1D("eventfired_Dpt60_L1Track12seed","eventfired_Dpt60_L1Track12seed",2,0,2);
	TH1D * eventfired_Dpt60_L1Track16seed = new TH1D("eventfired_Dpt60_L1Track16seed","eventfired_Dpt60_L1Track16seed",2,0,2);
	TH1D * eventfired_Dpt60_L1Track20seed = new TH1D("eventfired_Dpt60_L1Track20seed","eventfired_Dpt60_L1Track20seed",2,0,2);
	
	eventfired_Dpt60_MBseed->SetLineWidth(2.0);
	eventfired_Dpt60_L1Track8seed->SetLineWidth(2.0);
	eventfired_Dpt60_L1Track12seed->SetLineWidth(2.0);
	eventfired_Dpt60_L1Track16seed->SetLineWidth(2.0);
	eventfired_Dpt60_L1Track20seed->SetLineWidth(2.0);

	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt60_v1>>eventfired_Dpt60_MBseed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt60_v1>>eventfired_Dpt60_L1Track8seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleS1Jet8_BptxAND&&(L1_SingleTrack8_Centrality0_10||L1_SingleTrack8_Centrality10_30||L1_SingleTrack8_Centrality30_50||L1_SingleTrack8_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt60_v1>>eventfired_Dpt60_L1Track12seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleS1Jet16_BptxAND&&(L1_SingleTrack12_Centrality0_10||L1_SingleTrack12_Centrality10_30||L1_SingleTrack12_Centrality30_50||L1_SingleTrack12_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt60_v1>>eventfired_Dpt60_L1Track16seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleS1Jet28_BptxAND&&(L1_SingleTrack16_Centrality0_10||L1_SingleTrack16_Centrality10_30||L1_SingleTrack16_Centrality30_50||L1_SingleTrack16_Centrality50_100)","goff");
	gentree->Draw("HLT_DmesonTrackingGlobalPt8_Dpt60_v1>>eventfired_Dpt60_L1Track20seed","pt>15.&&abs(pdg)==421&&abs(eta)<1.0&&HLT_DmesonTrackingGlobalPt8_Dpt60_v1&&L1_SingleS1Jet40_BptxAND&&(L1_SingleTrack20_Centrality0_10||L1_SingleTrack20_Centrality10_30||L1_SingleTrack20_Centrality30_50||L1_SingleTrack20_Centrality50_100)","goff");

	TH1D * Events_Dpt60_MBseed = new TH1D( "Events_Dpt60_MBseed", "Events_Dpt60_MBseed", 5, 0, 5);
	TH1D * fraction_Events_Dpt60_L1Jetseed = new TH1D( "fraction_Events_Dpt60_L1Jetseed","fraction_Events_Dpt60_L1Jetseed", 5, 0, 5);
	fraction_Events_Dpt60_L1Jetseed->SetLineWidth(2.0);

	cout << "Dpt 20 fired events: " << eventfired_Dpt60_MBseed->GetEntries() << endl;

	for( int i = 0; i < 5; i++ )
	{
		Events_Dpt60_MBseed->SetBinContent( i+1, eventfired_Dpt60_MBseed->GetEntries());
		Events_Dpt60_MBseed->SetBinError( i+1, TMath::Sqrt(eventfired_Dpt60_MBseed->GetEntries()));
	}

	fraction_Events_Dpt60_L1Jetseed->SetBinContent(1, eventfired_Dpt60_MBseed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 1, TMath::Sqrt(eventfired_Dpt60_MBseed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 2, eventfired_Dpt60_L1Track8seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 2, TMath::Sqrt(eventfired_Dpt60_L1Track8seed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 3, eventfired_Dpt60_L1Track12seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 3, TMath::Sqrt(eventfired_Dpt60_L1Track12seed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 4, eventfired_Dpt60_L1Track16seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 4, TMath::Sqrt(eventfired_Dpt60_L1Track16seed->GetEntries()));

	fraction_Events_Dpt60_L1Jetseed->SetBinContent( 5, eventfired_Dpt60_L1Track20seed->GetEntries());
	fraction_Events_Dpt60_L1Jetseed->SetBinError( 5, TMath::Sqrt(eventfired_Dpt60_L1Track20seed->GetEntries()));


	for( int i = 0; i < 5; i++ )
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

	for( int i = 0; i < 5; i++ )
		cout << " fraction: " << fraction_Events_Dpt60_L1Jetseed->GetBinContent( i+1 ) << " +/- " << fraction_Events_Dpt60_L1Jetseed->GetBinError( i+1 ) << endl; 

	cfg_evtfraction_Dpt60_L1seed->SaveAs("plots/cfg_evtfraction_Dpt60_L1trackseed_AllMB_D0pt15p0_Pthat15.png");
	cfg_evtfraction_Dpt60_L1seed->SaveAs("plots/cfg_evtfraction_Dpt60_L1trackseed_AllMB_D0pt15p0_Pthat15.pdf");
}
