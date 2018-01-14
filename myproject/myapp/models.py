from django.db import models
from django.core.validators import RegexValidator

alphaSpaces = RegexValidator(r'^[a-zA-Z ]+$','Only letters and spaces are allowed')
Numerics = RegexValidator(r'\+?\d[\d -]{8,12}\d','Please enter valid contact number')
Number = RegexValidator(r'^[0-9]\d*(\.\d+)?$','Please Enter only Numbers')
alphanumeric = RegexValidator(r'^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')

ORM_CHOICES = (
    ('Item1','Item1'),
    ('Item2', 'Item2'),
)
Select_CHOICES = (
    ('Item1','Item1'),
    ('Item2', 'Item2'),
)
Spare_CHOICES = (
    ('Item1','Item1'),
    ('Item2', 'Item2'),
)
Nature_CHOICES = (
    ('Item1','Item1'),
    ('Item2', 'Item2'),
)
PO_CHOICES = (
    ('Item1','Item1'),
    ('Item2', 'Item2'),
)
DONE_CHOICES = (
    ('Item1','Item1'),
    ('Item2', 'Item2'),
)



# Create your models here.
class Jobsheet_trace(models.Model):
		From_Date = models.DateField()
		To_Date = models.DateField()
		JobSheet_No = models.CharField(max_length=100, validators=[alphanumeric])
		Vehicle_No = models.CharField(max_length=100, validators=[alphanumeric])

class Jobsheet(models.Model):
		Nature = models.CharField(max_length=100, validators=[alphanumeric])
		Vehicle_No = models.CharField(max_length=50, validators=[alphanumeric])
		JobSheet_No_List = models.CharField(max_length=100, validators=[alphanumeric])
		Office_list = models.CharField(max_length=100,  validators=[alphanumeric])
		Type = models.CharField(max_length=100, validators=[alphanumeric])
		In_Date = models.DateField()
		Expt_Date = models.DateField()
		Jobsheet_no = models.CharField(max_length=100, validators=[alphanumeric])
		Completion_Date = models.DateField()
		Vehicle = models.CharField(max_length=100, validators=[alphanumeric])
		Out_Date = models.DateField()
		Trailor = models.CharField(max_length=100, validators=[alphanumeric])
		KM_Reading = models.CharField(max_length=100, validators=[alphanumeric])
		Driver = models.CharField(max_length=100, validators=[alphanumeric])
		Additional_KM = models.CharField(max_length=100, validators=[alphanumeric])
		Owner = models.CharField(max_length=100, validators=[alphanumeric])
		Tyre_Supervisor = models.CharField(max_length=100, validators=[alphanumeric])
		Maintenance_Supervisor = models.CharField(max_length=100, validators=[alphanumeric])
		Total_KM_Run = models.CharField(max_length=100, validators=[alphanumeric])
		Remark = models.CharField(max_length=100, validators=[alphanumeric])
		pendding_Remark = models.CharField(max_length=100, validators=[alphanumeric])
		Store = models.CharField(max_length=100, validators=[alphanumeric])
		Close_Date = models.DateField()
		JobSheet_No_List1 = models.CharField(verbose_name=("JobSheet No List"),max_length=100, validators=[alphanumeric])
		InDate = models.DateField()
		OutDate = models.DateField()
		KM_Reading1 = models.CharField(verbose_name=("KM Reading"), max_length=100, validators=[alphanumeric])
		Remarks = models.CharField(max_length=100, validators=[alphanumeric])
		Completion_Remarks = models.CharField(max_length=100, validators=[alphanumeric])
		Check_list_Template = models.CharField(max_length=100, validators=[alphanumeric])

class OMR(models.Model):
		Vehicle_No = models.CharField(max_length=50, validators=[alphanumeric])
		OMR_No_List = models.CharField(max_length=100, validators=[alphanumeric])
		Office_list = models.CharField(max_length=100,  validators=[alphanumeric])
		Date = models.DateField()
		OMR_No = models.CharField(max_length=100, validators=[alphanumeric])
		ORM_Type = models.CharField(max_length=100, choices=ORM_CHOICES,)
		Spare_Group = models.CharField(max_length=100, validators=[alphanumeric])
		Completion_Date = models.DateField()
		ORM_Nature = models.CharField(max_length=100, validators=[alphanumeric])
		Vehicle_No1 = models.CharField(verbose_name=("Vehicle No"), max_length=100, validators=[alphanumeric])
		Driver = models.CharField(max_length=100, validators=[alphanumeric])
		Place = models.CharField(max_length=100, validators=[alphanumeric])
		Supervisor = models.CharField(max_length=100, validators=[alphanumeric])
		On_Road_Date = models.DateField()
		Trip_Detail = models.CharField(max_length=100, validators=[alphanumeric])
		Approx_Amount = models.CharField(max_length=100, validators=[alphanumeric])
		Remarks = models.CharField(max_length=100, validators=[alphanumeric])
		Comment = models.CharField(max_length=100, validators=[alphanumeric])
		Varification_Date = models.DateField()
		Verified_By = models.CharField(max_length=100, validators=[alphanumeric])
		Varification_Remarks = models.CharField(max_length=100, validators=[alphanumeric])

