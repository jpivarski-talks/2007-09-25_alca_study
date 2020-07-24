import ROOT

qcd_30_50 = ROOT.TFile("qcd_30-50.2.root")
qcd_50_80 = ROOT.TFile("qcd_50-80.root")
qcd_80_infty = ROOT.TFile("qcd_80-infty.root")
w_mu_nu = ROOT.TFile("w_mu_nu.2.root")
z_mu_mu = ROOT.TFile("z_mu_mu.root")

qcd30 = qcd_30_50.Get("CheckItGood/pt")
qcd50 = qcd_50_80.Get("CheckItGood/pt")
qcd80 = qcd_80_infty.Get("CheckItGood/pt")
w = w_mu_nu.Get("CheckItGood/pt")
z = z_mu_mu.Get("CheckItGood/pt")

canvas = ROOT.TCanvas()
canvas.SetLogy(1)

expo = ROOT.TF1("expo","[0]*exp(-[1]*x)",6,40);

qcd80.SetName("80 GeV - infinity")
qcd80.Fit("expo")

qcd50.Fit("expo")
qcd30.Fit("expo")
qcd50.GetFunction("expo").SetLineColor(4)
qcd30.GetFunction("expo").SetLineColor(2)
qcd50.SetLineColor(4)
qcd30.SetLineColor(2)

ROOT.gStyle.SetStatTextColor(2)
qcd30.UseCurrentStyle()
qcd30.SetName("QCD 30-50 GeV")
qcd30.Draw()

ROOT.gStyle.SetStatTextColor(4)
qcd50.UseCurrentStyle()
qcd50.SetName("QCD 50-80 GeV")
qcd50.Draw()

qcd30.Draw()
qcd50.Draw("same")

##################

canvas.SetLogy(0)
ROOT.gStyle.SetStatTextColor(1)
w.UseCurrentStyle()
w.SetName("W and Z events")
w.SetLineColor(1)
w.Draw()
ROOT.gStyle.SetStatTextColor(4)
z.UseCurrentStyle()
z.SetName("Z only (properly scaled)")
z.SetLineColor(4)
z.Draw()

w_events = 4438.
z_events = 1825.

w.Scale( (6.6/0.54) / (w_events / z_events) )
w.Add(z)

w.Draw()
z.Draw("same")
