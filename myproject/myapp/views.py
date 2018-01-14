from django.shortcuts import render, redirect
from .models import PM_Master
from .models import Jobsheet_trace
from .models import Jobsheet
from .models import OMR
from .models import Part_Tracker
from .models import PM_Chart
from .models import Repair_Dashboard
from .models import Repair_Consume



# Create your views here.
def pmadd(request):
    return render(request, 'pm_master/change.html')

def pmindex(request):
    members = PM_Master.objects.all()
    context = {'members': members}
    return render(request, 'pm_master/index.html', context)


def pmcreate(request):
    member = PM_Master(Preventive_list=request.POST['Preventive_list'], Preventive_Name=request.POST['Preventive_Name'], Spare_Group=request.POST['Spare_Group'], Nature=request.POST['Nature'], Description=request.POST['Description'])
    member.save()
    return redirect('/myapp/pm_master')


def pmedit(request, id):
    members = PM_Master.objects.get(id=id)
    context = {'members': members}
    return render(request, 'pm_master/change.html', context)


def pmupdate(request, id):
    member = PM_Master.objects.get(id=id)
    member.Preventive_list = request.POST['Preventive_list']
    member.Preventive_Name = request.POST['Preventive_Name']
    member.Spare_Group = request.POST['Spare_Group']
    member.Nature = request.POST['Nature']
    member.Description = request.POST['Description']
    member.save()
    return redirect('/myapp/pm_master')


def pmdelete(request, id):
    member = PM_Master.objects.get(id=id)
    member.delete()
    return redirect('/myapp/pm_master')

# jobsheet track

def sheetadd(request):
    return render(request, 'jobsheet_trace/change.html')

def sheetindex(request):
    members1 = Jobsheet_trace.objects.all()
    context = {'members1': members1}
    return render(request, 'jobsheet_trace/index.html', context)


def sheetcreate(request):
    
    member1 = Jobsheet_trace(From_Date=request.POST['From_Date'], To_Date=request.POST['To_Date'], JobSheet_No=request.POST['JobSheet_No'], Vehicle_No=request.POST['Vehicle_No'])
    member1.save()
    return redirect('/myapp/jobsheet_trace')


def sheetedit(request, id):
    members1 = Jobsheet_trace.objects.get(id=id)
    return render(request, 'jobsheet_trace/change.html', {'members1':members1})



def sheetupdate(request, id):
    member1 = Jobsheet_trace.objects.get(id=id)
    member1.From_Date = request.POST['From_Date']
    member1.To_Date = request.POST['To_Date']
    member1.JobSheet_No = request.POST['JobSheet_No']
    member1.Vehicle_No = request.POST['Vehicle_No']
    member1.save()
    return redirect('/myapp/jobsheet_trace')


def sheetdelete(request, id):
    member1 = Jobsheet_trace.objects.get(id=id)
    member1.delete()
    return redirect('/myapp/jobsheet_trace')

#Jobsheet

def jobadd(request):
    return render(request, 'jobsheet/change.html')

def jobindex(request):
    members2 = Jobsheet.objects.all()
    context = {'members2': members2}
    return render(request, 'jobsheet/index.html', context)


def jobcreate(request):
    member2 = Jobsheet(Nature=request.POST['Nature'], Vehicle_No=request.POST['Vehicle_No'], JobSheet_No_List=request.POST['JobSheet_No_List'], Office_list=request.POST['Office_list'],Type=request.POST['Type'], In_Date=request.POST['In_Date'], Expt_Date=request.POST['Expt_Date'], Jobsheet_no=request.POST['Jobsheet_no'],Completion_Date=request.POST['Completion_Date'], Vehicle=request.POST['Vehicle'], Out_Date=request.POST['Out_Date'], Trailor=request.POST['Trailor'],KM_Reading=request.POST['KM_Reading'], Driver=request.POST['Driver'], Additional_KM=request.POST['Additional_KM'], Owner=request.POST['Owner'],Tyre_Supervisor=request.POST['Tyre_Supervisor'], Maintenance_Supervisor=request.POST['Maintenance_Supervisor'], Total_KM_Run=request.POST['Total_KM_Run'], Remark=request.POST['Remark'],pendding_Remark=request.POST['pendding_Remark'], Store=request.POST['Store'], Close_Date=request.POST['Close_Date'], JobSheet_No_List1=request.POST['JobSheet_No_List1'],InDate=request.POST['InDate'], OutDate=request.POST['OutDate'], KM_Reading1=request.POST['KM_Reading1'], Remarks=request.POST['Remarks'],Completion_Remarks=request.POST['Completion_Remarks'], Check_list_Template=request.POST['Check_list_Template'])
    member2.save()
    return redirect('/myapp/jobsheet')


def jobedit(request, id):
    members2 = Jobsheet.objects.get(id=id)
    context = {'members2': members2}
    return render(request, 'jobsheet/change.html', context)


