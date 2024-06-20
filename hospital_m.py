from tkinter import *
from tkinter import ttk , messagebox
import random
import time
import datetime
import mysql.connector 

class hospital:
        def __init__(self, root):
                self.root = root
                self.root.title("TMH Management System")
                self.root.geometry("1560x900+0+0")
                self.nameoftablets = StringVar()
                self.Reference_No = StringVar()
                self.dose = StringVar()
                self.nooftablets = StringVar()
                self.lot = StringVar()
                self.issuedate = StringVar()
                self.expirydate = StringVar()
                self.dailydose = StringVar()
                self.storage = StringVar()
                self.ayushmancard = StringVar()
                self.patient_name = StringVar()
                self.dob = StringVar()
                self.address = StringVar()

                lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hospital Management System", fg="BLUE", bg="White", font=("times new Roman", 50, "bold"))
                lbltitle.pack(side=TOP, fill="x")

                



        #---------------------------data frame---------------------------------

                Dataframe = Frame(self.root, bd=20, relief=RIDGE)
                Dataframe.place(x=0, y=130, width=1540, height=400)
                
                DataframeLeft = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE, font=("times new Roman", 12, "bold"), text="Patient Information")
                DataframeLeft.place(x=1, y=0, width=1060, height=350)
                
                DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new Roman", 12, "bold"), text="Prescription")
                DataframeRight.place(x=1060, y=0, width=400, height=350)

        #----------------------------------button frame-----------------------------------------

                buttonframe = Frame(self.root, bd=20, relief=RIDGE)
                buttonframe.place(x=0, y=530, width=1530, height=83)

        #----------------------------------details frame-----------------------------------------

                Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
                Detailsframe.place(x=0, y=610, width=1530, height=225)

                ##++++++++++++++++++++++++++++++++++++++++++DataframeLeft++++++++++++++++++++++++++++++++++++++=
                lblNameTablet = Label(DataframeLeft , text="Names of Tablet ", font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblNameTablet.grid(row=0, column=0, sticky=W)      

                comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.nameoftablets, state="readonly", font=("arial ",12,"bold"), width=33)
                comNametablet["values"] = ("Aspirin", "Ibuprofen", "Paracetamol", "Naproxen", "Acetaminophen", "Diclofenac", "Celecoxib", "Meloxicam", "Indomethacin", "Tramadol", "Codeine", "Morphine", "Fentanyl", "Hydrocodone", "Oxycodone", "Acetaminophen/Codeine", "Acetaminophen/Oxycodone", "Acetaminophen/Hydrocodone", "Acetaminophen/Tramadol", "Acetaminophen/Morphine", "Rabeprazole", "Omeprazole", "Esomeprazole", "Lansoprazole", "Pantoprazole", "Famotidine", "Ranitidine", "Cimetidine", "Nizatidine", "Sucralfate", "Bismuth subsalicylate", "Metoclopramide", "Ondansetron", "Promethazine", "Dimenhydrinate", "Meclizine", "Loratadine", "Cetirizine", "Fexofenadine", "Desloratadine", "Diphenhydramine", "Chlorpheniramine", "Hydroxyzine", "Levocetirizine", "Azelastine", "Montelukast", "Zafirlukast", "Zileuton", "Theophylline", "Beclomethasone", "Budesonide", "Fluticasone", "Mometasone", "Triamcinolone", "Ciclesonide", "Prednisone", "Prednisolone", "Dexamethasone", "Hydrocortisone", "Methotrexate", "Leflunomide", "Azathioprine", "Mycophenolate mofetil", "Tacrolimus", "Cyclosporine", "Sirolimus", "Everolimus", "Belatacept", "Basiliximab", "Daclizumab", "Alemtuzumab", "Rituximab", "Trastuzumab", "Bevacizumab", "Cetuximab", "Panitumumab", "Pembrolizumab", "Nivolumab", "Ipilimumab", "Atezolizumab", "Durvalumab", "Avelumab", "Abatacept", "Tocilizumab", "Ustekinumab", "Secukinumab", "Ixekizumab", "Adalimumab", "Etanercept", "Infliximab", "Golimumab", "Certolizumab pegol", "Vedolizumab", "Natalizumab", "Eculizumab", "Soliris", "Eltrombopag", "Romiplostim", "Filgrastim", "Pegfilgrastim", "Sargramostim", "Epoetin alfa", "Darbepoetin alfa", "Ferrous sulfate", "Ferrous gluconate", "Ferrous fumarate", "Iron polymaltose", "Polysaccharide iron complex", "Elemental iron", "Cyanocobalamin", "Methylcobalamin", "Hydroxocobalamin", "Folic acid", "L-methylfolate", "Ferrous sulfate/folic acid", "Ferrous gluconate/folic acid", "Ferrous fumarate/folic acid", "Ferrous sulfate/vitamin C", "Ferrous gluconate/vitamin C", "Ferrous fumarate/vitamin C", "Multivitamin", "Prenatal vitamin", "Vitamin D3", "Calcium carbonate", "Calcium citrate", "Calcium phosphate", "Calcium gluconate", "Calcium lactate", "Calcium carbonate/vitamin D3", "Calcium citrate/vitamin D3", "Calcium phosphate/vitamin D3", "Calcium gluconate/vitamin D3", "Calcium lactate/vitamin D3", "Alendronate", "Risedronate", "Ibandronate", "Zoledronic acid", "Denosumab", "Teriparatide", "Abaloparatide", "Calcitonin", "Strontium ranelate", "Conjugated estrogens", "Estradiol", "Estriol", "Ethinylestradiol", "Norethindrone", "Levonorgestrel", "Drospirenone", "Desogestrel", "Norgestimate", "Medroxyprogesterone", "Progesterone", "Testosterone", "Dehydroepiandrosterone", "Danazol", "Finasteride", "Dutasteride", "Tamsulosin", "Alfuzosin", "Silodosin", "Doxazosin", "Terazosin", "Prazosin", "Metoprolol", "Atenolol", "Propranolol", "Bisoprolol", "Carvedilol", "Nebivolol", "Labetalol", "Sotalol", "Verapamil", "Diltiazem", "Amlodipine", "Felodipine", "Nifedipine", "Nicardipine","Doxazosin", "Dutasteride", "Erythromycin", "Escitalopram", "Ezetimibe", "Famotidine", "Febuxostat", "Fenofibrate", "Ferrous sulfate", "Finasteride", "Fluconazole", "Fluoxetine", "Fluticasone", "Folic acid", "Formoterol", "Fosinopril", "Gabapentin", "Gemfibrozil", "Glimepiride", "Glyburide", "Haloperidol", "Heparin", "Hydrochlorothiazide", "Hydrocodone", "Hydrocortisone", "Hydroxychloroquine", "Hydroxyzine", "Ibandronate", "Ibuprofen", "Imipramine", "Indapamide", "Indomethacin", "Infliximab", "Insulin", "Irbesartan", "Isosorbide mononitrate", "Isotretinoin", "Labetalol", "Lamivudine", "Lamotrigine", "Lansoprazole", "Latanoprost", "Leflunomide", "Levothyroxine", "Lidocaine", "Lisinopril", "Lithium", "Loperamide", "Loratadine", "Losartan", "Lovastatin", "Medroxyprogesterone", "Meloxicam", "Memantine", "Metformin", "Methadone", "Methotrexate", "Methylprednisolone", "Metoclopramide", "Metolazone", "Metoprolol", "Miconazole", "Midazolam", "Mirtazapine", "Mometasone", "Montelukast", "Morphine", "Nabumetone", "Nadolol", "Naproxen", "Nebivolol", "Nifedipine", "Nitroglycerin", "Nortriptyline", "Olanzapine", "Olmesartan", "Omeprazole", "Ondansetron", "Oxaliplatin", "Oxcarbazepine", "Oxybutynin", "Oxycodone", "OxyContin", "Pantoprazole", "Paroxetine", "Penicillin", "Pentoxifylline", "Phenobarbital", "Phenytoin", "Pioglitazone", "Pramipexole", "Prednisolone", "Prednisone", "Pregabalin", "Pravastatin", "Prednisolone", "Prochlorperazine", "Promethazine", "Propanolol", "Quetiapine", "Quinapril", "Raloxifene", "Ramelteon", "Ramipril", "Ranitidine", "Repaglinide", "Risedronate", "Risperidone", "Rivastigmine", "Ropinirole", "Rosiglitazone", "Rosuvastatin", "Salmeterol", "Selegiline", "Sertraline", "Simvastatin", "Sitagliptin", "Spironolactone", "Sumatriptan", "Tadalafil", "Tamoxifen", "Temazepam", "Terazosin", "Terbinafine", "Tetracycline", "Thalidomide", "Thyroxine", "Timolol", "Tiotropium", "Tizanidine", "Tolterodine", "Topiramate", "Torsemide", "Tramadol", "Trazodone", "Triamcinolone", "Triamterene", "Triazolam", "Trifluoperazine", "Trilostane", "Triptorelin", "Valacyclovir", "Valproate", "Valsartan", "Varenicline", "Venlafaxine", "Verapamil", "Warfarin", "Zafirlukast", "Ziprasidone", "Zolmitriptan", "Zolpidem", "Zonisamide")  # Add values here
                comNametablet.current(0)
                comNametablet.grid(row=0, column=1)

                lblReference_No = Label(DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
                lblReference_No.grid(row=1, column=0, sticky=W)
                txtReference_No = Entry(DataframeLeft, textvariable=self.Reference_No, font=("arial", 12, "bold"), width=35)
                txtReference_No.grid(row=1, column=1)

                lblDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
                lblDose.grid(row=2, column=0, sticky=W)
                txtdose = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtdose.grid(row=2, column=1)

                lblNoOftablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="Number of tablets:", padx=2, pady=6)
                lblNoOftablets.grid(row=3, column=0, sticky=W)
                txtNoOftablets = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtNoOftablets.grid(row=3, column=1)

                lblLot = Label(DataframeLeft, font=("arial", 13, "bold"), text="LOT : ", padx=2, pady=6)
                lblLot.grid(row=4, column=0, sticky=W)
                txtLot = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtLot.grid(row=4, column=1)

                lblissuedate = Label(DataframeLeft, font=("arial", 13, "bold"), text="Issue Date : ", padx=2, pady=6)
                lblissuedate.grid(row=5, column=0, sticky=W)
                txtissuedate = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtissuedate.grid(row=5, column=1)

                lblExpDate = Label(DataframeLeft, font=("arial", 13, "bold"), text="Expiry date : ", padx=2, pady=6)
                lblExpDate.grid(row=6, column=0, sticky=W)
                txtExpDate = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtExpDate.grid(row=6, column=1)

                lbldailydose = Label(DataframeLeft, font=("arial", 13, "bold"), text="Daily Dose : ", padx=2, pady=6)
                lbldailydose.grid(row=7, column=0, sticky=W)
                txtdailydose = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtdailydose.grid(row=7, column=1)
                
                lblsideeffect = Label(DataframeLeft, font=("arial", 13, "bold"), text="Side Effect : ", padx=2, pady=6)
                lblsideeffect.grid(row=8, column=0, sticky=W)
                txtsideeffect = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtsideeffect.grid(row=8, column=1)

                lblinformation = Label(DataframeLeft, font=("arial", 13, "bold"), text="information : ", padx=2, pady=6)
                lblinformation.grid(row=0, column=2, sticky=W)
                txtinformation = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtinformation.grid(row=0, column=3)

                lblblood_pressure = Label(DataframeLeft, font=("arial", 13, "bold"), text="blood pressure : ", padx=2, pady=6)
                lblblood_pressure.grid(row=1, column=2, sticky=W)
                txtblood_pressure = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtblood_pressure.grid(row=1, column=3)

                lblStrong_advice = Label(DataframeLeft, font=("arial", 13, "bold"), text="strong Advice : ", padx=2, pady=6)
                lblStrong_advice.grid(row=2, column=2, sticky=W)
                txtStrong_advice = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtStrong_advice.grid(row=2, column=3)

                lblmedication = Label(DataframeLeft, font=("arial", 13, "bold"), text="Medication : ", padx=2, pady=6)
                lblmedication.grid(row=3, column=2, sticky=W)
                txtmedication = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtmedication.grid(row=3, column=3)

                lblPatient_id = Label(DataframeLeft, font=("arial", 13, "bold"), text="Patient ID :", padx=2, pady=6)
                lblPatient_id.grid(row=4, column=2, sticky=W)
                txtPatient_id = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtPatient_id.grid(row=4, column=3)

                lblayushman_card = Label(DataframeLeft, font=("arial", 13, "bold"), text="Ayushman Card :", padx=2, pady=6)
                lblayushman_card.grid(row=5, column=2, sticky=W)
                txtayushman_card = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtayushman_card.grid(row=5, column=3)

                lblpatient_name = Label(DataframeLeft, font=("arial", 13, "bold"), text="Patient name :", padx=2, pady=6)
                lblpatient_name.grid(row=6, column=2, sticky=W)
                txtpatient_name = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtpatient_name.grid(row=6, column=3)

                lblDate_of_birth = Label(DataframeLeft, font=("arial", 13, "bold"), text="Date Of Birth :", padx=2, pady=6)
                lblDate_of_birth.grid(row=7, column=2, sticky=W)
                txtDate_of_birth = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtDate_of_birth.grid(row=7, column=3)

                lblpatientaddress = Label(DataframeLeft, font=("arial", 13, "bold"), text="Patient address :", padx=2, pady=6)
                lblpatientaddress.grid(row=8, column=2, sticky=W)
                txtpatientaddress = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
                txtpatientaddress.grid(row=8, column=3)

                #___________________________________________________DataframeRight______________________________________________________

                self.txtPrescription = Text(DataframeRight, font=("Arial", 12, "bold"), width=39, height=16, padx=2, pady=6)
                self.txtPrescription.grid(row=0, column=0)

                #-----------buttons------------------------------
                
                
                btnPrescription = Button(buttonframe, text="Prescription", bg="green", fg="white", font=("Arial", 12, "bold"), width=23, height=1, padx=2, pady=6)
                btnPrescription.grid(row=0, column=0)

                btnPrescriptiondata = Button(buttonframe, text="Prescription data", bg="green", fg="white", font=("Arial", 12, "bold"), width=23, height=1, padx=2, pady=6, command=self.iPrescriptionData)
                btnPrescriptiondata.grid(row=0, column=1)

                btnupdate = Button(buttonframe, text="Update", bg="green", fg="white", font=("Arial", 12, "bold"), width=24, height=1, padx=2, pady=6)
                btnupdate.grid(row=0, column=2)

                btndelete = Button(buttonframe, text="Delete", bg="green", fg="white", font=("Arial", 12, "bold"), width=24, height=1, padx=2, pady=6)
                btndelete.grid(row=0, column=3)

                btnclear = Button(buttonframe, text="Clear", bg="green", fg="white", font=("Arial", 12, "bold"), width=24, height=1, padx=2, pady=6)
                btnclear.grid(row=0, column=4)

                btnexit = Button(buttonframe, text="Exit", bg="green", fg="white", font=("Arial", 12, "bold"), width=24, height=1, padx=2, pady=6)
                btnexit.grid(row=0, column=5)

                
                #==================================table & scroll bar++++++++++++++++++++++++++++++++++
                #==================================table & scroll bar++++++++++++++++++++++++++++++++++
                scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
                scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

                self.hospital_table = ttk.Treeview(Detailsframe, column=("nameoftablets", "Reference_No", "dose", "nooftablets", "lot", "issuedate",
                                                                        "expdate", "dailydose", "storage", "ayushmancard", "patient_name",
                                                                        "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)

                scroll_x.config(command=self.hospital_table.xview)
                scroll_y.config(command=self.hospital_table.yview)

                self.hospital_table.heading("nameoftablets", text="Name of Tablets")
                self.hospital_table.heading("Reference_No", text="Reference No.")
                self.hospital_table.heading("dose", text="Dose")
                self.hospital_table.heading("nooftablets", text="Number of Tablets")
                self.hospital_table.heading("lot", text="Lot")
                self.hospital_table.heading("issuedate", text="Issue Date")
                self.hospital_table.heading("expdate", text="Expiry date")
                self.hospital_table.heading("dailydose", text="Daily dose")
                self.hospital_table.heading("storage", text="Storage")
                self.hospital_table.heading("ayushmancard", text="Ayushman number")
                self.hospital_table.heading("patient_name", text="Patient name")
                self.hospital_table.heading("dob", text="Date of birth")
                self.hospital_table.heading("address", text="Address")

                self.hospital_table["show"] = "headings"

                self.hospital_table.column("nameoftablets", width=100)
                self.hospital_table.column("Reference_No", width=100)
                self.hospital_table.column("dose", width=100)
                self.hospital_table.column("nooftablets", width=100)
                self.hospital_table.column("lot", width=100)
                self.hospital_table.column("issuedate", width=100)
                self.hospital_table.column("expdate", width=100)
                self.hospital_table.column("dailydose", width=100)
                self.hospital_table.column("storage", width=100)
                self.hospital_table.column("ayushmancard", width=100)
                self.hospital_table.column("patient_name", width=100)
                self.hospital_table.column("dob", width=100)
                self.hospital_table.column("address", width=100)

                self.hospital_table.pack(fill=BOTH, expand=1)


#======================================================functionality declaration =======================================================
        def iPrescriptionData(self):
                if self.nameoftablets.get() == "" or self.Reference_No.get() == "":
                        messagebox.showerror("Error", "All fields are required")
                else:
                        try:
                                conn = mysql.connector.connect(
                                        host="localhost",
                                        user="root",
                                        password="addyours@",
                                        database="mydata"
                                )
                                my_cursor = conn.cursor()

                                sql_query = "INSERT INTO hospital (nameoftablets, Reference_No, dose, nooftablets, lot, issuedate, expdate, dailydose, storage, ayushmancard, patient_name, dob, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                
                                data = (
                                        self.nameoftablets.get(),
                                        self.Reference_No.get(),
                                        self.dose.get(),
                                        self.nooftablets.get(),
                                        self.lot.get(),
                                        self.issuedate.get(),
                                        self.expirydate.get(),
                                        self.dailydose.get(),
                                        self.storage.get(),
                                        self.ayushmancard.get(),
                                        self.patient_name.get(),
                                        self.dob.get(),
                                        self.address.get()
                                )

                                my_cursor.execute(sql_query, data)
                                conn.commit()

                                messagebox.showinfo("Success", "Data inserted successfully")
                        
                        except mysql.connector.Error as e:
                                messagebox.showerror("Error", f"Error in inserting data: {str(e)}")

                        finally:
                                if 'conn' in locals() and conn.is_connected():
                                        my_cursor.close()
                                        conn.close()

if __name__ == "__main__":
    root = Tk()
    application = hospital(root)
    root.mainloop()
