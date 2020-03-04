import collections
from collections import OrderedDict
from datetime import datetime
from random import randint

import pyrebase
from cryptography.fernet import Fernet
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import Common
from . import PyConfig
from .SendMail import sendmail


def connect_firebase():
    firebase = pyrebase.initialize_app(PyConfig.config1)
    auth = firebase.auth()
    db = firebase.database()
    return db


def category(request, key):
    db = connect_firebase()
    schemes = OrderedDict()
    catname = request.GET['category']
    try:
        schemes = db.child("Scheme").order_by_child("level").equal_to(catname).get().val()
    except:
        print("Error")
    return render(request, 'category.html', {"scheme": schemes, "islog": Common.isLogin})


def home(request):
    db = connect_firebase()
    trusts = db.child("Trust").order_by_key().get().val()
    schemes = db.child("Scheme").order_by_key().limit_to_last(9).get().val()
    return render(request, 'home.html', {"scheme": schemes, "all_trusts": trusts, "islog": Common.isLogin})


def login(request):
    return render(request, 'login.html', {})


def adminlogin(request):
    return render(request, 'adminlogin.html', {})


def adminverify(request):
    adminname = request.POST.get('trust_username')
    password = request.POST.get('password')

    db = connect_firebase()
    username = db.child("Admin").child("username").get().val()
    passworddb = db.child("Admin").child("password").get().val()

    if adminname == username and password == passworddb:

        Common.isAdminLogin = True
        Common.admin = db.child("Admin").get().val()
        return HttpResponseRedirect('/adminhome')
    else:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Invalid Password or usrername",
                       "path": "admin-login"})