def jobupdate(request, id):
    member2 = Jobsheet.objects.get(id=id)
    member2.Nature = request.POST['Nature']
    member2.Vehicle_No = request.POST['Vehicle_No']
    member2.JobSheet_No_List = request.POST['JobSheet_No_List']
    member2.Office_list = request.POST['Office_list']
    member2.Type = request.POST['Type']
    member2.In_Date = request.POST['In_Date']
    member2.Expt_Date = request.POST['Expt_Date']
    member2.Jobsheet_no = request.POST['Jobsheet_no']
    member2.Completion_Date = request.POST['Completion_Date']
    member2.Vehicle = request.POST['Vehicle']
    member2.Out_Date = request.POST['Out_Date']
    member2.Trailor = request.POST['Trailor']
    member2.KM_Reading = request.POST['KM_Reading']
    member2.Driver = request.POST['Driver']
    member2.Additional_KM = request.POST['Additional_KM']
    member2.Owner = request.POST['Owner']
    member2.Tyre_Supervisor = request.POST['Tyre_Supervisor']
    member2.Maintenance_Supervisor = request.POST['Maintenance_Supervisor']
    member2.Total_KM_Run = request.POST['Total_KM_Run']
    member2.Remark = request.POST['Remark']
    member2.pendding_Remark = request.POST['pendding_Remark']
    member2.To_DStoreate = request.POST['Store']
    member2.Close_Date = request.POST['Close_Date']
    member2.JobSheet_No_List1 = request.POST['JobSheet_No_List1']
    member2.InDate = request.POST['InDate']
    member2.OutDate = request.POST['OutDate']
    member2.KM_Reading1 = request.POST['KM_Reading1']
    member2.Remarks = request.POST['Remarks']
    member2.Completion_Remarks = request.POST['Completion_Remarks']
    member2.Check_list_Template = request.POST['Check_list_Template']
    member2.save()
    return redirect('/myapp/jobsheet')


def jobdelete(request, id):
    member2 = Jobsheet.objects.get(id=id)
    member2.delete()
    return redirect('/myapp/jobsheet')

#OMR Registration

def omradd(request):
    return render(request, 'omr/change.html')

def omrindex(request):
    members3 = OMR.objects.all()
    context = {'members3': members3}
    return render(request, 'omr/index.html', context)


def omrcreate(request):
    member3 = OMR(Vehicle_No=request.POST['Vehicle_No'], OMR_No_List=request.POST['OMR_No_List'], Office_list=request.POST['Office_list'], Date=request.POST['Date'],OMR_No=request.POST['OMR_No'], ORM_Type=request.POST['ORM_Type'], Spare_Group=request.POST['Spare_Group'], Completion_Date=request.POST['Completion_Date'],ORM_Nature=request.POST['ORM_Nature'], Vehicle_No1=request.POST['Vehicle_No1'], Driver=request.POST['Driver'], Place=request.POST['Place'],Supervisor=request.POST['Supervisor'], On_Road_Date=request.POST['On_Road_Date'], Trip_Detail=request.POST['Trip_Detail'], Approx_Amount=request.POST['Approx_Amount'],Remarks=request.POST['Remarks'], Comment=request.POST['Comment'], Varification_Date=request.POST['Varification_Date'], Verified_By=request.POST['Verified_By'],Varification_Remarks=request.POST['Varification_Remarks'])
    member3.save()
    return redirect('/myapp/omr')


def omredit(request, id):
    members3 = OMR.objects.get(id=id)
    context = {'members3': members3}
    return render(request, 'omr/change.html', context)


def omrupdate(request, id):
    member3 = OMR.objects.get(id=id)
    member3.Vehicle_No = request.POST['Vehicle_No']
    member3.OMR_No_List = request.POST['OMR_No_List']
    member3.Office_list = request.POST['Office_list']
    member3.Date = request.POST['Date']
    member3.OMR_No = request.POST['OMR_No']
    member3.ORM_Type = request.POST['ORM_Type']
    member3.Spare_Group = request.POST['Spare_Group']
    member3.Completion_Date = request.POST['Completion_Date']
    member3.ORM_Nature = request.POST['ORM_Nature']
    member3.Vehicle_No1 = request.POST['Vehicle_No1']
    member3.Driver = request.POST['Driver']
    member3.Place = request.POST['Place']
    member3.Supervisor = request.POST['Supervisor']
    member3.On_Road_Date = request.POST['On_Road_Date']
    member3.Trip_Detail = request.POST['Trip_Detail']
    member3.Approx_Amount = request.POST['Approx_Amount']
    member3.Remarks = request.POST['Remarks']
    member3.Comment = request.POST['Comment']
    member3.Varification_Date = request.POST['Varification_Date']
    member3.Verified_By = request.POST['Verified_By']
    member3.Varification_Remarks = request.POST['Varification_Remarks']
    member3.save()
    return redirect('/myapp/omr')


