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

void Draw_recoDpt_L1seed_tktrig()
{
	TH1::SetDefaultSumw2();
    gStyle->SetOptFit(0);
    gStyle->SetOptStat(0);
    gStyle->SetOptTitle(0);

	TFile * input = new TFile("ntD_20151016_DinderMC_20151015_EvtMatching_Pyquen_D0tokaonpion_D0pt15p0_Pthat15_TuneZ2_Unquenched_5020GeV_GENSIM_75x_v2_20151010.root");
	TTree * ntDkpi = ( TTree * ) input->Get("ntDkpi");

    TH1D * dpt_recomatched_notrig = new TH1D("dpt_recomatched_notrig","dpt_recomatched_notrig",16,0,80);
	TH1D * dpt_recomatched_HIFullTrack12 = new TH1D("dpt_recomatched_HIFullTrack12","dpt_recomatched_HIFullTrack12",16,0,80);
	TH1D * dpt_recomatched_HIFullTrack30 = new TH1D("dpt_recomatched_HIFullTrack30","dpt_recomatched_HIFullTrack30",16,0,80);
	TH1D * dpt_recomatched_HIFullTrack45 = new TH1D("dpt_recomatched_HIFullTrack45","dpt_recomatched_HIFullTrack45",16,0,80);

    dpt_recomatched_notrig->SetLineWidth(2.0);
	dpt_recomatched_HIFullTrack12->SetLineWidth(2.0);
	dpt_recomatched_HIFullTrack30->SetLineWidth(2.0);
	dpt_recomatched_HIFullTrack45->SetLineWidth(2.0);

    ntDkpi->Draw("Dpt>>dpt_recomatched_notrig","Dgen==23333&&abs(Deta)<1.0&&(DsvpvDistance/DsvpvDisErr)>2.5&&TMath::Cos(Dalpha)>0.95&&(Dtrk1Pt>8.&&Dtrk2Pt>8.)","goff");
	ntDkpi->Draw("Dpt>>dpt_recomatched_HIFullTrack12","Dgen==23333&&abs(Deta)<1.0&&(DsvpvDistance/DsvpvDisErr)>2.5&&TMath::Cos(Dalpha)>0.95&&(Dtrk1Pt>8.&&Dtrk2Pt>8.)&&(Dtrk1Pt>12.||Dtrk2Pt>12.)&&HLT_HIFullTrack12_v1","goff");
	ntDkpi->Draw("Dpt>>dpt_recomatched_HIFullTrack30","Dgen==23333&&abs(Deta)<1.0&&(DsvpvDistance/DsvpvDisErr)>2.5&&TMath::Cos(Dalpha)>0.95&&(Dtrk1Pt>8.&&Dtrk2Pt>8.)&&(Dtrk1Pt>30.||Dtrk2Pt>30.)&&(HLT_HIFullTrack30_L1Centrality010_v1||HLT_HIFullTrack30_L1Centrality1030_v1||HLT_HIFullTrack30_L1Centrality3050_v1||HLT_HIFullTrack30_L1Centrality50100_v1)","goff");
	ntDkpi->Draw("Dpt>>dpt_recomatched_HIFullTrack45","Dgen==23333&&abs(Deta)<1.0&&(DsvpvDistance/DsvpvDisErr)>2.5&&TMath::Cos(Dalpha)>0.95&&(Dtrk1Pt>8.&&Dtrk2Pt>8.)&&(Dtrk1Pt>45.||Dtrk2Pt>45.)&&(HLT_HIFullTrack45_L1Centrality010_v1||HLT_HIFullTrack45_L1Centrality1030_v1||HLT_HIFullTrack45_L1Centrality3050_v1||HLT_HIFullTrack45_L1Centrality50100_v1)","goff");

    dpt_recomatched_HIFullTrack12->Divide( dpt_recomatched_HIFullTrack12, dpt_recomatched_notrig, 1.0, 1.0, "B");
	dpt_recomatched_HIFullTrack30->Divide( dpt_recomatched_HIFullTrack30, dpt_recomatched_notrig, 1.0, 1.0, "B");
	dpt_recomatched_HIFullTrack45->Divide( dpt_recomatched_HIFullTrack45, dpt_recomatched_notrig, 1.0, 1.0, "B");

    dpt_recomatched_HIFullTrack12->SetLineColor(1.0);
	dpt_recomatched_HIFullTrack30->SetLineColor(2.0);
	dpt_recomatched_HIFullTrack45->SetLineColor(4.0);

	TCanvas * cfg_HIFullTrack123045_genpt = new TCanvas("cfg_HIFullTrack123045_genpt","cfg_HIFullTrack123045_genpt",600,600);
    cfg_HIFullTrack123045_genpt->SetGridx();
	cfg_HIFullTrack123045_genpt->SetGridy();
	cfg_HIFullTrack123045_genpt->SetGrid();

	dpt_recomatched_HIFullTrack30->GetXaxis()->SetTitle("Reco D^{0} p_{T} (GeV/c)");
	dpt_recomatched_HIFullTrack30->GetYaxis()->SetTitle("Trigger/All");
	dpt_recomatched_HIFullTrack30->GetYaxis()->SetRangeUser(0.,1.0);
	dpt_recomatched_HIFullTrack30->Draw();
	dpt_recomatched_HIFullTrack12->Draw("same");
	dpt_recomatched_HIFullTrack45->Draw("same");

	cfg_HIFullTrack123045_genpt->SaveAs("plots/cfg_HIFullTrack123045_L1seed_AllMB_tketa2p0_D0pt15p0_Pthat15_genmatched.png");
	cfg_HIFullTrack123045_genpt->SaveAs("plots/cfg_HIFullTrack123045_L1seed_AllMB_tketa2p0_D0pt15p0_Pthat15_genmatched.pdf");
}
