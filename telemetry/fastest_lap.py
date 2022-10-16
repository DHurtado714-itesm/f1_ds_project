import fastf1 as ff1
from fastf1 import plotting

from matplotlib import pyplot as plt

from matplotlib.pyplot import figure


#Setup plotting
plotting.setup_mpl()

#Enable the cache
#ff1.Cache.enable_cache('cache')

#Load the session data
race = ff1.get_session(2022, 'Monaco', 'R')

#Collect all race laps
laps = race.load_laps(with_telemetry = True)

#Get laps of the drivers (VER and PER)
laps_VER = laps.pick_driver('VER')
laps_PER = laps.pick_driver('PER')

#Extract the fastest laps
fastest_VER = laps_VER.pick_fastest()
fastest_PER = laps_PER.pick_fastest()

#Get telemetry from fastest laps
telemetry_VER = fastest_VER.get_car_data().add_distance()
telemetry_PER = fastest_PER.get_car_data().add_distance()

fig, ax = plt.subplots(3)
fig.suptitle("Fastest Race Lap Telemetry Comparison")

ax[0].plot(telemetry_VER['Distance'], telemetry_VER['Speed'], label='VER')
ax[0].plot(telemetry_PER['Distance'], telemetry_PER['Speed'], label='PER')
ax[0].set(ylabel='Speed')
ax[0].legend(loc="lower right")

ax[1].plot(telemetry_VER['Distance'], telemetry_VER['Throttle'], label='VER')
ax[1].plot(telemetry_PER['Distance'], telemetry_PER['Throttle'], label='PER')
ax[1].set(ylabel='Throttle')

ax[2].plot(telemetry_VER['Distance'], telemetry_VER['Brake'], label='VER')
ax[2].plot(telemetry_PER['Distance'], telemetry_PER['Brake'], label='PER')
ax[2].set(ylabel='Brakes')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for a in ax.flat:
    a.label_outer()
    
plt.show()