def omrdelete(request, id):
    member3 = OMR.objects.get(id=id)
    member3.delete()
    return redirect('/myapp/omr')

# Part Tracker

def partadd(request):
    return render(request, 'Part_Tracker/change.html')

def partindex(request):
    members4 = Part_Tracker.objects.all()
    context = {'members4': members4}
    return render(request, 'Part_Tracker/index.html', context)


def partcreate(request):
    member4 = Part_Tracker(Type=request.POST['Type'], SNo=request.POST['SNo'], Doc_No=request.POST['Doc_No'], Doc_Date=request.POST['Doc_Date'],CR_AC=request.POST['CR_AC'], DR_AC=request.POST['DR_AC'], Status=request.POST['Status'], Trail_Status=request.POST['Trail_Status'],Card_No=request.POST['Card_No'], Life=request.POST['Life'], S=request.POST['S'], Place=request.POST['Place'],Vehicle_No=request.POST['Vehicle_No'], KM_Reading=request.POST['KM_Reading'], KM_Run=request.POST['KM_Run'], Purchase_Cost=request.POST['Purchase_Cost'],TP_Coast=request.POST['TP_Coast'], Scrap_Cost=request.POST['Scrap_Cost'], Est_Cost=request.POST['Est_Cost'], Reason=request.POST['Reason'])
    member4.save()
    return redirect('/myapp/Part_Tracker')


def partedit(request, id):
    members4 = Part_Tracker.objects.get(id=id)
    context = {'members4': members4}
    return render(request, 'Part_Tracker/change.html', context)


def partupdate(request, id):
    member4 = Part_Tracker.objects.get(id=id)
    member4.Type = request.POST['Type']
    member4.SNo = request.POST['SNo']
    member4.Doc_No = request.POST['Doc_No']
    member4.Doc_Date = request.POST['Doc_Date']
    member4.CR_AC = request.POST['CR_AC']
    member4.DR_AC = request.POST['DR_AC']
    member4.Status = request.POST['Status']
    member4.Trail_Status = request.POST['Trail_Status']
    member4.Card_No = request.POST['Card_No']
    member4.Life = request.POST['Life']
    member4.S = request.POST['S']
    member4.Vehicle_No = request.POST['Vehicle_No']
    member4.KM_Reading = request.POST['KM_Reading']
    member4.KM_Run = request.POST['KM_Run']
    member4.Purchase_Cost = request.POST['Purchase_Cost']
    member4.TP_Coast = request.POST['TP_Coast']
    member4.Scrap_Cost = request.POST['Scrap_Cost']
    member4.Est_Cost = request.POST['Est_Cost']
    member4.Reason = request.POST['Reason']
    member4.save()
    return redirect('/myapp/Part_Tracker')


def partdelete(request, id):
    member4 = Part_Tracker.objects.get(id=id)
    member4.delete()
    return redirect('/myapp/Part_Tracker')

#PM Chart

def chartadd(request):
    return render(request, 'pm_chart/change.html')

def chartindex(request):
    members5 = PM_Chart.objects.all()
    context = {'members5': members5}
    return render(request, 'pm_chart/index.html', context)


def chartcreate(request):
    member5 = PM_Chart(SNo=request.POST['SNo'], Date=request.POST['Date'], Inactive_Date=request.POST['Inactive_Date'], Class_Name=request.POST['Class_Name'],PM_Name=request.POST['PM_Name'], Days=request.POST['Days'], KM_Run=request.POST['KM_Run'], KM_Alert=request.POST['KM_Alert'],Map_Next_PM=request.POST['Map_Next_PM'], Remark=request.POST['Remark'])
    member5.save()
    return redirect('/myapp/pm_chart')


def chartedit(request, id):
    members5 = PM_Chart.objects.get(id=id)
    context = {'members5': members5}
    return render(request, 'pm_chart/change.html', context)


def chartupdate(request, id):
    member5 = PM_Chart.objects.get(id=id)
    member5.SNo = request.POST['SNo']
    member5.Date = request.POST['Date']
    member5.Inactive_Date = request.POST['Inactive_Date']
    member5.Class_Name = request.POST['Class_Name']
    member5.PM_Name = request.POST['PM_Name']
    member5.DaysDays = request.POST['DaysDays']
    member5.KM_Run = request.POST['KM_Run']
    member5.KM_Alert = request.POST['KM_Alert']
    member5.Map_Next_PM = request.POST['Map_Next_PM']
    member5.Remark = request.POST['Remark']
    member5.save()
    return redirect('/myapp/pm_chart')


def chartdelete(request, id):
    member5 = PM_Chart.objects.get(id=id)
    member5.delete()
    return redirect('/myapp/pm_chart')