def adminhome(req):
    if (Common.isAdminLogin):
        data = OrderedDict()

        db = connect_firebase()
        try:
            data = db.child("Trust").get().val()
        except:
            pass

        print(data)
        return render(req, 'admin_home.html',
                      {"admin": Common.admin, "trusts": data})
    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def addtrust(req):
    if (Common.isAdminLogin):

        timestamp = datetime.timestamp(datetime.now())
        trustkey = str(timestamp).replace('.', '')
        return render(req, 'addtrust.html',
                      {"admin": Common.admin, "trustkey": trustkey})
    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def addtrustdb(request):
    if (Common.isAdminLogin):
        tname = request.POST['tname']
        tcontact = request.POST['tcontact']
        temailid = request.POST['temailid']
        tabout = request.POST['tabout']
        taddress = request.POST['taddress']
        tvision = request.POST['tvision']
        tpass = request.POST['tpass']
        tkey = request.POST['trustkey']
        logo = request.POST['trustlogourl']
        print(logo)
        tlogo = "https://firebasestorage.googleapis.com/v0/b/scholar-help-966a2.appspot.com/o/trust_logo%2F" + tkey + ".png?alt=media"

        db = connect_firebase()
        temail = None
        tphone = None

        try:
            temail = db.child("Trust").order_by_child("mailid").equal_to(temailid).get().val()
            print(temail + "mailid")
        except:
            pass
        try:

            tphone = db.child("Trust").order_by_child("contact").equal_to(tcontact).get().val()

        except:
            pass
        if temail:
            return render(request, 'redirecthome.html',
                          {"swicon": "error", "swtitle": "Error", "swmsg": "Trust Email Exists", "path": "addtrust"})
        elif tphone:
            return render(request, 'redirecthome.html',
                          {"swicon": "error", "swtitle": "Error", "swmsg": "Trust Phone Exists", "path": "addtrust"})
        else:

            data = {
                "name": tname, "contact": tcontact, "mailid": temailid,
                "about": tabout, "address": taddress, "vision": tvision, "password": tpass
                , "logo": tlogo, "username": tname

            }
            msgsend = "" \
                      "You have been register on scholarhelp. " \
                      "Your password is " \
                      "" + tpass + " ."
            print(data)

            db.child("Trust").child(str(tkey)).update(data)
            sendmail(temailid, "Successfully Registered on Scholar Help -" + tkey
                     , msgsend
                     )

            return render(request, 'redirecthome.html',
                          {"swicon": "success", "swtitle": "Done", "swmsg": "Trust Added Successfully",
                           "path": "adminhome"})

    else:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def adminedittrustview(req):
    if (Common.isAdminLogin):
        tkey = req.POST['tkey']
        db = connect_firebase()
        tru = db.child("Trust").child(str(tkey)).get().val()

        return render(req, 'admin_edit_trust.html',
                      {"trustkey": str(tkey), "trust_val": tru})
    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def adminstudentview(req):
    if (Common.isAdminLogin):
        db = connect_firebase()
        try:
            data = db.child("users").get().val()
        except:
            pass

        print(data)
        return render(req, 'view_all_student.html',
                      {"admin": Common.admin, "Users": data})

    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def studentprofile(req):
    if (Common.isAdminLogin):
        tkey = req.POST['tkey']
        db = connect_firebase()
        userprofile = None
        accno = None
        try:
            userprofile = db.child("UserProfile").child(str(tkey)).get().val()

            cipher = Fernet(Common.encyptionkey)
            accno = cipher.decrypt(userprofile.get("account_number").encode()).decode()

        except:
            pass
        return render(req, 'student_comp_profile.html',
                      {

                          "userprofile": userprofile, "accno": accno,

                      })


    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def removestudent(req):
    if (Common.isAdminLogin):
        tkey = req.POST['tkey']
        db = connect_firebase()
        userprofile = None
        accno = None
        try:
            db.child("UserProfile").child(str(tkey)).remove()

        except:
            pass
        try:
            db.child("users").child(str(tkey)).remove()

        except:
            pass
        try:
            print(tkey + "user id")
            userapp = db.child("AppliedScheme").order_by_child("userid").equal_to(str(tkey)).get().val()
            all11 = db.child("AppliedScheme").get().val()
            all(map(all11.pop, userapp))
            db.child("AppliedScheme").set(all11)
        except:
            pass
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Student Remove Successfully",
                       "path": "adminhome"})


    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def removetrust(req):
    if (Common.isAdminLogin):
        tkey = req.POST['tkey']
        db = connect_firebase()
        userprofile = None
        print(tkey + " tt")
        accno = None
        try:
            tt = db.child("Trust").child(str(tkey)).remove()
            print(tt + " tt")

        except:
            pass

        try:

            tscheme = db.child("Scheme").order_by_child("trust_id").equal_to(str(tkey)).get().val()
            alls = db.child("Scheme").get().val()
            all(map(alls.pop, tscheme))
            db.child("Scheme").set(alls)
        except:
            pass
        try:

            ascheme = db.child("AppliedScheme").order_by_child("trust_id").equal_to(str(tkey)).get().val()
            allaps = db.child("AppliedScheme").get().val()
            all(map(allaps.pop, ascheme))
            db.child("AppliedScheme").set(allaps)
        except:
            pass
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Trust Remove Successfully",
                       "path": "adminhome"})


    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def adminupdattrust(request):
    if (Common.isAdminLogin):
        tname = request.POST['tname']
        tcontact = request.POST['tcontact']
        temailid = request.POST['temailid']
        tabout = request.POST['tabout']
        taddress = request.POST['taddress']
        tvision = request.POST['tvision']
        tpass = request.POST['tpass']
        tkey = request.POST['tkey']

        data = {
            "name": tname, "contact": tcontact, "mailid": temailid,
            "about": tabout, "address": taddress, "vision": tvision, "password": tpass
        }
        db = connect_firebase()
        db.child("Trust").child(tkey).update(data)

        return render(request, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Trust Updated Successfully",
                       "path": "adminhome"})

    else:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def trust_login(request):
    return render(request, 'trust_login.html', {})


def forgotpass(request):
    return render(request, 'forgotpass.html', {})


def sendotp(request):
    db = connect_firebase()
    user = OrderedDict()
    getmail = request.POST['mail']
    try:
        user = db.child("users").order_by_child("mail").equal_to(getmail).get().val()
    except:
        print("Error")

    if not user:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Mail Id is not registered",
                       "path": "forgotpassword"})

    otp = str(randint(1000, 9999))
    Common.forgotpassotp = otp
    Common.forgotpassotptime = datetime.now()
    title = "Reset Your Password"
    msg = "Enter following OTP within 15 minutes to chage your password.\nOTP is " + otp
    for key, value in user.items():
        Common.userphone = key

    sendmail(getmail, title, msg)
    return HttpResponseRedirect('/verifyotp')


