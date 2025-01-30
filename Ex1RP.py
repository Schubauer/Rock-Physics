import matplotlib.pyplot as plt

K1 = 37  #Bulk modulus (GPa)
mu1 = 44  #Shear modulus (GPa)
rho1 = 2650  #Density (kg/m^3)

K2 = 2.2  #Bulk modulus fluid (GPa)
rho2 = 1000  #Density fluid (kg/m^3)

K_eff = K1 
mu_eff = mu1
n = 1
i = 1
por = 1
#Creating the list
Vp_list = []
Vs_list = []
Vp_Slist = []
Vs_Slist = []
phi_list = []

for n in range(100):
    phi = por*(n/100) #Changes the x scale of the plot

    #Direct calc.
    K_direct = K1 * (1 - phi) + K2 * phi
    mu_direct = mu1 * (1 - phi)
    rho_direct = rho1 * (1 - phi) + rho2 * phi

    Vp_direct = ((K_direct + 4/3 * mu_direct) / rho_direct)**(1/2)
    Vs_direct = (mu_direct / rho_direct)**(1/2)
    Vp_list.append(Vp_direct)
    Vs_list.append(Vs_direct)

    phi_list.append(phi)

for i in range(100):
    phi2 = por*(i/100)
    #SCA calc.
    for n in range(100):
        esh_ratio = (3*K_eff + 4*mu_eff) / (3*K2 + 4*mu_eff) #e2/e fraction
        K_eff = K1 + (K2 - K1)*esh_ratio*phi2
        mu_eff = mu1 + (0 - mu1)*esh_ratio*phi2
    
    rho_sca = rho1 * (1 - phi) + rho2 * phi
    Vp_sca = ((K_eff + 4/3 * mu_eff) / rho_sca)**(1/2)
    Vs_sca = (mu_eff / rho_sca)**(1/2)
    Vp_Slist.append(Vp_sca)
    Vs_Slist.append(Vs_sca)

# Plot results
plt.plot(phi_list, Vp_list, label='Vp - Direct', linestyle='dashed')
plt.plot(phi_list, Vs_list, label='Vs - Direct', linestyle='dashed')
plt.plot(phi_list, Vp_Slist, label='Vp - SCA')
plt.plot(phi_list, Vs_Slist, label='Vs - SCA')
plt.axvline(x = 0.1,linestyle='dashed')
plt.xlabel('Porosity')
plt.ylabel('Velocity (Km/s)')
plt.title('P and S Wave Velocities vs. Porosity')
plt.legend()
plt.grid()
plt.show()