#Repair Dashboard

def dashadd(request):
    return render(request, 'dashboard/change.html')

def dashindex(request):
    members6 = Repair_Dashboard.objects.all()
    context = {'members6': members6}
    return render(request, 'dashboard/index.html', context)


def dashcreate(request):
    member6 = Repair_Dashboard(Office=request.POST['Office'], Vehicle_No=request.POST['Vehicle_No'], Jobsheet_no=request.POST['Jobsheet_no'], InDate=request.POST['InDate'],Expected_Date=request.POST['Expected_Date'], Vehicle_No1=request.POST['Vehicle_No1'], Driver_Name=request.POST['Driver_Name'], Supervisor_Name=request.POST['Supervisor_Name'],OutDate=request.POST['OutDate'])
    member6.save()
    return redirect('/myapp/dashboard')


def dashedit(request, id):
    members6 = Repair_Dashboard.objects.get(id=id)
    context = {'members6': members6}
    return render(request, 'dashboard/change.html', context)


def dashupdate(request, id):
    member6 = Repair_Dashboard.objects.get(id=id)
    member6.Office = request.POST['Office']
    member6.Vehicle_No = request.POST['Vehicle_No']
    member6.Jobsheet_no = request.POST['Jobsheet_no']
    member6.InDate = request.POST['InDate']
    member6.Expected_Date = request.POST['Expected_Date']
    member6.Vehicle_No1 = request.POST['Vehicle_No1']
    member6.Driver_Name = request.POST['Driver_Name']
    member6.Supervisor_Name = request.POST['Supervisor_Name']
    member6.OutDate = request.POST['OutDate']
    member6.save()
    return redirect('/myapp/dashboard')


def dashdelete(request, id):
    member6 = Repair_Dashboard.objects.get(id=id)
    member6.delete()
    return redirect('/myapp/dashboard')

#Repairs Consume

def conadd(request):
    return render(request, 'consume/change.html')

def conindex(request):
    members7 = Repair_Consume.objects.all()
    context = {'members7': members7}
    return render(request, 'consume/index.html', context)


def concreate(request):
    member7 = Repair_Consume(Nature=request.POST['Nature'], Vehicle_No1=request.POST['Vehicle_No1'], Supplier=request.POST['Supplier'], Consume_Search=request.POST['Consume_Search'],Office=request.POST['Office'], Supplier1=request.POST['Supplier1'], PO_Type=request.POST['PO_Type'], Narration=request.POST['Narration'],Document_Date=request.POST['Document_Date'], Voucher_Date=request.POST['Voucher_Date'], Document_No=request.POST['Document_No'], Vendor_No=request.POST['Vendor_No'],Vehicle_No=request.POST['Vehicle_No'], Expense_AC=request.POST['Expense_AC'], Ref=request.POST['Ref'], Labour_Code=request.POST['Labour_Code'],Labour_Qty=request.POST['Labour_Qty'], Labour_Rate=request.POST['Labour_Rate'], Labour_Amount=request.POST['Labour_Amount'], DoneBy=request.POST['DoneBy'],Labour_Remark=request.POST['Labour_Remark'])
    member7.save()
    return redirect('/myapp/consume')


def conedit(request, id):
    members7 = Repair_Consume.objects.get(id=id)
    context = {'members3': members7}
    return render(request, 'consume/change.html', context)


def conupdate(request, id):
    member7 = Repair_Consume.objects.get(id=id)
    member7.Nature = request.POST['Nature']
    member7.Vehicle_No1 = request.POST['Vehicle_No1']
    member7.Supplier = request.POST['Supplier']
    member7.Consume_Search = request.POST['Consume_Search']
    member7.Office = request.POST['Office']
    member7.Supplier1 = request.POST['Supplier1']
    member7.PO_Type = request.POST['PO_Type']
    member7.Narration = request.POST['Narration']
    member7.Document_Date = request.POST['Document_Date']
    member7.Voucher_Date = request.POST['Voucher_Date']
    member7.Document_No = request.POST['Document_No']
    member7.Vendor_No = request.POST['Vendor_No']
    member7.Vehicle_No = request.POST['Vehicle_No']
    member7.Expense_AC = request.POST['Expense_AC']
    member7.Ref = request.POST['Ref']
    member7.Labour_Code = request.POST['Labour_Code']
    member7.Labour_Qty = request.POST['Labour_Qty']
    member7.Labour_Rate = request.POST['Labour_Rate']
    member7.Labour_Amount = request.POST['Labour_Amount']
    member7.DoneBy = request.POST['DoneBy']
    member7.Labour_Remark = request.POST['Labour_Remark']
    member7.save()
    return redirect('/myapp/consume')


def condelete(request, id):
    member7 = Repair_Consume.objects.get(id=id)
    member7.delete()
    return redirect('/myapp/consume')