class Part_Tracker(models.Model):
		Type = models.CharField(max_length=100, choices=Select_CHOICES,)
		SNo = models.CharField(max_length=100, validators=[alphanumeric])
		Doc_No = models.CharField(max_length=100, validators=[alphanumeric])
		Doc_Date = models.DateField()
		CR_AC = models.CharField(max_length=100, validators=[alphanumeric])
		DR_AC = models.CharField(max_length=100, validators=[alphanumeric])
		Status = models.CharField(max_length=100, validators=[alphanumeric])
		Trail_Status = models.CharField(max_length=100, validators=[alphanumeric])
		Card_No = models.CharField(max_length=100, validators=[alphanumeric])
		Life = models.CharField(max_length=100, validators=[alphanumeric])
		S = models.BooleanField(max_length=100, validators=[alphanumeric])
		Vehicle_No = models.CharField(max_length=100, validators=[alphanumeric])
		KM_Reading = models.CharField(max_length=100, validators=[alphanumeric])
		KM_Run = models.CharField(max_length=100, validators=[alphanumeric])
		Purchase_Cost = models.CharField(max_length=100, validators=[alphanumeric])
		TP_Coast = models.CharField(max_length=100, validators=[alphanumeric])
		Scrap_Cost = models.CharField(max_length=100, validators=[alphanumeric])
		Est_Cost = models.CharField(max_length=100, validators=[alphanumeric])
		Reason = models.CharField(max_length=100, validators=[alphanumeric])

class PM_Chart(models.Model):
		SNo = models.CharField(max_length=50, validators=[alphanumeric])
		Date = models.DateField()
		Inactive_Date = models.DateField()
		Class_Name = models.CharField(max_length=100, validators=[alphanumeric])
		PM_Name = models.CharField(max_length=100, validators=[alphanumeric])
		Days = models.CharField(max_length=100, validators=[alphanumeric])
		KM_Run = models.CharField(max_length=100, validators=[alphanumeric])
		KM_Alert = models.CharField(max_length=100, validators=[alphanumeric])
		Map_Next_PM = models.CharField(max_length=100, validators=[alphanumeric])
		Remark = models.CharField(max_length=100, validators=[alphanumeric])

class PM_Master(models.Model):
		Preventive_list = models.CharField(max_length=100, validators=[alphanumeric])
		Preventive_Name = models.CharField(max_length=100, validators=[alphanumeric])
		Spare_Group = models.CharField(max_length=100, choices=Spare_CHOICES,)
		Nature = models.CharField(max_length=100, choices=Nature_CHOICES,)
		Description = models.CharField(max_length=200, validators=[alphanumeric])


class Repair_Dashboard(models.Model):
		Office = models.CharField(max_length=100,  validators=[alphanumeric])
		Vehicle_No = models.CharField(max_length=100, validators=[alphanumeric])
		Jobsheet_no = models.CharField(max_length=100, validators=[alphanumeric])
		InDate = models.DateField()
		Expected_Date = models.DateField()
		Vehicle_No1 = models.CharField(verbose_name=("Vehicle No"), max_length=200, validators=[alphanumeric])
		Driver_Name =  models.CharField(max_length=100,  validators=[alphanumeric])
		Supervisor_Name =  models.CharField(max_length=100,  validators=[alphanumeric])
		OutDate = models.DateField()

class Repair_Consume(models.Model):
		Nature = models.CharField(max_length=100, choices=Nature_CHOICES,)
		Vehicle_No1 = models.CharField(verbose_name=("Vehicle No"),max_length=100,  validators=[alphanumeric])
		Supplier = models.CharField(max_length=100, validators=[alphanumeric])
		Consume_Search = models.CharField(max_length=100, validators=[alphanumeric])
		Office = models.CharField(max_length=100,  validators=[alphanumeric])
		Supplier1 = models.CharField(verbose_name=("Supplier"), max_length=200, validators=[alphanumeric])
		PO_Type = models.CharField(max_length=100, choices=PO_CHOICES,)
		Narration =  models.CharField(max_length=100,  validators=[alphanumeric])
		Document_Date = models.DateField()
		Voucher_Date = models.DateField()
		Document_No =  models.CharField(max_length=100,  validators=[alphanumeric])
		Vendor_No =  models.CharField(max_length=100,  validators=[alphanumeric])
		Vehicle_No =  models.CharField(max_length=100,  validators=[alphanumeric])
		Expense_AC = models.CharField(max_length=100,  validators=[alphanumeric])
		Ref =  models.CharField(verbose_name=("Ref / PONo"), max_length=100,  validators=[alphanumeric])
		Labour_Code = models.CharField(max_length=100,  validators=[alphanumeric])
		Labour_Qty = models.CharField(max_length=100,  validators=[alphanumeric])
		Labour_Rate = models.CharField(max_length=100,  validators=[alphanumeric])
		Labour_Amount = models.CharField(max_length=100,  validators=[alphanumeric])
		DoneBy = models.CharField(max_length=100, choices=DONE_CHOICES,)
		Labour_Remark = models.CharField(max_length=100,  validators=[alphanumeric])

