import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# Problem (Initial)
# define variables
CVTP = LpVariable("CVTP",0, None)
CHKN = LpVariable("CHKN",0, None)
RICE = LpVariable("RICE",0, None)
SLMN = LpVariable("SLMN",0, None)
MASH = LpVariable("MASH",0, None)

# defines the problem
prob = LpProblem("problem", LpMinimize)
# Note, LpMaximize for a maximization problem, 
# and LpMinimize for a minimization problem

# define constraints
prob += 980*CVTP + 920*CHKN + 880*RICE + 850*SLMN + 770*MASH <= 5000*7 #Sodium
prob += 29*CVTP + 41*CHKN + 34*RICE + 37*SLMN + 41*MASH >= 50*7 #Protein
prob += 0.0*CVTP + 0.1*CHKN + 0.1*RICE + 11.2*SLMN + 0.1*MASH >= 20*7 #Vitamin D
prob += 160*CVTP + 380*CHKN + 130*RICE + 110*SLMN + 100*MASH >= 1300*7 #Calcium
prob += 2.2*CVTP + 1.8*CHKN + 3.5*RICE + 1.3*SLMN + 2.5*MASH >= 18*7 #Iron
prob += 930*CVTP + 980*CHKN + 1010*RICE + 910*SLMN + 1430*MASH >= 4700*7 #Potassium

# Note, if <= then <=
# If >= then >=
# If = then ==

# define objective function
#Cost
prob += (440*CVTP + 690*CHKN + 580*RICE + 660*SLMN + 500*MASH) #Energy

# solve the problem
status = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status]}")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    
print(f"Objective = {value(prob.objective)}")
print(f"")
