import matplotlib.pyplot as plt

def plot_times(runtime):

    plt.figure(figsize=(15, 5)) 

    plt.plot(range(1, len(runtime) + 1), runtime, 
         linewidth=1.5, 
         color="red",
         linestyle="-", 
         marker=">", 
         markersize=10, 
         markerfacecolor="blue", 
         markeredgecolor="grey",
         markeredgewidth=1) 

    # plt.xticks(runtime, fontsize=10)
    plt.xlabel("Times", fontsize=15)
    plt.ylabel("Runtime", fontsize=15)
    plt.grid()
    plt.show()
    