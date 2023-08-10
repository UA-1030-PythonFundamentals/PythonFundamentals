def correct_tail(body, tail):
    sub = body[-len(tail):] 
    return sub == tail