def verifyotp(request):
    return render(request, 'verifyotp.html', {})


def checkotp(request):
    getOTP = request.POST['otp']
    diff = datetime.now() - Common.forgotpassotptime
    otptime = diff.total_seconds()
    if getOTP != Common.forgotpassotp:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Wrong OTP Entered", "path": "verifyotp"})
    elif otptime > 15 * 60:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "OTP Expired", "path": "login"})
    else:
        return HttpResponseRedirect('/changepassword')


def changepassword(request):
    return render(request, 'changepassword.html', {})


def updatepassword(request):
    new_password = request.POST['pass']
    db = connect_firebase()

    db.child("users").child(Common.userphone).child("password").set(
        new_password
    )

    return render(request, 'redirecthome.html',
                  {"swicon": "success", "swtitle": "Done", "swmsg": "Password Changed Successfully.",
                   "path": "login"})


def verify(request):
    if not Common.isLogin:
        mail = request.POST.get('mail')
        password = request.POST.get('password')

        db = connect_firebase()
        user = db.child("users").child(mail).get()

        if not user.val():
            return render(request, 'redirecthome.html',
                          {"swicon": "error", "swtitle": "Error", "swmsg": "User does not exists", "path": "login"})
        elif password == user.val().get("password"):
            c = {'user': user.val()}
            Common.currentUser = user
            Common.isLogin = True
            return HttpResponseRedirect('/')
        else:
            return render(request, 'redirecthome.html',
                          {"swicon": "error", "swtitle": "Error", "swmsg": "Invalid Password",
                           "path": "login"})
    else:
        c = {'user': Common.currentUser.val()}
        return HttpResponseRedirect('/')


def trust_verify(request):
    if not Common.isTrustLogin:
        trustusername = request.POST.get('trust_username')
        password = request.POST.get('password')

        print(password)
        db = connect_firebase()
        user = db.child("Trust").order_by_child("mailid").equal_to(trustusername).get().val()
        for key, value in user.items():
            trustkey = key
            trust = value

        if not trust:
            return render(request, 'redirecthome.html',
                          {"swicon": "error", "swtitle": "Error", "swmsg": "Invalid Trust Id", "path": "trustlogin"})
        elif password == trust.get("password"):
            Common.trustkey = trustkey
            Common.trustVal = trust
            Common.isTrustLogin = True
            return HttpResponseRedirect('/trusthome')
        else:
            return render(request, 'redirecthome.html',
                          {"swicon": "error", "swtitle": "Error", "swmsg": "Invalid Password",
                           "path": "trustlogin"})
    else:
        c = {'user': Common.currentUser.val()}
        return HttpResponseRedirect('/')


