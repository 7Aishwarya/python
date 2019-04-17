def check_baggage(baggage_weight):
    try:
        if(baggage_weight>=0 and baggage_weight<=40):
            return True
        else:
            return False
    except:
        print("Error occured in checking the baggage weight")
        return None
def check_immigration(expiry_year):
    try:
        if(expiry_year>=2001 and expiry_year<=2025):
            return True
        else:
            return False
    except:
        print("Error occured in checking the expiry year")
        return None
def check_security(noc_status):
    try:
        if(noc_status=="valid" or noc_status=="VALID"):
            return True
        else:
            return False
    except:
        print("Error occured in checking the status")
        return None
def traveler():
    traveler_id=1001
    traveler_name="Jim"
    check_baggage("a")
    check_immigration(2019)
    check_security("not valid")
    if(check_baggage("a")==True and check_immigration(2019)==True and check_security("VALID")==True):
        print(traveler_id, traveler_name, "\nAllow traveler to fly")
    else:
        print(traveler_id, traveler_name, "\nDetain traveler for re-checking")
    return

traveler()
