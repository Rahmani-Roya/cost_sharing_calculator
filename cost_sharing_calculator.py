def main():
    family =[]
    family_weight = []
    family_paid = []
    costs_by_family = []
    family_balance =[]

    total_weight = 0
    total_paid = 0
    kid = 0
    family_count= int(input("enter the number of families:"))
    kid_weight = float(input("Each kid has a weight between 0 and 1.\nPLease Enter the weight value for kids: "))
    for i in range(0,family_count):
        print(f"\n---family{i+1}---")
        adult = int(input("Number of adults: "))
        if kid_weight != 0:
            kid = int(input("Number of Kids: "))
        family.append([adult,kid])
        family_weight.append(family[i][0] + (family[i][1] * kid_weight))
        total_weight += family_weight[i]
        family_paid.append(int(input("Amount paid:")))
        total_paid += family_paid[i]
    cost_per_unit_weight = total_paid / total_weight
    for i in range(0,family_count):
        costs_by_family.append (cost_per_unit_weight* family_weight[i] )
    family_balance = [a-b for a,b in zip(family_paid , costs_by_family)]
    for i in range(0,family_count):
        print("---Balance---")
        if family_balance[i]< 0 :
            print(f"Family {i+1} needs to pay {abs(family_balance[i]):.2f}.\n")
        elif family_balance[i]> 0 :
            print(f"Family {i+1} should receive {family_balance[i]:.2f}.\n")
if __name__ == "__main__":
    main()
