from django.shortcuts import render, redirect
from supercoin.models import Accounts, Loyalty_Programs, Transactions
from django.contrib import messages
from django.db.models import Q

from brownie import *
p = project.load("D:/flipkart/brownieBackend/token", name="TokenProject")
p.load_config()
from brownie.project.TokenProject import *
network.connect("matic_mumbai")

address = "0x8a0c0366985A2A070d836A5E6C84E52bfc381975"
abi = SuperCoin.abi
acct = accounts.load("defac", password="def123")
# acct1 = accounts.load("testac", password="test123")
response = Contract.from_abi("SuperCoin", address, abi)

def get_balance(email):
    return response.getBalance(email)

def total_coins():
    return response.totalCoins()

def create_account(email):
    response.createAccount(email, {"from": acct})
    
def add_coins(amount):
    tx = response.addCoins(amount, {"from": acct})
    
    sender = tx.events[0]["sender"]
    recipient = tx.events[0]["recipient"]
    amount1 = str(tx.events[0]["amount"])
    time = str(tx.events[0]["t"])
    
    txn = Transactions()
    txn.sender = Accounts.objects.get(email=recipient)
    txn.recipient = recipient
    txn.amount = str(amount1)
    txn.save()
    
def transfer(sender, recipient, amount):
    tx = response.transfer(sender, recipient, amount, {"from": acct})
    return tx

def auth_login(request, user):
    request.session["email"] = user.email

def authenticate(email, password):
    if Accounts.objects.filter(email=email, password=password).exists():
        user = Accounts.objects.get(email=email, password=password)
        return user
    else:
        return None

def index(request):
    return redirect("login")

def signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        category = request.POST["category"]
        password = request.POST["password"]

        is_customer = False
        is_superuser = False

        if Accounts.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect("signup")
        
        if len(name) > 100:
            messages.error(request, "Name should be within 100 characters")
            return redirect("signup")
        
        if len(password) > 200:
            messages.error(request, "Password should be within 200 characters")
            return redirect("signup")
        if category == "admin":
            is_superuser = True
        elif category == "customer":
            is_customer = True
        else:
            is_customer = False
        myuser = Accounts()
        myuser.name = name
        myuser.email = email
        myuser.is_customer = is_customer
        myuser.is_superuser = is_superuser
        myuser.password = password
        myuser.save()

        create_account(email=email)
        messages.success(request, "Account created successfully")
        return redirect("login")
    
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(email=email, password=password)

        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect("admin")
            elif user.is_customer:
                return redirect("customer")
            else:
                return redirect("seller")
        else:
            messages.error(request, "Email/Password is incorrect")
            return redirect("login")

    return render(request, "login.html")

def review(request):
    return render(request, "review.html")

def customer(request):
    if Accounts.objects.get(email=request.session["email"]).is_customer:
        user = Accounts.objects.get(email=request.session["email"])
        name = user.name
        balance = get_balance(user.email)
        txns = Transactions.objects.filter(Q(sender=user)|Q(recipient=request.session["email"]))
        return render(request, "customer.html", {"name": name, "balance": balance, "txns": list(txns)})
    else:
        return redirect("login")
 
def admin(request):
    if Accounts.objects.get(email=request.session["email"]).is_superuser:
        if request.method == "POST":
            if request.POST.get("email") is not None:
                email = request.POST["email"]
                amount = request.POST["amount"]
            
                tx = transfer(sender=request.session["email"], recipient=email, amount=amount)
                sender = tx.events[0]["sender"]
                recipient = tx.events[0]["recipient"]
                amount1 = str(tx.events[0]["amount"])
                time = str(tx.events[0]["t"])
                
                txn = Transactions()
                txn.sender = Accounts.objects.get(email=sender)
                txn.recipient = recipient
                txn.amount = str(amount1)
                txn.save()
                
                messages.success(request, "Transaction was successful")
                return redirect("admin")
            else:
                amount = request.POST["iamount"]
                add_coins(amount=amount)
            
                messages.success(request, "Coins issued successfully")
                return redirect("admin")

        user = Accounts.objects.get(email=request.session["email"])
        balance = get_balance(user.email)
        total = total_coins()
        wid = acct.address
        wb = acct.balance()
        wb = wb/10**18
        
        txns = Transactions.objects.filter(sender = Accounts.objects.get(email=request.session["email"]))
        
        return render(request, "admin.html", {"name": user.name, "balance": balance, "total": total, "wid": wid, "wb": wb, "txns":list(txns)})
    else:
        return redirect("login")

def rewards(request):
    if Accounts.objects.get(email=request.session["email"]).is_customer:
        # products = []
        # user = Accounts.objects.get(email=request.session["email"])
        # if LP_Map.objects.filter(user=user).exists():
        #     redeemed = LP_Map.objects.get(user=user)
        #     all = LP_Map.objects.get()

        #     for reward in redeemed:
        #         if reward in all:
        #             products.push({"product": reward.program.program_name, "desc": reward.program.program_desc, "redeemed": True})
        #         else:
        #             products.push({"product": reward.program.program_name, "desc": reward.program.program_desc, "redeemed": False})
        # else:
        #     all = LP_Map.objects.get()
        #     for one in all:
        #         one.push({"product": reward.program.program_name, "desc": reward.program.program_desc, "redeemed": False})
        return render(request, "rewards.html")
    else:
        return redirect("login")

def store(request):
    if Accounts.objects.get(email=request.session["email"]).is_customer:
        return render(request, "store.html")
    else:
        return redirect("login")

def seller(request):
    if not Accounts.objects.get(email=request.session["email"]).is_customer:
        if request.method=="POST":
            email = request.POST["email"]
            amount = request.POST["amount"]
        
            tx = transfer(sender=request.session["email"], recipient=email, amount=amount)
            sender = tx.events[0]["sender"]
            recipient = tx.events[0]["recipient"]
            amount1 = str(tx.events[0]["amount"])
            time = str(tx.events[0]["t"])
            
            txn = Transactions()
            txn.sender = Accounts.objects.get(email=sender)
            txn.recipient = recipient
            txn.amount = str(amount1)
            txn.save()
            
            messages.success(request, "Transaction was successful")
            return redirect("seller")
        
        balance = get_balance(request.session["email"])
        user = Accounts.objects.get(email=request.session["email"])
        print(balance)
        txns = Transactions.objects.filter(Q(sender=user)|Q(recipient=request.session["email"]))
        return render(request, "seller.html", {"balance": balance, "name": user.name, "txns": list(txns)})
    else:
        return redirect("login")

def s_rewards(request):
    owner = Accounts.objects.get(email=request.session["email"])
    if not owner.is_customer:
        if request.method == "POST":
            program_name = request.POST["program"]
            price = request.POST["price"]

            myprogram = Loyalty_Programs()
            myprogram.program_name = program_name
            myprogram.program_desc = "Redeem for "+str(price)+" Supercoins"
            myprogram.price = str(price)
            myprogram.owner = owner
    
            myprogram.save()

            messages.success(request, "Loyalty Program created successfully")
            
            return redirect("s_rewards")
        
        lps = Loyalty_Programs.objects.filter(owner=owner)
        balance = get_balance(request.session["email"])
        print(balance)
        user = Accounts.objects.get(email=request.session["email"])
        if lps.exists():
            return render(request, "s_rewards.html", {"lps":list(lps), "balance": balance, "name": user.name})
        else:
            return render(request, "s_rewards.html", {"balance": balance, "name": user.name})
    else:
        return redirect("login")

def zara(request):
    if request.session["email"]:
        print("OK")