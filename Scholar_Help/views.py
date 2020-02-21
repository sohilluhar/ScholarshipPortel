from collections import OrderedDict
from datetime import datetime
from random import randint

import pyrebase
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
        user = db.child("Trust").order_by_child("username").equal_to(trustusername).get().val()
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
    return render(req, 'trust_home.html', {"trustkey": Common.trustkey, "trust_val": Common.trustVal})


def addscholarhip(req):
    if (Common.isTrustLogin):
        return render(req, 'add_scholarship.html',
                      {"trustkey": Common.trustkey, "trust_val": Common.trustVal})
    else:
        return render(req, 'redirecthome.html',
                      {"swicon": "error", "swtitle": "Error", "swmsg": "Please try again", "path": ""})


def register(request):
    return render(request, 'register.html', {})


def trust_logout(request):
    Common.trustkey = None
    Common.trustVal = None
    Common.isTrustLogin = False
    Common.isLogin = False
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

    db.child("Scheme").child(strtimestamp).set(
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
    scheme = db.child("Scheme").child(str(pk)).get().val()
    trust = db.child("Trust").child(scheme.get("trust_id")).get().val()
    other_schemes = db.child("Scheme").order_by_child("level").equal_to(scheme.get("level")).get().val()
    del other_schemes[str(pk)]
    return render(request, 'schemedetails.html',
                  {"scheme": scheme, 'trust': trust,
                   "other_schemes": other_schemes, "islog": Common.isLogin, "scheme_key": str(pk)
                   })


# User Profiles#
def profile_personalDetails(request):
    if (Common.isLogin):
        userprofile = OrderedDict()

        db = connect_firebase()

        Common.currentUser = db.child("users").child(Common.currentUser.val().get("phone")).get()
        try:
            userprofile = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
        except:
            print("Error")

        return render(request, 'user_profileDetails.html',
                      {"userprofile": userprofile, "currentuser": Common.currentUser.val()})
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

        return render(request, 'user_familyDetails.html',
                      {"userprofile": userprofile, "currentuser": Common.currentUser.val()})
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

        return render(request, 'user_education.html',
                      {"userprofile": userprofile, "currentuser": Common.currentUser.val()})
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

    account_number = req.POST['account_number']
    bank_name = req.POST['bank_name']
    ifsc_code = req.POST['ifsc_code']
    fill = req.POST['fill']
    save_draft = req.POST['saveasdraft']

    db = connect_firebase()
    olddata = dict()
    try:
        olddata = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
        olddata = dict(olddata)
    except:
        pass

    data = {
        "sname": surname, "fname": first_name, "lname": last_name, "dob": dob, "age": age, "gender": gender,
        "email": email, "phone": phone, "parent_phone": parent_phone,
        "religious": religious, "cast": cast, "annual_income": annual_income,
        "account_number": account_number, "bank_name": bank_name, "ifsc_code": ifsc_code.upper()

    }

    data.update(olddata)
    db.child("UserProfile").child(str(phone)).set(
        data
    )

    db.child("users").child(str(phone)).child("profilefill").set(fill)
    if save_draft == "1":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Personal Info Saved Successfully.",
                       "path": ""})
    if save_draft == "0":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Personal Info Saved Successfully.",
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

    olddata = db.child("UserProfile").child(Common.currentUser.val().get("phone")).get().val()
    olddata = dict(olddata)
    print(olddata)
    data = {
        "address": address, "pincode": pincode,
        "fatheralive": fatheralive, "fathername": fathername, "fatheroccupation": fatheroccupation,
        "fatherincome": fatherincome,
        "motheralive": motheralive, "mothername": mothername, "motheroccupation": motheroccupation,
        "motherincome": motherincome
    }

    data.update(olddata)
    print(data)
    db.child("UserProfile").child(Common.currentUser.val().get("phone")).set(
        data
    )

    db.child("users").child(Common.currentUser.val().get("phone")).child("profilefill").set(fill)
    if save_draft == "1":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Family Info Saved Successfully.",
                       "path": ""})
    if save_draft == "0":
        return render(req, 'redirecthome.html',
                      {"swicon": "success", "swtitle": "Done", "swmsg": "Family Info Saved Successfully.",
                       "path": "profile-education"})