def trust_home(req):
    if (Common.isTrustLogin):
        data = OrderedDict()

        db = connect_firebase()
        try:
            data = db.child("AppliedScheme").order_by_child("trust_id").equal_to(
                Common.trustkey).get().val()
            data = collections.OrderedDict(reversed(list(data.items())))
        except:
            pass

        print(data)
        return render(req, 'trust_home.html',
                      {"trustkey": Common.trustkey, "trust_val": Common.trustVal, "applied_schemes": data})
    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def viewtakeaction(request):
    userphone = request.POST['userphone']
    applicationid = request.POST['applicationid']

    if (Common.isTrustLogin):

        db = connect_firebase()
        applied = OrderedDict()
        amount_received = 0
        application = db.child("AppliedScheme").child(applicationid).get().val()
        userprofile = db.child("UserProfile").child(userphone).get().val()
        cipher = Fernet(Common.encyptionkey)
        accno = cipher.decrypt(userprofile.get("account_number").encode()).decode()
        pendingamt = int(userprofile.get("coursefees"))
        schemeeligibility = db.child("Scheme").child(application.get("scheme_id")).child("eligibility").get().val()

        userappliedscholarship = db.child("AppliedScheme").order_by_child("userid").equal_to(
            userphone).get().val()
        del userappliedscholarship[applicationid]
        print(userappliedscholarship)

        for key, value in userappliedscholarship.items():
            print(key, "is ", value.get("status"))
            if value.get("status") == "Approve":
                print(value, "is approve")
                amount_received += int(value.get("sanctionedamount"))
                tmp = {key: value}
                applied.update(tmp)
                print(applied)
        pendingamt = pendingamt - amount_received
        return render(request, 'trust_takeaction.html',
                      {"trustkey": Common.trustkey, "trust_val": Common.trustVal,
                       "application": application, "applicationid": applicationid,
                       "userprofile": userprofile, "accno": accno, "appliedscholarship": applied,
                       "amtrec": str(amount_received), "amtpen": str(pendingamt), "schemeeligibility": schemeeligibility

                       })
    else:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def updateapplicationstatus(request):
    if (Common.isTrustLogin):
        applicationid = request.POST['applicationid']
        status = request.POST['status']
        interviewdate = request.POST['interviewdate']
        sancamt = request.POST['sancamt']
        remark = request.POST['remark']
        mail = request.POST['mail']
        schemename = request.POST['schemename']

        data = {
            "interviewdate": interviewdate, "status": status, "sanctionedamount": sancamt,
            "remark": remark
        }
        db = connect_firebase()
        db.child("AppliedScheme").child(applicationid).update(data)

        title = "ScholarHelp - Status updated fo applicatiod id " + applicationid
        msg = "Your application status for " + schemename + " has been updated to " + status + ".Please login to " \
                                                                                               "ScholarHelp to view " \
                                                                                               "more details. "
        print(msg)
        sendmail(mail, title, msg)
        return render(request, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Application Status Updated Successfully",
                       "path": "trusthome"})

    else:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def viewtrustprofile(request):
    db = connect_firebase()
    Common.trustVal = db.child("Trust").child(Common.trustkey).get().val()

    return render(request, 'trust_profile.html',
                  {"trustkey": Common.trustkey, "trust_val": Common.trustVal})


def updatetrustprofile(request):
    if (Common.isTrustLogin):
        tname = request.POST['tname']
        tcontact = request.POST['tcontact']
        temailid = request.POST['temailid']
        tabout = request.POST['tabout']
        taddress = request.POST['taddress']
        tvision = request.POST['tvision']
        tpass = request.POST['tpass']

        data = {
            "name": tname, "contact": tcontact, "mailid": temailid,
            "about": tabout, "address": taddress, "vision": tvision, "password": tpass
        }
        db = connect_firebase()
        db.child("Trust").child(Common.trustkey).update(data)

        return render(request, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Profile Updated Successfully",
                       "path": "trusthome"})

    else:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def addscholarhip(req):
    if (Common.isTrustLogin):
        return render(req, 'add_scholarship.html',
                      {"trustkey": Common.trustkey, "trust_val": Common.trustVal})
    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def viewallscholarships(request):
    schemes = OrderedDict()
    db = connect_firebase()
    try:
        schemes = db.child("Scheme").order_by_child("trust_id").equal_to(Common.trustkey).get().val()
    except:
        print("Error")
    return render(request, 'trust_allscheme.html',
                  {"trustkey": Common.trustkey, "trust_val": Common.trustVal,
                   "scholarships": schemes
                   })


def register(request):
    return render(request, 'register.html', {})


def trust_logout(request):
    Common.trustkey = None
    Common.trustVal = None
    Common.isTrustLogin = False
    Common.isLogin = False

    return render(request, 'redirecthome.html',
                  {"swicon": "success", "swtitle": "Done", "swmsg": "Logout Successfully", "path": ""})


def adminlogout(request):
    Common.isAdminLogin = False

    return render(request, 'redirecthome.html',
                  {"swicon": "success", "swtitle": "Done", "swmsg": "Logout Successfully", "path": ""})


def logout(request):
    Common.currentUser = None
    Common.isLogin = False
    return render(request, 'redirecthome.html',
                  {"swicon": "success", "swtitle": "Done", "swmsg": "Logout Successfully", "path": ""})


def adduser(req):
    name = req.POST['name']
    email = req.POST['email']
    phone = req.POST['phone']
    passwrd = req.POST['pass']
    useremail = None
    db = connect_firebase()

    user = db.child("users").child(phone).get()
    try:
        useremail = db.child("users").order_by_child("mail").equal_to(email).get().val()
    except:
        pass
    print(useremail)
    if user.val():
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "User Already Exists", "path": "register"})
    elif useremail:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "User Mail Exists", "path": "register"})
    else:
        data = {
            "name": name, "mail": email, "password": passwrd, "phone": phone, "profilefill": "0"
        }
        db.child("users").child(phone).set(data)

        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Registration Done Successfully.",
                       "path": "login"})


