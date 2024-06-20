import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np

# Define the list of KIC IDs
kic_list = ['KIC 3733346', 'KIC 8462852', 'KIC 9832227', 'KIC 11026764', 'KIC 9246715', 'KIC 11145123']

# Loop through each KIC ID
for kic in kic_list:
    try:
        # Search for light curve data
        search_result = lk.search_lightcurve(kic, author='Kepler')

        # Check if data exists for Kepler Quarter 2
        if len(search_result) > 0:
            quarter2_index = np.where(search_result.table['mission'] == 'Kepler Quarter 02')[0]
            if len(quarter2_index) > 0:
                # Download and plot data for Kepler Quarter 2
                lc = search_result[quarter2_index[0]].download()
                print(f"Downloaded light curve for {kic}")

                lc.plot()
                #plt.xlim(205,215)
                plt.pause(5)
                plt.show()


                # Perform periodogram analysis
                periodogram = lc.to_periodogram(method="bls", period=np.arange(1, 100, 0.1))
                periodogram.plot()
                plt.title("Periodogram")
                plt.pause(5)
                plt.show()

                # Get the period corresponding to the highest peak
                best_fit_period = periodogram.period_at_max_power
                print(f"Best-fit period for {kic}: {best_fit_period} days")

                lc.fold(period=best_fit_period).plot()
                plt.title("Folded Light Curve")
                plt.pause(5)
                plt.show()

            else:
                print(f"No Kepler Quarter 2 data found for {kic}")
        else:
            print(f"No light curve data found for {kic}")

    except Exception as e:
        print(f"Error retrieving data for {kic}: {e}")
