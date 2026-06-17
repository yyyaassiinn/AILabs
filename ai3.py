goals = {
    "can_graduate": ["is_eligible"],
    "is_eligible": ["completed_all_courses","no_fees_due"]
}
facts = ["completed_all_courses","no_fees_due"]

def prove(goal):
    if goal in facts:
        return True
    elif goal in goals:
        is_proven = True
        for fact in goals[goal]:
            if not prove(fact):
                is_proven = False
        return is_proven
    else: return False

val = prove("can_graduate")  
print(val)     
        
        
