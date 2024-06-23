import numpy as np

total_x_lenght = 2
number_grid_points_x = 41
dx = total_x_lenght / (number_grid_points_x-1)
number_of_timesteps = 25
dt = 0.025
c = 1

# starting with numpy ones
u = np.ones(number_grid_points_x)

# setting u = 2 between 0.5 and 1 in everyone else
# u^0 then is:
u[int(0.5/dx):int(1/dx+1)] = total_x_lenght

print(u)
# plotting the initial conditions of the velocity in the space
# plt.plot(np.linspace(0, total_x_lenght, number_grid_points_x), u)

un = np.ones(number_grid_points_x)
# temporary arrays of ones

for n in range(number_of_timesteps):  # run from 0 to number_of_timesteps times
    un = u.copy()  # copy the existing values of u into un
    for i in range(1, number_grid_points_x):
        u[i] = un[i] - c*dt/dx*(un[i] - un[i-1])