def updatescholarhiptofire(req):
    sname = req.POST['sname']
    samt = req.POST['samt']
    scourse = req.POST['scoursename']
    scat = req.POST['scat']
    seligibility = req.POST['seligibility']

    key = req.POST['key']
    strdead = 'sdeadline-' + key
    sdeadline = req.POST[strdead]
    logo = Common.trustVal.get("logo")
    trust_id = Common.trustkey
    db = connect_firebase()

    data = {
        "amount": samt, "course": scourse, "eligibility": seligibility, "lastdate": sdeadline,
        "level": scat, "logo": logo, "name": sname, "trust_id": trust_id
    }

    db.child("Scheme").child(key).update(
        data
    )

    return render(req, 'redirecthome.html',
                  {"swicon": "success", "swtitle": "Done", "swmsg": "Scholarhip Updated Successfully.",
                   "path": "trusthome"})


def addscholarhiptofire(req):
    sname = req.POST['sname']
    samt = req.POST['samt']
    scourse = req.POST['scoursename']
    scat = req.POST['scat']
    seligibility = req.POST['seligibility']
    sdeadline = req.POST['sdeadline']
    timestamp = datetime.timestamp(datetime.now())
    logo = Common.trustVal.get("logo")
    trust_id = Common.trustkey
    db = connect_firebase()

    data = {
        "amount": samt, "course": scourse, "eligibility": seligibility, "lastdate": sdeadline,
        "level": scat, "logo": logo, "name": sname, "trust_id": trust_id
    }
    print(str(timestamp))

    strtimestamp = str(timestamp).replace('.', '')

    db.child("Scheme").child(strtimestamp[:13]).set(
        data
    )

    return render(req, 'redirecthome.html',
                  {"swicon": "success", "swtitle": "Done", "swmsg": "Scholarhip Added Successfully.",
                   "path": "trusthome"})


def viewtrustdetails(request, pk):
    global schemes
    schemes = OrderedDict()
    db = connect_firebase()
    trust = db.child("Trust").child(str(pk)).get().val()
    all_trusts = db.child("Trust").order_by_key().get().val()
    del all_trusts[str(pk)]
    try:
        schemes = db.child("Scheme").order_by_child("trust_id").equal_to(str(pk)).get().val()
    except:
        print("Error")

    return render(request, 'trustdetails.html',
                  {"scheme": schemes, 'trust': trust, "all_trusts": all_trusts, "islog": Common.isLogin
                   })


def viewschemedetails(request, pk):
    global schemes
    db = connect_firebase()
    #
    # all_trusts = db.child("Trust").order_by_key().get().val()
    # del all_trusts[str(pk)]
    applied_scheme = None
    try:

        applied_scheme = Common.currentUser.val().get("applied_scheme")
    except:
        pass
    if applied_scheme == None:
        applied_scheme = []
    isapply = "False"
    if str(pk) in applied_scheme:
        isapply = "True"
    scheme = db.child("Scheme").child(str(pk)).get().val()
    trust = db.child("Trust").child(scheme.get("trust_id")).get().val()
    other_schemes = db.child("Scheme").order_by_child("level").equal_to(scheme.get("level")).get().val()
    del other_schemes[str(pk)]
    isclosed = False
    print(scheme.get("lastdate"))
    deadline = datetime.strptime(scheme.get("lastdate"), "%d-%B-%Y")
    today = datetime.now()
    if deadline < today:
        isclosed = True

    return render(request, 'schemedetails.html',
                  {"scheme": scheme, 'trust': trust,
                   "other_schemes": other_schemes, "islog": Common.isLogin, "scheme_key": str(pk),
                   "isapply": isapply, "isclosed": isclosed

                   })


# User Profiles#
def profile_personalDetails(request):
    if (Common.isLogin):
        userprofile = OrderedDict()

        db = connect_firebase()
        accno = ""
        Common.currentUser = db.child("users").child(Common.currentUser.val().get("phone")).get()
        try:
            userprofile = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
            cipher = Fernet(Common.encyptionkey)
            accno = cipher.decrypt(userprofile.get("account_number").encode()).decode()
        except:
            print("Error")
        
        if (Common.currentUser.val().get("profilefill") != "100"):
            return render(request, 'user_profileDetails.html',
                          {"userprofile": userprofile, "currentuser": Common.currentUser.val(), "accno": accno})
        else:
            return render(request, 'user_completeprofile.html',
                          {"userprofile": userprofile, "currentuser": Common.currentUser.val(), "accno": accno
                           })

    else:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": "login"})


