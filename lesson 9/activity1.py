medical_cause=input("medical cause ? Y/N:")
if medical_cause=="Y": 
    print("allowed")
else:
    att=int(input("attendance:"))
    if att >=75:
        print("allowed")
    else:
        print("not allowed")