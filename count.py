import ROOT

tfile = ROOT.TFile("qcd_30-50.2.root")
pt = tfile.Get("CheckItGood/pt")
pt.Draw()

total = 0.
above20 = 0.
for i in range(pt.GetNbinsX()):
  total += pt.GetBinContent(i+1)
  if pt.GetBinLowEdge(i+1) >= 20.:
    above20 += pt.GetBinContent(i+1)