def profile_familyDetails(request):
    if (Common.isLogin):
        userprofile = OrderedDict()

        db = connect_firebase()

        Common.currentUser = db.child("users").child(Common.currentUser.val().get("phone")).get()
        try:
            userprofile = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
        except:
            print("Error")

        if (Common.currentUser.val().get("profilefill") != "100"):
            return render(request, 'user_familyDetails.html',
                          {"userprofile": userprofile, "currentuser": Common.currentUser.val()})
        else:
            return render(request, 'user_completeprofile.html',
                          {"userprofile": userprofile, "currentuser": Common.currentUser.val(),
                           })
    else:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": "login"})


def profile_education(request):
    if (Common.isLogin):
        userprofile = OrderedDict()

        db = connect_firebase()

        Common.currentUser = db.child("users").child(Common.currentUser.val().get("phone")).get()
        try:
            userprofile = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
        except:
            print("Error")

        if (Common.currentUser.val().get("profilefill") != "100"):
            return render(request, 'user_education.html',
                          {"userprofile": userprofile, "currentuser": Common.currentUser.val()})
        else:
            return render(request, 'redirecthome.html',
                          {"swicon": "error", "swtitle": "Profile Submitted", "swmsg": "You cant change any details",
                           "path": ""})

    else:
        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": "login"})


def profile_doc(request):
    if (Common.isLogin):
        userprofile = OrderedDict()

        db = connect_firebase()

        Common.currentUser = db.child("users").child(Common.currentUser.val().get("phone")).get()
        try:
            userprofile = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
        except:
            print("Error")

        if (Common.currentUser.val().get("profilefill") != "100"):
            return render(request, 'user_doc.html',
                          {"userprofile": userprofile, "currentuser": Common.currentUser.val(),
                           "config": PyConfig.config1})
        else:
            return render(request, 'user_completeprofile.html',
                          {"userprofile": userprofile, "currentuser": Common.currentUser.val(),
                           })
    else:

        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": "login"})


def saveuserpersonalinfo(req):
    surname = req.POST['sname']
    first_name = req.POST['fname']
    last_name = req.POST['lname']
    dob = req.POST['dob']
    age = req.POST['age1']
    gender = req.POST['gender']

    email = req.POST['email']
    phone = req.POST['phone']
    parent_phone = req.POST['parent_phone']

    religious = req.POST['religious']
    cast = req.POST['cast']
    annual_income = req.POST['anual_income']

    nameinpassbook = req.POST['nameinpassbook']
    account_number = req.POST['account_number']
    bank_name = req.POST['bank_name']
    ifsc_code = req.POST['ifsc_code']
    fill = req.POST['fill']
    save_draft = req.POST['saveasdraft']

    db = connect_firebase()
    data = dict()
    try:
        data = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
        data = dict(data)
    except:
        pass
    if data == None:
        data = dict()

    cipher = Fernet(Common.encyptionkey)
    encaccountnum = cipher.encrypt(account_number.encode())
    print(encaccountnum)

    newdata = {
        "sname": surname, "fname": first_name, "lname": last_name, "dob": dob, "age": age, "gender": gender,
        "email": email, "phone": phone, "parent_phone": parent_phone,
        "religious": religious, "cast": cast, "annual_income": annual_income,
        "account_number": encaccountnum.decode(), "bank_name": bank_name, "ifsc_code": ifsc_code.upper(),
        "nameinpassbook": nameinpassbook

    }

    data.update(newdata)
    print(data)
    db.child("UserProfile").child(str(phone)).set(
        data
    )

    db.child("users").child(str(phone)).child("profilefill").set(fill)
    if save_draft == "1":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Personal Details Saved Successfully.",
                       "path": ""})
    if save_draft == "0":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Personal Details Saved Successfully.",
                       "path": "profile-familyDetails"})


def saveuserfamilyinfo(req):
    address = req.POST['address']
    pincode = req.POST['pincode']

    fatheralive = req.POST['fatheralive']
    fathername = req.POST['fathername']
    fatheroccupation = req.POST['father_occupation']
    fatherincome = req.POST['father_income']

    motheralive = req.POST['motheralive']
    mothername = req.POST['mothername']
    motheroccupation = req.POST['mother_occupation']
    motherincome = req.POST['mother_income']

    fill = req.POST['fill']
    save_draft = req.POST['saveasdraft']

    db = connect_firebase()

    data = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
    data = dict(data)
    print(data)
    newdata = {
        "address": address, "pincode": pincode,
        "fatheralive": fatheralive, "fathername": fathername, "fatheroccupation": fatheroccupation,
        "fatherincome": fatherincome,
        "motheralive": motheralive, "mothername": mothername, "motheroccupation": motheroccupation,
        "motherincome": motherincome
    }

    data.update(newdata)
    print(data)
    db.child("UserProfile").child(Common.currentUser.val().get("phone")).set(
        data
    )

    db.child("users").child(Common.currentUser.val().get("phone")).child("profilefill").set(fill)
    if save_draft == "1":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Family Details Saved Successfully.",
                       "path": ""})
    if save_draft == "0":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Family Details Saved Successfully.",
                       "path": "profile-education"})


def saveusereducation(req):
    collegename = req.POST['collegename']
    collegeaddress = req.POST['collegeaddress']

    coursename = req.POST['coursename']
    coursefees = req.POST['coursefees']

    course1name = req.POST['course1name']
    course1year = req.POST['course1year']
    course1board = req.POST['course1board']
    course1per = req.POST['course1per']

    course2name = req.POST['course2name']
    course2year = req.POST['course2year']
    course2board = req.POST['course2board']
    course2per = req.POST['course2per']

    course3name = req.POST['course3name']
    course3year = req.POST['course3year']
    course3board = req.POST['course3board']
    course3per = req.POST['course3per']

    achievement = req.POST['achievement']

    fill = req.POST['fill']
    save_draft = req.POST['saveasdraft']

    db = connect_firebase()

    data = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
    data = dict(data)
    print(data)
    newdata = {
        "collegename": collegename, "collegeaddress": collegeaddress, "coursename": coursename,
        "coursefees": coursefees,
        "course1name": course1name, "course1board": course1board, "course1year": course1year, "course1per": course1per,
        "course2name": course2name, "course2board": course2board, "course2year": course2year, "course2per": course2per,
        "course3name": course3name, "course3board": course3board, "course3year": course3year, "course3per": course3per,
        "achievement": achievement
    }

    data.update(newdata)
    print(data)
    db.child("UserProfile").child(Common.currentUser.val().get("phone")).set(
        data
    )

    db.child("users").child(Common.currentUser.val().get("phone")).child("profilefill").set(fill)
    if save_draft == "1":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Education Details Saved Successfully.",
                       "path": ""})
    if save_draft == "0":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Education Details Saved Successfully.",
                       "path": "profile-uploaddoc"})


def savedocuments(req):
    docphotoidname = req.POST['docphotoidname']
    docageproofname = req.POST['docageproofname']

    docadmissionname = req.POST['docadmissionname']
    doccurrentfeename = req.POST['doccurrentfeename']

    docaddressname = req.POST['docaddressname']
    docincomename = req.POST['docincomename']

    docphotoidurl = req.POST['docphotoidurl']

    docageproofurl = req.POST['docageproofurl']

    docadmissionurl = req.POST['docadmissionurl']
    doccurrentfeeurl = req.POST['doccurrentfeeurl']
    docaddressurl = req.POST['docaddressurl']
    docincomeurl = req.POST['docincomeurl']

    doccourse1url = req.POST['doccourse1url']
    doccourse2url = req.POST['doccourse2url']
    doccourse3url = req.POST['doccourse3url']
    docpassbookurl = req.POST['docpassbookurl']

    fill = req.POST['fill']
    save_draft = req.POST['saveasdraft']

    db = connect_firebase()

    data = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
    data = dict(data)
    print(data)
    newdata = {
        "docphotoidname": docphotoidname, "docageproofname": docageproofname, "docadmissionname": docadmissionname,
        "doccurrentfeename": doccurrentfeename, "docaddressname": docaddressname, "docincomename": docincomename,
        "docphotoidurl": docphotoidurl, "docageproofurl": docageproofurl, "docadmissionurl": docadmissionurl,
        "doccurrentfeeurl": doccurrentfeeurl,
        "docaddressurl": docaddressurl, "docincomeurl": docincomeurl, "doccourse1url": doccourse1url,
        "doccourse2url": doccourse2url, "doccourse3url": doccourse3url, "docpassbookurl": docpassbookurl
    }

    data.update(newdata)
    print(data)
    db.child("UserProfile").child(Common.currentUser.val().get("phone")).set(
        data
    )

    db.child("users").child(Common.currentUser.val().get("phone")).child("profilefill").set(fill)
    if save_draft == "1":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Documents Saved Successfully.",
                       "path": ""})
    if save_draft == "0":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Profile Submitted Successfully.",
                       "path": "user-completeprofile"})


def user_completeprofile(request):
    if (Common.isLogin):
        userprofile = OrderedDict()

        db = connect_firebase()

        Common.currentUser = db.child("users").child(Common.currentUser.val().get("phone")).get()
        try:
            userprofile = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
        except:
            print("Error")

        if Common.currentUser.val().get("profilefill") == "100":
            return render(request, 'user_completeprofile.html',
                          {"userprofile": userprofile, "currentuser": Common.currentUser.val(),
                           })
        else:
            return render(request, 'redirecthome.html',
                          {"swicon": "error", "swtitle": "Profile Not Submitted", "swmsg": "Please Complete profile",
                           "path": ""})
    else:

        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": "login"})


# Apply for scheme/scholarship

def applyscholarship(request):  # user has click on apply button add userinfo to db
    if (Common.isLogin):
        userprofile = OrderedDict()

        db = connect_firebase()

        Common.currentUser = db.child("users").child(Common.currentUser.val().get("phone")).get()
        try:
            userprofile = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
        except:
            print("Error")

        if Common.currentUser.val().get("profilefill") == "100":

            schemeid = request.POST['schemeid_apply']
            amount = request.POST['amount']
            trust_id = request.POST['trust_id']
            schemename = request.POST['schemename']

            userphone = Common.currentUser.val().get("phone")
            name = userprofile.get("sname") + " " + userprofile.get("fname") + " " + userprofile.get("lname")
            status = "Pending"

            applicationid = datetime.timestamp(datetime.now())
            applicationid = str(applicationid).replace('.', '')
            applicationid = applicationid[:13]

            tname = db.child("Trust").child(trust_id).child("name").get().val()
            print(tname)

            data = {
                "userid": userphone, "username": name,
                "scheme_id": schemeid, "scheme_name": schemename, "schemeamount": amount,
                "status": status, "remark": "", "sanctionedamount": "0", "trust_id": trust_id, "tname": tname
            }

            db.child("AppliedScheme").child(applicationid).set(
                data
            )

            applied_scheme = None
            try:

                print(Common.currentUser.val())
                applied_scheme = Common.currentUser.val().get("applied_scheme")

                print(Common.currentUser.val())
                print("inside try" + applied_scheme)
            except:
                pass
            if applied_scheme == None:
                applied_scheme = []
            print(applied_scheme)
            applied_scheme.append(schemeid)

            db.child("users").child(userphone).update(
                {"applied_scheme": applied_scheme}
            )

            return render(request, 'redirecthome.html',
                          {"swicon": "success", "swtitle": "Done",
                           "swmsg": "Applied Successfully. Your Application number is " + applicationid,
                           "path": "appliedscholarship"})
        else:
            return render(request, 'redirecthome.html',
                          {"swicon": "error", "swtitle": "Profile Not Submitted", "swmsg": "Please Complete profile",
                           "path": "profile-personalDetails"})
    else:

        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": "login"})


def appliedscholarship(request):
    if (Common.isLogin):
        data = OrderedDict()

        db = connect_firebase()
        try:
            data = db.child("AppliedScheme").order_by_child("userid").equal_to(
                Common.currentUser.val().get("phone")).get().val()
        except:
            pass

        return render(request, 'user_appliedscheme.html',
                      {"currentuser": Common.currentUser.val(), "applied_schemes": data})
    else:

        return render(request, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": "login"})
